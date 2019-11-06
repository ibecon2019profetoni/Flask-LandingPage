from flask import Flask
from flask import render_template
from flask import request

import json
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # los datos de tiempo en este momento
    # ahora = datetime.datetime(2019,11,6)
    ahora = datetime.datetime.now()
    # El día de la senama, en número
    num_dia_sem = ahora.strftime('%w')
    """ según el día de la semana hay cambios en la web """
    # Abrir el archivo Json y leerlo
    with open('plantillas.json') as archivo_json:
        datos = json.loads(archivo_json.read())
    # sacar datos según el día
    context = {
        # insertar en html
        'titulo' : datos[num_dia_sem].get('titulo'),
        'imagen' : datos[num_dia_sem].get('imagen'),
        # insertar en las clases
        'class_fondo' : datos[num_dia_sem].get('class_fondo'),
        'class_color' : datos[num_dia_sem].get('class_color'),
        'class_boton' : datos[num_dia_sem].get('class_boton'),
        'class_boton_texto' : datos[num_dia_sem].get('class_boton_texto'),
        'class_posicion' : datos[num_dia_sem].get('class_posicion'),
    }

    # return titulo + ' - ' + color + ' - ' + imagen

    return render_template('index.html', **context)


if __name__ == "__main__":
    app.run('127.0.0.1',5500,debug='True')