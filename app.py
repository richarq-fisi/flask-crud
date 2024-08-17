from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

#template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#template_dir = os.path.join(template_dir, 'templates')

app = Flask(__name__, template_folder = "templates")

#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM clientes")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form['telefono']

    if nombre and correo and telefono:
        cursor = db.database.cursor()
        sql = "INSERT INTO clientes (nombre, correo, telefono) VALUES (%s, %s, %s)"
        data = (nombre, correo, telefono)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM clientes WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form['telefono']

    if nombre and correo and telefono:
        cursor = db.database.cursor()
        sql = "UPDATE clientes SET nombre = %s, correo = %s, telefono = %s WHERE id = %s"
        data = (nombre, correo, telefono, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000, host="0.0.0.0")