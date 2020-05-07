import subprocess
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/admin")
def index():
    return render_template("index.html")

@app.route('/')
def hello():
    output=(subprocess.check_output("python tambola.py --generate 1", shell=True))
    output=str(output)
    print output
    return "<xmp>" + output + "</xmp>"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)

