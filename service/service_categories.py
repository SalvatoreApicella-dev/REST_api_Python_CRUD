from dao.dao import ArticlesDAO
from dao.dao_categories import CategoriesDAO
import service
DAO_cat = CategoriesDAO()
DAO_art = ArticlesDAO()


def create_newCat(self, new_cat):
    return DAO_cat.create(new_cat)


def get_newCat(self):
    return DAO_cat.find_all()


def put_newCat(self, id, new_cat):
    return DAO_cat.update(id, new_cat)


def get_id_newCat(self, id):
    return DAO_cat.find_id(id)


def delete_newCat(self, id):
    return DAO_cat.delete(id)


def put_newArt(self, id_category, id, new_cat):
    if DAO_cat.find_id(id_category):
        return DAO_art.update(id, new_cat)


def get_id_newArt(self, id_category, id):
    if DAO_cat.find_id(id_category):
        return service.get_id_newArt(self,id)


def delete_newArt(self, id_category, id):
    if DAO_cat.find_id(id_category):
        return DAO_art.delete( id)

def get_all_bycat(self, id_category):
    if DAO_cat.find_id(id_category):
        return DAO_art.find_all_by_cat(id_category)

def create_newArt(self, id_category, new_art):
    if DAO_cat.find_id(id_category):
        return DAO_art.create(new_art)

