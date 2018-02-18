# Сумасшедший богач
# Один сумасшедший богач на старости лет впал в маразм и стал еще более сумасшедшим. Он решил отдать половину своих богатств тому, 
# кто выиграет в математической игре.
# Правила игры: изначально каждый игрок начинает с нулевой суммой. Он может либо получить у богача 1 миллион сантиков, 
# либо отдать ему 1 миллион сантиков, либо получить от богача ту же сумму, которая есть у него сейчас.
# Выигрывает тот, кто за минимальное количество действий наберет сумму, равную половине состояния богача.
# На беду других игроков, нашелся человек, который что-то слышал про жадные алгоритмы и двоичную систему счисления (возможно это вы).

# Формат входных данных
# В стандартном потоке записано единственное натуральное число - размер половины состояния богача (в миллионах).

# Формат результата
# Каждая строка выхода содержит ровно одну операцию (inc, dec или dbl) из кратчайшей последовательности действий для победы.
# Если кто-то решил отнимать деньги у умалишенных людей - значит, он очень жадный.
# Поэтому если решений несколько, выведите то, в котором больше операций удвоения суммы 
# (и отдавать деньги невменяемым людям стоит только при крайней необходимости).
# Результат работы программы выводится в стандартный поток вывода.

import re 
import sys

start = 0
step = []
step1 = []
flag1 = False 
flag2 = False
clear = False
for line in sys.stdin:
    parser = re.findall(r'\d+',line)
    start = int(parser.pop())


start1 = start

while (start != 0):
    if (start % 2 == 0):
        start = start/2
        step.append("dbl")

    if (start == 1):
        step.append("inc")
        start = start - 1
		
    if (start % 2 == 1):
        
        parser1 = re.findall(r'\d',bin(int(start+1)))
        
        parser2 = re.findall(r'\d',bin(int(start-1)))

        if (clear == False):
            parser1.pop(0)
            parser2.pop(0)
            clear = True
        it1 = 0
        it2 = 0
        
        for i in parser1:
            if (int(i) == 1):
                it1 = it1 + 1
        for j in parser2:
            if (int(j) == 1):
                it2 = it2 + 1
        
        if (it1 < it2):
            step.append("dec")
            start = start + 1
            

        if (it1 == it2):
            ps1 = re.findall(r'\d',bin(int(start+1)))
            ps2 = re.findall(r'\d',bin(int(start-1)))
            ps1.pop(0)
            ps2.pop(0)
            itlen = len(ps1)/2
            
            for i in range(int(itlen),len(ps1)-1):
                
                if (int(ps1[i]) > int(ps2[i])):
                    step.append("dec")
                    start = start + 1
                    break
                if (int(ps1[i]) < int(ps2[i])) or (len(ps2)<len(ps1)):
                    step.append("inc")
                    start = start - 1
                    break
     
            

        if (it1 > it2):
            start = start - 1
            step.append("inc")
            
while (start1 != 0):
    if (start1 % 2 == 0):
        start1 = start1/2
        step1.append("dbl")

    if (start1 == 1):
        step1.append("inc")
        start1 = start1 - 1
		
    if (start1 % 2 == 1):
        
        parser1 = re.findall(r'\d',bin(int(start1+1)))
        
        parser2 = re.findall(r'\d',bin(int(start1-1)))
        it1 = 0
        it2 = 0
        for i in parser1:
            if (int(i) == 1):
                it1 = it1 + 1
        for j in parser2:
            if (int(j) == 1):
                it2 = it2 + 1
        if (it1 < it2):
            step1.append("dec")
            start1 = start1 + 1
            flag = True

        if (it1 == it2):
            start1 = start1 - 1
            step1.append("inc")
            flag = True

        if (it1 > it2):
            start1 = start1 - 1
            step1.append("inc")
            
        

step.reverse()        
step1.reverse()

if (len(step)>=len(step1)):
    for i in step1:
        print(i)
		
if (len(step)<len(step1)):
    for i in step:
        print(i)