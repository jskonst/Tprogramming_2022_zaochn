import math
from flask import Flask, redirect
from flask import abort
from datetime import datetime
from flask import render_template
from flask import request
import person
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, World! {datetime.now()}</p>"

@app.route("/simple")
def simple_markup():
    return f"""
    <h1>Hello, World!</h1>
    <h2>Subtitle</h2>
    <p> {datetime.now()}</p>
    """

@app.route("/template")
def simple_template():
    user = {"username": "SomeName"}
    numbers = [1, "some", 3, 9, 5]
    return render_template('index.html', title='Home', user=user, numbers=numbers)

@app.route('/params')
def params():
    print(request.args)
    a = request.args.get("a", default=0, type=float)
    b = request.args.get("b", default=0, type=float)
    return f"<h1>Params a={a} b={b} result = {a + b}</h1>"

@app.route('/form',  methods=['GET', 'POST'])
def form():
    action = request.args.get("action", default="+")
    a = request.form.get("a", default=0, type=float)
    b = request.form.get("b", default=0, type=float)
    res = 0
    # match action:
    #     case "+":
    #         res = a + b
    #     case "-":
    #         res = a - b
    #     case "*":
    #         res = a * b
    #     case "\\/":
    #         if b != 0:
    #             res = a / b
    #         else:
    #             res = math.inf
    #     case _ :
    #         res = a + b
    if action == "+":
        res = a + b
    elif action == "-":
        res = a - b
    elif action == "*":
        res = a * b
    elif action == "\\/":
        if b != 0:
            res = a / b
        else:
            res = math.inf
    else:
        res = a + b
    return render_template('form.html', res=res, a=a, b=b)


person1 = person.Person("Вася", 13)
person2 = person.Person("Петя", 14)
person3 = person.Person("Коля", 13)
#             0        1        2
persons = [person1, person2, person3]

@app.route("/persons")
def persons_list():
    return render_template('persons.html', persons=persons)

@app.route("/persons/<id>")
def person_item(id):
    print("personID", id)
    id = int(id)
    if id > len(persons) or id <= 0:
        abort(404)
    person = persons[id-1]
    return render_template('person.html', person=person)

@app.route("/add", methods=['GET', 'POST'])
def persons_add():
    if request.method == 'POST':
        name = request.form.get("name")
        age = request.form.get("age", default=0, type=float)
        description = request.form.get("description")
        p = person.Person(name, age, description)
        persons.append(p)
        return redirect("/persons")
    return render_template('add_person.html')

@app.route("/persons/<id>", methods=['DELETE'])
def person_item(id):
    print("personID", id)
    id = int(id)
    if id > len(persons) or id <= 0:
        abort(404)
    person = persons[id-1]
    return render_template('person.html', person=person)
