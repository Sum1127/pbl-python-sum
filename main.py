from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from database import read_fruit,add_fruit,read_fruit_select,update_fruit

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "This is Sum's server! "}


@app.get("/fruits/{id}")
def get_select_fruit(id:int):
    select_fruit=read_fruit_select(id)
    return select_fruit

@app.get("/fruits")
def get_fruit():
    fruits = read_fruit()
    return fruits

@app.put("/fruits/{id}")
def put_update_fruit(id: int, name,price,storename):
    put_fruit=update_fruit(id,name,price,storename)
    return {"id":put_fruit.id,"name":put_fruit.name,"price":put_fruit.price,"storename":put_fruit.storename}

@app.post("/fruits/{id}")
def post_fruit(id,name,price,storename):
    postfruit=add_fruit(id,name,price,storename)
    return {"id":postfruit.id,"name":postfruit.name,"price":postfruit.price,"storename":postfruit.storename}

@app.delete("/fruits/{id}")
def delete_fruit(id:int):
    return 



