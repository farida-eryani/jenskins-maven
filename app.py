from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
        <style>
            body {
                color: blue;
                font-size: 48px;
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 20%;
            }
        </style>
    </head>
    <body>
        <p>Hello World from Docker!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

