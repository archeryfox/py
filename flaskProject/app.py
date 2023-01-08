from flask import Flask
from templates.renderer import parser

app = Flask(__name__)


@app.route('/')
def render():
    return parser("G:\site\ещо один\Новая папка\index(1).html")


if __name__ == '__main__':
    app.run()
