from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder=".")


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
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"service": "private-cloud-calculator", "status": "online"})


@app.route("/calculate", methods=["POST"])
def do_calculate():
    data = request.get_json(silent=True) or {}
    try:
        a = float(data["a"])
        b = float(data["b"])
        op = data.get("op")
        result = calculate(a, b, op)
        return jsonify({"result": result})
    except ZeroDivisionError as e:
        return jsonify({"error": str(e)}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
