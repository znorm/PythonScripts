from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

BASE_URL = 'http://www.tunefind.com'



model_URL = "http://www.tunefind.com/show/greys-anatomy/season-"
seasonsList = []
for i in range (1,13):
	seasonsList.append(model_URL + str(i))

def removeDuplicates(seq):
   # Not order preserving
   keys = {}
   for e in seq:
       keys[e] = 1
   return keys.keys()

def get_html(url):
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	html = urlopen(req)
	return BeautifulSoup(html, 'html.parser')

def get_episodelinks(season_url):
	mainpart = get_html(season_url).find('ul', 'list-group')

	links = [BASE_URL + something.a["href"] for something in mainpart.findAll('div', "col-lg-2 col-md-3 col-xs-6")]
	links = removeDuplicates(links)
	return links

episodes_List = []

for seasons in seasonsList:
	episodes_List.extend(get_episodelinks(seasons))

songFile = open('songsfile.csv', 'w')

def getsongname(episode_url):
	mainpart = get_html(episode_url).find()
	for names in mainpart.findAll('div', 'media-body'):
		if (names.find(names.find("a", "js-song-name")) == None):
			songFile.write(names.find("a", "js-song-name").string + ",")
		if (names.find(href= re.compile('/artist*')) != None):
			songFile.write(names.find(href= re.compile('/artist/*')).string  + "\n")

for url in episodes_List:
	getsongname(url)
	
songFile.close()
# html_file = open('html_file.txt', 'w')
# html_file.write(get_html("http://www.tunefind.com/show/greys-anatomy/season-11/23192").prettify())
# html_file.close()

# html_secondfile = open('html_secondfile.txt', 'w')
# html_secondfile.write(getsongname("http://www.tunefind.com/show/greys-anatomy/season-11/23192"))
# html_secondfile.close()