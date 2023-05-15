def btrinpt(type,k,n):
    global mylist
    mylist=[]
    try:
        if type=="str":
            for i in range(0,n):
               ic=str(i)
               kf=str(k+ic+":")
               xu=str(input(kf))
               mylist.append(xu)
               return mylist    
        elif type=="int":
            for j in range(0,n):
             jc=str(j)
             kf=str(k+jc+":")
             xu=int(input(kf))
             mylist.append(xu)
             return mylist
        elif type=="mixed":
           for l in range(0,l):
              lc=str(l)
              kf=str(k+ic+":")
              xu=input(kf)
              mylist.append(xu)
              return mylist
    except: 
       print("Invalid type entered")