from flask import Flask,jsonify,request


app = Flask(__name__)

todos = [
    { "label": "Feed the turtle", "done": False },
    { "label": "Walk the turtle", "done": False }
]
@app.route('/todos', methods=['GET'])
def hello_world():
    my_list = jsonify(todos)
    return my_list

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['GET'])
def get_todo(position):
    get_task = todos[position]
    return jsonify(get_task)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)