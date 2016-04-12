#Jai Hind
#--- Code is pretty long.. REFER page_replacement.py .....Its an improvised code
#random number generation
from random import randint

bel=[-1,-1,-1,-1]
sec=[-1,-1]
def base():
    ref,revref=[],[]
    #for i in range(20):
     #   ref.append(randint(1,9))
    ref=[1,2,3,4,1,2,5,1,2,3,4,5]
    revref=ref[::-1]
    print("Length of string"+str(len(ref)))
    #for i in range(20):
    revref=ref[::-1]
    print(ref)
    print(revref)
    while 1:
        print("1:FIFO 2:lru 3:optimal 4:second chance(changes for repeated pages) 5:second chance(no change for repeated pages) ")
        ch=int(input())
        if(ch==1):
            print("1:reference string 2:reverse ref string 3:belady's anamoly")
            choice=int(input())
            if(choice==1):
                pgf=fifo(ref)
                print("No. of page faults in fifo for 3 frames = " + str(pgf))
                pgf=fifo_bel(ref)
                print("No. of page faults in fifo for 4 frames = " + str(pgf))
                pgf=fifo_5(ref)
                print("No. of page faults in fifo for 5 frames = "+ str(pgf))
            elif(choice==2):
                pgf=fifo(revref)
                print("No. of page faults in fifo for 3 frames(rev string)= " + str(pgf))
                pgf=fifo_bel(revref)
                print("No. of page faults in fifo for 4 frames(rev string) = " + str(pgf))
                pgf=fifo_5(revref)
                print("No. of page faults in fifo for 5 frames (rev string)= "+ str(pgf))
            elif(choice==3):
                tempo=[]
                pgf=fifo(ref)
                tempo.append(pgf)
                print("No. of page faults in fifo for 3 frames= " +str(pgf))
                pgf=fifo_bel(ref)
                tempo.append(pgf)
                print("No. of page faults in fifo for 4 frames = " + str(pgf))
                pgf=fifo_5(ref)
                tempo.append(pgf)
                print("No. of page faults in fifo for 5 frames = "+ str(pgf))
                if(tempo[0]>=tempo[1] and tempo[1]>=tempo[2]):
                    print("there is no Belady's anamoly here")
                else:
                    print("there is Belady's anamoly here")

                    
        elif(ch==2):
            print("1:reference string 2:reverse ref string 3:belady's anamoly")
            choice=int(input())
            if(choice==1):
                pgf=lru(ref)
                print("No. of page faults in lru for 3 frames = " + str(pgf))
                pgf=lru_bel(ref)
                print("No. of page faults in lru for 4 frames = " + str(pgf))
                pgf=lru_5(ref)
                print("No. of page faults in lru for 5 frames = "+ str(pgf))
            elif(choice==2):
                pgf=lru(revref)
                print("No. of page faults in lru for 3 frames(rev string)= " + str(pgf))
                pgf=lru_bel(revref)
                print("No. of page faults in lru for 4 frames(rev string) = " + str(pgf))
                pgf=lru_5(revref)
                print("No. of page faults in lru for 5 frames (rev string)= "+ str(pgf))
            elif(choice==3):
                tempo=[]
                pgf=lru(ref)
                tempo.append(pgf)
                print("No. of page faults in lru for 3 frames= " +str(pgf))
                pgf=lru_bel(ref)
                tempo.append(pgf)
                print("No. of page faults in lru for 4 frames = " + str(pgf))
                pgf=lru_5(ref)
                tempo.append(pgf)
                print("No. of page faults in lru for 5 frames = "+ str(pgf))
                if(tempo[0]>=tempo[1] and tempo[1]>=tempo[2]):
                    print("there is no Belady's anamoly here")
                else:
                    print("there is Belady's anamoly here")             
                
                
        elif(ch==4):
            print("1:reference string 2:reverse ref string 3:belady's anamoly")
            choice=int(input())
            if(choice==1):
                pgf=sec(ref)
                print("No. of Page faults in Second chance for 3 frames= "+str(pgf))
                pgf=sec_bel(ref)
                print("No. of page faults in second chance for 4 frames = " +str(pgf))
                pgf=sec_5(ref)
                print("No. of page faults in second chance for 5 frames = "+ str(pgf))
            elif(choice==2):
                pgf=sec(revref)
                print("No. of Page faults in Second chance for 3 frames = "+str(pgf))
                pgf=sec_bel(revref)
                print("No. of page faults in second chance for 4 frames = " +str(pgf))
                pgf=sec_5(revref)
                print("No. of page faults in second chance for 5 frames = "+ str(pgf))
            elif(choice==3):
                tempo=[-1,-1,-1]
                pgf=sec(ref)
                tempo[0]=pgf
                print("No. of page faults in second chance for 3 frames = " +str(pgf))
                pgf=sec_bel(ref)
                tempo[1]=pgf
                print("No. of page faults in second chance for 4 frames = " +str(pgf))
                pgf=sec_5(ref)
                tempo[2]=pgf
                print("No. of page faults in second chance for 5 frames = "+ str(pgf))
                if(tempo[0]>=tempo[1] and tempo[1]>=tempo[2]):
                    print("there is no Belady's anamoly here")
                else:
                    print("there is Belady's anamoly here")

        elif(ch==5):
            print("1:reference string 2:reverse ref string 3:belady's anamoly")
            choice=int(input())
            if(choice==1):
                pgf=sec2(ref)
                print("No. of Page faults in Second chance for 3 frames= "+str(pgf))
                pgf=sec2_bel(ref)
                print("No. of page faults in second chance for 4 frames = " +str(pgf))
                pgf=sec2_5(ref)
                print("No. of page faults in second chance for 5 frames = "+ str(pgf))
            elif(choice==2):
                pgf=sec2(revref)
                print("No. of Page faults in Second chance for 3 frames = "+str(pgf))
                pgf=sec2_bel(revref)
                print("No. of page faults in second chance for 4 frames = " +str(pgf))
                pgf=sec2_5(revref)
                print("No. of page faults in second chance for 5 frames = "+ str(pgf))
            elif(choice==3):
                tempo=[]
                pgf=sec2(ref)
                tempo.append(pgf)
                print("No. of page faults in second chance for 3 frames = " +str(pgf))
                pgf=sec2_bel(ref)
                tempo.append(pgf)
                print("No. of page faults in second chance for 4 frames = " +str(pgf))
                pgf=sec2_5(ref)
                tempo.append(pgf)
                print("No. of page faults in second chance for 5 frames = "+ str(pgf))
                if(tempo[0]>=tempo[1] and tempo[1]>=tempo[2]):
                    print("there is no Belady's anamoly here")
                else:
                    print("there is Belady's anamoly here")
        elif(ch==3):
            print("1:reference string 2:reverse ref string 3:belady's anamoly")
            choice=int(input())
            if(choice==1):
                pgf=opt(ref)
                print("No. of Page faults in Optimal for 3 frames = "+str(pgf))
                pgf=opt_bel(ref)
                print("No. of page faults in Optimal for 4 frames = " +str(pgf))
                pgf=opt_5(ref)
                print("No. of page faults in optimal for 5 frames = " +str(pgf))
            elif(choice==2):
                pgf=opt(revref)
                print("No. of Page faults in Optimal for 3 frames(rev)= "+str(pgf))
                pgf=opt_bel(revref)
                print("No. of page faults in Optimal for 4 frames(rev) = " +str(pgf))
                pgf=opt_5(revref)
                print("No. of page faults in optimal for 5 frames (rev)= " +str(pgf))
            elif(choice==3):
                pgf=opt(ref)
                print("No. of page faults in Optimal for 3 frames = " +str(pgf))
                pgf=opt_bel(ref)
                print("No. of page faults in Optimal for 4 frames = " +str(pgf))
                pgf=opt_5(ref)
                print("No. of page faults in optimal for 5 frames = " +str(pgf))
                print("there is no Belady's anamoly here")
        else:
            exit()

