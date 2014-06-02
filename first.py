import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

liveBirth = sum([1 for rec in table.records if rec.outcome == 1])
print 'Number of live birth', liveBirth

firstLiveBirth = 0
otherLiveBirth = 0
for rec in table.records:
    if rec.outcome == 1:
        if rec.birthord == 1:
            firstLiveBirth += 1
        else:
            otherLiveBirth += 1
print 'Number of live birth first babies', firstLiveBirth
print 'Number of live birth non-first babies', otherLiveBirth

pregnancyFirst = [rec.prglength for rec in table.records if rec.outcome == 1 and rec.birthord == 1]
pregnancyNonFirst = [rec.prglength for rec in table.records if rec.outcome == 1 and rec.birthord != 1]
averagePregnancyFirst = sum(pregnancyFirst) / float(len(pregnancyFirst))
averagePregnancyNonFirst = sum(pregnancyNonFirst) / float(len(pregnancyNonFirst))
print 'Average pregnancy for first babies', averagePregnancyFirst, 'weeks'
print 'Average pregnancy for after first babies', averagePregnancyNonFirst, 'weeks'
print 'Difference', abs(averagePregnancyFirst - averagePregnancyNonFirst), 'weeks'
print 'Difference', abs(averagePregnancyFirst - averagePregnancyNonFirst) * 7, 'days'
print 'Difference', abs(averagePregnancyFirst - averagePregnancyNonFirst) * 7 * 24, 'hours'

