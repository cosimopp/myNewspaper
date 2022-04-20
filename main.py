import newspaper #aggiungere meteo, mail, YT trends, translator a lato
import pygooglenews
import random

nationalNewspapers = ["https://www.open.online", "https://www.tgcom24.mediaset.it", "https://www.corriere.it", "https://www.repubblica.it", "https://www.ilsole24ore.com", "https://www.lastampa.it", "https://tg24.sky.it", "https://www.ilmessaggero.it", "https://www.ilfattoquotidiano.it"]
interNewspapers = ["https://apnews.com", "https://www.washingtonpost.com", "https://www.bbc.com", "https://www.telegraph.co.uk", "https://www.independent.co.uk", "https://www.bbc.co.uk", "https://www.nytimes.com", "https://www.theguardian.com", "https://www.cnn.com", "https://www.wsj.com", "https://nypost.com"]
stories = []
allNewspapers = nationalNewspapers + interNewspapers

def getStoriesFrom(country):
	if country == "IT": gn = pygooglenews.GoogleNews(lang = "it", country = "IT")
	elif country == "UK": gn = pygooglenews.GoogleNews(lang = "en", country = "UK")
	else: gn = pygooglenews.GoogleNews()

	top = gn.top_news(proxies=None, scraping_bee = None)#tutti servizi proxy
	for item in top["entries"]:
		
		if item.source.href in allNewspapers:
			
			story = {
				"title": item.title,
				"published": item.published,
				"source": item.source.title,
				"link": item.link
			}
			
			stories.append(story)

getStoriesFrom("IT")
getStoriesFrom("UK")
getStoriesFrom("US")

random.shuffle(stories)

for story in stories:
	print(f'DATE: {story["published"]}')
	print(f'TITLE: {story["title"]}')
	print(f'NEWSPAPER: {story["source"]}')
	print(f'\nCTRL+E to explore\nARROW_UP to previous article')
	input()


'''
for URL in interNewspapers:
	news = newspaper.build(URL, language="en")
	for article in news.articles:
		#article.download()
		#article.parse()
		print(article.title)
		print(article.summary)
		input()
'''