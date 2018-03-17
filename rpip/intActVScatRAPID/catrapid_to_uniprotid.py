import csv
import re


def catrapid_to_uniprot_id(catrapid_list):
    catra_ids = []
    cat_ids_final = []
    with open(catrapid_list, 'r') as cr:
        crreader = csv.reader(cr, delimiter='\t', quotechar='|')
        crreader = list(crreader)[1:]
        # print(crreader)
        for row in crreader:
            catra_ids.append(row[0])

    for i in catra_ids:
        # print(i)
        cr_filter = re.search(r'\|([A-Z]*[0-9]*)*\|', i)
        cr_filter = cr_filter.group()[1:-1]
        # print(cr_filter)
        cat_ids_final.append(cr_filter)
    #print(cat_ids_final)
    return cat_ids_final

#catrapid_to_uniprot_id("/home/hoody/Desktop/PIK3CD/PIK3CD_catRAPID_all_interactions.txt")