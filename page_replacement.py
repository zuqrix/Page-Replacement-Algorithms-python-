#God bless India
#author- Kushal(Zuqrix)
from random import randint

def base():
  #Reference string is randomly generated..reference string of own choice can be added
  ref=[]
  for i in range(20):  #reference string random generation
    ref.append(randint(0,9))
  revref=ref[::-1]     #Reverse reference string
  print("reference string ")
  print(ref)
  print(revref)
  while 1:
    print(" 1: FIFO 2: LRU 3: Optimal 4: Second Chance 5:exit ")
    ch=int(input())
    if ch==1:
      print(" 1: FIFO on reference string 2:FIFO on reverse reference string 3:Show Belady's anamoly ")
      sub_choice=int(input())
      if sub_choice==1:
        num=user_input()
        pgf=fifo(ref,num)
        print("No. of Page faults- FIFO " + str(pgf))
      elif sub_choice==2:
        num=user_input()
        pgf=fifo(revref,num)
        print("No. of Page faults- FIFO(reverse string) " + str(pgf))
      elif sub_choice==3:
        print("Enter 3 different no. of frames to check belady's anamoly")
        #Show belady's anamoly for 3 different no. of frames
        bel=[]
        for i in range(3):
          print("Please enter")
          bel.append(int(input()))
        for i in range(3):
          pgf=fifo(ref,bel[i])
          print("No. of page faults for " + str(bel[i]) +" no. of frames is "+ str(pgf))
      else:
        print("invalid choice")
    
    elif ch==2:
      print(" 1: LRU on reference string 2:LRU on reverse reference string 3:Show Belady's anamoly ")
      sub_choice=int(input())
      if sub_choice==1:
        num=user_input()
        pgf=lru(ref,num)
        print("No. of Page faults- lru " + str(pgf))
      elif sub_choice==2:
        num=user_input()
        pgf=lru(revref,num)
        print("No. of Page faults- lru(reverse string) " + str(pgf))
      elif sub_choice==3:
        print("Enter 3 different no. of frames to check belady's anamoly")
        #Show belady's anamoly for 3 different no. of frames
        bel=[]
        for i in range(3):
          print("Please enter")
          bel.append(int(input()))
        for i in range(3):
          pgf=lru(ref,bel[i])
          print("No. of page faults for " + str(bel[i]) +" no. of frames is "+ str(pgf))
      else:
        print("invalid choice")
    
    elif ch==3:
      print(" 1: OPT on reference string 2:OPT on reverse reference string 3:Show Belady's anamoly ")
      sub_choice=int(input())
      if sub_choice==1:
        num=user_input()
        pgf=opt(ref,num)
        print("No. of Page faults- OPT " + str(pgf))
      elif sub_choice==2:
        num=user_input()
        pgf=opt(revref,num)
        print("No. of Page faults- OPT(reverse string) " + str(pgf))
      elif sub_choice==3:
        print("Enter 3 different no. of frames to check belady's anamoly")
        #Show belady's anamoly for 3 different no. of frames
        bel=[]
        for i in range(3):
          print("Please enter")
          bel.append(int(input()))
        for i in range(3):
          pgf=opt(ref,bel[i])
          print("No. of page faults for " + str(bel[i]) +" no. of frames is "+ str(pgf))
      else:
        print("invalid choice")
    
    elif ch==5:
      exit()
    
    else:
      print("Invalid choice")
      
        
def user_input():
  print(" How many frames do you wish to use ")
  no_frames=int(input())
  return no_frames 

#-------------FIFO-----------------  
def fifo(ref,num):
  frames=[]
  pgf=0
  for i in range(num):
    frames.append(-1)
  marker=0
  i=0
  #first fill all the free frames and later page replacement by fifo
  while(marker!=num and i<len(ref)):
    if (ref[i] not in frames):
      frames[marker]=ref[i]
      marker+=1
      pgf+=1
    i+=1
    print(frames)
  marker=0
  for i in range(i,len(ref)):
    if(ref[i] not in frames):
      pgf+=1
      frames[marker]=ref[i]
      marker=(marker+1)%num
    print(frames)
  frames=[]
  return pgf
  
#---------------LRU---------------
def lru(ref):
  frames=[]
  pgf=0
  for i in range(num):
    frames.append(-1)
  marker=0
  i=0
  while(marker!=num and i<len(ref)):
    if (ref[i] not in frames):
      frames[marker]=ref[i]
      marker+=1
      pgf+=1
    i+=1
    print(frames)
  while(i<len(ref)):
    if(ref[i] not in frames):
      least=-1
      ret_val=-1
      for j in range(num):
        x=ref[i::-1].index(que[j])
        if(x>least):
          least=x
          ret_val=frames[j]
      x=frames.index(ret_val)
      frames[x]=ref[i]
      pgf+=1
    i+=1
    print(frames)
  frames=[]
  return pgf
  
#-----------OPT--------
def opt(ref,num):
  frames=[]
  for i in range(num):
    frames.append(-1)
  pgf,marker,i=0,0,0
  while(marker!=num and i<len(ref)):
    if (ref[i] not in frames):
      frames[marker]=ref[i]
      marker+=1
      pgf+=1
    i+=1
    print(frames)
  while(i<len(ref)):
    if(ref[i] not in frames):
      value=find_opt(num,ref,i)
      frames[value]=ref[i]
      pgf+=1
    i+=1
    print(frames)
  frames=[]  
  return pgf
  
#Optimal page selection

def find_opt(num,ref,i):
  array=[]
  for i in range(num):
    array.append(0)
  ret_val,last,temp=-1,-1,-1
  for j in range(num):
    if frames[j] in ref[i:]:
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
    else:
      return 0
  elif array.count(1)>1 and array.count(1)<num-1:
    x=array.index(0)
    return x
  elif array.count(1)==num-1:
    x=array.index(0)
    return x
  else:
    return ret_val
  
  
  
  
