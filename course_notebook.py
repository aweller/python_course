# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

%matplotlib inline

# <codecell>

filename = "quasar.tsv"

df = pd.read_csv(filename, sep="\t")

df["DP"] = df.FAO + df.FDP

# <codecell>

df.describe()

# <codecell>

df.head(2)

# <codecell>

df.Effect.unique()

# <codecell>

strong_impact = ['STOP_GAINED', 'FRAME_SHIFT']

len(df[ df.Effect.isin(strong_impact) ])

# <codecell>

strong_impact = ['STOP_GAINED', 'FRAME_SHIFT']

def judge(row):
    if row["Effect"] in strong_impact:
        return "strong"
    else:
        return "weak"

df.apply(judge, axis=1).unique()

# <codecell>

df.Effect_Impact = df.Effect_Impact.str.lower()

# <codecell>


# <codecell>

df.head(2)

# <codecell>

df.Effect.groupby(df.sample).nunique()

# <codecell>

sdf = dict(sample = df.Effect.groupby(df.sample).count(), 
           qc = df.GQ.groupby(df.sample).mean(),
           dp = df.DP.groupby(df.sample).mean()
           )

sdf = pd.DataFrame(sdf)
sdf

# <codecell>

pd.pivot_table(df, rows=["sample", "Effect"]).head()

# <codecell>

help(pd.groupby)

# <codecell>

plt.scatter(df.FDP, df.FAO)

# <codecell>

sns.jointplot("FDP", "FAO", df)

# <codecell>


