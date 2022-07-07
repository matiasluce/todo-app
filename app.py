from flask import Flask ,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://bf59d8ce673298:9e144ef3@us-cdbr-east-06.cleardb.net/heroku_29a20ab690b553e'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Tarea(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(500))
    desc = db.Column(db.String(500))
    done = db.Column(db.Boolean())
    def __init__(self,name,desc,done):
        self.name = name
        self.desc = desc
        self.done = done
    
db.create_all() #Crea las tablas

class TareaSchema(ma.Schema):
    class Meta:
        fields=('id','name','desc','done')

producto_schema = TareaSchema()
productos_schema = TareaSchema(many = True)

@app.route('/tareas',methods=['GET'])
def get_Productos():
    all_productos = Tarea.query.all()
    result = productos_schema.dump(all_productos)
    return jsonify(result)

@app.route('/tareas/<id>',methods=['GET'])
def get_producto(id):
    producto=Tarea.query.get(id)
    return producto_schema.jsonify(producto)

@app.route('/tareas/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Tarea.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)

@app.route('/tareas', methods=['POST']) # crea ruta o endpoint
def create_producto():
    print(request.json)  # request.json contiene el json que envio el cliente
    name=request.json['name']
    desc=request.json['desc']
    done=request.json['done']
    new_producto=Tarea(name,desc,done)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)

@app.route('/tareas/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Tarea.query.get(id)
   
    name=request.json['name']
    desc=request.json['desc']
    done=request.json['done']
 
    producto.name=name
    producto.desc=desc
    producto.done=done
    db.session.commit()
    return producto_schema.jsonify(producto)

if __name__=='__main__':
    app.run(debug=True, port=5000)  