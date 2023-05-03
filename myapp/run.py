import os
from flask import Flask
from flask_socketio import SocketIO, emit
import file_explorer

app = Flask(__name__)
app.register_blueprint(file_explorer.bp)
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

