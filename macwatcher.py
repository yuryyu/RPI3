import subprocess
import numpy as np
from rpi_manager import *
import comparemac
import time


def wait_timeout(proc, seconds):
   """Wait for a process to finish, or raise exception after timeout"""
   start = time.time()
   end = start + seconds
   interval = min(seconds / 1000.0, .25)
   while True:
      result = proc.poll()
      if result is not None:
         return result
      if time.time() >= end:
         return 1
      time.sleep(interval)

def scan_net():
   command = "sudo arp-scan --retry=8 --ignoredups -I " + netinterface + " --localnet"
   rez = subprocess.Popen(command, shell=True,   
                                       stdout=subprocess.PIPE).stdout.read()   
   rez=str(rez)
   lns= rez.split('\\n')   
   macs=[]
   for ln in lns:
      if netstart not in ln:
         continue
      spln=ln.split('\\t')[1]
      print(spln)
      macs.append(spln) 
   write2file(macs)  

def write2file(maclist,filename ='connected.txt'):    
   with open(filename, 'w') as f:
    for item in maclist:
        f.write("%s\n" % item)

def send2manager(client, comp):
   # mqtt client
   tnow = time.localtime(time.time())
   msg = 'Watcher Msg: ' + str(comp) + ' at ' + time.asctime(tnow)
   client.publish(sub_topic[1], msg)
   print('message ' + msg + ' sent')
   pass

if __name__ == "__main__":
   cname = "RPI3_watcher-"
   client = client_init(cname)
   try:
      while conn_time == 0:
         #scan_net()
         time.sleep(10)
         print('main procedure ended peacefully')
         send2manager(client, comparemac.compare_files()[1])
         print('send2manager procedure for admin presence update ended peacefully, next loop started')
         send2manager(client, comparemac.compare_files()[0])
         print('send2manager procedure for intruder presence update ended peacefully, next loop started')
   except KeyboardInterrupt:
      client.disconnect()  # disconnect from broker
      print("interrrupted by keyboard")
   finally: 
      client.disconnect()
