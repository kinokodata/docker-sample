from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    data = {
        "message": "Hello World!",
        "time": datetime.now().strftime('%H:%M:%S'),
        "random_number": random.randint(1, 100)
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)