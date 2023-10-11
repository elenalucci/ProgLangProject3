Python FSA Graph Generator

This program takes the Finite State Automata given and checks .txt files for legal and illegal FSA
sequences. The program reads fsa.txt which contains the FSA rules, then reads a .txt file that contains
a FSA sequence to test. If successful the program will generate a new graph of the FSA sequence we have
tested and display it on a GUI. If unsuccessful an error message will be displayed. Created and Tested on Visual Studio Code and Gitbash.

How to Run:
1.) Verify that you have the fsa.txt file in the same folder as the program.
2.) Verify you have a .txt file containing the fsa sequence you are checking in the form of a string, in the same folder as the program.
I have provided legal.txt which will run successfully and generate a new graph, and illegal.txt which will output an error message to the console.
3.) In your command line (ensure you are inside the programs folder) run the command <python3 main.py fsa.txt yourfsa.txt> (not including '<>', replace yourfsa.txt with the sequence you are testing ie: legal.txt or illegal.txt)
4.) The program will either output a GUI with the FSA graph and your sequence, or will display an error message to the console.
