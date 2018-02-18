import sys
import re
parser = []

class AutoCorrect(object):

    __dictionary = []
    __size_dict = 0
    __input_words = []
    __A = []
    __result = []
    def add_dict(self,data):
        self.__dictionary.append(data)
		
    def add_size_dict(self,data):
        self.__size_dict = data
		
    def add_words(self,data):
        self.__input_words.append(data)
		
    def get_size_dict(self):
        return self.__size_dict
    
    def get_input_words(self):
        return self.__input_words	
    def get_in_words(self):
        return self.__input_words
    
    def get_result(self):
        return self.__result	
	
    def damerau_levenshtein_distance(self,s1, s2):
        d = {}
        lenstr1 = len(s1)
        lenstr2 = len(s2)
        for i in range(-1,lenstr1+1):
            d[(i,-1)] = i+1
        for j in range(-1,lenstr2+1):
            d[(-1,j)] = j+1
 
        for i in range(lenstr1):
            for j in range(lenstr2):
                if s1[i] == s2[j]:
                    cost = 0
                else:
                    cost = 1
                d[(i,j)] = min(
                                d[(i-1,j)] + 1, # deletion
                                d[(i,j-1)] + 1, # insertion
                                d[(i-1,j-1)] + cost, # substitution
                                )
                if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                    d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition

        					
        return d[lenstr1-1,lenstr2-1]
    
    def calc_distanse(self):
        self.__A = [[0 for i in range(len(self.__dictionary))] for j in range(len(self.__input_words))]
        for i in range(len(self.__input_words)):
            for j in range(len(self.__dictionary)):
                self.__A[i][j] = self.damerau_levenshtein_distance(str(self.__input_words[i]).lower(),str(self.__dictionary[j]))
        
	
    def correct_words(self):
        for i in range(len(self.__input_words)):
            
            buffer = []
            buffer1 = []
            for j in range(len(self.__dictionary)):
                
                if (int(self.__A[i][j]) == 0):
                    buffer.append("ok")
                    self.__result.append(buffer)
                    break
                
                if (int(self.__A[i][j]) == 1):
                    buffer1.append(self.__dictionary[j])
                   
                  
                if (j == len(self.__dictionary)-1) and (len(buffer1)!=0):
                    
                    buffer1.sort()
                    self.__result.append(buffer1)
                if (j == len(self.__dictionary)-1) and (len(buffer)==0) and (len(buffer1)==0):
                    buffer.append("?")
                    self.__result.append(buffer)
                    
        
                
					
for line in sys.stdin:
    res = re.findall(r'.+',line)
    
    if (len(res)!=0):
        parser.append(res)

correct = AutoCorrect()
correct.add_size_dict(int(parser[0][0]))
parser.pop(0)
for i in range(0,(correct.get_size_dict())):
    correct.add_dict(str(parser.pop(0)[0]).lower())	

for i in parser:
    correct.add_words(i[0])

correct.calc_distanse()
correct.correct_words()

for i in range(0,len(correct.get_in_words())):
    
        
	
    if (correct.get_result()[i][0] == "ok"):
        print(str(correct.get_in_words()[i]) + " - " + "ok")
        
    if (correct.get_result()[i][0] == "?"):
        print(str(correct.get_in_words()[i]) + " -" + "?")
        
            
    if (correct.get_result()[i][0] != "ok") and (correct.get_result()[i][0] != "?"):
        print(str(correct.get_in_words()[i]) + " -> " + ", ".join(map(str,correct.get_result()[i])))
