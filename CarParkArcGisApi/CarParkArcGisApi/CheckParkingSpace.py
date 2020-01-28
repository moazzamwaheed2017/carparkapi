
from flask import Flask

app = Flask(__name__)

@app.route('/<name>')

def default(name):
    return 'the value !' + name

if __name__ == '__main__':
    app.run(debug=True)

