from flask import Flask
from flask import render_template
from flask import request
from block import *
from flask import redirect
from flask import url_for
from flask import Flask, render_template, request
#from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
from flask_uploads import UploadSet, configure_uploads, ALL
app = Flask(__name__)

"""
photos = UploadSet('photos', ALL)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename
    return render_template('upload.html')
"""



@app.route('/', methods=['POST', 'GET'] )
def index():

	if request.method == 'POST':
		lender = request.form['lender']

		#amount = request.form['amount']
		#borrower = request.form['borrower']

		write_block(name=lender)
		#write_block(name=lender, amount=amount, to_whom=borrower)
		return redirect(url_for('index'))

	return render_template('index.html')


@app.route('/checking', methods=['GET'] )
def check():
	results = check_integrity()
	return render_template('index.html', results=results)


@app.route('/showing')
def show(private_key):
	private_key = "100"
	return render_template('index.html', private_key=private_key)


if __name__ == '__main__':
	app.run(debug=True)