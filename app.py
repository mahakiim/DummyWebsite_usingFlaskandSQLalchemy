from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for storing registered users (for simplicity)
users = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Simple user storage
        users.append({'username': username, 'password': password})
        return redirect(url_for('home'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
