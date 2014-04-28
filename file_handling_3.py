# print chromosome and position of the first sample

with open("quasar.tsv") as variant_file:
    for row in variant_file:
        f = row.split("\t")  
        
        sample = f[0]
        chrom = f[1]
        pos = f[2]
    
        if sample == "Q2PL1_A01_v1_T":
            print chrom, pos