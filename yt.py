import youtubesearchpython.__future__ as ytFuture
import asyncio
import requests
import clearconsole
import multibar

likesAPI = "https://returnyoutubedislikeapi.com/votes?videoId="
htmlPath = "/var/www/html/index.html"
embedCode = ""

def watch(video):


	#overwrite its content
	with open(htmlPath, 'w') as file:
		file.write('new content')


async def main():

	clearconsole.cls()

	searchQuery = input("Search\n> ")

	videosSearch = ytFuture.VideosSearch(searchQuery, limit = 10)
	videosResult = await videosSearch.next() #next method to get the results on the next pages
	
	results = videosResult["result"]
	links = [res["link"] for res in results]

	i = 0
	for res in results:
		response = requests.get(likesAPI + res['id']) #Rate Limiting: There are per client rate limits in place of 100 per minute and 10'000 per day. This will return a 429 status code indicating that your application should back off.
		data = response.json()
		print(f"\n{i}) TITLE: {res['title']}")

		likes = data.get('likes')
		dislikes = data.get('dislikes')
		print(f"VIEWS: {res['viewCount']['short']}   LIKES: {likes}   DISLIKES: {dislikes}")

		likesPercentage = (likes/(likes + dislikes))*100
		bar = multibar.ProgressBar(likesPercentage*2, 200).write_progress(fill="#", line="-")

		print(f"CHANNEL: {res['channel']['name']}  {bar.bar} {likesPercentage:.2f}%")
		print(f"POSTED: {res['publishedTime']}   DURATION: {res['duration']}")
		i+=1

	toPick = input("\n[index][a|v]: ")
	watch(results[i])

	return
	

asyncio.run(main())