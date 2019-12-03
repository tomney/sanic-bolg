from sanic import Blueprint

bp = Blueprint('images', url_prefix='/images')
bp.static("/", "./static/images")