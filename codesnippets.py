
from locale import currency
from typing import Optional
from urllib import response
from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import json

    
app = FastAPI()


@app.get("/cmc/dex")
def hello():
    response = requests.get("https://ton-swap-indexer.broxus.com/v1/cmc/dex")
    return response.json()

@app.get("/cmc/farming")
def cmcfarming():
    response = requests.get("https://ton-swap-indexer.broxus.com/v1/cmc/farming")
    return response.json()

@app.post("/currencies/{currencies}")
async def read_item(currencies):
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/currencies/"+currencies)
    return response.json()

@app.post("/currencies_usdt_prices")
async def get_body(request: Request):
    json1 =await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/currencies_usdt_prices", json = json1)
    return response.json()

@app.post("/currencies")
async def get_body(request: Request):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/currencies", json = json1)
    return response.json()

@app.post("/currencies/{currencies}/prices")
async def get_body(request: Request, currencies:str):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/currencies/" + currencies + "/prices", json = json1)
    return response.json()

@app.post("/currencies/{currencies}/volume")
async def get_body(request: Request, currencies:str):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/currencies/" + currencies + "/volume", json = json1)
    return response.json()

@app.post("/currencies/{currencies}/tvl")
async def get_body(request: Request, currencies:str):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/currencies/" + currencies + "/tvl", json = json1)
    return response.json()

@app.post("/currencies/{currencies}/fee")
async def get_body(request: Request, currencies:str):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/currencies/" + currencies + "/fee", json = json1)
    return response.json()

@app.post("/main/volume")
async def get_body(request: Request):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/main/volume", json = json1)
    return response.json()

@app.post("/main/tvl")
async def get_body(request: Request):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/main/tvl", json = json1)
    return response.json()

@app.post("/pairs")
async def get_body(request: Request):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/pairs", json = json1)
    return response.json()

@app.get("/pairs/meta")
async def get_body(request: Request):
    response = requests.get("https://ton-swap-indexer.broxus.com/v1/pairs/meta")
    return response.json()
    
@app.post("/pairs/address/{address}")
async def read_item(address:str):
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/pairs/address/" + address)
    return response.json()
    
@app.post("/pairs/cross_pairs")
async def get_body(request: Request):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/pairs/cross_pairs", json = json1)
    return response.json()

@app.post("/pairs/left/{left}/right/{right}")
async def read_item(left:str, right:str):
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/pairs/left/" + left + "/right/" + right)
    return response.json()
    
@app.post("/pairs/left/{left}/right/{right}/ohlcv")
async def get_body(request: Request, left:str, right:str):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/pairs/left/" + left + "/rigth/" + right + "/ohlcv", json = json1)
    return response.json()

@app.post("/pairs/address/{address}/ohlcv")
async def get_body(request: Request, address:str):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/pairs/address/" + address+"/ohlcv", json = json1)
    return response.json()

@app.post("/pairs/address/{address}/volume")
async def get_body(request: Request, address:str):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/pairs/address/" + address + "/volume", json=json1)
    return response.json()

@app.post("/pairs/address/{address}/tvl")
async def get_body(request: Request, address:str):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/pairs/address/" + address + "/tvl", json=json1)
    return response.json()

@app.post("/pairs/address/{address}/fee")
async def get_body(request: Request, address:str):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/pairs/address/" + address + "/fee", json=json1)
    return response.json()

@app.post("/transactions")
async def get_body(request: Request):
    json1 = await request.json()
    response = requests.post("https://ton-swap-indexer.broxus.com/v1/transactions", json = json1)
    return response.json()

