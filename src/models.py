import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# ACA DEFINIMOS LA CLASE USUARIO. (LAS CLASES COMIENZAN CON MAYUS)
class Usuario(Base): 
    __tablename__ = 'usuario'
    # Here we define columns for the table usuario
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

# ACA DEFINIMOS LA CLASE PERSONAJES (LAS CLASES COMIENZAN CON MAYUS)
class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table personajes
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String (250))
    gender = Column(String (250))
    birth_year = Column(String (250))
    
# ACA DEFINIMOS LA CLASE PLANETAS (LAS CLASES COMIENZAN CON MAYUS)
class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table planetas
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String (250))
    diameter = Column(String (250))
    climate = Column(String (250))
    
# ACA DEFINIMOS LA CLASE VEHICULOS. (LAS CLASES COMIENZAN CON MAYUS)
class Naves(Base): 
    __tablename__ = 'naves'
    # Here we define columns for the table naves
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String (250))
    model = Column(String (250))
    starship_class = Column(String (250))
    
class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    naves_id= Column(Integer, ForeignKey('naves.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))


def to_dict(self):
        return {}

    ## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

# Created by N3o3N