

import subprocess
command="arp-scan --retry=8 --ignoredups -I br0 --localnet"
rez=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

rez=str(rez)
l=rez.split()
l
h=list(l[11])
num=len(h)
i=0
sum=0
while i<num-1:
  if h[i]=='\\'
     if h[i+1]=='n'
       i=0
       sum=sum+1
else
i=i+1

print(sum)
f=1;
while f<sum+1
   i=0;

   y=zeros(17);

while i<num-1:
if h[i]=='\\'
  if h[i+1]=='t'
   j=0
   g=i+2
   while j<17
     y[j]=h[g]
      g=g+1
      j=j+1

   end
 f=f+1


print('the first mac address is  ' '.join(y)')-convert from an arry to string




   




