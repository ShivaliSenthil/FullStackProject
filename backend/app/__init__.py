from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register Blueprints or routes here
    from app.routes import main
    app.register_blueprint(main)

    return app
