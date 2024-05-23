from flask import Flask
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQLdb, MySQL
#PRUEBA COMENTARIO
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

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')

#FUNCIONES DE LOGIN
#OTRO COMENTARIO
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
                session['logueado'] = True #asdasdasdasdasdas
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
