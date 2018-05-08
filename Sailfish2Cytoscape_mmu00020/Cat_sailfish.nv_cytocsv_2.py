import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys

args = sys.argv
filename = args[1]
name = filename.split('.')[0]
f1 = open(filename, 'r')
f2 = f1.read()
f2 = f2.split('\n')

data = pd.read_csv(filename,index_col="Gene_symbol")
df = pd.DataFrame(data)
del df["NCBI gene ID"]


plt.figure()
sns.heatmap(df,cmap="Blues")
namei = name.split(":")
save_name = "{0}_{1}.png".format(namei[1],namei[2])
plt.savefig(save_name)

f1.close()


