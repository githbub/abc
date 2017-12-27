import csv
 
rows = [
    {'name': u'Anton\xedn Dvo\u0159\xe1k','country': u'\u010cesko'},
    {'name': u'Bj\xf6rk Gu\xf0mundsd\xf3ttir', 'country': u'\xcdsland'},
    {'name': u'S\xf8ren Kierkeg\xe5rd', 'country': u'Danmark'}
    ]
fields=['name', 'country']
out = open('test.csv', 'w')
writer = csv.DictWriter(out, fieldnames=fields)
writer.writeheader()
for row in rows:
    writer.writerow( dict( (k, v.encode('utf-8')) for k, v in row.items()))
out.close()
