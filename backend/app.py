from flask import Flask, request, jsonify
from flask_cors import CORS

from llm_sql import generate_sql
from db import run_query
from safety import is_safe

app = Flask(__name__)
CORS(app)

@app.route("/query", methods=["POST"])
def query():
    question = request.json["question"]

    try:
        sql = generate_sql(question)

        if not is_safe(sql):
            return jsonify({"error": "Unsafe query blocked"})

        result = run_query(sql)

        return jsonify({
            "sql": sql,
            "result": result
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
