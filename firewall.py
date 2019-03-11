from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.addresses import EthAddr
import sys
import random

def rulecreator(x):
    xrule=""
    if x<10:
	xrule="00:00:00:00:00:0"+str(x)
    elif x<100:
	xrule="00:00:00:00:00:"+str(x)
    else:
	xrule="00:00:00:00:0"+str(x[0])+":"+str(x[1:])
    return xrule



numrules=random.randint(1,15)

ruleset=[]
for i in range(numrules):
    j=random.randint(1,50)
    k=random.randint(1,50)
    jrule=rulecreator(j)
    krule=rulecreator(k)
    ruleset.append([jrule,krule])


class SDNFirewall (EventMixin):
    
    def __init__ (self):
        print ruleset
        self.listenTo(core.openflow)
        
    def _handle_ConnectionUp (self, event):
        for rule in ruleset:
            block = of.ofp_match()
            block.dl_src = EthAddr(rule[0])
            block.dl_dst = EthAddr(rule[1])
            flow_mod = of.ofp_flow_mod()
            flow_mod.match = block
            event.connection.send(flow_mod)
        
def launch ():
    core.registerNew(SDNFirewall)
