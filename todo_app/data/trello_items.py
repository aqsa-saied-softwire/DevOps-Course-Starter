import requests, json, os

board_id = os.getenv('BOARD_ID')
api_key = os.getenv('TRELLO_API_KEY')
token = os.getenv('TRELLO_API_TOKEN')

url = 'https://api.trello.com/1/boards/{board_id}/lists'.format(board_id=board_id)
headers = {
    "Accept": "*/*"
}

query = {
    'key': api_key,
    'token': token,
    'cards': 'open'
}

def trello_get_items():
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
            items.append({ 'id': task['idShort'], 'status': status, 'title': task['name']})
    return items