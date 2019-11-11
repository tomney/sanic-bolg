from sanic import Sanic
from sanic.response import json
from sanic.log import logger
from sanic import response

app = Sanic()
app.config.from_pyfile("./config.py")

@app.route("/")
async def test(request):
    logger.info("Testing it up")
    return json({"hello": "world"})

@app.route("/story")
async def story(request):
    logger.info("Telling a story")
    return response.html("<h1>Once upon a time some Stuff happened</h1>")

if __name__ == "__main__":
    app.run(debug=True, access_log=True)