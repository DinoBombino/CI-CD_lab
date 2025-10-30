from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calc.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель для хранения операций
class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Integer, nullable=False)
    b = db.Column(db.Integer, nullable=False)
    op = db.Column(db.String(10), nullable=False)
    result = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'a': self.a,
            'b': self.b,
            'op': self.op,
            'result': self.result
        }

# Функции вычислений
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a // b  # Целочисленное деление для Integer полей

# Создаём таблицы перед запуском приложения
with app.app_context():
    db.create_all()

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        a = data.get('a')
        b = data.get('b')
        op = data.get('op')
        
        # Валидация
        if a is None or b is None or not op:
            return jsonify({'error': 'Missing required fields: a, b, op'}), 400
        
        try:
            a = int(a)
            b = int(b)
        except (TypeError, ValueError):
            return jsonify({'error': 'a and b must be integers'}), 400
        
        # Выполнение операции
        operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }
        
        if op not in operations:
            return jsonify({'error': f'Invalid operation: {op}'}), 400
        
        try:
            result = operations[op](a, b)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
        # Сохранение в БД
        calc = Calculation(a=a, b=b, op=op, result=result)
        db.session.add(calc)
        db.session.commit()
        
        return jsonify({
            'result': result,
            'id': calc.id,
            'message': f'{a} {op} {b} = {result}'
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/history', methods=['GET'])
def history():
    try:
        # Получаем лимит из query параметров (по умолчанию 10)
        limit = request.args.get('limit', 10, type=int)
        if limit > 100:  # Защита от слишком больших запросов
            limit = 100
            
        calcs = Calculation.query.order_by(Calculation.id.desc()).limit(limit).all()
        return jsonify([calc.to_dict() for calc in calcs])
    except Exception as e:
        return jsonify({'error': 'Failed to fetch history'}), 500

@app.route('/history/<int:calc_id>', methods=['GET'])
def get_calculation(calc_id):
    calc = Calculation.query.get_or_404(calc_id)
    return jsonify(calc.to_dict())

@app.route('/history/<int:calc_id>', methods=['DELETE'])
def delete_calculation(calc_id):
    calc = Calculation.query.get_or_404(calc_id)
    db.session.delete(calc)
    db.session.commit()
    return jsonify({'message': f'Calculation {calc_id} deleted'})

@app.route('/history', methods=['DELETE'])
def clear_history():
    try:
        num_deleted = db.session.query(Calculation).delete()
        db.session.commit()
        return jsonify({'message': f'Cleared {num_deleted} calculations from history'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to clear history'}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# import os

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calc.db'  # Локальная SQLite БД
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # Модель для хранения операций
# class Calculation(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     a = db.Column(db.Integer)
#     b = db.Column(db.Integer)
#     op = db.Column(db.String(10))
#     result = db.Column(db.Integer)

# # Перенос функций из main.py
# def add(a, b):
#     return a + b

# def min(a, b):
#     return a - b

# # Создаём таблицы перед запуском приложения
# with app.app_context():
#     db.create_all()

# @app.route('/calculate', methods=['POST'])
# def calculate():
#     data = request.json
#     a, b, op = data['a'], data['b'], data['op']
#     if op == 'add':
#         result = add(a, b)
#     elif op == 'subtract':
#         result = min(a, b)
#     else:
#         return jsonify({'error': 'Invalid operation'}), 400
#     calc = Calculation(a=a, b=b, op=op, result=result)
#     db.session.add(calc)
#     db.session.commit()
#     return jsonify({'result': result, 'id': calc.id})

# @app.route('/history', methods=['GET'])
# def history():
#     calcs = Calculation.query.limit(10).all()
#     return jsonify([{'id': c.id, 'a': c.a, 'b': c.b, 'op': c.op, 'result': c.result} for c in calcs])

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)