from flask import Flask, render_template, redirect, request, url_for
from dbconnect.connection import *


app = Flask(__name__)#App

@app.route('/')
def home():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)



#Se utiliza para agregar un comentario
@app.route('/addtask', methods=['GET', 'POST'])
def add_task():
    """
    Agrega tareas a la base de datos
    """
    if request.method == 'POST':
        task = request.form['content-task']#Tarea para ser agregada
        #si la tarea contiene texto y no solo espacios en blanco  
        if len(task.replace(' ', '')) > 0:
            query = 'insert into tasks (task) values ("{}")'.format(task)
            value = (task,)
            cursor.execute(query, value[0])#Ejecuta la consulta
            connection.commit()#Actualiza la base de datos
        
        return redirect(url_for('home'))


#Obtiene todas las tareas almacenadas en la base de datos
def get_tasks():
    """
    Retorna una lista de las tareas almacenadas en la base de datos
    """
    cursor.execute('select task from tasks')
    result = cursor.fetchall()#Todas las tareas

    result = [r[0] for r in result]#[(t1,), (t2,)] -> [t1, t2]
    return result

#Borra una tarea de acuerdo a su contenido

@app.route('/delete_task', methods=['GET', 'POST'])
def delete_task():
    """
    Busca en la base de datos una tarea que tenga dicho mensaje 
    """
    if request.method == 'POST':
        task = request.form['task']#Contenido de la tarea que se quiere eliminar
        cursor.execute('delete from tasks where task="{}"'.format(task))
        
        connection.commit()#Actualiza la base de datos

        newtasks = get_tasks()#Obtiene los datos ya actualizados
        return redirect(url_for('home', tasks=newtasks))



if __name__ == "__main__":
    app.run(debug=True)