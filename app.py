# Importar el módulo sqlite3
import email
import sqlite3
# Importar modulo de error de sqlite3
from sqlite3 import Error
from tkinter.tix import Form
from flask import Flask,request,render_template, session, g, Blueprint
import os
from models import tipoPersona, habitaciones, personas, reservas, comentarios, loginForm
import hashlib



# bp = Blueprint('app', __name__, url_prefix='/app')


app = Flask(__name__)
app.secret_key = os.urandom(24)

# @app.route("/")
# def inicio():
#    return "<p>Hola, World!!!!</p>"

######  RUTAS BASE #################################
@app.route("/")
def index():
   return render_template('index.html')

@app.route("/registro")
def registro():
   return render_template('registro.html')

@app.route("/superadmin_usu")
def superadmin_usu():
   return render_template('superadmin_usu.html')

@app.route("/superadmin_adm")
def superadmin_adm():
   return render_template('superadmin_adm.html')

@app.route("/superadmin_hab")
def superadmin_hab():
   return render_template('superadmin_hab.html')

@app.route("/disponibilidad")
def disponibilidad():
   return render_template('usu_disp.html')

@app.route("/reservas")
def reservas():
   return render_template('usu_rese.html')


# @app.route("/administrador")
# def administrador():
    
#    return render_template('administrador.html')

# @app.route("/administrador2")
# def administrador2():
#    return render_template('administrador2.html')

# @bp.before_app_request
# def load_logged_in_user():
#   user_id = session.get('user_id')
#   if user_id is None:
#   g.user = None
#   else:
#   g.user = get_db().execute(
#   ' SELECT * FROM user WHERE id = ?', (user_id,)
#   ).fetchone()

######  ACCIONES EN LA BASE DE DATOS #################################

def sql_connection():
    try:
        con = sqlite3.connect('database/hotelgevora.db')
        return con;
    except Error:
        print(Error)

    ################## LOGIN ############

@app.route("/login", methods=['GET', 'POST'])
def login():
    if  request.method == "GET": 
        form = loginForm() 
        return render_template('login.html', form=form) 
    if  request.method == "POST":
        usuario = request.args.get("usuarioLogin")
        password = request.args.get("passwordLogin")
        # md5 = hashlib.new('md5', password.encode('utf-8'))
        # password = md5.hexdigest()
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM personas WHERE usuario = ? and password = ?", (usuario, password))
        data = cursorObj.fetchone()
        if data is None:
            return 'Incorrect username and password.'
        else:
            return 'Welcome %s! Your rank is %s.' % (usuario, data[2])
    

    
# if  request.method == "GET": 
    #     form = loginForm() 
    #     return render_template('login.html', form=form) 
    # if  request.method == "POST":
    #     cod = request.form["usuarioLogin"] 
    #     nom = request.form["passwordLogin"]
    #     sql_select_user(cod)
    #     return "Vas Bien"


def sql_select_user(id):
    strsql = "SELECT * FROM personas WHERE usuario = '" + id + "';"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    usuario = cursorObj.fetchall()
    if usuario.lenght != 0:
        return "no encontrado"
    else:
        return usuario


    ## Tipo Persona ##

