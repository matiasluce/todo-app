from flask import Flask ,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://b38b54c3f7ee8b:151ee4fe@us-cdbr-east-06.cleardb.net/heroku_aafbe21240cea6e'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Producto(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(500))
    desc = db.Column(db.String(500))
    done = db.Colum(db.Boolean())
    def __init__(self,name,desc,done):
        self.name = name
        self.desc = desc
        self.done = done
    
db.create_all() #Crea las tablas

class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','name','desc','done')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many = True)

@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos = Producto.query.all()
    result = productos_schema.dump(all_productos)
    return jsonify(result)

@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)

@app.route('/producto/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)

@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    print(request.json)  # request.json contiene el json que envio el cliente
    name=request.json['name']
    desc=request.json['desc']
    done=request.json['done']
    new_producto=Producto(name,desc,done)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)

@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)
   
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