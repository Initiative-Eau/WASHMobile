from flask import Flask, render_template

app = Flask(__name__)

@app.route("/WashMobile/home")
def home():
    return render_template('home.html')

@app.route("/WashMobile/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)