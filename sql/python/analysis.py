import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER=...;DATABASE=parch_and_poesy;Trusted_Connection=yes;"
)

query = """
SELECT 
    a.name,
    o.occurred_at,
    o.total_amt_usd
FROM orders o
JOIN accounts a ON o.account_id = a.id
"""

df = pd.read_sql(query, conn)

df["occurred_at"] = pd.to_datetime(df["occurred_at"])
df["mese"] = df["occurred_at"].dt.to_period("M")

vendite_mensili = df.groupby("mese")["total_amt_usd"].sum()

plt.plot(vendite_mensili.index.astype(str), vendite_mensili.values)
plt.title("Vendite Mensili")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("output/grafico_vendite.png")
plt.show()

df.groupby("name")["total_amt_usd"].sum().to_excel("output/top_clienti.xlsx")
