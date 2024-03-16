from flask import Flask, render_template
app = Flask(name)

@app.route('/')
def hello():
    # Show the world symple
    return 'Hello World from Docker!'

if name == 'main':
    app.run(host='0.0.0.0', port=80)
