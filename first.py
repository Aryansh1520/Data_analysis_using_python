import csv
with open(r"D:\course material\albumlist.csv",'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = 5
    for x in reader:
        rows -=1
        if rows>0:
           # print(x)
           pass
        else:
            pass
with open(r"D:\course material\albumlist.csv",'r') as csvfile:
    reader = csv.DictReader(csvfile)
    a = []
    rows = 200
    for x in reader:
        rows -= 1
        if rows>0:
            a.append(x)
        else:
            pass
    #print('\n\n\n',a)
   # print(len(a))

#list comprehension
#print(a)
query = [row for row in a if row['Year']=='1974']
print(len(query))
for album in query:
    print(album['Album'],album['Artist'])
