import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales'],
    'Starting': [50, 80, 60, 70, 90],
    'Ending': [55, 75, 65, 80, 85],
    'Joiners': [10, 5, 10, 15, 8],
    'Leavers': [5, 10, 5, 5, 13]
}

df = pd.DataFrame(data)

# Set the style
sns.set(style="whitegrid")

# Create a new figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Stacked Bar Chart for Starting and Ending Numbers
df_melt = df.melt(id_vars='Department', value_vars=['Starting', 'Ending'], var_name='Status', value_name='Count')
sns.barplot(x='Department', y='Count', hue='Status', data=df_melt, ax=ax1)
ax1.set_title('Starting and Ending Number of Employees')
ax1.set_ylabel('Number of Employees')
ax1.set_xlabel('Department')

# Add data labels for the first subplot
for p in ax1.patches:
    ax1.annotate(format(int(p.get_height()), 'd'),
                 (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha = 'center', va = 'center',
                 xytext = (0, 9),
                 textcoords = 'offset points')

# Grouped Bar Chart for Joiners and Leavers
df_melt2 = df.melt(id_vars='Department', value_vars=['Joiners', 'Leavers'], var_name='Type', value_name='Count')
sns.barplot(x='Department', y='Count', hue='Type', data=df_melt2, ax=ax2)
ax2.set_title('Number of New Joiners and Leavers')
ax2.set_ylabel('Number of Employees')
ax2.set_xlabel('Department')

# Add data labels for the second subplot
for p in ax2.patches:
    ax2.annotate(format(int(p.get_height()), 'd'),
                 (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha = 'center', va = 'center',
                 xytext = (0, 9),
                 textcoords = 'offset points')

# Adjust the layout
plt.tight_layout()
plt.show()











import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Sample data
data = {
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales'],
    'Starting': [50, 80, 60, 70, 90],
    'Ending': [55, 75, 65, 80, 85],
    'Joiners': [10, 5, 10, 15, 8],
    'Leavers': [5, 10, 5, 5, 13]
}

df = pd.DataFrame(data)

# Create a subplot with 2 rows
fig = make_subplots(rows=2, cols=1, subplot_titles=('Starting and Ending Number of Employees', 'Number of New Joiners and Leavers'))

# Add bar chart for Starting and Ending numbers
fig.add_trace(go.Bar(x=df['Department'], y=df['Starting'], name='Starting', marker_color='blue'), row=1, col=1)
fig.add_trace(go.Bar(x=df['Department'], y=df['Ending'], name='Ending', marker_color='green'), row=1, col=1)

# Add data labels for Starting and Ending numbers
fig.update_traces(texttemplate='%{y}', textposition='outside', row=1, col=1)

# Add bar chart for Joiners and Leavers
fig.add_trace(go.Bar(x=df['Department'], y=df['Joiners'], name='Joiners', marker_color='orange'), row=2, col=1)
fig.add_trace(go.Bar(x=df['Department'], y=df['Leavers'], name='Leavers', marker_color='red'), row=2, col=1)

# Add data labels for Joiners and Leavers
fig.update_traces(texttemplate='%{y}', textposition='outside', row=2, col=1)

# Update layout
fig.update_layout(height=800, width=800, showlegend=True, title_text="Employee Data")

# Convert the plotly figure to an HTML string
html_str = fig.to_html(full_html=False)

# Save the HTML string to an HTML file
with open("chart.html", "w") as html_file:
    html_file.write(html_str)

# Display the figure (optional)
fig.show()
