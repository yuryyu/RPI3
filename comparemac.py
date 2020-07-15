
def compare_files():
  try:
    f=open("connected.txt","r")
    f_counter=0
    r=f.read()
    f_s=r.split("\n")

    for j in f_s:
        if j:
            f_counter=f_counter+1
    print('numbers of devices that are connected:' +str(f_counter))

    t=open("permissionlist.txt","r")
    t_counter=0
    t_read=t.read()
    t_s=t_read.split("\n")

    for y in t_s:
        if y:
            t_counter=t_counter+1
    print('number of permission list is:' +str(t_counter))
    #print(t_counter)

    t=open("permissionlist.txt","r")
    #a2 is an array of the permission list
    a2=t.readlines()
    print('Array of MAC address of permmision devices:' )
    print(a2)

    f=open("connected.txt","r")
    #a1 is an array of the connected devices
    a1=f.readlines()
    print('Array of MAC addresses of connected devices:')
    print(a1)

    t=open("admins.txt","r")
    #aa is an array of the admins list
    aa=t.readlines()
    print(aa)
    admin = 'None admin'
    for a in aa:
      if a in a1:
        admin='admin presented'
        break

    if len(list(set(a1)-set(a2)))==0:
      print('None detected')
      return 'None detected', admin
    else:
      print('Intruder detected')
      return 'Intruder' , admin  
  except:
    return 'None detected', admin


if __name__ == "__main__":
    try:
        print(compare_files()[1])
    except:
        pass