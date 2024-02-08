from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

vendas = {
    1: {'item': 'lata', 'preco_unitario': 4, 'quantidade': 5},
    2: {'item': 'garrafa 2L', 'preco_unitario': 15, 'quantidade': 5},
    3: {'item': 'garrafa 750ml', 'preco_unitario': 10, 'quantidade': 5},
    4: {'item': 'lata mini', 'preco_unitario': 2, 'quantidade': 5},
}


class Inputs(BaseModel):
    input1: int
    input2: str


class UpdateVenda(BaseModel):
    item: str
    preco_unitario: int
    quantidade: int


@app.get('/')
def home():
    return {'Vendas': len(vendas)}


@app.get('/vendas/{id_venda}')
def pegar_venda(id_venda: int):
    if id_venda <= 2:
        return 'Testando 1 2 3'
    return vendas[id_venda]


@app.post('/cadastro-venda')
def cadastrar_venda(inputs: Inputs):
    return inputs


@app.delete('/delete')
def delete_venda(id: int):
    if id > len(vendas):
        return f'id deve ser menor ou igual a {len(vendas)}'
    name = vendas[id]['item']
    vendas.pop(id)
    
    return f"Item {name} excluído com sucesso!"


@app.put('/update/{id}')
def update_venda(id: int, input: UpdateVenda):
    vendas[id]['item'] = input.item
    vendas[id]['preco_unitario'] = input.preco_unitario
    vendas[id]['quantidade'] = input.quantidade
    
    return vendas[id]
