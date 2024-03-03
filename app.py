from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Simulated database (you should use a real database like MySQL or PostgreSQL)
users = {}

@app.route('/')
def index():
    return render_template('evento.html')

@app.route('/org')
def org():
    return render_template('org.html')

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

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    role = data.get('role')  # 'organizer' or 'participant'

    # Validate input (you can add more validation checks)
    if not email or not password or not role:
        return jsonify({'error': 'Invalid input'}), 400

    # Save user to the database (you should hash the password before saving)
    users[email] = password

    return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)

