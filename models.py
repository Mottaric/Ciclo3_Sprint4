import email
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired
        

####### Constructores de cada tabala ###############333

class loginForm(FlaskForm):
    usuario = StringField('usuario', validators=[DataRequired()])
    password = StringField('contraseña', validators=[DataRequired()])

class tipoPersona(FlaskForm):
    id_tipo_persona = IntegerField('Codigo tipo Persona', validators=[DataRequired(message='No dejar vacío, completar')])
    tipo_persona_name = StringField('Tipo de persona', validators=[DataRequired()])
    enviar = SubmitField('Agregar TIpo Persona')

class habitaciones(FlaskForm):
    id_habitaciones = IntegerField('Habitaciones', validators=[DataRequired(message='No dejar vacío, completar')])
    name = StringField('Nombre', validators=[DataRequired()])
    camas = IntegerField('Camas', validators=[DataRequired()])
    disponibilidad = StringField('Disponibiliad', validators=[DataRequired()])

class personas(FlaskForm):
    id_personas = IntegerField('id_personas', validators=[DataRequired(message='No dejar vacío, completar')])
    nombre = StringField('nombre', validators=[DataRequired()])
    usuario = StringField('usuario', validators=[DataRequired()])
    password = StringField('contraseña', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    telefono = StringField('telefono', validators=[DataRequired()])
    tipo_persona = StringField('tipo_Persona', validators=[DataRequired()])
    
class reservas(FlaskForm):
    id_reservas = IntegerField('id_Reserv', validators=[DataRequired(message='No dejar vacío, completar')])
    id_personas = IntegerField('Usuario', validators=[DataRequired()])
    id_habitaciones = IntegerField('Habitacion', validators=[DataRequired()])
    fecha = StringField('Fecha', validators=[DataRequired()])
    noches = IntegerField('No de Noches', validators=[DataRequired()])

class comentarios(FlaskForm):
   id_comentarios = IntegerField('id_Comentario', validators=[DataRequired(message='No dejar vacío, completar')])
   id_habitaciones = IntegerField('Habitacion', validators=[DataRequired()])
   id_personas = IntegerField('Usuario', validators=[DataRequired()])
   calificacion = StringField('Calificacion', validators=[DataRequired()])
   mensaje = StringField('Mensaje')
   

# class Comentarios(db.FlaskForm):
#     rowid = db.Column(db.Integer, primary_key=True)
#     habid = db.Column(db.Integer)
#     usuario = db.Column(db.Integer)
#     calificacion = db.Column(db.String(200))
#     mensaje = db.Column(db.String(500))


# class habitaciones(db.Model):
#     rowid = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200))
#     camas = db.Column(db.Integer)
#     disponibilidad = db.Column(db.Bool)


# class personas(db.Model):
#     rowid = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200))
#     usuario = db.Column(db.String(200))
#     email = db.Column(db.String(200))
#     telefono = db.Column(db.String(200))
#     tipoPersona = db.Column(db.Integer)

#     def readPersonas():
#         conn = sql.connect("hotelgevora.db")
#         cursor = conn.cursor()
#         instruction = f"SELECT * FROM personas "
#         cursor.execute(instruction)
#         datos = cursor.fetchall()
#         conn.commit()
#         conn.close()
#         print(datos)
        


# class reservas(db.Model):
#     rowid = db.Column(db.Integer, primary_key=True)
#     usuario = db.Column(db.String(200))
#     fecha = db.Column(db.String(200))
#     noches = db.Column(db.Integer)


# class tipoPersona(db.Model):
#     rowid = db.Column(db.Integer, primary_key=True)
#     tipoPersona = db.Column(db.String(200))




