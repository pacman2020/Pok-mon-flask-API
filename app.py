from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    name = 'geraldo'
    return render_template('home.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)