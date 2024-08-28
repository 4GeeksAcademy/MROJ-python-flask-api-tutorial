

# Añade el método jsonify a tu importación de Flask
from flask import Flask, jsonify,request
app = Flask(__name__)

# Supongamos que tienes tus datos en la variable some_data
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
    
]

# todos = [
#     {  "label": "Sample Todo 1","done": True }
# ]

@app.route('/todos', methods=['GET'])
def hello_world():
    # Puedes convertir esa variable en una cadena json de la siguiente manera
    json_text = jsonify(todos)

    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)