from flask import Flask, request
app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return app.send_static_file('index.html')
    else:
        values = {key: val if val else '123456789'
                  for key, val in request.form.items()}
        return app.send_static_file('index.html')
