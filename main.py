import requests
import os

from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()

@app.get("/")
async def index():

  load_dotenv()

  api_key = os.environ['API_KEY']

  # ゲーム情報を取得するためのURL
  url = f"https://api.rawg.io/api/games?key={api_key}&page_size=10&metacritic=80,100&ordering=-released"

  response = requests.get(url)

  data = response.json()

  new_data = []

  for game in data['results']:
    game_info = {
      'name': game['name'],
      'released': game['released'],
      'metacritic': game.get('metacritic', 'N/A'),
      'platforms': ', '.join([platform['platform']['name'] for platform in game['platforms']])
    }
    new_data.append(game_info)

  return new_data
