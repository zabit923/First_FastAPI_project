from fastapi import FastAPI


app = FastAPI(title='Trading App')




users = [
    {'id': 1, 'role': 'admin', 'name': 'Zabit'},
    {'id': 2, 'role': 'client', 'name': 'Maga'},
    {'id': 3, 'role': 'client', 'name': 'Vasya'},
]

@app.get('/users/{user_id}')
def get_users(user_id: int):
    return [user for user in users if user.get('id') == user_id]


@app.get('/users/')
def get_trades(limit: int = 1, offset: int = 0):
    return users[offset:][:limit]


@app.post('/users/{user_id}')
def change_username(user_id: int, new_name: str):
    curent_user = list(filter(lambda user: user.get('id') == user_id, users))[0]
    curent_user['name'] = new_name
    return {'status': 200, 'user': curent_user}