from flask import Flask
from app.config import Settings
from app.routes import main, auth
from flask_session import Session

def create_app():
    app = Flask(__name__)
    app.config.from_object(Settings)
    
    @app.context_processor
    def inject_site_title():
        settingWeb = {
            "SITE_APP": app.config["SITE_APP"],
            "API_KEY": app.config["API_KEY"],
        }
        return settingWeb
    

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    return app
