#! /usr/bin/python3
#sudo -E python3 main.py TO_RUN
#aggiungere meteo, mail, YT trends, translator a lato

import pygooglenews
import goose3
import requests

#italian newspapers list
newspapersIT = [
	"https://www.corriere.it",
	"https://www.repubblica.it",
	"https://www.ilsole24ore.com",
	"https://www.tgcom24.mediaset.it",
	"https://www.lastampa.it",
	"https://tg24.sky.it",
	"https://www.ansa.it",
	"https://www.ilmessaggero.it",
	"https://www.quotidiano.net",
	"https://www.ilgiornale.it",
	"https://www.ilfattoquotidiano.it"
]
#english newspapers list
newspapersEN = [
	"https://www.nytimes.com",
	"https://www.bbc.com",
	"https://www.bbc.co.uk",
	"https://www.cnn.com",
	"https://www.wsj.com",
	"https://apnews.com"
]

stories = [] #list of articles we will show
def getNews(lang, country, list):

	gn = pygooglenews.GoogleNews(lang = lang, country = country)
	extractor = goose3.Goose()

	top = gn.top_news()
	for mainTopicArticle in top["entries"]: #topic articles cluster, with one that stands out
		
		if mainTopicArticle.source.href not in list: continue

		res = requests.head(mainTopicArticle.link, allow_redirects=True)
		resolvedLink = res.url #resolved

		article = extractor.extract(url = resolvedLink)
		text = article.cleaned_text
		summary = article.meta_description
		print(image)
		input()

		story = {
			"title": mainTopicArticle.title,
			"published": mainTopicArticle.published,
			"sourceLink": mainTopicArticle.source.href,
			"sourceName": mainTopicArticle.source.title,
			"articleLink": resolvedLink,
			"text": text,
			"summary": summary
		}
		
		stories.append(story)

	return

getNews("it", "IT", newspapersIT)
getNews("en", "US", newspapersEN)

for story in stories:
	print(f"newspaper: {story['sourceName']}")
	print(f"title: {story['title']}")
	print(f"summary: {story['summary']}")
	print(f"published date: {story['published']}")
	input()