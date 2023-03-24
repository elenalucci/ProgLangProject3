#Programming Languages Project3 Elena Lucci

import sys
from fsa import fsa
#sets the params for running, argv[1] is fsa.txt and argv[2] is the legal.txt or illegal.txt
fsaStarter = fsa(sys.argv[1],sys.argv[2])
#calls the function that runs the program
fsaStarter.start();

