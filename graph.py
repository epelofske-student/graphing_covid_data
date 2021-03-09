import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("new-mexico-history.csv")
y_axis_positive_cases = df["positive"].tolist()
y_axis_positive_cases.reverse()
x_axis_date = df["date"].tolist()
x_axis_date.reverse()
plt.ylabel("Total Positive Cases", fontsize=20)
plt.xlabel("Date", fontsize=20)
plt.plot(x_axis_date, y_axis_positive_cases, '-b.')
plt.xticks(rotation=30)
modified_dates = [x_axis_date[i] if i%9==0 else "" for i in range(len(x_axis_date))]
plt.xticks(modified_dates, fontsize=10)
plt.yticks(fontsize=15)
plt.rcParams['figure.figsize'] = (25, 10)
plt.tight_layout()
plt.savefig("Total Positive Cases New Mexico")
