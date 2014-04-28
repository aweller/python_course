# read file as a list of rows
handle = open("quasar.tsv", "r")
rows = handle.readlines()
handle.close()

# print chromosome and position of the first sample
for row in rows:
    f = row.split("\t")  
    
    sample = f[0]
    chrom = f[1]
    pos = f[2]

    if sample == "Q2PL1_A01_v1_T":
        print chrom, pos