import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("india_age_distribution_2022.csv")

plt.figure(figsize=(8,5))
bars = plt.bar(df["Age Group"], df["Population (Mn)"])
plt.title("India's Population Distribution by Age (2022)")
plt.xlabel("Age Group")
plt.ylabel("Population (in millions)")

for bar, pop, pct in zip(bars, df["Population (Mn)"], df["Percentage"]):
    h = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, h, f"{pop} Mn\n{pct}%", ha="center", va="bottom")

plt.tight_layout()
plt.savefig("india_age_bar_chart.png", dpi=200)
plt.show()
