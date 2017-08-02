
import sys
#Class for reading file from folder
class Task2:
   
   def __init__(self,filename):
         self.filename=filename



   def makinglist(self,listname):
       self.listname=listname
       for i in range(0,len(listname)):
          if listname[i]!='':
             listname[i]=int(listname[i])
       return listname

   def averageof(self,lst,a,b):
       sum1=0
       for i in range(0,len(lst)):
          if lst[i]!='':
           sum1 = sum1+lst[i]
       avg = sum1/len(lst)        
       print a,avg,b


   def findreport(self):
        #self.filename1=filename1
        file =open(self.filename,"r")

        list1 =[]
        list2 =[]
        list3 =[]
        for line in file:
             x=line.split(",")[1]
             y=line.split(",")[3]
             z=line.split(",")[8]


#Making list in list
             if x!="Max TemperatureC":
                 list1.append(x)
                 list2.append(y)
                 list3.append(z)
        self.makinglist(list1)
        self.makinglist(list2)
        self.makinglist(list3)

        self.averageof(list1,"Highest Temprature Avg","C")
        self.averageof(list2,"Lowest Temprature Avg ","C")
	self.averageof(list3,"Average Mean Humidity ","%")
       
          
        
        
     
#main for calling functions

if __name__ == '__main__':
#Taking file as a input from Console
  inFile = raw_input("Enter the input File Name: ")
  y = Task2(inFile)
  y.findreport()
