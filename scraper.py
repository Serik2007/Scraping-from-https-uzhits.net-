#import all libraries
import requests
from bs4 import BeautifulSoup
import lxml

i = 1
while i < 37: #37 is max page

	url = f'https://uzhits.net/xfsearch/Yulduz+Usmonova/page/{i}/'#main url

	response = requests.get(url=url).text #get
  
	bs = BeautifulSoup(response, 'lxml').find_all('a', class_='track-title nowrap') #All links
  
	for url in bs: 
  
		
    
		response2 = requests.get(url.get('href'))
    
		bs2 = BeautifulSoup(response2.text, 'lxml')
    
		name_mp3 = bs2.find('h1', class_='ftitle sect-title h1uchun').text #name of mp3 file
    
		mp3 = bs2.find('a', class_='fbtn fdl').get('href') #link for mp3 file
    
    print(name_mp3)
    
		r = requests.get(url = mp3) 
    
		with open(f'{name_mp3}.mp3', 'wb') as mp3_file:
			mp3_file.write(r.content)
      
	i+=1

