from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    yas = None
    if request.method == 'POST':
        dogum_yili = int(request.form['dogum_yili'])
        mevcut_yil = datetime.now().year
        yas = mevcut_yil - dogum_yili
    return render_template('index.html', yas=yas)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
