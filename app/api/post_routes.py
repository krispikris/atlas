from flask import Blueprint, jsonify, session
from flask_login import login_required
from app.models import Post

post_routes = Blueprint('posts', __name__)
