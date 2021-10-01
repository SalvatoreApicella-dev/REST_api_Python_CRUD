from flask import request, Blueprint
from flask_restplus import fields, Resource, Api
from service import service

blueprint = Blueprint('api', __name__)
articles_blueprint = Blueprint('articles', __name__)

api = Api(blueprint)


article_model = api.model('Article', {
    'id':fields.Integer,
    'title': fields.String(description='The title', required=True),
    'author': fields.String(description='The author', required=True),
    'id_category': fields.Integer,
    'datePublished': fields.Date(description='The date', required=True)
})


@api.route('/articles/')
class ArticleController(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''

    @api.expect(article_model, validate=True)
    @api.marshal_with(article_model)
    def post(self):  # check errore unexpected
        return service.create_newArt(self, new_art=request.json), 201

    @api.marshal_with(article_model, code=200)
    def get(self):
        return service.get_newArt(self)


@api.route('/articles/<int:id>')
class ArticleController(Resource):
    #verifico che esista la categoria
    @api.expect(article_model, validate=True)
    @api.marshal_with(article_model)
    def put(self, id):
        return service.put_newArt(self, id, new_art=request.json), 201

    @api.marshal_with(article_model)
    def get(self, id):
        return service.get_id_newArt(self, id)

    def delete(self,  id):
        return service.delete_newArt(self, id)



