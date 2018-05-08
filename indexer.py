# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import os


class datapoint():
    classNum = 0;
    absPath = ""
    def __init__(self,classNumber,absolutPath):
        self.classNum = classNumber
        self.absPath = absolutPath    
        
class fileSet():
    listOfDatapoints = []
    numOfClasses = 0;
    def __init__(self):
        self.listOfDatapoints = []
    def appendDatapoint(self,classNum,absPath,):
        self.listOfDatapoints.append(datapoint(classNum,absPath))
       
    def setNumOfClasses(self, intNumOfClass):
        self.numOfClasses = intNumOfClass
    def getClass(self,index):
        return self.listOfDatapoints[index].classNum
    def getPath(self,index):
        return self.listOfDatapoints[index].absPath
    def getSize(self):
        return len(self.listOfDatapoints)
    def getNumberOfclasses(self):
        return self.numOfClasses
        

class fileindexer():
    mainFolder =""
    className2Num = {}
    num2ClassName = {}
    def __init__(self,mainFolderPath):
        self.mainFolder = mainFolderPath
        print(self.mainFolder)
    
    def printTree(self):    
        
        for name in os.listdir(self.mainFolder):
            if os.path.isdir(os.path.join(self.mainFolder, name)):
                
                print(os.path.join(self.mainFolder,name))
    def makeTrainFileSet(self):
        path = os.path.join(self.mainFolder,"train")
        fileSetToReturn = fileSet()
        classNumber = 0;
        #start from Train 
        for className in os.listdir(path):
            if os.path.isdir(os.path.join(path, className)):
                for filename in os.listdir(os.path.join(path,os.path.join(className,"images"))):
                    if filename[0] != '.':
                        fileSetToReturn.appendDatapoint(classNumber,os.path.join(path,os.path.join(className,os.path.join("images",filename))))
                self.className2Num[className] =classNumber 
                self.num2ClassName[classNumber] = className
                classNumber = classNumber +1 
        fileSetToReturn.setNumOfClasses(classNumber)
        
        
        return fileSetToReturn
    
    def makeValidationSet(self):
        path = os.path.join(self.mainFolder,"val")
        
        #Read in annotations and create a dictionary to match with
        tempDic_Filename2ClassName = {}
        
        file = open(os.path.join(path,"val_annotations.txt"), "r") 
        for line in file: 
            buffer = line.split() 
            #print(buffer[0] +"  "+ buffer[1])
            tempDic_Filename2ClassName[buffer[0]] = buffer[1]
            
        #Read in file paths
        fileSetToReturn = fileSet()
        for filename in os.listdir(os.path.join(path,"images")):
            if filename in tempDic_Filename2ClassName:
                buffer_classNumber = self.className2Num[tempDic_Filename2ClassName[filename]]
                #print(filename + " class " + tempDic_Filename2ClassName[filename])
                fileSetToReturn.appendDatapoint(buffer_classNumber,os.path.join(path,os.path.join("images",filename)))
                
        
        return fileSetToReturn
    def classNum2FolderName(self,number):
        return self.num2ClassName[number]
        
# if __name__ == "__main__":
#     FI =  fileindexer("/home/viktoros/tiny-imagenet-200")
#     FI.printTree()
#     FSTrain = FI.makeTrainFileSet()
#     #print(FSTrain.getClass(10)," <-classnum | path -> ",FSTrain.getPath(10))
#     print(FSTrain.getSize()," <-total number of elements  | number of classes -> ",FSTrain.getNumberOfclasses())
#     FSval = FI.makeValidationSet()
#     print(FSval.getClass(200)," <-classnum | path -> ",FSval.getPath(10))
#     print(FSval.getSize()," <-total number of elements  | number of classes -> ",FSval.getNumberOfclasses())
#     print(FI.classNum2FolderName(10))



