
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


   def graphchart(self,listn,listm,listdate):
    self.listn=listn
    self.listm=listm
    self.listdate=listdate
    

    for i in range(0,len(listn)):
       print listdate[i]," ",

       if listn[i] !='':
        for j in range(1,listn[i]):
           print "\033[31m+",
        print " \033[37m",listn[i],'C'
       else:
          print 0,"C"
       
       print listdate[i]," ",

       if listm[i] !='':
        for k in range(1,listm[i]):
           print "\033[34m+",
        print " \033[37m",listm[i],'C'
       else:
          print 0,"C"


   def findreport(self):
       
        file =open(self.filename,"r")

        list1 =[]
        list2 =[]
        list3 =[]
        
        for line in file:
             x=line.split(",")[1]
             y=line.split(",")[3]
             z=line.split(",")[0]
            
#Making list in list
             if x!="Max TemperatureC":
                 list1.append(x)
                 list2.append(y)
                 list3.append(z)
                 
        self.makinglist(list1)
        self.makinglist(list2)
        
        
        self.graphchart(list1,list2,list3)


     
#main for calling functions

if __name__ == '__main__':
  inFile = raw_input("Enter the input File Name: ")
  y = Task2(inFile)
  y.findreport()
