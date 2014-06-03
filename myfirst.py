import survey
import thinkstats
import math

def main():
    table = survey.Pregnancies()
    table.ReadRecords()
    print 'Number of pregnancies', len(table.records)

    liveBirth = sum([1 for rec in table.records if rec.outcome == 1])
    print 'Number of live birth', liveBirth

    pregnancyFirst = [rec.prglength for rec in table.records if rec.outcome == 1 and rec.birthord == 1]
    pregnancyNonFirst = [rec.prglength for rec in table.records if rec.outcome == 1 and rec.birthord != 1]

    print 'Number of live birth first babies', len(pregnancyFirst)
    print 'Number of live birth non-first babies', len(pregnancyNonFirst)

    averagePregnancyFirst = sum(pregnancyFirst) / float(len(pregnancyFirst))
    averagePregnancyNonFirst = sum(pregnancyNonFirst) / float(len(pregnancyNonFirst))
    print 'Average pregnancy for first babies', averagePregnancyFirst, 'weeks'
    print 'Average pregnancy for after first babies', averagePregnancyNonFirst, 'weeks'
    print 'Difference', abs(averagePregnancyFirst - averagePregnancyNonFirst), 'weeks'
    print 'Difference', abs(averagePregnancyFirst - averagePregnancyNonFirst) * 7, 'days'
    print 'Difference', abs(averagePregnancyFirst - averagePregnancyNonFirst) * 7 * 24, 'hours'

    print "SD gestation time first baby", math.sqrt(thinkstats.Var(pregnancyFirst)), "weeks"
    print "SD gestation time others baby", math.sqrt(thinkstats.Var(pregnancyNonFirst)), "weeks"
    sdDiff = abs(math.sqrt(thinkstats.Var(pregnancyFirst)) - math.sqrt(thinkstats.Var(pregnancyNonFirst)))
    print "SD gestation time diff", sdDiff, "weeks", sdDiff * 7, "days", sdDiff * 7 * 24, "hours"

if __name__ == '__main__':
    main()
