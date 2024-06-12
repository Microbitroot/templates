from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify({"status": "running"}), 200

if __name__ == '__main__':
    app.run(debug=True)
