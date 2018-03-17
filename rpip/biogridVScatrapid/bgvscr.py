import re
import sys
import csv


biogrid = sys.argv[1]
catra = sys.argv[2]
output_file = sys.argv[3]

biogrid_ids = []
catra_ids = []
cat_ids_final = []
mapped_ids = []


with open(biogrid, 'r') as bg:
    bgreader = csv.reader(bg, delimiter='\t', quotechar='|')
    for row in bgreader:
        if len(row) > 6:
            biogrid_ids.append(row[2])

with open(catra, 'r') as cr:
    crreader = csv.reader(cr, delimiter='\t', quotechar='|')
    crreader = list(crreader)[1:]
    #print(crreader)
    for row in crreader:
        catra_ids.append(row[0])

for i in catra_ids:
    #print(i)
    cr_filter = re.search(r'\|([A-Z]*[0-9]*)*_', i)
    cr_filter = cr_filter.group()[1:-1]
    #print(cr_filter)
    cat_ids_final.append(cr_filter)

biogrid_ids = sorted(biogrid_ids)
#print(cat_ids_final)
cat_ids_final = sorted(cat_ids_final)

with open("catr_out.txt", 'w') as cot, open("biogrid_out.txt", 'w') as bot:
    for cat in cat_ids_final:
        cot.write(cat + "\n")
    for bio in biogrid_ids:
        bot.write(bio + "\n")

if len(biogrid_ids) < len(cat_ids_final):
    for b in biogrid_ids:
        if b in cat_ids_final:
            mapped_ids.append(b)
else:
    for c in cat_ids_final:
        if c in biogrid_ids:
            mapped_ids.append(c)

with open(output_file, 'w') as of:
    for m in mapped_ids:
        of.write(m + "\n")
        print(m)

print("finished!!!")
