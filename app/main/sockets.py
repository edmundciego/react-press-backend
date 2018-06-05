from flask import request
from flask_socketio import emit

from .. import socket
from ..schema import schema
from ..helpers import auth_required, save_to_db, get_unread_notifications

@socket.on('connect')
@auth_required
def connect(user):
    user.session_id = request.sid
    save_to_db(user)

    emit('notifications', get_unread_notifications(user))

@socket.on('disconnect')
def disconnect():
    print('User disconnected')
 