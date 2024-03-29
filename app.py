from flask import Flask
from extensions import db
from dotenv import load_dotenv
import os
from auth import auth_bp

def create_app():

    app = Flask(__name__)

    load_dotenv()

    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
    app.config['DEBUG'] = os.getenv('FLASK_DEBUG')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('FLASK_SQLALCHEMY_DATABASE_URI')

    # initialize extensions
    db.init_app(app)

    app.register_blueprint(auth_bp,url_prefix='/auth')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()