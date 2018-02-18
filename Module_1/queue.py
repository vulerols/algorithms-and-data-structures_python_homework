# Задача про очередь
# Это как задача про стек, только про очередь.
# Реализуйте очередь, используя только массив.
# Ввод и вывод данных осуществляется через файлы. Имена входного и выходного файлов задаются через аргументы командной строки (первый и второй соответственно).

# Формат входных данных
# Во входном файле задаётся последовательность команд. Пустые строки игнорируются.
# Первая строка всегда содержит "set_size N", где N - максимальный размер очереди, целое число.
# Каждая последующая строка содержит ровно одну команду: push X, pop или print, где X - произвольная строка без пробелов.

# Формат результата
# Команда print выводит содержимое очередь (от головы к хвосту) одной строкой, значения разделяются пробелами. Если очередь пуста, то выводится "empty".
# В случае переполнения очереди выводится "overflow".
# Команда pop выводит элемент или "underflow", если очередь пуста.
# Память под очередь должна быть выделена не более одного раза, при вызове команды "set_size".
# В любой непонятной ситуации результатом работы любой команды будет "error".

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