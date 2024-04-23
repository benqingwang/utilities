import matplotlib.pyplot as plt

# Create a scatter plot
plt.figure(figsize=(10, 6))  # Set the figure size
colors = ['red' if x == 1 else 'blue' for x in data['BinaryColumn']]  # Color red for 1, blue for 0
plt.scatter(data.index, data['FractionColumn'], c=colors, alpha=0.5)  # Plot fraction column with coloring

# Adding title and labels
plt.title('Fraction Values Colored by Binary Column')
plt.xlabel('Index')
plt.ylabel('Fraction Value')

# Show the plot
plt.show()
