from copy import deepcopy, copy
from sqlalchemy_dao import Dao
from werkzeug.exceptions import NotFound

from schema import Articles, DB, Categories


# aggiunta gestione categorie

class ArticlesDAO(object):

    def __init__(self):
        self.dao = Dao(DB)

    def find_all(self):
        with self.dao.create_session() as session:
            articles = session.query(Articles).all()
            return deepcopy(articles)  # con copy non funziona

    def create(self, new_art):
        with self.dao.create_session() as session:
            new_article = Articles(**new_art)
            session.add(new_article)
            session.flush()
            return {"id": new_article.id, **new_art}

    def update(self, get_id, new_art):
        with self.dao.create_session() as session:
            session.query(Articles).filter_by(id=get_id).update(new_art)
            session.commit()
            a = session.query(Articles).get(get_id)
            return {"id": get_id, **new_art}

    def find_id(self, id):
        with self.dao.create_session() as session:
            articles = session.query(Articles).filter(Articles.id == id).first()
            if articles:
                return deepcopy(articles)
            else:
                raise NotFound

    def delete(self, id):
        with self.dao.create_session() as session:
            articles = session.query(Articles).filter(Articles.id == id).first()

            if articles:
                session.delete(articles)
                session.commit()
                return "", 200
            else:
                raise NotFound

    def find_all_by_cat(self, id):
        with self.dao.create_session() as session:
            articles = session.query(Articles).filter(Articles.id_category == id).all()
            if articles:
                return deepcopy(articles)


