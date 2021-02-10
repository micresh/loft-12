import requests
from bs4 import BeautifulSoup as bs

resp = requests.get('https://python.org/events/')
soup = bs(resp.text, 'lxml')
events = []
events_names = soup.find_all('h3', class_='event-title')
events_dates = soup.find_all('time')
events_years = soup.find_all('span', class_='say-no-more')
events_location = soup.find_all('span', class_='event-location')

for x in range(len(events_names)):
	# todo rewrite to formatted string or create iterator
	s = events_names[x].text + ' ' + events_dates[x].text + ' ' + events_years[x].text + ' ' + events_location[x].text 
	events.append(s)
	
for c in events:
	print(c)

