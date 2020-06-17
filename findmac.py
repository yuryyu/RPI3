import subprocess
import numpy as np
command="arp-scan --retry=8 --ignoredups -I br0 --localnet"
#print(command)
rez=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
print(rez)
rez=str(rez)
#print(rez)
l=rez.split()
num=len(l)
#print(num)
#print(l)
#
i=0		
for l[i] in l:
   if l[i] != 'packets':
      i=i+1
   else:
      num_of_devices=l[i-1]
      break
#print(num_of_devices)
num_of_devices=int(num_of_devices)


ma=14
print(l[ma])
f=open('connected.txt','w') 
f.write(l[ma])
f.write('\n')
ma=ma+1

num_of_devices_real=0
while (l[ma] != num_of_devices) & (l[ma+1] != 'packets'):
   y=list(l[ma])
   if y[2] == ':': 
    f.write(l[ma])
    f.write('\n')    
    print(l[ma])
    ma=ma+1
    num_of_devices_real=num_of_devices_real+1
   else:
    ma=ma+1
#print(num_of_devices_real+1)
#print('number of devices that are connected are' , num_of_devices_real+1)
f.close()

       





  







