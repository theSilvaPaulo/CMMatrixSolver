from flask import Flask
from app.views import app_views
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(app_views)

app.config['FLASK_DEBUG'] = True

if __name__ == '__main__':
    app.run()