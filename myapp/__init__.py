import os
from flask import Flask
from flask_socketio import SocketIO, emit
import file_explorer

# application factory function
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(file_explorer.bp)

    # Initialise socketio
    socketio = SocketIO(app)

    # Define event handlers
    @socketio.on('connnect')
    def handle_connect():
        print('client connected')


    return app, socketio

app, socketio = create_app()

if __name__ == "__main__":
    socketio.run(app)