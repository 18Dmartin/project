import pandas as pd
import matplotlib.pyplot as plt

# Bring some raw data.
frequencies = [5,17,22]
# In my original code I create a series and run on that,
# so for consistency I create a series from the list.
freq_series = pd.Series(frequencies)

x_labels = [
    1,
    2,
    3
]

# Plot the figure.
plt.figure(figsize=(12, 8))
ax = freq_series.plot(kind="bar")
ax.set_title("Amount Frequency")


ax.set_xlabel("Amount ($)")
ax.set_ylabel("Frequency")




rects = ax.patches

# Make some labels.
labels = ["5.0", "17.5", "22.5"]

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height - 5, label, ha="center", va="bottom"
    )

plt.show()
