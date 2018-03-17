from intActVScatRAPID import catrapid_to_uniprotid as ctu
from intActVScatRAPID import mitab_to_uniprotid as mtu


def compare_cat_mitab(catrapid_list, mitab_file, query_prot, alternative_prot_upID):
    matched_prots = []
    cat_ids = ctu.catrapid_to_uniprot_id(catrapid_list)
    mitab_ids = mtu.mitab_to_uniprot_id(mitab_file, query_prot, alternative_prot_upID)
    for c in cat_ids:
        if c in mitab_ids:
            matched_prots.append(c)
    matched_prots = sorted(matched_prots)
    output_file_path = "cat_vs_mitab_matched_{}_output.txt".format(query_prot)
    with open(output_file_path, 'w') as outf:
        for m in matched_prots:
            outf.write(m + "\n")
    return matched_prots

compare_cat_mitab("/home/hoody/Desktop/PIK3CD/PIK3CD_catRAPID_all_interactions.txt", "/home/hoody/Desktop/PIK3CD/clusteredQuery__-17032018_1120.txt", "Q6UWP7", "LCLT1_HUMAN")
