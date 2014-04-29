# plot a histogram from a pandas DataFrame

data = df.DP

plt.hist(data, bins=100)
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0,1000)
plt.title("Title")