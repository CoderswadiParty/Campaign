from flask import Flask, render_template, json, request, session, url_for, escape, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
