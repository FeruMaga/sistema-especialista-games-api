from requests import post
import json
import os

api_key = os.getenv("API_KEY")

def fetch_games():
    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": "SEU_CLIENT_ID",
        "Authorization": "Bearer ${API_KEY}"
    }
    data = """
    fields age_ratings,aggregated_rating,alternative_names,artworks,cover,first_release_date,
    genres,name,platforms,summary,tags,themes,total_rating,total_rating_count,url;
    """

    response = post(url, headers=headers, data=data)
    if response.status_code == 200:
        games_data = response.json()
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(games_data, f, ensure_ascii=False, indent=4)
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    fetch_games()