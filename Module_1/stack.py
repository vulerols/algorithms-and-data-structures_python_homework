import re
import sys
import array
 
stack = [] 
commands = ['set_size','push','pop','print'] 
flag = False
stack_size = 0 
top = -1 
for line in sys.stdin: 
    if (line[len(line)-1]==" "): 
        print("error") 
    else: 
        if((re.match(r"set_size\s[0-9]*",line))or(re.match(r"push\s\w*",line))or(re.match(r"pop",line))or(re.match(r"print",line))):
                
                if(re.match(r"set_size\s[0-9]*",line)):
                    if(flag==False):
                        flag=True
                        stack_size=int(line[9:len(line)-1:1])
                        stack=[0]*stack_size
                        
                    else:
                        print("error")
            
                if(re.match(r"push\s\w*",line)):
                    k=0
                    for i in line:
                        if(i==" "):
                            k=k+1
                    if (flag==False):
                        print("error")
                    else:
                        if((k==0)or(k>1)or(len(line)<=6)):
                                print("error")
                        else:
                            if (top + 1> stack_size - 1):
                                print("overflow")
                            else:
                                if ((k==1)and(len(line)>6)):
                                    num=line[5:len(line)-1:1]
                                    top=top+1
                                    stack[top]=num
                                    
                if((re.match(r"pop",line))):
                    if (flag==False):
                        print("error")
                    else:
                        if(len(line)==4):
                            if(top==-1):
                                print("underflow")
                            else:
                                print(stack[top])
                                top=top-1
                        else:
                            print("error")
                if(re.match(r"print",line)):
                    if(flag==False):
                        print("error")
                    else:
                        if(len(line)==6):
                            if(top==-1):
                                print("empty")
                            else:
                                print(" ".join(map(str,stack[0:top+1])))
                        else:
                            print("error")
        elif (line == "\n"):
            pass        
        else:
            print("error")
