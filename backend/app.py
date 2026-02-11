from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:id>', methods=['POST'])
def add_task(id):
    tasks.append({'id': id, 'title': f'Task {id}'})
    return jsonify({'message': 'Added'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
