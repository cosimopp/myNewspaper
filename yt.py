#!/usr/bin/python3 
import youtubesearchpython.__future__ as ytFuture
import asyncio
import requests
import clearconsole
import multibar
import keyboard

import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        K_SPACE,
        )

# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
#pip3 install webdriver-manager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

likesAPI = "https://returnyoutubedislikeapi.com/votes?videoId="
# options = webdriver.ChromeOptions()

async def watch(video):
    url ="https://www.youtube.com/embed/{}?autoplay=1"
    url = url.format(video['id'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    return driver

async def main():

    clearconsole.cls()

    searchQuery = input("Search\n> ")

    videosList = []

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

        # try: print(f"description snippet: {res['descriptionSnippet'][0]['text']}")
        #la ricerca automata produceva errore
        print(f"description snippet: {res['descriptionSnippet']}")
        #videosList.append(res['link'])
        i+=1


    playlistsSearch = ytFuture.PlaylistsSearch(searchQuery, limit=5)
    playlistsResult = await playlistsSearch.next()
    p_results = playlistsResult["result"]
    p_links = [res["link"] for res in p_results]

    j = i #number of listed videos

    print(f"\n-------PLAYLISTS-------\n")
    print("playlist viewCount != its videos viewCount")

    for res in p_results:
        print(f"\n{i}) TITLE: {res['title']}")
        print(f"CHANNEL: {res['channel']['name']}")
        print(f"has {res['videoCount']} videos")
        #per vedere il lint, scorrere la riga incriminata e verrà fuori un pop up sul punto sbagliato
        playlistInfo = await ytFuture.Playlist.getInfo(res['link'])  
        print(playlistInfo['viewCount'])
        i += 1


    #get urls from playlist
    #pytube.Playlist()



    toPick = input("\n[a|v][index]: ")
    if int(toPick[1:])-j-1 >= 0: #è stata scelta una playlist
        pass
    else:
        driver = await watch(results[int(toPick[1:])])
    # https://stackoverflow.com/questions/9549729/vim-insert-the-same-characters-across-multiple-lines                 


    pygame.init()

    while True:

        for event in pygame.event.get():
            print("dentro primo")
            if event.type == K_LEFT:

                driver.find_element_by_tag_name("body").send_keys(Keys.LEFT)
            if event.type == K_RIGHT:

                driver.find_element_by_tag_name("body").send_keys(Keys.RIGHT)

            if event.type == K_SPACE:
                print("premuto space")
                driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)

    return


asyncio.run(main())
