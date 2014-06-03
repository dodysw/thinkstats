import Pmf

def PmfMean(pmf):
    return sum([val * pmf.Prob(val) for val in pmf.Values()])

def PmfVar(pmf):
    mean = PmfMean(pmf)
    return sum([pmf.Prob(val) * (val - mean)**2 for val in pmf.Values()])


if __name__ == '__main__':
    pmf = Pmf.MakePmfFromList([75,79,71,72,72,73,65,30,100])
    print "Mean", PmfMean(pmf)
    print "Var", PmfVar(pmf)
    print "Using lib. Must be the same."
    print "Mean", pmf.Mean()
    print "Var", pmf.Var()

