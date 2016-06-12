from flask import Flask, render_template, json, request, session, url_for, escape, redirect
import threading
#import plots
#import plots2
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main():
    return render_template('index.html')

@app.route('/clinton')
def clinton():
    # if not thread2.stopped():
    #     thread2.stop()
    # thread1.run()


    return render_template('clinton.html')
@app.route('/trump')
def trump():
    # if not thread1.stopped():
    #     thread1.stop()
    #
    # thread2.run()

    return render_template('trump.html')

if __name__ == '__main__':
    app.run(debug=True)
