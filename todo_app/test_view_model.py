from todo_app.ViewModel import ViewModel
def test_view_model_done_property():
    items = [
        {
            'id': '1',
            'title': 'Item 1',
            'status': 'doing'
        },
        {
            'id': '2',
            'title': 'Item 2',
            'status': 'done'
        },
        {
            'id': '3',
            'title': 'Item 3',
            'status': 'doing'
        },
        {
            'id': '4',
            'title': 'Item 4',
            'status': 'done'
        }
    ]
    view_model = ViewModel(items)
    assert view_model.done_items == [
        {
            'id': '2',
            'title': 'Item 2',
            'status': 'done'
        },
        {
            'id': '4',
            'title': 'Item 4',
            'status': 'done'
        }
    ]