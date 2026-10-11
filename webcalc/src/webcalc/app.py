from flask import Flask, request, jsonify
from webcalc.calculadora import Calculadora

app = Flask(__name__)
calc = Calculadora()

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = calc.add(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid parameters'}), 400

@app.route('/sub')
def sub():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = calc.sub(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid parameters'}), 400

@app.route('/mut')
def mut():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = calc.mut(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid parameters'}), 400

@app.route('/div')
def div():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = calc.div(a, b)
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid parameters'}), 400

if __name__ == '__main__':
    app.run(debug=True)