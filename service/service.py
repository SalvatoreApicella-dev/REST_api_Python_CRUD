from dao.dao import ArticlesDAO

DAO_art = ArticlesDAO()


def create_newArt(self, new_art):
    return DAO_art.create(new_art)


def get_newArt(self):
    return DAO_art.find_all()


def put_newArt(self, id, new_art):
    return DAO_art.update( id, new_art)


def get_id_newArt(self, id):
    return DAO_art.find_id(id)


def delete_newArt(self, id):
    return DAO_art.delete(id)

def find_all(self, id):
    return DAO_art.find_all_by_cat(id)