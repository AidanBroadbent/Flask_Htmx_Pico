from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/login',methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email,password)
    #real auth logic here
    return render_template('main.html')
    

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 