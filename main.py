from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/list_prof/ul')
def main():
    return render_template('index.html')


@app.route('/list_prof/ol')
def mainr():
    return render_template('indexir.html')


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')