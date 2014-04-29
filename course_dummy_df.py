# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

%matplotlib inline

# <codecell>

df = pd.DataFrame({'coverage':[632, 1638, 569, 115, 433, 1130, 754, 555, 345],
                     'sample':["A", "A", "A", "B","B","B", "C","C","C"],
                     'chrom':[1,2,3,1,2,3,1,2,3]})
df

# <codecell>

df.loc[:4, "chrom"]

# <codecell>

df["test"] = "test"

# <codecell>

df.groupby(df.chrom).mean()

# <codecell>

#kind : {‘line’, ‘bar’, ‘barh’, ‘kde’, ‘density’, ‘scatter’}

plt.barh(df.coverage)

# <codecell>

df = pd.DataFrame({'coverage':[632, 1638, 569, 115, 433, 1130, 754, 555, 345],
                     'sample':["A", "A", "A", "B","B","B", "C","C","C"],
                     'chrom':[1,2,3,1,2,3,1,2,3]})

plt.hist(df.coverage, bins=10)
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0,1000)
plt.title("Title")

# <codecell>


