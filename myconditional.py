import first, survey, Pmf, descriptive, myplot
import matplotlib.pyplot as pyplot

def DropValues(table, week):
    # clear all records of gestation before @week weeks
    table.lengths = [length for length in table.lengths if length >= week]

def BornAtButNotBefore(week):
    table, firsts, others = first.MakeTables(".")
    first.ProcessTables(firsts, others)
    DropValues(firsts, week)
    DropValues(others, week)

    firstBabies = Pmf.MakePmfFromList(firsts.lengths, name="First babies")
    otherBabies = Pmf.MakePmfFromList(others.lengths, name="Other babies")
    return (firstBabies, otherBabies)

def main():
    weeks = range(35, 46)
    pyplot.clf()
    p = {'first': [], 'others': []}
    for week in weeks:
        firstBabies, otherBabies = BornAtButNotBefore(week)
        p['first'].append(firstBabies.Prob(week))
        p['others'].append(otherBabies.Prob(week))

    pyplot.plot(weeks, p['first'], label="First babies")
    pyplot.plot(weeks, p['others'], label="Others babies")
    
    myplot.Save(root='first_conditional_pmf',
                title='My conditional',
                xlabel='weeks',
                ylabel='probability')


if __name__ == "__main__":
    main()
