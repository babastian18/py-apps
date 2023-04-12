from flask import Flask, render_template, request
import time

app = Flask(__name__)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    if request.method == 'POST':
        input_number = int(request.form['inputNumber'])
        for i in range(input_number):
            result = fibonacci(i)
            results.append(result)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
