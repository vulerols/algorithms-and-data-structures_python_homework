import sys
 
graf_type=""
start=0
searh_type=""
flag = False
keys = []
guest = []
iter_guest=[]
graf = dict()
k = 0

for line in sys.stdin:
    splitted = line.split()
    if(flag==False):
        graf_type=splitted[0]
        start=splitted[1]
        searh_type=splitted[2]
        flag = True
    if((flag==True) and (len(splitted)==2)):
        if (graf_type=="d"):
            key=splitted[0]
            if(key not in graf):
                graf[key]=[]
            if(splitted[1] not in graf):
                graf[splitted[1]]=[]
            graf[key].append(splitted[1])
        if (graf_type=="u"):
            key=splitted[0]
            if(key not in graf):
                graf[key]=[]
            if(splitted[1] not in graf):
                graf[splitted[1]]=[]
            graf[key].append(splitted[1])
            graf[splitted[1]].append(splitted[0])

for i in graf:
    graf[i].sort()#graph is sorted in the lexicographic order
#print (graf)
if(searh_type=="b"): #search in width
    guest = []  #task list
    guest_end = [start] #visited vertices
    graf[start].sort() #adjacent vertices sorted in the lexicographic order
    for i in graf[start]:
        guest.append(i) # fill the task list
    buf_guest = [] #the list of neighbors
    while (len(guest) > 0): #performed the bypass adjacent vertices
        go = guest.pop(0) 
        while ((go in guest_end) and (len(guest) > 0)):
            go = guest.pop(0)
        guest_end.append(go)

        for i in graf[go]:
            if i in guest_end:
                pass
            elif i in guest:
                pass
            else:
                buf_guest.append(i)
        guest.extend([i for i in buf_guest])
        del buf_guest[:]
    for i in guest_end: #output all visited vertices
        print(i)


if(searh_type=="d"): #search in deep
    guest = [] #task list
    guest_end = [start] #visited vertices
    guest.extend(graf[start])
    guest.reverse()
    buf_guest = [] #the list of neighbors
    while (len(guest) > 0):
        go = guest.pop() #current node
        while ((go in guest_end) and (len(guest) > 0)):
            go = guest.pop()
        if go not in guest_end:
            guest_end.append(go) #add the current vertex as passed
        for i in graf[go]:
            if i in guest_end: #continue the cycle bypass
                pass
            elif i in guest: #remove the vertices of the task list
                guest.remove(i)
                buf_guest.append(i)
            else:
                buf_guest.append(i)
        buf_guest.reverse()
        guest.extend([i for i in buf_guest]) # add in task list deleted vertices
        del buf_guest[:]
    for i in guest_end:
        print(i)
 #output all visited vertices
