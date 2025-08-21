from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

class Preferencias(BaseModel):
    genero: str
    faixa_etaria: str



def carregar_dados():
    with open(r'D:\TCC\sistema especialista\sistema-especialista-games-api\expert-sys-games\app\games_data\data.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
    return dados

def recomendar_jogos(preferencias: Preferencias):
    recomendacoes = []
    for regra in regras:
        condicao = regra["Condição"]
        if (preferencias.genero.title() == condicao["Gênero"] and
                preferencias.faixa_etaria.title() == condicao["Faixa Etária"]):
            recomendacoes.extend(regra["Recomendação"])
    return recomendacoes



dados = carregar_dados()
jogos = dados['jogos']
regras = dados['regras']
print(dados)

@app.post("/recomendar-jogos/")
async def recomendar_jogos_api(preferencias: Preferencias):
    jogos_recomendados = recomendar_jogos(preferencias)
    if jogos_recomendados:
        return {"Jogos Recomendados": jogos_recomendados}
    else:
        return {"Mensagem": "Nenhuma recomendação disponível para suas preferências."}