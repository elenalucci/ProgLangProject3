#Programming Languages Project3 Elena Lucci
import sys
import tkinter as tk

class fsa:

    fsaFile = ""
    testFile = ""
    tokens = []
    testString = ""
    totalStates = 0
    legalVars = []
    legalMoves = []
    legalSet = []
    startState = 0;
    currState = 0;
    legalEndStates = []
    isLegal = True
    circleList = []


    def __init__(self,fsaFile,testFile):
        self.fsaFile = fsaFile
        self.testFile = testFile;
        #print("INIT")
    
    def readFiles(self):
        #read fsaFile
        f = open(self.fsaFile)
        content = f.readline()
        print("the FSA: " + content)
        self.tokens = content.split(";")
        f.close()
        
        self.tokens.pop()

        for x in self.tokens:
           print("token - " + x)
    
        #read testFile
        
        f = open(self.testFile)
        self.testString = f.readline()
        #print("the test string: " + testString)
        f.close()
        self.testString = self.testString.strip()
        
        print("processing " + self.testString)

        self.setVars()

    def setVars(self):
        self.totalStates = int(self.tokens[0])
        #print(self.totalStates)
        self.legalVars = self.tokens[1].split(',')
        #print(self.legalVars)
        self.legalMoves = self.tokens[2].split(',')
        #print(self.legalMoves)
        self.startState = self.tokens[3]
        #print(self.startState)
        self.legalEndStates = self.tokens[4].split(',')
        #print(self.legalEndStates)

    def testStringVar(self):
        self.currState = self.startState
        
        for x in self.testString:
            #print("CURR STATE: " + self.currState)
            #print(x)
            self.checkLegalVars(x)
            
            for y in self.legalMoves:
               # print(y)
                temp = y.replace(")","")
                temp = temp.replace("(","")
                tempSplit = temp.split(':')
                

                if tempSplit[0] is self.currState:
                    #print("CurrStateMatch")
                    if tempSplit[2] is x:
                        #print("VARMATCH")
                        self.currState = tempSplit[1]
                        break;


        if self.currState not in self.legalEndStates:
            print(self.testString + " is not a legal string")
            exit(1)
                
                        
                

    def checkLegalVars(self,currChar):
        #print(currChar)
        if currChar in self.legalVars:
            return
        else:
            print(self.testString + " is not a legal string")
            exit(1)

    def printGUI(self):
        root = tk.Tk()

        canvas = tk.Canvas(root, width=500, height=600,borderwidth=0,highlightthickness=0, bg="white")
        
        #canvas.create_line(40, 75, 40, 200, width =2, arrow=tk.LAST)
        #coord = 10,200, 70, 260
        i = 0
        x0,y0,x1,y1 = 210,50,270,110
        tempList = [x0,y0,x1,y1]
        self.circleList.append(tempList)
        while i < self.totalStates:
            cir = canvas.create_oval(x0,y0,x1,y1, fill="grey")
            canvas.create_text((x1 - 30),(y1 - 30),text = i)
            
            y0 += 100
            y1 += 100
            newList = tempList.copy()
            newList[1] = y0
            newList[3] = y1
            self.circleList.append(newList)
            i += 1
        
        self.circleList.pop()
        
        for x in self.legalEndStates:
            #print(self.circleList[int(x)][0])
            x0 = self.circleList[int(x)][0] -5
            y0 = self.circleList[int(x)][1] -5
            x1 = self.circleList[int(x)][2] +5
            y1 = self.circleList[int(x)][3] +5

            bigCir = canvas.create_oval(x0,y0,x1,y1)  
    
        for x in self.legalMoves:
            temp = x.replace(")","")
            temp = temp.replace("(","")
            tempSplit = temp.split(':')
            
            if(tempSplit[0] == tempSplit[1]):
                x0 = self.circleList[int(tempSplit[0])][0] + 25
                y0 = self.circleList[int(tempSplit[0])][1] 
                x1 = self.circleList[int(tempSplit[0])][2] + 25
                y1 = self.circleList[int(tempSplit[0])][3] 

                halfCir = canvas.create_oval(x0,y0,x1,y1, outline="grey",width = 1)
                canvas.create_line(x0+15, y0, x1-30, y1-55, width =2)
                canvas.create_line(x0+15, y0, x1-30, y1-65, width =2)
                canvas.create_text((x1 +8),(y1 -30),text =tempSplit[2])
            elif(((int(tempSplit[1]))-int(tempSplit[0])) == 1):
                x0 = self.circleList[int(tempSplit[0])][0] + 30
                y0 = self.circleList[int(tempSplit[0])][1] + 60
                x1 = self.circleList[int(tempSplit[0])][2] - 30
                y1 = self.circleList[int(tempSplit[0])][3] + 40
                canvas.create_line(x0, y0, x1, y1, width =2, arrow=tk.LAST)
                canvas.create_text((x1 +8),(y1 -25),text =tempSplit[2])
            elif(((int(tempSplit[1]))<int(tempSplit[0]))):
                x0 = self.circleList[int(tempSplit[0])][0] - 55
                y0 = self.circleList[int(tempSplit[0])][1] + 35
                x1 = self.circleList[int(tempSplit[1])][2]
                y1 = self.circleList[int(tempSplit[1])][3] - 35
                
                arc = canvas.create_arc(x0,y0,x1,y1,start = 90,width = 2,extent = 180, style = "arc",)
                canvas.create_line(x0+45, y0-300, x1-60, y1, width =2)
                canvas.create_line(x0+45, y0-320, x1-60, y1, width =2)
                canvas.create_text((x1 -130),(y1 +150),text =tempSplit[2])
        #print(self.circleList)
        canvas.pack()

        root.wm_title("FSA")

        root.mainloop()



    def start(self):
        self.readFiles()
        self.testStringVar()
        self.printGUI()
        print("success processing " + self.testString)
        #print("START")

    
