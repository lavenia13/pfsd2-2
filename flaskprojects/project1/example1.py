from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/a')
def hello1():
    return 'Welcme to PFSD - S11 '

@app.route('/emp/<int:emp1>')
def show_emp(emp1):
    return 'EMP ID NUMBER %d' %emp1

@app.route('/emp/<float:emp1>')
def show_emp1(emp1):
    return 'EMP ID NUMBER %f' %emp1

@app.route('/ex1')
def index():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(debug=True)