from sanic import Blueprint


articles = Blueprint('articles', url_prefix='/articles')
articles.static("/", "./static/articles")

images = Blueprint('images', url_prefix='/images')
images.static("/", "./static/images")

bolg = Blueprint.group(articles, images, url_prefix="/bolg")
