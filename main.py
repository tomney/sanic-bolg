from sanic import Sanic, Blueprint

from app.articles import bp as articles_bp
from app.images import bp as images_bp

bolg = Blueprint.group(articles_bp, images_bp, url_prefix="/bolg")

app = Sanic()
app.config.from_pyfile("./config.py")
app.static("/", "./static/main.html")
app.blueprint(bolg)

if __name__ == "__main__":
    app.run(debug=True, access_log=True)
