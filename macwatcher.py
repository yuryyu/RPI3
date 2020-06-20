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
   command = "arp-scan --retry=8 --ignoredups -I " + netinterface + " --localnet"
   rez = wait_timeout(subprocess.Popen(command, shell=True,
   stdout=subprocess.PIPE), waittime)
                                       #stdout=subprocess.PIPE).stdout.read(), waittime)
   if rez==1:
      return
   rez = str(rez)   
   l = rez.split()
   num = len(l)
   i = 0
   for l[i] in l:
      if l[i] != 'packets':
         i = i+1
      else:
         num_of_devices = l[i-1]
         break
   num_of_devices = int(num_of_devices)
   ma = 14
   print(l[ma])
   f = open('connected.txt', 'w')
   f.write(l[ma])
   f.write('\n')
   ma = ma+1
   num_of_devices_real = 0
   while (l[ma] != num_of_devices) & (l[ma+1] != 'packets'):
      y = list(l[ma])
      if y[2] == ':':
         f.write(l[ma])
         f.write('\n')
         print(l[ma])
         ma = ma+1
         num_of_devices_real = num_of_devices_real+1
      else:
         ma = ma+1
   f.close()

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
         scan_net()
         print('main procedure ended peacefully')
         send2manager(client, comparemac.compare_files())
         print('send2manager procedure ended peacefully, next loop started')
   except KeyboardInterrupt:
      client.disconnect()  # disconnect from broker
      print("interrrupted by keyboard")