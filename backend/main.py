from models import db, Babosos, Datos_baboso
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://enzo:121629@localhost:5432/babosos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def inicio():
    return "Hola, Es la ruta principal"

@app.route("/babosos", methods=["GET", "POST"])
def data():
    if request.method == 'GET':
        try:
            babosos = Babosos.query.all()
            babosos_data = []
            for baboso in babosos:
                baboso_data = {
                    "id": baboso.id_baboso,
                    "nombre": baboso.nombre,
                }
                babosos_data.append(baboso_data)
            return jsonify(babosos_data)
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"mensaje": "no existe el baboso"}), 500
    elif request.method == 'POST':
        try:
            data = request.json
            nombre = data.get('nombre')
            encuentro = data.get('lugar_acercamiento')
            tiempo_declaracion = data.get('tiempo_declararse')
            aparicion = data.get('forma')
            frase_ingeniosa = data.get('frase')
            respuesta = data.get('respuesta')
            prop_indecentes = data.get('indecentes')
            prop_previsibles = data.get('previsibles')
            prop_divertidas = data.get('divertidos')
            voto_autoestima = data.get('autoestima')
            voto_insistente = data.get('insistencia')
            voto_originalidad = data.get('originalidad')
            conclusion = data.get('veredicto')
            nuevo_baboso = Datos_baboso(
                nombre=nombre, 
                encuentro=encuentro, 
                tiempo_declaracion=tiempo_declaracion, 
                aparicion=aparicion, 
                frase_ingeniosa=frase_ingeniosa, 
                respuesta=respuesta, 
                prop_indecentes=prop_indecentes, 
                prop_previsibles=prop_previsibles, 
                prop_divertidas=prop_divertidas, 
                voto_autoestima=voto_autoestima, 
                voto_insistente=voto_insistente, 
                voto_originalidad=voto_originalidad, 
                conclusion=conclusion
            )
        
            db.session.add(nuevo_baboso)
            db.session.commit()
            return jsonify({'id': nuevo_baboso.id, 'nombre': nuevo_baboso.nombre})
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'mensaje': 'Error del servidor'}), 500

@app.route("/babosos/<int:id_baboso>", methods=["GET", "DELETE", "PUT"])
def nuevo_baboso(id_baboso):
    baboso = Datos_baboso.query.get(id_baboso)
    if request.method == 'GET':
        if not baboso:
            return jsonify({"mensaje": "Baboso no encontrado"}), 404
        baboso_data = {
            "nombre": baboso.nombre, 
            "encuentro": baboso.encuentro, 
            "tiempo_declaracion": baboso.tiempo_declaracion, 
            "aparicion": baboso.aparicion, 
            "frase_ingeniosa": baboso.frase_ingeniosa, 
            "respuesta": baboso.respuesta, 
            "prop_indecentes": baboso.prop_indecentes, 
            "prop_previsibles": baboso.prop_previsibles, 
            "prop_divertidas": baboso.prop_divertidas, 
            "voto_autoestima": baboso.voto_autoestima, 
            "voto_insistente": baboso.voto_insistente, 
            "voto_originalidad": baboso.voto_originalidad, 
            "conclusion": baboso.conclusion
        }
        return jsonify(baboso_data)
    elif request.method == 'DELETE':
        if not baboso:
            return jsonify({"mensaje": "Baboso no encontrado"}), 404
        db.session.delete(baboso)
        db.session.commit()
        return jsonify({"Mensaje": "Baboso eliminado"}), 200
    elif request.method == 'PUT':
        if not baboso:
            return jsonify({"mensaje": "Baboso no encontrado"}), 404
        data_baboso = request.get_json()
        baboso.nombre = data_baboso.get('nombre', baboso.nombre)
        baboso.encuentro = data_baboso.get('encuentro', baboso.encuentro)
        baboso.tiempo_declaracion = data_baboso.get('tiempo_declaracion', baboso.tiempo_declaracion)
        baboso.aparicion = data_baboso.get('aparicion', baboso.aparicion)
        baboso.frase_ingeniosa = data_baboso.get('frase_ingeniosa', baboso.frase_ingeniosa)
        baboso.respuesta = data_baboso.get('respuesta', baboso.respuesta)
        baboso.prop_indecentes = data_baboso.get('prop_indecentes', baboso.prop_indecentes)
        baboso.prop_previsibles = data_baboso.get('prop_previsibles', baboso.prop_previsibles)
        baboso.prop_divertidas = data_baboso.get('prop_divertidas', baboso.prop_divertidas)
        baboso.voto_autoestima = data_baboso.get('voto_autoestima', baboso.voto_autoestima)
        baboso.voto_insistente = data_baboso.get('voto_insistente', baboso.voto_insistente)
        baboso.voto_originalidad = data_baboso.get('voto_originalidad', baboso.voto_originalidad)
        baboso.conclusion = data_baboso.get('conclusion', baboso.conclusion)
        db.session.commit()
        return jsonify({"id": baboso.id, "nombre": baboso.nombre}), 200

if __name__ == '__main__':
    print('Starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=5000)
    print('Started...')
