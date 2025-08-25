Task 2: REST API (Flask, Python)
Objective
Design a minimal REST API for a Todo resource with endpoints:
- POST /todos        -> create {title, done:false}
- GET /todos         -> list all
- GET /todos/<id>    -> detail
- PATCH /todos/<id>  -> update fields {title?, done?}
- DELETE /todos/<id> -> delete

Requirements
- In-memory storage is acceptable (dictionary).
- Validate payloads; return proper HTTP status codes; JSON only.
- Add basic input validation and error messages.
- Provide a simple OpenAPI-like doc string in README or code comments.

Expected Output
- Functional endpoints returning JSON with correct codes (201 on create, 404 on missing, etc.).
- A small test script or curl examples to demonstrate usage.
