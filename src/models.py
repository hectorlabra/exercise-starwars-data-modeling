from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    nombre = Column(String(250))
    apellido = Column(String(250))
    fecha_de_subscripción = Column(String(250))

    favoritos_planetas = relationship('Planeta', secondary='favoritos')
    favoritos_personajes = relationship('Personaje', secondary='favoritos')


class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), unique=True, nullable=False)
    período_de_rotación = Column(String(250))
    período_orbital = Column(String(250))
    diámetro = Column(String(250))
    clima = Column(String(250)) 
    gravedad = Column(String(250))
    terreno = Column(String(250))
    agua_superficial = Column(String(250))
    población = Column(String(250))
    residentes = Column(String(250))

    comentarios = relationship('Comentario')
    favoritos = relationship('Favorito')


class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), unique=True, nullable=False)
    altura = Column(String(250))
    peso = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    color_de_ojos = Column(String(250))
    birth_year = Column(String(250))
    género = Column(String(250))
    mundo_natal = Column(String(250))
    vehículos = Column(String(250))
    naves_estelares = Column(String(250))

    comentarios = relationship('Comentario')
    favoritos = relationship('Favorito')


class Comentario(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    contenido = Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    personaje_id = Column(Integer, ForeignKey('personajes.id'))

    usuario = relationship('Usuario')
    planeta = relationship('Planeta')
    personaje = relationship('Personaje')


class Favorito(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    personaje_id = Column(Integer, ForeignKey('personajes.id'))

    usuario = relationship('Usuario')
    planeta = relationship('Planeta')
    personaje = relationship('Personaje')

    def to_dict(self):
        return {}

# Generar el diagrama de entidad-relación
render_er(Base, 'diagram.png')
