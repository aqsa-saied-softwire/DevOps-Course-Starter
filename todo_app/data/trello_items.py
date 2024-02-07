import requests, json, os

board_id = os.getenv('BOARD_ID')
api_key = os.getenv('TRELLO_API_KEY')
token = os.getenv('TRELLO_API_TOKEN')
to_do_list = os.getenv('TO_DO_LIST_ID')
doing_list = os.getenv('DOING_LIST_ID')
done_list = os.getenv('DONE_LIST_ID')


def trello_get_items():
    url = 'https://api.trello.com/1/boards/{board_id}/lists'.format(board_id=board_id)
    headers = {
        "Accept": "*/*"
    }

    query = {
        'key': api_key,
        'token': token,
        'cards': 'open'
    }
    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    lists = json.loads(response.text)
    items = []
    for list in lists:
        status = list["name"]
        tasks = list["cards"]
        for task in tasks:
            items.append({ 'id': task['id'], 'status': status, 'title': task['name']})
    return items

def trello_add_item(title):
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

def change_to_doing(item):
    url = 'https://api.trello.com/1/cards/{id}'.format(id=item)
    headers = {
        "Accept": "*/*"
    }
    print(item)

    query = {
        'key': api_key,
        'token': token,
        'idList': doing_list
    }

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )
    print(response.reason)

def change_to_done(item):
    url = 'https://api.trello.com/1/cards/{id}'.format(id=item)
    headers = {
        "Accept": "*/*"
    }
    print(item)

    query = {
        'key': api_key,
        'token': token,
        'idList': done_list
    }

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )
    print(response.reason)