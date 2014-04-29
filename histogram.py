# plot a histogram from a pandas DataFrame

data = {'coverage':[632, 1638, 569, 115, 433, 1130, 754, 555, 345],
        'sample':["A", "A", "A", "B","B","B", "C","C","C"],
        'chrom':[1,2,3,1,2,3,1,2,3]}

df = pd.DataFrame()

plt.hist(df.coverage)

plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0,1000)
plt.title("Title")