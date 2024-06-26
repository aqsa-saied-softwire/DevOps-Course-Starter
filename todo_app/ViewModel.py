class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def done_items(self):
        return [item for item in self._items if item['status'] == 'done']

    @property
    def doing_items(self):
        return [item for item in self._items if item['status'] == 'doing']

    @property
    def to_do_items(self):
        return [item for item in self._items if item['status'] == 'to do']