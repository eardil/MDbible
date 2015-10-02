import requests
from bs4 import BeautifulSoup, Comment



def getVerses(passage,version):
	bgw = "http://www.biblegateway.com/passage/?search="
	book = passage[0]
	verseIni = str(passage[1]) + "%" + "3A" + str(passage[2])
	verseEnd = str(passage[3]) + "%" + "3A" + str(passage[4])
	url = bgw + book + verseIni + "-" + verseEnd + "&version=" + version
	page = requests.get(url)
	soup = BeautifulSoup(page.content)

	verse1 = soup.find_all('div',{"class": "passage-text"})

	verse = ""
	for item in verse1:
		verse2 = item.contents[0].find_all('span',{"class":  lambda x: x and x.startswith('text')})
		for item2 in verse2:
			verse = verse + "\n" + item2.text

	verse = verse.replace(u'\xa0', u' ')
	return(verse)


passage = ('Jude', 1, 2, 1, 2)
version = "KJV"

print(getVerses(passage,version))





#	url = "https://www.biblegateway.com/passage/?search=Jude1%3A2-1%3A2&version=NIV"
#	page = requests.get(url)
#	soup = BeautifulSoup(page.content)
#	verse1 = soup.find_all('div',{"class": "passage-text"})
#	verse = ""
#	for item in verse1:
#		verse2 = item.contents[0].find_all('span',{"class":  lambda x: x and x.startswith('text')})
#		for item2 in verse2:
#			verse = verse + "\n" + item2.text
#			verse = verse.replace(u'\xa0', u' ')
#	text_file = open("Output.txt", "w")
#	text_file.write(str(soup.prettify))
#	text_file.close()