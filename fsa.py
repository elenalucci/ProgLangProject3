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
        while i < self.totalStates:
            cir = canvas.create_oval(x0,y0,x1,y1, fill="white")
            canvas.create_text((x1 - 30),(y1 - 30),text = i)
            self.circleList.append(cir)
            y0 += 100
            y1 += 100
            i += 1

        canvas.create_text(50,145,text='a')
        canvas.pack()

        root.wm_title("FSA")

        root.mainloop()



    def start(self):
        self.readFiles()
        self.printGUI()
        self.testStringVar()
        print("success processing " + self.testString)
        #print("START")

    
