from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form.get('email')

        username = email[:email.index('@')]
        domain = email[email.index('@') + 1:]

        return render_template('sliced.html', username=username, domain=domain)