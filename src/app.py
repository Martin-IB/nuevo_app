from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario
from dao.DAOEmpleados import DAOEmpleados

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()
db_emp = DAOEmpleados()

ruta='/usuario'
ruta_emp = '/empleados'

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route(ruta+'/')
def usuario_index():
    data = db.read(None)
    return render_template('usuario/index.html', data = data)

@app.route(ruta_emp + '/')
def empleado_index():
    data = db_emp.read(None)
    return render_template('empleados/index.html', data=data)

# ------------------ RUTAS USUARIO ------------------

@app.route(ruta+'/add/')
def add():
    return render_template('/usuario/add.html')

@app.route(ruta+'/addusuario', methods = ['POST', 'GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo usuario creado")
        else:
            flash("ERROR, al crear usuario")

        return redirect(url_for('usuario_index'))
    else:
        return redirect(url_for('usuario_index'))

@app.route(ruta+'/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('usuario_index'))
    else:
        session['update'] = id
        return render_template('usuario/update.html', data = data)

@app.route(ruta+'/updateusuario', methods = ['POST'])
def updateusuario():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('usuario_index'))
    else:
        return redirect(url_for('usuario_index'))

@app.route(ruta+'/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('usuario_index'))
    else:
        session['delete'] = id
        return render_template('usuario/delete.html', data = data)

@app.route(ruta+'/deleteusuario', methods = ['POST'])
def deleteusuario():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('usuario_index'))
    else:
        return redirect(url_for('usuario_index'))

# ------------------ RUTAS EMPLEADO ------------------

@app.route(ruta_emp + '/add/')
def empleado_add():
    return render_template('empleados/add.html')

@app.route(ruta_emp + '/addempleado', methods=['POST','GET'])
def addempleado():
    if request.method == 'POST' and request.form['save']:
        if db_emp.insert(request.form):
            flash("Nuevo empleado creado")
        else:
            flash("ERROR al crear empleado")
        return redirect(url_for('empleado_index'))
    else:
        return redirect(url_for('empleado_index'))
    
@app.route(ruta_emp + '/update/<int:id>/')
def empleado_update(id):
    data = db_emp.read(id)
    if len(data) == 0:
        return redirect(url_for('empleado_index'))
    session['update_emp'] = id
    return render_template('empleados/update.html', data=data)

@app.route(ruta_emp + '/updateempleado', methods=['POST'])
def updateempleado():
    if request.method == 'POST' and request.form['update']:

        if db_emp.update(session['update_emp'], request.form):
            flash('Empleado actualizado correctamente')
        else:
            flash('ERROR en actualizar empleado')
        session.pop('update_emp', None)
        return redirect(url_for('empleado_index'))
    else:
        return redirect(url_for('empleado_index'))

@app.route(ruta_emp + '/delete/<int:id>/')
def empleado_delete(id):
    data = db_emp.read(id)
    if len(data) == 0:
        return redirect(url_for('empleado_index'))
    session['delete_emp'] = id
    return render_template('empleados/delete.html', data=data)

@app.route(ruta_emp + '/deleteempleado', methods=['POST'])
def deleteempleado():
    if request.method == 'POST' and request.form['delete']:
        if db_emp.delete(session['delete_emp']):
            flash('Empleado eliminado')
        else:
            flash('ERROR al eliminar empleado')
        session.pop('delete_emp', None)
        return redirect(url_for('empleado_index'))
    else:
        return redirect(url_for('empleado_index'))
#------------------------------------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000)




