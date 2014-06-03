import Pmf

def RemainingLifetime(pmf, age):
    # get original list of pmf values larger than age then return as new Pmf
    return Pmf.MakePmfFromList([val for val in pmf.Values() if val >= age])

if __name__ == '__main__':
    pmf = Pmf.MakePmfFromList([75,79,71,72,72,73,65,30,100])
    remainingPmf = RemainingLifetime(pmf, 90)
    print "Remaining PMF", remainingPmf.Items()
