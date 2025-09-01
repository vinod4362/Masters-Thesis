from flask import Flask, request, jsonify
from werkzeug.exceptions import NotFound, BadRequest


"""
OpenAPI-like docstring:
Endpoints:
POST   /todos         Create a todo. JSON: {title: str, done?: bool}
GET    /todos         List all todos.
GET    /todos/<id>    Get a todo by id.
PATCH  /todos/<id>    Update title/done fields. JSON: {title?, done?}
DELETE /todos/<id>    Delete a todo by id.
All responses are JSON. 201 on create, 204 on delete, 404 on missing, 400 on bad input.
"""

app = Flask(__name__)

# In-memory store
DB = {}
NEXT_ID = 1

def _next_id():
    global NEXT_ID
    nid = NEXT_ID
    NEXT_ID += 1
    return nid

@app.route('/todos', methods=['POST'])
def create_todo():
    if not request.is_json:
        return jsonify({"error": "JSON required"}), 400
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON object"}), 400
    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Missing or invalid 'title'"}), 400
    done = data.get("done", False)
    if not isinstance(done, bool):
        return jsonify({"error": "'done' must be boolean"}), 400
    tid = _next_id()
    todo = {"id": tid, "title": title, "done": done}
    DB[tid] = todo
    return jsonify(todo), 201

@app.route('/todos', methods=['GET'])
def list_todos():
    return jsonify(list(DB.values())), 200

@app.route('/todos/<int:tid>', methods=['GET'])
def get_todo(tid):
    todo = DB.get(tid)
    if not todo:
        return jsonify({"error": "Not found"}), 404
    return jsonify(todo), 200

@app.route('/todos/<int:tid>', methods=['PATCH'])
def update_todo(tid):
    todo = DB.get(tid)
    if not todo:
        return jsonify({"error": "Not found"}), 404
    if not request.is_json:
        return jsonify({"error": "JSON required"}), 400
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON object"}), 400
    if "title" in data:
        title = data["title"]
        if not isinstance(title, str) or not title.strip():
            return jsonify({"error": "Invalid 'title'"}), 400
        todo["title"] = title
    if "done" in data:
        done = data["done"]
        if not isinstance(done, bool):
            return jsonify({"error": "'done' must be boolean"}), 400
        todo["done"] = done
    return jsonify(todo), 200

@app.route('/todos/<int:tid>', methods=['DELETE'])
def delete_todo(tid):
    if tid not in DB:
        return jsonify({"error": "Not found"}), 404
    del DB[tid]
    return "", 204

if __name__ == '__main__':
    app.run(debug=True)
