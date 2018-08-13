from flask import Flask, render_template, request,redirect, url_for

from project import Project

from datetime import date

app = Flask(__name__)


@app.route('/')
def dashboard():
    projects = Project.select()
    return render_template('index.html',projects_to_send=projects)

@app.route('/add', methods=['POST'])
def login():
    name = request.form['name_form']
    type=request.form['select_form']
    start_date = request.form['start_date']
    amount = request.form['amount']
    end_date = request.form['end_date']
    description = request.form['description']


    Project.create(name = name, type=type, start_date = start_date, end_date= end_date, amount= amount, description=description)

    return redirect('/')
@app.route('/delete/<int>')
def delete(int):
    Project.delete_by_id(int)
    return redirect('/')

@app.route('/update/<int:id>', methods =['POST'])
def update(id):
    name = request.form['name_edit']
    type=request.form['select_edit']
    start_date = request.form['start_date_edit']
    amount= request.form['amount_edit']
    end_date = request.form['end_date_edit']
    description = request.form['description_edit']

    project= Project.get(Project.id==id)
    project.name=name
    project.type=type
    project.start_date=start_date
    project.end_date=end_date
    project.amount=amount
    project.description=description
    project.save()
    return redirect('/')
    return name

if __name__ == '__main__':

    app.run(debug='true')
