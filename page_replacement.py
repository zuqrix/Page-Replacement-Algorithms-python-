#God bless India
#author- Kushal(Zuqrix)
frames=[]
pgf=0   # Number of page faults variable
def base():
  #Reference string is randomly generated..reference string of own choice can be added
  ref=[]
  for i in range(20):  #reference string random generation
    ref.append(randint(0,9))
  revref=ref[::-1]     #Reverse reference string
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
  return no_frames#

#-------------FIFO-----------------  
def fifo(ref,num):
  pgf=0
  for i in range(num):
    frames.append(-1)
  marker=0
  i=0
  #first fill all the free frames and later page replacement by fifo
  while(marker!=num and i<len(ref)):
    if (ref[i] not in que):
      frames[marker]=ref[i]
      marker+=1
      pgf+=1
    i+=1
    print(que)
  marker=0
  for i in range(i,len(ref)):
    if(ref[i] not in que):
      pgf+=1
      frames[marker]=ref[i]
      marker=(marker+1)%num
    print(que)
  return pgf
  
#---------------LRU---------------
def lru(ref):
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
    print(que)
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
    print(que)
  return pgf
  
  
