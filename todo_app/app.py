from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import trello_get_items, trello_add_item, change_status
from todo_app.ViewModel import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items = trello_get_items()
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/add', methods=['POST'])
    def submit_film():
        title = request.form['title']
        trello_add_item(title)
        return redirect('/')

    @app.route('/update-doing', methods=['POST'])
    def update_item_to_doing():
        id = request.form['id']
        change_status(id, 'doing')
        return redirect('/')

    @app.route('/update-done', methods=['POST'])
    def update_item_to_done():
        id = request.form['id']
        change_status(id, 'done')
        return redirect('/')

    return app
