import newspaper

article = newspaper.Article("https://edition.cnn.com/2022/04/21/business/lukoil-ceo-alekperov-resigns/index.html")

article.download()
article.parse()
print(article.text)
