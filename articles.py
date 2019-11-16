from sanic import Blueprint
from sanic.log import logger
from sanic import response


articles = Blueprint('articles', url_prefix='/articles')
articles.static("/article", "./static/articles")  # ./ works locally for now


@articles.route("/")
async def story(request):
    logger.info("Here is the article")
    return response.html("something")
