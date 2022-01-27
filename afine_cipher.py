import math
def euclid3():
    r1=26
    r2=int(input("enter the key\n"))
    h=r1
    n=r2
    q=[]
    while(1):
        l=r1//r2
        q.append(l)
        p=r1%r2
        if(p==0):
            break
        else:
            r1=r2
            r2=p
    s1=1
   
    s2=0
    i=0
    while(i<len(q)):
        s=s1-q[i]*s2
        s1=s2
        s2=s
        i=i+1
    t1=0
    t2=1
    i=0
    while(i<len(q)):
        t=t1-q[i]*t2
        t1=t2
        t2=t
        i=i+1

    r1=h
    r2=n
    o=int(math.gcd(r1,r2))
    f=(s1*r1)+(t1*r2)
    if(math.gcd(r1,r2)==1):
        if(t1>=0):
            return t1
        else:
            while 1:
                t1=t1+26
                if(t1>=0):
                    break
            return t1
    else:
        return 0


def decry():
    p=[]
    while(1):
        print("enter the /x if you dont more messages")
        print("enter the string which you decrypted")
        i=input()
        if(i=="/x"):
            break
        else:
            # print(i)
            p.append(i)
            continue
    while 1:
        j=euclid3()
        j=int(j)
        if(j==0):
            print("your key have no multiplicative inverse posible")
            print("please enter another key")
        if(j!=0):
            break
    if(j!=0):
        print("enter the key2")
        ke2=int(input())
        n=0
        boo=True
        che=[]
        k=0
        while(k<len(p)):
            n=0
            u=p[k]
            while(n<len(u)):
                
                boo=u[n].islower()
                # if(u[n]=="?"):
                #     che.append(" ")
                if(boo==True):
                    y=ord(u[n])
                    y=int(y)
                    y=y-97
                    y=(y-ke2)*j
                    y=y%26
                    y=y+97
                    f=chr(y)
                    che.append(f)
                elif(boo==False):
                    y=ord(u[n])
                    y=int(y)
                    y=y-65
                    y=(y-ke2)*j
                    y=y%26
                    y=y+65
                    f=chr(y)
                    che.append(f)
                
                n=n+1
            k=k+1
        k=0
        print("your decrypted message is "+"".join(che))
        return "".join(che)
def encryp():
    a=[]
    while(1):
        print("enter the string which you encrypted")
        print("enter the /x if you dont more messages")
        i=input()
        if(i=="/x"):
            break
        else:
 
            a.append(i)
            continue
    print("enter the key")
    ke=int(input())
    print("enter the key2")
    ke2=int(input())
    remove_str=" "
    r=""
    k=0
    while(k<len(a)):
        j=a[k]
        r=j
        for character in remove_str:
            r=r.replace(character,"")
            a[k]=r
        # print(a[k])
        k=k+1
    n=0
    boo=True
    che=[]
    k=0
    while(k<len(a)):
        n=0
        p=a[k]
        while(n<len(p)):
            boo=p[n].islower()
            # if(p[n]==" "):
                # che.append("?")
            if(boo==True):
                y=ord(p[n])
                y=int(y)
                y=y-97
                y=((y*ke)+ke2)
                y=y%26
                y=y+97
                f=chr(y)
                che.append(f)
            elif(boo==False):
                y=ord(p[n])
                y=int(y)
                y=y-65
                y=((y*ke)+ke2)
                y=y%26
                y=y+65
                f=chr(y)
                che.append(f)
            
            n=n+1
        k=k+1
    k=0
    print("your encrpted message is "+"".join(che))
    return " ".join(che)
while(1):
    print("enter 1 for encrypted the message")
    print("enter 2 for decypted the message")
    print("enter 3 exit")
    op=int(input())
    if(op==1):
        encryp()
    elif(op==2):
        decry()
    elif(op==3):
        break
    else:
        print("please enter correct option")