from os import environ

from flask import Flask
from schema import init_schema
from controller.controller import blueprint as api
from controller.controller_categories import blueprint as api_controller

app = Flask(__name__)
init_schema()

#categories_blueprint.register_blueprint(articles_blueprint)  # nesting blueprint
#app.register_blueprint(categories_blueprint)  # nesting blueprint
app.register_blueprint(api)
app.register_blueprint(api_controller)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
