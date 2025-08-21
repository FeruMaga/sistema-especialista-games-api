import requests
import json
import os
from dotenv import load_dotenv
import time

load_dotenv(dotenv_path="app/env/.env") 

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY não encontrada. Verifique env/.env")
FILE = "games_data/data_api.json"

def fetch_games(total_pages=5, delay=1):
    jogos_filtrados = []

    for page in range(1, total_pages + 1):
        url = "https://api.rawg.io/api/games"
        params = {
            "key": api_key,
            "page": page,
            "page_size": 50
        }
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            for jogo in data.get("results", []):
                jogos_filtrados.append({
                    "Título": jogo.get("name"),
                    "Gênero": [g["name"] for g in jogo.get("genres", [])],
                    "Faixa Etária": jogo.get("esrb_rating", {})
                })
            print(f"Página {page} processada, total de jogos: {len(jogos_filtrados)}")
        else:
            print(f"Erro na página {page}: {response.status_code}", response.text)
            break

        time.sleep(delay)

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(jogos_filtrados, f, ensure_ascii=False, indent=4)
    print(f"Todos os jogos salvos em {FILE}, total: {len(jogos_filtrados)}")

if __name__ == "__main__":
    fetch_games(total_pages=30, delay=2)