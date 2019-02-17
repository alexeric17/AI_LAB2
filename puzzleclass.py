#Lab2 AI Constraint Satisfaction and Backtracking Search
import copy
class puzzle:
    def __init__(self,word_list): 
    	#Set word_list,puzzle
        self.wordList = word_list #full domain
        self.A = ["A1","A2","A3"]
        self.D = ["D1","D2","D3"]
        self.ID = { "A1" : [None,1,self.D],
        			"A2" : [None,2,self.D],
        			"A3" : [None,3,self.D],
        			"D1" : [None,1,self.A],
        			"D2" : [None,2,self.A], 
        			"D3" : [None,3,self.A]} #Dict, A1,D1,..D3 [word,index]

    def constraint(self,var,i):     #Check constraints on all positions. IF any doesnt work, false will be returned.
    	valueA = self.ID.get(var) #From dict, ID [word,index,const]
    	check = valueA[2] 		  #Check = variables to check against i.e A1 checks D1,D2,D3
    	x = valueA[1]

    	valueD = self.ID.get(check[i]) #Variable where constraints are checked against
    	y = valueD[1]
    	if valueD[0] == None:
    		return (True)
    	else:
   			if valueA[0][y-1] == valueD[0][x-1]:
   				return(True)
   			else:
   				return(False)

    def checkConstraints(self,var): #Checks all constraints for any given var
    	for i in range(3):
    		if self.constraint(var,i) == False:
    			return(False)
    	return (True)

    def insertVariable(self,PosA,word): #inserts a word
    	values = self.ID[PosA]
    	temp = values
    	values[0] = word
    	self.ID[PosA] = values
    	if self.checkConstraints(PosA) == False:
    		self.ID[PosA] = temp
    		return (False)
    	else:
    		return (True)

    def checkUnassigned(self): #returns a list with all unassigned variables
    	U = []
    	for key in self.ID:
    		if self.ID[key][0] == None:
    			U.append(key)
    	return (U)

    def tryWords(self):
    	u = self.checkUnassigned()
    	li = self.wordList.copy()
    	for next in u:
    		#insert on next#
    		while(li):
    			result = self.insertVariable(next,li[i])
    			if result == True:
    				li.remove(li[i])
    		

    
    #def BacktrackingSearch(self):
    #	return self.RecursiveBacktrackingSearch()

   #def RecursiveBackTrackingSearch():
