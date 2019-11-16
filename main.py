from sanic import Sanic
from sanic import response
from sanic.log import logger
from bolg import bolg


app = Sanic()
app.config.from_pyfile("./config.py")
app.blueprint(bolg)


@app.route("/")
async def test(request):
    logger.info("Testing it up")
    return response.json({"hello": "world"})


if __name__ == "__main__":
    app.run(debug=True, access_log=True)