from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/test')
def hello(): 
    return jsonify(austin="brovick")


if __name__ == '__main__':
    app.run(debug=True)
