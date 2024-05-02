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
