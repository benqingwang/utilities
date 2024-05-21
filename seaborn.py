import seaborn as sns
import matplotlib.pyplot as plt
import mpld3

# Load example dataset
data = sns.load_dataset("penguins")

# Create first histogram
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.histplot(data['flipper_length_mm'], bins=30, kde=True, color='blue', ax=ax1)
ax1.set_title('Histogram of Flipper Lengths')
ax1.set_xlabel('Flipper Length (mm)')
ax1.set_ylabel('Frequency')

# Create second histogram
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.histplot(data['body_mass_g'], bins=30, kde=True, color='green', ax=ax2)
ax2.set_title('Histogram of Body Mass')
ax2.set_xlabel('Body Mass (g)')
ax2.set_ylabel('Frequency')

# Convert figures to HTML strings
html_str1 = mpld3.fig_to_html(fig1)
html_str2 = mpld3.fig_to_html(fig2)

# Combine HTML strings and save to a single file
combined_html = f"<html><body>{html_str1}<hr>{html_str2}</body></html>"
with open("multiple_histograms.html", "w") as f:
    f.write(combined_html)
