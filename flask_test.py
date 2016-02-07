from flask import Flask, abort, render_template

app = Flask(__name__)

ages = {
    'bob': '43',
    'alice': '29'
}


@app.route('/users/<user>')
def users(user):
    # age = ages.get(user)
    # if age:
    #     return '<html><h1>%s is %s years old</h1></html>' % (user, age)
    # else:
    #     abort(404)
    age = ages.get(user)
    return render_template('users.html',
                           user=user, age=age)


@app.route('/')
def hello_world():
    return 'Goodbye World!'


if __name__ == '__main__':
    app.run(debug=True)
