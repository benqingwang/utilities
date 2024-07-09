from pyvis.network import Network
import pandas as pd

# Create a sample DataFrame for illustration
data = {
    'node': ['A', 'B', 'C', 'D'],
    'attribute': [1, 2, 3, 4],  # This is the attribute you want to base the color on
    'detail': ['Detail A', 'Detail B', 'Detail C', 'Detail D']  # Additional details for each node
}
df_nodes = pd.DataFrame(data)

# Assuming net is your Network instance
net = Network()

# Define a function to map attribute values to colors
def get_color(attribute_value):
    if attribute_value == 1:
        return 'red'
    elif attribute_value == 2:
        return 'green'
    elif attribute_value == 3:
        return 'blue'
    elif attribute_value == 4:
        return 'yellow'
    else:
        return 'gray'

# Add nodes to the network with color and details based on the attribute
for idx, row in df_nodes.iterrows():
    node = row['node']
    attribute = row['attribute']
    detail = row['detail']
    color = get_color(attribute)
    net.add_node(node, label=node, size=30, font={'size': 50}, color=color, title=detail)

# Add edges to the network with larger arrows
# Example DataFrame for edges
df_risk_rel = pd.DataFrame({
    'upstream_model': ['A', 'B', 'C'],
    'gmd_id': ['B', 'C', 'D']
})
for idx, row in df_risk_rel.iterrows():
    net.add_edge(row['upstream_model'], row['gmd_id'], length=300, width=5, arrows='to', arrowStrikethrough=False)

# Set the initial physics options for interactive dragging
net.set_options("""
var options = {
  "physics": {
    "barnesHut": {
      "gravitationalConstant": -80000,
      "centralGravity": 0.3,
      "springLength": 300,
      "springConstant": 0.04,
      "damping": 0.09,
      "avoidOverlap": 0
    },
    "minVelocity": 0.75
  },
  "edges": {
    "arrows": {
      "to": { "enabled": true, "scaleFactor": 2 }
    }
  }
}
""")

# Show the interactive graph with physics enabled initially
net.show('my_network.html')

# Modify the HTML/JavaScript to add a title and disable physics after layout stabilization
with open('my_network.html', 'r') as file:
    html_content = file.read()

# Add a script to disable physics after the initial layout
disable_physics_script = """
<script type="text/javascript">
  var network;
  function init() {
    var container = document.getElementById('mynetwork');
    var options = {
      physics: {
        enabled: true
      }
    };
    network = new vis.Network(container, data, options);
    network.once('stabilizationIterationsDone', function () {
      network.setOptions({ physics: false });
    });
  }
  window.addEventListener('load', init, false);
</script>
"""

# Add a title to the HTML content with CSS for wrapping
title_html = """
<div style="text-align: center; width: 100%; white-space: normal; word-wrap: break-word;">
  <h1>My Network Graph Title with Wrapping</h1>
</div>
"""

# Insert the title and script before the closing </body> tag
html_content = html_content.replace('<body>', '<body>' + title_html)
html_content = html_content.replace('</body>', disable_physics_script + '</body>')

# Write the modified HTML content back to the file
with open('my_network.html', 'w') as file:
    file.write(html_content)