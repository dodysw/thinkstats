import Pmf
import operator

def Mode(hist):
    return max(hist.Items(), key=lambda x: x[1])[0]

def AllModes(hist):
    return sorted(hist.Items(), key=operator.itemgetter(1), reverse=True)

if __name__ == '__main__':
    hist = Pmf.MakeHistFromList([1,2,2,5,3,-1, -1, -1, -1]) 
    print "Mode of hist is", Mode(hist)
    print "All modes", AllModes(hist)
