import requests

def get_weather(city, units ='metric', API_key = 'c2973de5c7abab8a9323eb0a28aa0f89'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units={units}"
  r = requests.get(url)
  #results = []
  content = r.json()
  #articles = content["temp"]
  for dicty in content["list"]:
    print(dicty["dt_txt"], dicty["main"]["temp"])
   # results.appednd(article["title"], article["description"])
  #return content

print(get_weather(city = "posen"))