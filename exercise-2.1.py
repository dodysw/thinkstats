import thinkstats
import sys, math

def Pumpkin():
    pumpkins = [1, 1, 1, 3, 3, 591]
    pumpkins = [1, 1, 1, 3, 3, 2]
    print "Mean:", thinkstats.Mean(pumpkins), "lbs"
    print "Variance:", thinkstats.Var(pumpkins) 
    print "SD:", math.sqrt(thinkstats.Var(pumpkins)), "lbs" 

if __name__ == '__main__':
    Pumpkin()
