import requests, json, os
from todo_app import app
from todo_app.data.item_class import Item


def trello_get_items():
    board_id = os.getenv('BOARD_ID')
    api_key = os.getenv('TRELLO_API_KEY')
    token = os.getenv('TRELLO_API_TOKEN')
    url = f'https://api.trello.com/1/boards/{board_id}/lists?cards=open&key={api_key}&token={token}'
    response = requests.get(
        url
    )
    lists = response.json()
    items = []
    for listOfItems in lists:
        status = listOfItems["name"]
        tasks = listOfItems["cards"]
        for task in tasks:
            task['status'] = status
            item = Item.from_trello_card(card=task)
            items.append(item)
    return items


def trello_add_item(title):
    api_key = os.getenv('TRELLO_API_KEY')
    token = os.getenv('TRELLO_API_TOKEN')
    to_do_list = os.getenv('TO_DO_LIST_ID')
    url = 'https://api.trello.com/1/cards'
    headers = {
        "Accept": "*/*"
    }

    query = {
        'key': api_key,
        'token': token,
        'name': title,
        'idList': to_do_list
    }

    requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )


def change_status(item, newStatus):
    api_key = os.getenv('TRELLO_API_KEY')
    token = os.getenv('TRELLO_API_TOKEN')
    doing_list = os.getenv('DOING_LIST_ID')
    done_list = os.getenv('DONE_LIST_ID')
    if newStatus == 'doing':
        idList = doing_list
    elif newStatus == 'done':
        idList = done_list
    url = 'https://api.trello.com/1/cards/{id}'.format(id=item)
    headers = {
        "Accept": "*/*"
    }
    print(item)

    query = {
        'key': api_key,
        'token': token,
        'idList': idList
    }

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )
    print(response.reason)
