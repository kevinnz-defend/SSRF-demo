from flask import Flask, render_template, request, url_for, Response
import os
import requests
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/image', methods=['GET','POST'])
def image():
    try:
        print(request)
        print("===================")
        print(request.method)
        print("===================")
        if request.method == 'GET':
            image_url = request.args['image']
        else:
            image_url = request.form['image']
        print('url',image_url)
        filename = Path(str(os.getcwd())) / 'static' / 'temp.jpg'
        image_req = requests.get(image_url)
        with open(str(filename), 'wb') as f:
            f.write(image_req.content)
            f.close()
        return Response(image_req.content, content_type=image_req.headers['Content-Type'])
    except Exception as e:
        print(e)
        return 'error'

if __name__ == '__main__':
    app.run()