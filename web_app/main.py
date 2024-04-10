from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Делайте что-то с пользовательским вводом, например, обрабатывайте его здесь
        return f'Вы ввели: {user_input}'

if __name__ == '__main__':
    app.run(debug=True)

