import re
import sys
import array
 
stack = [] 
commands = ['set_size','push','pop','print'] 
flag = False
stack_size = 0 
top = -1
bottom = 0
input = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')
for line in input: 
    if (line[len(line)-1]==" "): 
        output.write("error\n") 
    else: 
        if((re.match(r"set_size\s[0-9]*",line))or(re.match(r"push\s\w*",line))or(re.match(r"pop",line))or(re.match(r"print",line))):
                
                if(re.match(r"set_size\s[0-9]*",line)):
                    if(flag==False):
                        flag=True
                        stack_size=int(line[9:len(line)-1:1])
                        stack=[0]*stack_size
                    else:
                        output.write("error\n")
            
                if(re.match(r"push\s\w*",line)):
                    k=0
                    for i in line:
                        if(i==" "):
                            k=k+1
                    if (flag==False):
                        output.write("error\n")
                    else:
                        if((k==0)or(k>1)or(len(line)<=6)):
                                output.write("error\n")
                        else:
                            if (top + 1> stack_size - 1):
                                output.write("overflow\n")
                            else:
                                if ((k==1)and(len(line)>6)):
                                    num=line[5:len(line)-1:1]
                                    top=top+1
                                    stack[top]=num
                if((re.match(r"pop",line))):
                    if (flag==False):
                        output.write("error\n")
                    else:
                        if(len(line)==4):
                            if(top==-1):
                                output.write("underflow\n")
                            else:
                              
                                output.write(str(stack[0]))
                                output.write("\n")
                                top=top-1
                                i=len(stack)-1
                                buf=stack[i]
                                while(i!=-1):
                                    buf1=stack[i-1]
                                    stack[i-1]=buf
                                    buf=buf1
                                    i=i-1
									
								
                        else:
                            output.write("error\n")
                if(re.match(r"print",line)):
                    if(flag==False):
                        output.write("error\n")
                    else:
                        if((len(line)==6)or((len(line)==5))):
                            if(top==-1):
                                output.write("empty\n")
                            else:
                                output.write(" ".join(map(str,stack[0:top+1])))
                                output.write("\n")
                        else:
                            output.write("error\n")
        elif (line == "\n"):
            pass        
        else:
            output.write("error\n")
