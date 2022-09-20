# Importing pandas
import pandas as pd

# Reading the data
df = pd.read_csv('datasets/cookie_cats.csv')

# Showing the first few rows
print(df.head())

# Counting the number of players in each AB group.
print(df.groupby(by='version').count())

# Counting the number of players for each number of gamerounds
plot_df = df.groupby(by='sum_gamerounds')['userid'].count()

# The % of users that came back the day after they installed
df['retention_1'].mean()

# Calculating 1-day retention for each AB-group
df.groupby('version')['retention_1'].mean()

# Creating an list with bootstrapped means for each AB-group
boot_1d = []
for i in range(500):
    boot_mean = df.sample(frac=1, replace=True).groupby('version')['retention_1'].mean()
    boot_1d.append(boot_mean)

# Transforming the list to a DataFrame
boot_1d = pd.DataFrame(boot_1d)

# Adding a column with the % difference between the two AB-groups
boot_1d['diff'] = ((boot_1d['gate_30']-boot_1d['gate_40'])/boot_1d['gate_40']*100)

# Calculating the probability that 1-day retention is greater when the gate is at level 30
prob = (boot_1d['diff'] > 0).mean()

# Pretty printing the probability
print(prob)

# Calculating 7-day retention for both AB-groups
df.groupby('version')['retention_7'].mean()

# Creating a list with bootstrapped means for each AB-group
boot_7d = []
for i in range(500):
    boot_mean = df.sample(frac=1, replace=True).groupby('version')['retention_7'].mean()
    boot_7d.append(boot_mean)

# Transforming the list to a DataFrame
boot_7d = pd.DataFrame(boot_7d)

# Adding a column with the % difference between the two AB-groups
boot_7d['diff'] = ((boot_7d['gate_40'] - boot_7d['gate_30']) / boot_7d['gate_40'] * 100)

# Calculating the probability that 7-day retention is greater when the gate is at level 30
prob = (boot_7d['diff'] > 0).mean()

# Pretty printing the probability
print(prob)
