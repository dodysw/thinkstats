import first, survey, Pmf

def ProbEarly(pmf):
    return sum([prob for val, prob in pmf.Items() if val <= 37]) 

def ProbOnTime(pmf):
    return sum([prob for val, prob in pmf.Items() if val in (38, 39,40)]) 

def ProbLate(pmf):
    return sum([prob for val, prob in pmf.Items() if val >= 41]) 

if __name__ == '__main__':
    table, firsts, others = first.MakeTables(".")

    alls = survey.Pregnancies()
    for p in firsts.records + others.records:
        alls.AddRecord(p)

    #easy access to gestation length (e.g. firsts.lengths)
    first.ProcessTables(firsts, others, alls)

    pmfs = {}
    pmfs['First babies'] = Pmf.MakePmfFromList(firsts.lengths)
    pmfs['Others'] = Pmf.MakePmfFromList(others.lengths)
    pmfs['Alls'] = Pmf.MakePmfFromList(alls.lengths)

    for name, pmf in pmfs.items():
        print name
        print "Probability of early arrival", ProbEarly(pmf)
        print "Probability of ontime arrival", ProbOnTime(pmf)
        print "Probability of late arrival", ProbLate(pmf)

    print "Ratio first babies vs others"
    print "Early arrival", ProbEarly(pmfs['First babies']) / ProbEarly(pmfs['Others'])
    print "Ontime arrival", ProbOnTime(pmfs['First babies']) / ProbOnTime(pmfs['Others'])
    print "Late arrival", ProbLate(pmfs['First babies']) / ProbLate(pmfs['Others'])

