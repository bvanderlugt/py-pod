from flask import Flask, json, render_template
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        APP_VERSION=os.getenv('APP_VERSION', '0.0.0'),
    )

    @app.route('/')
    def index():
        return render_template('index.html', app_version=app.config['APP_VERSION'])

    @app.route('/healthz')
    def health_check():
        return 'OK', 200

    @app.route('/readyz')
    def readiness_check():
        return 'OK', 200

    return app