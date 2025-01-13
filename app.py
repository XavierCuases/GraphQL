from flask import Flask, send_from_directory, request, jsonify
from ariadne import graphql_sync
from schema.schema import schema

app = Flask(__name__, static_folder="static")

@app.route("/graphiql")
def serve_graphiql():
    return send_from_directory(app.static_folder, "graphiql.html")

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=True)
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True)
