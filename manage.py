from flask import Flask
from config import dict_config

app = Flask(__name__)
app.config.from_object(dict_config['config'])

@app.route('/')
def index():
    return "ok"
if __name__ == '__main__':
    app.run()