@app.route('/nuevotp', methods=['GET', 'POST'])
def nuevotp():
    if  request.method == "GET": # Si la ruta es accedida a través del método GET entonces
        form = tipoPersona() # Crea un nuevo formulario de tipo producto
        return render_template('nuevotp.html', form=form) # Redirecciona vista nuevo.html enviando la variable form
    if  request.method == "POST": # Si la ruta es accedida a través del método POST entonces
        cod = request.form["id_tipo_persona"] # Asigna variable cod con valor enviado desde formulario  en la vista HTML
        nom = request.form["tipo_persona_name"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        sql_insert_tipo_persona(cod, nom) # Llamado de la función para insertar el nuevo producto
        return "Consulta correcta"

def sql_insert_tipo_persona(id_tipo_persona, tipo_persona_name):
    strsql="insert into tipo_personas (id_tipo_persona, tipo_persona_name) values ("+id_tipo_persona+",'"+tipo_persona_name+"');"
    con=sql_connection()
    cursorObj=con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()  


    ####### HABITACION ############

@app.route('/nuevahabitacion', methods=['GET', 'POST'])
def nuevahabitacion():
    if  request.method == "GET": # Si la ruta es accedida a través del método GET entonces
        habitaciones =  verHabitaciones()
       # form = habitaciones() # Crea un nuevo formulario de tipo producto
        return render_template('nuevahabitacion.html', habitaciones = habitaciones) # Redirecciona vista nuevo.html enviando la variable form
    if  request.method == "POST": # Si la ruta es accedida a través del método POST entonces
        cod = request.form["id_habitaciones"] # Asigna variable cod con valor enviado desde formulario  en la vista HTML
        nom = request.form["name"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        cam = request.form["camas"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        dis = request.form["disponibilidad"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        sql_insert_habitacion(cod, nom, cam, dis) # Llamado de la función para insertar el nuevo producto
        habitaciones =  verHabitaciones()
        return render_template('nuevahabitacion.html', habitaciones = habitaciones)
        #return "Consulta correcta"

def sql_insert_habitacion(id_habitaciones, name, camas, disponibilidad):
    strsql="insert into habitaciones (id_habitaciones, name, camas, disponibilidad) values ("+id_habitaciones+",'"+name+"',"+camas+", '"+disponibilidad+"');"
    con=sql_connection()
    cursorObj=con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()  

def verHabitaciones(): 
    habitaciones = sql_select_habitaciones()
    return habitaciones

def sql_select_habitaciones():
    strsql = "SELECT * FROM habitaciones;"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    habitaciones = cursorObj.fetchall()
    return habitaciones


@app.route('/borrar_habitacion', methods=['GET'])
def borrar_habitacion():
    id = request.args.get('id') # Captura de la variable id enviada a través de la URL
    sql_delete_habitacion(id) # Llamado a la función de borrado de la base de datos
    return "Borrado exitosamente. Redireccionando <BR><META HTTP-EQUIV='REFRESH' CONTENT='4;URL=/nuevahabitacion'>"

def sql_delete_habitacion(id):
    strsql = "DELETE FROM habitaciones WHERE id_habitaciones = " + id + ";"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()


@app.route('/edithabitacion', methods=['GET', 'POST'])
def edithabitacion():
    # id = request.args.get('id')
        
    print ("Funcion ejecutando")
    # id = request.args['id']
    # sql_select_habitacion(id)
    if  request.method == "GET": 
        id = request.args['id']
        print ("Metodo GET")
        print (id)
        
        return render_template('edithabitacion.html', id = id)
    if  request.method == "POST": # Si la ruta es accedida a través del método POST entonces
        # cod = request.form["id_habitaciones"] # Asigna variable cod con valor enviado desde formulario  en la vista HTML
        id2 = request.form["id_habitaciones"]
        print("#########################################################3")
        print (id2)
        nom = request.form["name"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        cam = request.form["camas"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        dis = request.form["disponibilidad"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        sql_edit_habitacion(id2, nom, cam, dis) # Llamado de la función para insertar el nuevo producto
        print ("Metodo POST")
        return "Editado exitosamente. Redireccionando <BR><META HTTP-EQUIV='REFRESH' CONTENT='4;URL=/nuevahabitacion'>"

def sql_edit_habitacion(id_habitaciones, name, camas, disponibilidad):
    print(id_habitaciones)
    print(name)
    print(camas)
    print(disponibilidad)
    strsql = "UPDATE habitaciones SET id_habitaciones = "+str(id_habitaciones)+", name = '"+name+"', camas = "+str(camas)+", disponibilidad = '"+disponibilidad+"' WHERE id_habitaciones = " +str(id_habitaciones) + ";"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()

def sql_select_habitacion(id):
    strsql = "SELECT * FROM habitaciones WHERE id_habitaciones = '" + id + "';"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    habitacion = cursorObj.fetchall()
    return habitacion


    ########## PERSONAS #########

@app.route('/nuevousuario', methods=['GET', 'POST'])
def nuevousuario():
    if  request.method == "GET": # Si la ruta es accedida a través del método GET entonces
        personas =  verPersonas()
       # form = habitaciones() # Crea un nuevo formulario de tipo producto
        return render_template('nuevousuario.html', personas = personas) # Redirecciona vista nuevo.html enviando la variable form
    if  request.method == "POST": # Si la ruta es accedida a través del método POST entonces
        cod = request.form["id233"] # Asigna variable cod con valor enviado desde formulario  en la vista HTML
        nom = request.form["nombre"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        usu = request.form["usuario"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        pas = request.form["password"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        ema = request.form["email"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        tel = request.form["telefono"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        tpe = request.form["tipo_persona"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        sql_insert_personas(cod, nom, usu, pas, ema, tel, tpe) # Llamado de la función para insertar el nuevo producto
        personas =  verPersonas()
        return render_template('nuevousuario.html', personas = personas)
        #return "Consulta correcta"

def sql_insert_personas(id_personas, nombre, usuario, password, email, telefono, tipo_persona):
    strsql="insert into personas (id_personas, nombre, usuario, password, email, telefono, tipo_persona) values ("+id_personas+",'"+nombre+"','"+usuario+"','"+password+"', '"+email+"', '"+telefono+"', '"+tipo_persona+"');"
    con=sql_connection()
    cursorObj=con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()  

def verPersonas(): 
    personas = sql_select_personas()
    return personas

def sql_select_personas():
    strsql = "SELECT * FROM personas;"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    personas = cursorObj.fetchall()
    return personas


