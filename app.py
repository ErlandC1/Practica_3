from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Datos de seminarios (esto normalmente estaría en una base de datos)
seminarios_disponibles = ["Inteligencia Artificial", "Machine Learning", "Simulación con Arena", "Robótica Educativa"]

# Ruta para la página de registro
@app.route('/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        fecha = request.form['fecha']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        turno = request.form['turno']
        seminarios = request.form.getlist('seminarios')
        
        # Guarda el registro en la sesión (usado para simplificar)
        if 'registros' not in session:
            session['registros'] = []
        session['registros'].append({
            'fecha': fecha,
            'nombre': nombre,
            'apellidos': apellidos,
            'turno': turno,
            'seminarios': seminarios
        })
        return redirect(url_for('lista'))

    return render_template('registro.html', seminarios=seminarios_disponibles)

# Ruta para la lista de inscritos
@app.route('/lista')
def lista():
    registros = session.get('registros', [])
    return render_template('lista.html', registros=registros)

if __name__ == '__main__':
    app.run(debug=True)
