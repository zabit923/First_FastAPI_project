from datetime import datetime
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing_extensions import List, Optional




app = FastAPI(title='Trading App')


users = [
    {'id': 1, 'role': 'admin', 'name': 'Zabit'},
    {'id': 2, 'role': 'client', 'name': 'Maga'},
    {'id': 3, 'role': 'client', 'name': 'Vasya', 'degree': [
        {'id': 1, 'created_at': '2024-01-01T00:00:00', 'type_degree': 'expert'}
    ]},
]


class DegreeType(Enum):
    newbie: 'newbie'
    expert: 'expert'

class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType

class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get('/users/{user_id}', response_model=List[User])
def get_users(user_id: int):
    return [user for user in users if user.get('id') == user_id]



fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.12},
    {'id': 2, 'user_id': 2, 'currency': 'RUB', 'side': 'sell', 'price': 1, 'amount': 2.12},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=3)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}