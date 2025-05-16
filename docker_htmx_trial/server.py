from flask import Flask, render_template

app = Flask(__name__)

# Route to serve the main page
@app.route('/')
def home():
    return render_template('index.html')

# Route for HTMX request
@app.route('/message')
def message():
    return "Hello from HTMX!"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)



