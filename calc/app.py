from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    """Adds a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route('/sub')
def subtraction():
    """Subtracts a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def multipy():
    """Multiplies a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route('/div')
def divide():
    """Divides a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

#PART TWO

math_ops = {
    "add": add,
    "sub": sub,
    "div": div,
    "mult": mult
}

@app.route("/math/<oper>")
def do_math(oper):
    """Use Math function on a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = math_ops[oper](a, b)

    return str(result)