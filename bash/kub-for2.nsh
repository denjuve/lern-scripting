#!/bin/bash
#exec 1>log.log 2>&1
node3='node03'
node3_ip='192.168.122.239'
node1='node01'
node1_ip='192.168.122.9'
node2='node02'
node2_ip='192.168.122.32'

user=ubuntu
nt=3

#allNodes=()
#i=1
#
#while [ $i -le $nt ]; do
#allNodes+=( "$i" )
#((i+=1))
#done
#echo "${allNodes[@]} all nodes"

sudo bash -c "cat << EOF >> /etc/hosts
$node3_ip $node3
$node1_ip $node1
$node2_ip $node2
EOF"

cat <<EOF > kube_node_install.sh
#!/bin/bash
sudo apt-get update -y >/dev/null
sudo apt-get install -y nmap >/dev/null
EOF

for ((NODENUM=1;NODENUM<=nt;NODENUM++)); do
#$(seq 1 $nt); do
#${allNodes[@]}; do
echo "installing on node0${NODENUM}"
ssh -i ../key -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${user}@node0${NODENUM} 'sudo bash -s' < kube_node_install.sh
done
