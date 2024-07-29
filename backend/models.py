from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Babosos(db.Model):
    __tablename__ = 'baboso'
    id_baboso = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), unique=True, nullable=False)

class Datos_baboso(db.Model):
    __tablename__ = 'datos_baboso'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    encuentro = db.Column(db.String(255), nullable=False)
    tiempo_declaracion = db.Column(db.String(255), nullable=False)
    aparicion = db.Column(db.String(255), nullable=False)
    frase_ingeniosa = db.Column(db.String(255), nullable=False)
    respuesta = db.Column(db.String(255), nullable=False)
    prop_indecentes = db.Column(db.String(255), nullable=False)
    prop_previsibles = db.Column(db.String(255), nullable=False)
    prop_divertidas = db.Column(db.String(255), nullable=False)
    voto_autoestima = db.Column(db.Integer, nullable=False)
    voto_insistente = db.Column(db.Integer, nullable=False)
    voto_originalidad = db.Column(db.Integer, nullable=False)
    conclusion = db.Column(db.String(255), nullable=False)
    id_baboso = db.Column(db.Integer, db.ForeignKey('baboso.id_baboso'))
