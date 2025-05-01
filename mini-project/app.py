from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'e81b847af21fc6ba7f0b1bcb380d195a37e23349eae9957a7958bc7e82af233e'  # Needed for flash messages

# Home Page
@app.route('/')
def home():
    return render_template('Index.html')

# Course Pages (Add more if needed)
@app.route('/python')
def python_course():
    return render_template('python.html')

@app.route('/java')
def java_course():
    return render_template('java.html')

@app.route('/c')
def c_course():
    return render_template('c.html')


@app.route('/css')
def css_course():
    return render_template('css.html')

@app.route('/sql')
def sql_course():
    return render_template('sql.html')

@app.route('/js')
def js_course():
    return render_template('js.html')

@app.route('/react')
def react_course():
    return render_template('react.html')

# Newsletter form submission
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    print(f"New newsletter subscription: {email}")  # For demonstration
    flash('Thank you for subscribing!')
    return redirect(url_for('home'))

# Login & Register routes
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    name = request.form['name']
    email = request.form['email']
    # Optional: Collect more fields like dob, branch, etc.
    flash(f"Registration submitted for {name}")
    return redirect(url_for('register'))


if __name__ == '__main__':
    app.run(debug=True)
