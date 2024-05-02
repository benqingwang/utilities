<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spyder-like Code Editor Theme</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="editor">
        <pre><code class="python">
# Example Python Code
def hello_world():
    print("Hello, world!")

hello_world()
        </code></pre>
    </div>
</body>
</html>
body {
    background-color: #1e1e1e; /* Dark background similar to Spyder */
    color: #d4d4d4; /* Light grey text, good for dark themes */
    font-family: 'Consolas', 'Monaco', monospace; /* Monospace font for code */
    margin: 0;
    padding: 20px;
}

.editor {
    border: 1px solid #333;
    padding: 10px;
}

code {
    color: #ce9178; /* Orange color for function names and keywords */
}

.python .keyword { color: #569cd6; } /* Blue for Python keywords */
.python .function { color: #dcdcaa; } /* Yellow for function calls */
.python .string { color: #ce9178; } /* Light orange for strings */


# light
body {
    background-color: #ffffff; /* White background */
    color: #000000; /* Black text color */
    font-family: 'Consolas', 'Monaco', monospace; /* Monospace font for code */
    margin: 0;
    padding: 20px;
}

.editor {
    border: 1px solid #ccc;
    padding: 10px;
    background-color: #f7f7f7; /* Light grey background for the editor area */
}

code {
    color: #000000; /* Black color for general code */
}

.python .keyword { color: #0000FF; } /* Blue for Python keywords */
.python .function { color: #008000; } /* Green for function names */
.python .string { color: #FF0000; } /* Red for strings */



.code-container {
    border: 1px solid #ccc; /* Light grey border */
    background-color: #fff; /* White background for the code area */
    box-shadow: 0 2px 10px rgba(0,0,0,0.1); /* Subtle shadow for depth */
    padding: 20px; /* Padding inside the box */
    margin: 20px 0; /* Spacing around the box */
}
