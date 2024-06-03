from flask import Flask
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQLdb, MySQL

app = Flask(__name__,template_folder='template')

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='login'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/usuario.html')
def usuario():
    return render_template('usuario.html')

@app.route('/test.html')
def test():
    return render_template('test.html')

@app.route('/Ejercicios_Interactivos.html')
def ejercicios_interactivos():
    return render_template('Ejercicios_Interactivos.html')

@app.route('/Informes.html')
def informes():
    return render_template('Informes.html')

@app.route('/Recomendaciones.html')
def recomendaciones():
    return render_template('Recomendaciones.html')


@app.route('/acceso-login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        if 'txtUsuario' in request.form and 'txtPassword' in request.form:
            _usuario = request.form['txtUsuario']
            _contrasena = request.form['txtPassword']

            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s', (_usuario, _contrasena,))
            account = cur.fetchone()

            if account:
                session['logueado'] = True 
                session['id'] = account['id']
                return render_template("usuario.html")
            else:
                return render_template("index.html", error="Usuario o contraseña incorrectos")
        else:
            return render_template("index.html", error="Por favor, complete todos los campos")
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key="rafael"
    app.run(debug=True, host='0.0.0.0',port=5000, threaded=True)
