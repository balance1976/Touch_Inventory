from flask import Flask, render_template, url_for
#Make sure your in the virtual envrionment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rumor/')
def rumors():
    return render_template('rumor.html')

if __name__ == "__main__":
    app.run(debug=True)


##document any additions and the understanding behind them 
