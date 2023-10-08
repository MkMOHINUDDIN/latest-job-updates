from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')  # decorator function, tells the app to route this url and do something with it when requested by a client (browser)
def First():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)