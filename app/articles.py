from dataclasses import dataclass, field

from sanic import Blueprint

from app.shared import get_header, get_footer


bp = Blueprint('articles', url_prefix='/articles')
bp.static("/", "./static/articles")


@bp.middleware('response')
def add_header(request, response):
    header = get_header()
    response.body = header + response.body


@bp.middleware('response')
def add_footer(request, response):
    footer = get_footer()
    response.body = response.body + footer


@dataclass
class Article():
    title: str
    filename: str
    filepath: float = field(init=False)

    def __post_init__(self):
        self.filepath = f'{self.filename}.html'


articles = [
    Article("Here's a big dumb test article", "test")
]
