import subprocess




command="arp-scan --retry=8 --ignoredups -I br0 --localnet"
rez=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
print(rez)