def fifo(ref):
    pgf=0
    que=[-1,-1,-1]
    marker=0
    i=0
    while(marker!=3 and i<len(ref)):
        if (ref[i] not in que):
            que[marker]=ref[i]
            marker+=1
            pgf+=1
        i+=1
    marker=0
    for i in range(i,len(ref)):
        if(ref[i] not in que):
            pgf+=1
            que[marker]=ref[i]
            marker=(marker+1)%3
    return pgf

def fifo_bel(ref):
    bel=[-1,-1,-1,-1]
    pgf=0
    marker=0
    i=0
    while(marker!=4 and i<len(ref)):
        if (ref[i] not in bel):
            bel[marker]=ref[i]
            marker+=1
            pgf+=1
        i+=1
    marker=0
    for i in range(i,len(ref)):
        if(ref[i] not in bel):
            pgf+=1
            bel[marker]=ref[i]
            marker=(marker+1)%4
    return pgf

def fifo_5(ref):
    bel=[-1,-1,-1,-1,-1]
    pgf=0
    marker=0
    i=0
    while(marker!=5 and i<len(ref)):
        if (ref[i] not in bel):
            bel[marker]=ref[i]
            marker+=1
            pgf+=1
        i+=1
    marker=0
    for i in range(i,len(ref)):
        if(ref[i] not in bel):
            pgf+=1
            bel[marker]=ref[i]
            marker=(marker+1)%5
    return pgf
