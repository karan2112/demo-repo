import sys
import numpy as np

def sum(x,y):
    print(x+y)


if __name__ == "__main__":
    print(sys.argv)
    sum(int(sys.argv[1]), int(sys.argv[2]))
else:
    print ("Executed when imported")