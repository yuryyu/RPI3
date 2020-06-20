import socket

nb=1 # 0- HIT, 1 - open HiveMQ - broker.hivemq.com
brokers=["139.162.222.115",str(socket.gethostbyname('broker.hivemq.com'))]
ports=[80,1883]
usernames = ['','']
passwords = ['','']
broker_ip=brokers[nb]
port=ports[nb]
username = usernames[nb]
password = passwords[nb]
conn_time = 0 # 0 stands for endless
sub_topic = ['door/state','watcher/state']
pub_topic = 'home/state'
msg_device = ['opened', 'Intruder']
waittime = 30
netinterface = 'wlan0' #'br0'
netstart = '192.168.1.'