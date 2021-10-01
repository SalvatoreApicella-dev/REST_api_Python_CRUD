from flask import request, Blueprint
from flask_restplus import fields, Resource, Api
from service import service_categories, service
from controller.controller import article_model

blueprint = Blueprint('api_controller', __name__)
categories_blueprint = Blueprint('categories', __name__)

api = Api(blueprint)

categories_model = api.model('Categories', {
    'id_category': fields.Integer,
    'name': fields.String(description='The name', required=True),
    'target': fields.String(description='The target', required=True),
})


@api.route('/categories/')
class CategoriesController(Resource):

    @api.expect(categories_model, validate=True)
    @api.marshal_with(categories_model)
    def post(self):  # check errore unexpected
        return service_categories.create_newCat(self, new_cat=request.json), 201

    @api.marshal_with(categories_model, code=200)
    def get(self):
        return service_categories.get_newCat(self)


@api.route('/categories/<int:id_category>')
class ArticleController(Resource):
    @api.expect(categories_model, validate=True)
    @api.marshal_with(categories_model)
    def put(self, id_category):
        return service_categories.put_newCat(self, id_category, new_cat=request.json), 201

    @api.marshal_with(categories_model)
    def get(self, id_category):
        return service_categories.get_id_newCat(self, id_category)

    def delete(self, id_category):
        return service_categories.delete_newCat(self, id_category)


@api.route('/categories/<int:id_category>/articles/<int:id>')
class ArticleController(Resource):

    def put(self, id_category, id):
        return service_categories.put_newArt(self, id_category, id, new_cat=request.json), 201

    @api.marshal_with(article_model)
    def get(self, id_category, id):
        return service_categories.get_id_newArt(self, id_category, id)

    def delete(self, id_category, id):
        return service_categories.delete_newArt(self, id_category, id)


@api.route('/categories/<int:id_category>/articles/')
class ArticleController(Resource):

    @api.expect(article_model, validate=True)
    @api.marshal_with(article_model)
    def post(self,id_category):  # check errore unexpected
        return service_categories.create_newArt(self, id_category, new_art=request.json), 201

    @api.marshal_with(article_model)
    def get(self, id_category):
        return service_categories.get_all_bycat(self, id_category)
