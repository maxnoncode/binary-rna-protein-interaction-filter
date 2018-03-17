import csv


def mitab_to_uniprot_id(intact_mitab_file, query_protein_upID, alternative_prot_upID):
    up_id_interactors = []
    with open(intact_mitab_file, 'r') as imf:
        imf.readline()
        imf_reader = list(csv.reader(imf, delimiter='\t', quotechar='|'))
        #print(imf_reader)
        print("Jumping in mitab_to_uniprot_id():")
        for row in imf_reader:
            #print(row)
            if row[0] == "uniprotkb:" + query_protein_upID or row[0] == "uniprotkb:" + alternative_prot_upID:
                up_id_interactors.append((row[1])[10:])
            elif row[1] == "uniprotkb:" + query_protein_upID or row[1] == "uniprotkb:" + alternative_prot_upID:
                up_id_interactors.append((row[0])[10:])
            else:
                print(row[:2])
                print("No UniPROT ID here")
        #print(up_id_interactors)
    return up_id_interactors

#mitab_to_uniprot_id("/home/hoody/Desktop/PIK3CD/clusteredQuery__-17032018_1120.txt", "Q6UWP7")