def opt(ref):
    que=[-1,-1,-1]
    pgf=0
    marker=0
    i=0
    while(marker!=3 and i<len(ref)):
        if (ref[i] not in que):
            que[marker]=ref[i]
            marker+=1
            pgf+=1
        i+=1
    while(i<len(ref)):
        if(ref[i] not in que):
            value=find_opt(que,ref,i)
            que[value]=ref[i]
            pgf+=1
        i+=1
    return pgf

def opt_bel(ref):
    bel=[-1,-1,-1,-1]
    pgf=0
    marker=0
    i=0
    while(marker!=4 and i<len(ref)):
        if (ref[i] not in bel):
            bel[marker]=ref[i]
            marker+=1
            pgf+=1
        i+=1
    while(i<len(ref)):
        if(ref[i] not in bel):
            value=find_opt_bel(bel,ref,i)
            bel[value]=ref[i]
            pgf+=1
        i+=1
    return pgf

def opt_5(ref):
    bel=[-1,-1,-1,-1,-1]
    pgf=0
    marker=0
    i=0
    while(marker!=5 and i<len(ref)):
        if (ref[i] not in bel):
            bel[marker]=ref[i]
            marker+=1
            pgf+=1
        i+=1
    while(i<len(ref)):
        if(ref[i] not in bel):
            value=find_opt_5(bel,ref,i)
            bel[value]=ref[i]
            pgf+=1
        i+=1
    return pgf

def find_opt_5(bel,ref,i):
    array=[0,0,0,0,0]
    ret_val=-1
    last=-1
    temp=-1
    ret_val=-1
    for j in range(5):
        if bel[j] in ref[i:]:
            array[j]=1
            temp=ref[i:].index(bel[j])
        if temp>last:
            last=temp
            ret_val=j
    if array.count(1)==0:
        return 0
    elif array.count(1)==1:
        x=array.index(1)
        if(x==0):
            return 1
        else:
            return 0
    elif array.count(1)==2:
        x=0
        for k in range(5):
            if(array[k]==0):
                x=k
        return x
    elif array.count(1)==3:
        x=0
        for k in range(5):
            if(array[k]==0):
                x=k
        return x
    
    elif array.count(1)==4:
        x=array.index(0)
        if(x==0):
            return 0
        elif(x==1):
            return 1
        elif(x==2):
            return 2
        elif(x==3):
            return 3
        else:
            return 4
    else:
        return ret_val

def find_opt(que,ref,i):
    array=[0,0,0]
    ret_val=-1
    last=-1
    temp=-1
    ret_val=-1
    for j in range(3):
        if que[j] in ref[i:]:
            array[j]=1
            temp=ref[i:].index(que[j])
        if temp>last:
            last=temp
            ret_val=j
    if array.count(1)==0:
        return 0
    elif array.count(1)==1:
        x=array.index(1)
        if(x==0):
            return 1
        elif(x==1):
            return 0
        else:
            return 0
    elif array.count(1)==2:
        x=array.index(0)
        if(x==0):
            return 0
        elif(x==1):
            return 1
        elif(x==2):
            return 2
    else:
        return ret_val

def find_opt_bel(bel,ref,i):
    array=[0,0,0,0]
    ret_val=-1
    last=-1
    temp=-1
    ret_val=-1
    for j in range(4):
        if bel[j] in ref[i:]:
            array[j]=1
            temp=ref[i:].index(bel[j])
        if temp>last:
            last=temp
            ret_val=j
    if array.count(1)==0:
        return 0
    elif array.count(1)==1:
        x=array.index(1)
        if(x==0):
            return 1
        else:
            return 0
    elif array.count(1)==2:
        x=0
        for k in range(4):
            if(array[k]==0):
                x=k
        return x
    elif array.count(1)==3:
        x=array.index(0)
        if(x==0):
            return 0
        elif(x==1):
            return 1
        elif(x==2):
            return 2
        else:
            return 3
    else:
        return ret_val


def sec(ref):
    pgf=0
    que=[-1,-1,-1]
    valid=[0,0,0]
    i=0
    count=0
    while( i<len(ref)):
        if (ref[i] not in que):
            flag=True
            while flag:
                if valid[count]==0:
                    que[count]=ref[i]
                    flag=False
                    valid[count]=1
                    count=(count+1)%3
                    pgf+=1
                elif valid[count]==1:
                    valid[count]=0
                    count=(count+1)%3            
           
        elif(ref[i] in que):
            ind=que.index(ref[i])
            if(valid[ind]==1):
                valid[ind]=0
            elif valid[ind]==0:
                valid[ind]=1
        i+=1
    return pgf


