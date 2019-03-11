#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import sys
def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c1=net.addController(name='c1',
                      controller=Controller,
                      protocol='tcp',
                      port=6634)

    c2=net.addController(name='c2',
                      controller=Controller,
                      protocol='tcp',
                      port=6635)

    c0=net.addController(name='c0',
                      controller=RemoteController,
                      protocol='tcp',
                      port=6633)
    numswitches=int(sys.argv[1])
    numhosts=int(sys.argv[2])
    info( '*** Add switches\n')

    switches=[]
    for i in range(1,numswitches+1):
	switch = net.addSwitch('s'+str(i), cls=OVSKernelSwitch)
	switches.append(switch)
    print switches
	
    s999 = net.addSwitch('s999', cls=OVSKernelSwitch)
    s998 = net.addSwitch('s998', cls=OVSKernelSwitch)
    s997 = net.addSwitch('s997', cls=OVSKernelSwitch)
    net.addLink(s999, s997)
    net.addLink(s997, s998)
   
    scount=0
    for i in switches:
	if scount<int( numswitches/2):
	    net.addLink(s999,i)
	    scount+=1
	else:
	    net.addLink(s998,i)


    info( '*** Add hosts\n')
    hosts=[]
    for i in range(1,numhosts+1):
	if i<10:
	    host=net.addHost('h'+str(i), cls=Host, ip='10.0.0.'+str(i),
	    defaultRoute=None,mac="00:00:00:00:00:0"+str(i))
	elif i<100:
	    host=net.addHost('h'+str(i), cls=Host, ip='10.0.0.'+str(i),
	    defaultRoute=None,mac="00:00:00:00:00:"+str(i))
	else:  
	    host=net.addHost('h'+str(i), cls=Host, ip='10.0.0.'+str(i),
	    defaultRoute=None,mac="00:00:00:00:0"+str(i[0])+":"+str(i[1:]))
	hosts.append(host)

    info( '*** Add links\n')
    
    perswitch=int(numhosts/numswitches)
    

    print hosts
    print switches
    print perswitch

    for i in switches:
	for j in range(0,perswitch):
	    net.addLink(i,hosts[j])
	del hosts[:perswitch]


#	


	
	    







    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s999').start([c0])
    net.get('s998').start([c0])
    net.get('s997').start([c0])

    
    scount=0
    for i in switches:
	if scount<int( numswitches/2):
	    net.get(str(i)).start([c1])
	    scount+=1
	else:
	    net.get(str(i)).start([c2])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

