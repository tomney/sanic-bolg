from sanic import Sanic
from sanic import response
from sanic.log import logger
from articles import articles


app = Sanic()
app.config.from_pyfile("./config.py")
app.blueprint(articles)


@app.route("/")
async def test(request):
    logger.info("Testing it up")
    return response.json({"hello": "world"})


if __name__ == "__main__":
    app.run(debug=True, access_log=True)