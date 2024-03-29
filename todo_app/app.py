from flask import Flask, render_template, request, redirect
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html',items=items)

@app.route('/add', methods=['POST'])
def submit_film():
    title = request.form['title']
    add_item(title)
    return redirect('/')