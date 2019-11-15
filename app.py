
from flask import Flask,jsonify,request,escape
from sklearn.externals import joblib

app=Flask(__name__)

@app.route('/')
def home():
    #caracteristicas=request.args.get("grados")
    return "Pagina activa"
    
@app.route('/predicciones',methods=['POST'])
def prediccion1():
    json=request.get_json(force=True)
    medidas=json['Medidas']
    arbol=joblib.load('random_forest_entrenado.pkl')
    predicciones=arbol.predict(medidas)
    return '\n\nEl vino corresponde a la clase {}'.format(predicciones)


if __name__ =='__main__':
    app.run()