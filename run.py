from flask import Flask
from app.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

app.config['FLASK_DEBUG'] = True

if __name__ == '__main__':
    app.run()