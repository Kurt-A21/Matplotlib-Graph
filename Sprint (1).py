import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

mydb = sqlite3.connect("Sprint 2.db")

sns.set()
df = pd.read_csv("C:/Users/MICT043/Documents/Python fundamentals/Week 3/Day 5/Data.csv") 
print(df)
print(mydb)

df.pivot(index="Items", columns="Opt1", values="Amounts").plot(kind="bar", figsize=(11, 6))


plt.xlabel("Items")
plt.ylabel("Amount")
plt.title("Stock amount of products")
plt.legend(loc="upper right")
plt.show()
