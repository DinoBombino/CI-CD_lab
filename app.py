from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calc.db'  # Локальная SQLite БД
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель для хранения операций
class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Integer)
    b = db.Column(db.Integer)
    op = db.Column(db.String(10))
    result = db.Column(db.Integer)

# Перенос функций из main.py
def add(a, b):
    return a + b

def min(a, b):
    return a - b

# Создаём таблицы перед запуском приложения
with app.app_context():
    db.create_all()

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    a, b, op = data['a'], data['b'], data['op']
    if op == 'add':
        result = add(a, b)
    elif op == 'subtract':
        result = min(a, b)
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    calc = Calculation(a=a, b=b, op=op, result=result)
    db.session.add(calc)
    db.session.commit()
    return jsonify({'result': result, 'id': calc.id})

@app.route('/history', methods=['GET'])
def history():
    calcs = Calculation.query.limit(10).all()
    return jsonify([{'id': c.id, 'a': c.a, 'b': c.b, 'op': c.op, 'result': c.result} for c in calcs])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)