def sec_bel(ref):
    pgf=0
    que=[-1,-1,-1,-1]
    valid=[0,0,0,0]
    i=0
    count=0
    while( i<len(ref)):
        if (ref[i] not in que):
            flag=True
            while flag:
                if valid[count]==0:
                    que[count]=ref[i]
                    valid[count]=1
                    flag=False
                    pgf+=1
                elif valid[count]==1:
                    valid[count]=0
                    count=(count+1)%4            
           
        elif(ref[i] in que):
            ind=que.index(ref[i])
            if(valid[ind]==1):
                valid[ind]=0
            elif valid[ind]==0:
                valid[ind]=1
        i+=1

    return pgf


def sec_5(ref):
    pgf=0
    que=[-1,-1,-1,-1,-1]
    valid=[0,0,0,0,0]
    i=0
    count=0
    while( i<len(ref)):
        if (ref[i] not in que):
            flag=True
            while flag:
                if valid[count]==0:
                    que[count]=ref[i]
                    valid[count]=1
                    flag=False
                    pgf+=1
                elif valid[count]==1:
                    valid[count]=0
                    count=(count+1)%5            
           
        elif(ref[i] in que):
            ind=que.index(ref[i])
            if(valid[ind]==1):
                valid[ind]=0
            elif valid[ind]==0:
                valid[ind]=1
        i+=1

    return pgf
    
def sec2(ref):
    pgf=0
    que=[-1,-1,-1]
    valid=[0,0,0]
    i=0
    count=0
    while( i<len(ref)):
        if (ref[i] not in que):
            flag=True
            while flag:
                if valid[count]==0:
                    que[count]=ref[i]
                    flag=False
                    valid[count]=1
                    count=(count+1)%3
                    pgf+=1
                elif valid[count]==1:
                    valid[count]=0
                    count=(count+1)%3         
           
        i+=1
    return pgf

def sec2_bel(ref):
    pgf=0
    que=[-1,-1,-1,-1]
    valid=[0,0,0,0]
    i=0
    count=0
    while( i<len(ref)):
        if (ref[i] not in que):
            flag=True
            while flag:
                if valid[count]==0:
                    que[count]=ref[i]
                    flag=False
                    valid[count]=1
                    count=(count+1)%4
                    pgf+=1
                elif valid[count]==1:
                    valid[count]=0
                    count=(count+1)%4            
           
        i+=1
    return pgf

def sec2_5(ref):
    pgf=0
    que=[-1,-1,-1,-1,-1]
    valid=[0,0,0,0,0]
    i=0
    count=0
    while( i<len(ref)):
        if (ref[i] not in que):
            flag=True
            while flag:
                if valid[count]==0:
                    que[count]=ref[i]
                    flag=False
                    valid[count]=1
                    count=(count+1)%5
                    pgf+=1
                elif valid[count]==1:
                    valid[count]=0
                    count=(count+1)%5            
           
        i+=1
    return pgf

def lru(ref):
    pgf=0
    que=[-1,-1,-1]
    marker=0
    i=0
    while(marker!=3 and i<len(ref)):
        if (ref[i] not in que):
            que[marker]=ref[i]
            marker+=1
            pgf+=1
        i+=1
    while(i<len(ref)):
        if(ref[i] not in que):
            least=-1
            ret_val=-1
            for j in range(3):
                x=ref[i::-1].index(que[j])
                if(x>least):
                    least=x
                    ret_val=que[j]
            x=que.index(ret_val)
            que[x]=ref[i]
            pgf+=1
        i+=1
    return pgf
                    
def lru_bel(ref):
    pgf=0
    que=[-1,-1,-1,-1]
    marker=0
    i=0
    while(marker!=4 and i<len(ref)):
        if (ref[i] not in que):
            que[marker]=ref[i]
            marker+=1
            pgf+=1
        i+=1
    while(i<len(ref)):
        if(ref[i] not in que):
            least=-1
            ret_val=-1
            for j in range(4):
                x=ref[i::-1].index(que[j])
                if(x>least):
                    least=x
                    ret_val=que[j]
            x=que.index(ret_val)
            que[x]=ref[i]
            pgf+=1
        i+=1
    return pgf                
    
def lru_5(ref):
    pgf=0
    que=[-1,-1,-1,-1,-1]
    marker=0
    i=0
    while(marker!=5 and i<len(ref)):
        if (ref[i] not in que):
            que[marker]=ref[i]
            marker+=1
            pgf+=1
        i+=1
    while(i<len(ref)):
        if(ref[i] not in que):
            least=-1
            ret_val=-1
            for j in range(5):
                x=ref[i::-1].index(que[j])
                if(x>least):
                    least=x
                    ret_val=que[j]
            x=que.index(ret_val)
            que[x]=ref[i]
            pgf+=1
        i+=1
    return pgf        
    
    
        
        
                
                


        
    
            
    
        
    
    
    
    

        

