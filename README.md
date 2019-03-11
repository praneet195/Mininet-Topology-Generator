# Mininet-Topology-Generator
#### Simple Data Center Topology Generator <br/>
##### The reason i've written this script is because the sudo mn --topo tree,node,leafnode command takes a lifetime and core dumps most of the time. <br/>

Install Mininet by following the instructions at : <br/>
https://github.com/mininet/mininet<br/>

Once installed run the topogen script as follows: <br/>

- **sudo python topogen.py** \<no-of-switches\> \<no-of-hosts\> <br/>

- Example: sudo python topogen.py 4 16 creates a datacenter topology with 4+ switches and 16 hosts. <br/>

The diagram below shows the type of topology being generated: <br/>

<p align="center">
<img src="https://github.com/praneet195/Mininet-Topology-Generator/blob/master/topo.png">
</p>


### To Enable Pox Firewall <br/>
Clone the Pox Repo from the following address: <br/>
-https://github.com/noxrepo/pox <br/>

Run the topogen_remote.py script with the same syntax as above <br/>
- Here each node gets assigned a mac address in the follwing form: <br/>
  - If node number a<100 : MAC:: 00:00:00:00:00:01.........00:00:00:00:00:99 <br/>
  - If node number a>=100: MAC:  00:00:00:00:01:00.........00:00:00:00:09:99 <br/>
  
Use the following tutorial to create the firewall script: <br/>
- http://www.anshumanc.ml/networks/2017/09/19/firewall/ <br/>

The firewall.py script provided in the repo adds few random firewall rules. Feel free to edit it as per your liking. <br/>

Always controller c[0] is used as remote controller since it takes all connections. <br/>

Run the scripts as per the tutorial and now you have a network setup with a working firewall :) <br/>

### To generate a network with random link and host parameters.. use the random_var_topogen.py script <br/>









