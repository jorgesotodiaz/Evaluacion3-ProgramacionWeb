from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None

    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        if all(10 <= nota <= 70 for nota in
               [nota1, nota2, nota3]) and 0 <= asistencia <= 100:

            promedio = round((nota1 + nota2 + nota3) / 3, 1)

            if promedio >= 40 and asistencia >= 75:
                estado = 'APROBADO'
            else:
                estado = 'REPROBADO'

        else:
            estado = 'Datos fuera de rango'

    return render_template(
        'ejercicio1.html',
        promedio=promedio,
        estado=estado
    )


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    cantidad = None
    error = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        nombres = [nombre1, nombre2, nombre3]

        if not all(nombres):
            error = 'Debes ingresar los tres nombres.'

        elif len(set(nombre.casefold() for nombre in nombres)) != 3:
            error = 'Los tres nombres deben ser diferentes.'

        else:
            nombre_mayor = max(nombres, key=len)
            cantidad = len(nombre_mayor)

    return render_template(
        'ejercicio2.html',
        nombre_mayor=nombre_mayor,
        cantidad=cantidad,
        error=error
    )



if __name__ == '__main__':
    app.run(debug=True)
