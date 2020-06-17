
def main():
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



    s=0
    while s<f_counter:
        u=0
        while u<t_counter:
            if s!=f_counter:
                if a1[s]==a2[u]:
                    s=s+1
                    u=0
                else:
                    u=u+1
                    if u==t_counter:
                        print('An unauthorized person connected to the network')
                        print(a1[s])
                        return True
                        if s!=f_counter:
                            s=s+1
    print('done')
    return False


if __name__ == "__main__":
    main()
   