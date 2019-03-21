# sudoku-solver
Just playing around with a web app that solves sudoku puzzles

To run the web server locally, first make sure you are using python 3, then:
```
cd sudoku-solver
pip install virtualenv  # make sure this is python3 pip
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
FLASK_APP=website/server.py flask run
```

Then visit http://127.0.0.1:5000/ with your browser.
