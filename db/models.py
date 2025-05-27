from .database import Base
from sqlalchemy import Column,Integer,String, ForeignKey

#Crear la clase modelo (Entidad)
class Categoria(Base):
    __tablename__="categorias"
    id = Column(Integer,
                primary_key=True
                )
    nombre = Column(String(50))

class Productos(Base):
    __tablename__="productos"
    id = Column(Integer,
                primary_key=True)
    nombre =Column(String(50))
    modelo=Column(String(50))
    precio=Column(Integer)
    
    categoria_id=Column(Integer, ForeignKey("categorias.id"))
    