import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Docker sets HOSTNAME to the container ID automatically.
# We use this to show which backend instance served each request,
# so the load-balancing effect is visible during the demo.
INSTANCE_ID = os.environ.get("HOSTNAME", "unknown")


def calculate(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Unknown operator")


@app.route("/")
def home():
    return render_template("index.html", instance_id=INSTANCE_ID)


@app.route("/calculate", methods=["POST"])
def do_calculate():
    data = request.get_json()
    try:
        a = float(data.get("a"))
        b = float(data.get("b"))
        op = data.get("op")
        result = calculate(a, b, op)
        return jsonify({"result": result, "served_by": INSTANCE_ID})
    except ZeroDivisionError as e:
        return jsonify({"error": str(e)}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
