import requests
import html

res = requests.get("https://www.youtube.com/results?search_query=news")

print(html.unescape(res.text))