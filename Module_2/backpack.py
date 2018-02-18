import re 
import sys

class Backpack(object):
    __A = []
    __backpack_size = 0
    __subjects = []
    __ans = []
    __res_cash = 0
    __res_sum = 0
    __res_gcd = 0
    def add_subject(self, data):
        self.__subjects.append(data)
    def add_backpack_size(self, data):
        self.__backpack_size = data	
    def gen_matrix(self):
        self.__subjects.pop(0)
        self.__A = [[0 for i in range(self.__backpack_size + 1)] for j in range(len(self.__subjects) + 1)]
        for i in range(1, len(self.__subjects) + 1):
            for j in range(1, self.__backpack_size + 1):
                if (int(self.__subjects[i - 1][0]) > j):
                    self.__A[i][j] = self.__A[i - 1][j]
                else:
                    self.__A[i][j] = max(self.__A[i - 1][j], self.__A[i - 1][j - int(self.__subjects[i - 1][0])] + int(self.__subjects[i - 1][1]))	
        
        self.__res_cash = int(self.__A[len(self.__subjects)][self.__backpack_size])
        		
        self.findAns(len(self.__subjects),self.__backpack_size)						
    def findAns(self,k,s):
        if (self.__A[k][s] == 0):
            return
        if (self.__A[k-1][s] == self.__A[k][s]):
            self.findAns(k-1,s)
        else:
            self.findAns(k-1,s - int(self.__subjects[k-1][0]))
            self.__ans.append(k)
    
    def calc_massa(self):
        for i in range(0,len(self.__subjects)):
            for j in self.__ans:
                if (i == j-1):
                    self.__res_sum = int(self.__subjects[i][0]) + self.__res_sum

    def printAns(self):
        for i in self.__ans:
            print(i)
    
    def print_res(self):
        print(str(self.__res_sum*self.__res_gcd) + " " + str(self.__res_cash))
    
    def gcd(self,a,b):
        if a == 0 or b == 0: 
            return max(a, b)
        else:
            if a > b:
                return self.gcd(a - b, b)
            else:
                return self.gcd(a, b - a)
	
    def all_gcd(self):
	    self.__res_gcd = int(max(self.__subjects)[0])
	    for i in range(1,len(self.__subjects)-1):
		    if (self.__res_gcd > self.gcd(int(self.__subjects[i][0]),int(self.__subjects[i+1][0]))):
			    self.__res_gcd = self.gcd(int(self.__subjects[i][0]),int(self.__subjects[i+1][0]))

    def correct_subjects(self):
        self.__backpack_size = int(self.__backpack_size/self.__res_gcd)
        for i in range(1,len(self.__subjects)):
            self.__subjects[i][0] = int(int(self.__subjects[i][0])/self.__res_gcd)	
        			
		


    



flag = False

digit = Backpack()

for line in sys.stdin:
	parser = re.findall(r'\d+', line)
	if (len(parser)!=0):
	    if (flag == False):
		    digit.add_backpack_size(int(parser[0]))
		    flag = True
	    if (flag == True):
		    digit.add_subject(parser)
digit.all_gcd()
digit.correct_subjects()
digit.gen_matrix()
digit.calc_massa()
digit.print_res()
digit.printAns()
