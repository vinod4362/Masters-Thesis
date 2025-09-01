"""
Minimal Todo REST API (Flask)

OpenAPI-like notes
------------------
Resource: Todo
Object:
  {
    "id": integer,
    "title": string,
    "done": boolean
  }

Endpoints:
- POST   /todos
    Request JSON: { "title": string, "done"?: boolean }
    Responses:
      201: {id, title, done}
      400: {"error":"bad_request","message": "..."}
- GET    /todos
    Responses:
      200: [ {id, title, done}, ... ]
- GET    /todos/<id>
    Responses:
      200: {id, title, done}
      404: {"error":"not_found","message": "..."}
- PATCH  /todos/<id>
    Request JSON: { "title"?: string, "done"?: boolean }
    Responses:
      200: {id, title, done}
      400: {"error":"bad_request","message": "..."}
      404: {"error":"not_found","message": "..."}
- DELETE /todos/<id>
    Responses:
      204: (no body)
      404: {"error":"not_found","message": "..."}

Notes:
- In-memory storage; JSON-only responses, with clear error messages.
"""

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound, HTTPException

app = Flask(__name__)

# In-memory store
DB = {}
NEXT_ID = 1


def _next_id():
    global NEXT_ID
    nid = NEXT_ID
    NEXT_ID += 1
    return nid


# -------- Error handlers (JSON-only) --------
@app.errorhandler(BadRequest)
def _handle_bad_request(e: BadRequest):
    return jsonify(error="bad_request", message=str(e)), 400


@app.errorhandler(NotFound)
def _handle_not_found(e: NotFound):
    return jsonify(error="not_found", message=str(e)), 404


@app.errorhandler(HTTPException)
def _handle_http_exception(e: HTTPException):
    # Fallback for other HTTP errors, still JSON
    return jsonify(error=e.name.replace(" ", "_").lower(), message=e.description), e.code


# -------- Endpoints --------
@app.route("/todos", methods=["POST"])
def create_todo():
    # Use silent=True so missing/invalid JSON doesn't trigger 415 automatically
    data = request.get_json(silent=True)
    if not data:
        raise BadRequest("Payload must be JSON")
    if "title" not in data or not isinstance(data["title"], str):
        raise BadRequest("Payload must include 'title' (string)")
    if "done" in data and not isinstance(data["done"], bool):
        raise BadRequest("'done' must be boolean if provided")

    tid = _next_id()
    todo = {"id": tid, "title": data["title"], "done": bool(data.get("done", False))}
    DB[tid] = todo
    return jsonify(todo), 201


@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(list(DB.values())), 200


@app.route("/todos/<int:tid>", methods=["GET"])
def get_todo(tid: int):
    if tid not in DB:
        raise NotFound(f"Todo with id={tid} not found")
    return jsonify(DB[tid]), 200


@app.route("/todos/<int:tid>", methods=["PATCH"])
def update_todo(tid: int):
    if tid not in DB:
        raise NotFound(f"Todo with id={tid} not found")

    data = request.get_json(silent=True)
    if not data:
        raise BadRequest("Payload must be JSON")

    todo = DB[tid]

    if "title" in data:
        if not isinstance(data["title"], str):
            raise BadRequest("'title' must be string")
        todo["title"] = data["title"]

    if "done" in data:
        if not isinstance(data["done"], bool):
            raise BadRequest("'done' must be boolean")
        todo["done"] = data["done"]

    return jsonify(todo), 200


@app.route("/todos/<int:tid>", methods=["DELETE"])
def delete_todo(tid: int):
    if tid not in DB:
        raise NotFound(f"Todo with id={tid} not found")
    del DB[tid]
    # No body on 204
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
