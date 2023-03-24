#Programming Languages Project3 Elena Lucci
import sys
import tkinter as tk

class fsa:
    #global variables
    fsaFile = ""
    testFile = ""
    #list for each part of the fsa
    tokens = []
    #holds the string we are testing
    testString = ""
    #number of state variables
    totalStates = 0
    #holds the legal variables (x,y,z,a)
    legalVars = []
    #holds the legal move set
    legalMoves = []
    #start state
    startState = 0;
    #keeps track of current state
    currState = 0;
    #holds legal end states
    legalEndStates = []
    #holds coordinates for circles in GUI
    circleList = []

    #DEFAULT holds file name params
    def __init__(self,fsaFile,testFile):
        self.fsaFile = fsaFile
        self.testFile = testFile;
    
    #reads the files
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
        f.close()
        self.testString = self.testString.strip()
        
        print("processing " + self.testString)
        self.setVars()

    #parses and sets variables
    def setVars(self):
        #sets total states
        self.totalStates = int(self.tokens[0])
        #sets legal variables
        self.legalVars = self.tokens[1].split(',')
        #holds legal moves set
        self.legalMoves = self.tokens[2].split(',')
        #holds the start state
        self.startState = self.tokens[3]
        #holds legal end states
        self.legalEndStates = self.tokens[4].split(',')
    
    #determines if string is legal or not
    def testStringVar(self):
        #sets current state to start state
        self.currState = self.startState
        #loops through each character in the test string
        for x in self.testString:
            #check if the variable is legal
            self.checkLegalVars(x)
            #parses each legal move to get each individual rule
            for y in self.legalMoves:
               #parsing
                temp = y.replace(")","")
                temp = temp.replace("(","")
                tempSplit = temp.split(':')
                
                #looks for matches
                if tempSplit[0] is self.currState:
                    if tempSplit[2] is x:
                        self.currState = tempSplit[1]
                        break;


        if self.currState not in self.legalEndStates:
            print(self.testString + " is not a legal string")
            exit(1)
                
                        
                
    #checks to see if the variable is legal
    def checkLegalVars(self,currChar):
        #print(currChar)
        if currChar in self.legalVars:
            return
        else:
            print(self.testString + " is not a legal string")
            exit(1)
    #draws and displays the GUI
    def printGUI(self):
        root = tk.Tk()

        canvas = tk.Canvas(root, width=500, height=600,borderwidth=0,highlightthickness=0, bg="white")
        
        i = 0
        x0,y0,x1,y1 = 210,50,270,110
        tempList = [x0,y0,x1,y1]
        self.circleList.append(tempList)
        #draws circle for each state spaced evenly
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
        #draws a bigger circle around end states
        for x in self.legalEndStates:
            #print(self.circleList[int(x)][0])
            x0 = self.circleList[int(x)][0] -5
            y0 = self.circleList[int(x)][1] -5
            x1 = self.circleList[int(x)][2] +5
            y1 = self.circleList[int(x)][3] +5

            bigCir = canvas.create_oval(x0,y0,x1,y1)  
        #parses through each legal move and draws arrows
        for x in self.legalMoves:
            temp = x.replace(")","")
            temp = temp.replace("(","")
            tempSplit = temp.split(':')
            #if start state is the same as next state
            if(tempSplit[0] == tempSplit[1]):
                x0 = self.circleList[int(tempSplit[0])][0] + 25
                y0 = self.circleList[int(tempSplit[0])][1] 
                x1 = self.circleList[int(tempSplit[0])][2] + 25
                y1 = self.circleList[int(tempSplit[0])][3] 

                halfCir = canvas.create_oval(x0,y0,x1,y1, outline="grey",width = 1)
                #create arrow heads
                canvas.create_line(x0+15, y0, x1-30, y1-55, width =2)
                canvas.create_line(x0+15, y0, x1-30, y1-65, width =2)
                #print variable
                canvas.create_text((x1 +8),(y1 -30),text =tempSplit[2])
            #if the difference between the start state and next state is 1, draw straight line
            elif(((int(tempSplit[1]))-int(tempSplit[0])) == 1):
                x0 = self.circleList[int(tempSplit[0])][0] + 30
                y0 = self.circleList[int(tempSplit[0])][1] + 60
                x1 = self.circleList[int(tempSplit[0])][2] - 30
                y1 = self.circleList[int(tempSplit[0])][3] + 40
                canvas.create_line(x0, y0, x1, y1, width =2, arrow=tk.LAST)
                canvas.create_text((x1 +8),(y1 -25),text =tempSplit[2])
            #if next state is smaller than current state, draw arc
            elif(((int(tempSplit[1]))<int(tempSplit[0]))):
                x0 = self.circleList[int(tempSplit[0])][0] - 55
                y0 = self.circleList[int(tempSplit[0])][1] + 35
                x1 = self.circleList[int(tempSplit[1])][2]
                y1 = self.circleList[int(tempSplit[1])][3] - 35
                
                arc = canvas.create_arc(x0,y0,x1,y1,start = 90,width = 2,extent = 180, style = "arc",)
                #draw arrow head
                canvas.create_line(x0+45, y0-300, x1-60, y1, width =2)
                canvas.create_line(x0+45, y0-320, x1-60, y1, width =2)
                canvas.create_text((x1 -130),(y1 +150),text =tempSplit[2])
        canvas.pack()

        root.wm_title("FSA")

        root.mainloop()


    #runs program
    def start(self):
        self.readFiles()
        self.testStringVar()
        self.printGUI()
        print("success processing " + self.testString)


    
