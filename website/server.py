from flask import Flask, request
app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return app.send_static_file('index.html')
    else:
        pass
