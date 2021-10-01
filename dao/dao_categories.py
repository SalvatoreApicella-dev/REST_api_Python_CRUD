from copy import deepcopy, copy
from sqlalchemy_dao import Dao
from werkzeug.exceptions import NotFound

from schema import DB, Categories, Articles


class CategoriesDAO(object):

    def __init__(self):
        self.dao = Dao(DB)

    def find_all(self):
        with self.dao.create_session() as session:
            category = session.query(Categories).all()
            return deepcopy(category)  # con copy non funziona

    def create(self, new_cat):
        with self.dao.create_session() as session:
            new_category = Categories(**new_cat)
            session.add(new_category)
            session.flush()
            return {"id": new_category.id_category, **new_cat}

    def update(self, get_id, new_cat):
        with self.dao.create_session() as session:
            session.query(Categories).filter_by(id_category=get_id).update(new_cat)
            session.commit()
            return {"id": get_id, **new_cat}

    def find_id(self, id):
        with self.dao.create_session() as session:
            category = session.query(Categories).filter(Categories.id_category == id).first()
            if category:
                return deepcopy(category)
            else:
                raise NotFound

    def delete(self, id):
        with self.dao.create_session() as session:
            category = session.query(Categories).filter(Categories.id_category == id).first()

            if category:
                session.delete(category)
                session.commit()
                return "", 200
            else:
                raise NotFound


