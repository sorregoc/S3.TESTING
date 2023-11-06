from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Mysql Coneccion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskficha'
MySQL = MySQL(app)

# Configuraciones
app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        apellido = request.form['apellido']
        cur = MySQL.connection.cursor()
        cur.execute('SELECT * FROM fichamedica WHERE Apellidos = %s', (apellido,))
        data = cur.fetchall()
    else:
        cur = MySQL.connection.cursor()
        cur.execute('SELECT * FROM fichamedica')
        data = cur.fetchall()
    return render_template('index.html', datosficha=data)

@app.route('/add_ficha', methods=['POST'])
def add_ficha():
    if request.method == 'POST':
        Rut = request.form['rut']
        Nombres = request.form['nombres']
        Apellidos = request.form['apellidos']
        Direccion = request.form['direccion']
        Ciudad = request.form['ciudad']
        Telefono = request.form['telefono']
        Email = request.form['email']
        FechadeNacimiento = request.form['fechadeNacimiento']
        EstadoCivil = request.form['estadoCivil']
        Comentarios = request.form['comentarios']
        cur = MySQL.connection.cursor()
        cur.execute('INSERT INTO fichamedica (Rut, Nombres, Apellidos, Direccion, Ciudad, Telefono, Email, FechadeNacimiento, EstadoCivil, Comentarios) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (Rut, Nombres, Apellidos, Direccion, Ciudad, Telefono, Email, FechadeNacimiento, EstadoCivil, Comentarios))
        MySQL.connection.commit()
        flash('Ficha Medica Agregada Satisfactoriamente')
        return redirect(url_for('index'))
    return 'add_ficha'


if __name__ == '__main__':
    app.run(port=3000, debug=True)


