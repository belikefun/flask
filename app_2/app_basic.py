import os
from flask import Flask, render_template, request
from block import *


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        #filename = file.filename
        razshirenie = file.filename.split(".")


        filees = get_files2()
        prev_file = filees[-1]
        filename = str(prev_file + 1)
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
        aes_encrypt(filename,razshirenie[-1])

    
    return render_template("complete.html")


@app.route('/checking', methods=['GET'] )
def check():
    results = check_integrity()
    return render_template('index.html', results=results)






if __name__ == "__main__":
    app.run(port=4555, debug=True)