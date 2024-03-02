from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This is a mock database to store user information
# Replace it with a proper database setup in a real application
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    return render_template('evento.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # if username in users and users[username] == password:
    #     # Successful login, redirect to another page or perform actions
    return render_template('part.html')
    # else:
    #     # Failed login, redirect back to login page with an error message
    #     return redirect(url_for('index', error='Invalid username or password'))


@app.route('/success')
def success():
    return 'Login Successful!'
    
if __name__ == '__main__':
    app.run(debug=True)