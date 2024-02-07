from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import trello_get_items, trello_add_item, change_to_doing, change_to_done

app = Flask(__name__)
app.config.from_object(Config())
trello_get_items()

@app.route('/')
def index():
    items = trello_get_items()
    return render_template('index.html',items=items)

@app.route('/add', methods=['POST'])
def submit_film():
    title = request.form['title']
    trello_add_item(title)
    return redirect('/')

@app.route('/update-doing', methods=['POST'])
def update_item_to_doing():
    id = request.form['id']
    change_to_doing(id)
    return redirect('/')

@app.route('/update-done', methods=['POST'])
def update_item_to_done():
    id = request.form['id']
    change_to_done(id)
    return redirect('/')