import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv ('gif2/data_cross.csv')
print(df.head(5))

p = sns.lineplot(data=df, x="epoch", y="fitness_estimate")

# axes lables 
plt.xlabel("Generation")
plt.ylabel("Fittest Individual")

plt.title("Fittest Individual (Delta_E) vs. Generation")

# asymptote line 
plt.axhline(15, ls='--')

# include 0 in y axis 
plt.ylim(0, 70)

plt.show()