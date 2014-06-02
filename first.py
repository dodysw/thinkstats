import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

liveBirth = sum([1 for rec in table.records if rec.outcome == 1])
print 'Number of live birth', liveBirth
    
