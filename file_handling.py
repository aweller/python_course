# read file as a list of rows
handle = open("quasar.tsv", "r")
rows = handle.readlines()
handle.close()

# print rows
for row in rows:
    print row

# write file
output = open("test.txt", "w")
output.write("This is a test.")
output.close()
