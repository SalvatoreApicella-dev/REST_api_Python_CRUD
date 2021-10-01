from sqlalchemy import Column, Integer, String, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_dao import Dao
Base = declarative_base()
DB = 'mysql+pymysql://root:1234@localhost/articoli'

class Articles(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    id_category = Column(Integer, nullable=False)
    datePublished = Column(Date, nullable=False)

    def __repr__(self):
        return self._repr(id=self.id,
                          title=self.title,
                          author=self.author,
                          id_category=self.id_category,
                          datePublished=self.datePublished)

class Categories(Base):
        __tablename__ = 'categories'

        id_category = Column(Integer, primary_key=True)
        name = Column(String(255), nullable=False)
        target = Column(String(255), nullable=False)

        def __repr__(self):
            return self._repr(id_category=self.id_category,
                              name=self.name,
                              target=self.target)



def init_schema():
    engine = create_engine('mysql+pymysql://root:1234@localhost/articoli', encoding='latin1', echo=True)
    Base.metadata.create_all(bind=engine)
    dao = Dao(DB)


