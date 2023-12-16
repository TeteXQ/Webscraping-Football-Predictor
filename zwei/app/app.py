from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/current_chart')
def current_chart():
    return render_template('current_chart.html')

@app.route('/predictions')
def predictions():
    return render_template('predictions.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/current_matchday')
def current_matchday():
    return render_template('current_matchday.html')

if __name__ == '__main__':
    app.run(debug=True)