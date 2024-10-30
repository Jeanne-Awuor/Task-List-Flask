from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {'id': 1, "title": "Buy groceries", "description": "Buy milk,bread,sugar,flour"},
    {'id': 2, "title": "Study", "description": "Study Python Flask"}
]


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/create', methods= ['POST'])
def create():
    if request.method == "POST":
        new_id= len(tasks)+1
        title = request.form['title']
        description = request.form['description']
        tasks.append({'id': new_id, 'title': title, 'description': description})
        return redirect(url_for('index'))


@app.route('/delete/<int:id>' ,methods= ['POST','GET'])
def delete(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return redirect(url_for('index'))


@app.route('/edit/<int:id>' ,methods= ['POST','GET'])
def edit(id):
    task = next(( task for task in tasks if task['id'] == id ),None)
    print(task)
    if request.method == "POST":
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))

    return render_template('edit.html', task=task)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
