import requests
from bs4 import BeautifulSoup as bs

resp = requests.get('https://python.org/events/') # get target web-page
soup = bs(resp.text, 'lxml') # converting to soup for easily navigation in tags
events = [] # init events_list
events_names = soup.find_all('h3', class_='event-title') # get events names
events_dates = soup.find_all('time') # get events dates, e.g. days and month
events_years = soup.find_all('span', class_='say-no-more') # get events years
events_location = soup.find_all('span', class_='event-location') # get events location

for x in range(len(events_names)):
	# todo rewrite to formatted string or create iterator
	s = events_names[x].text + ' ' + events_dates[x].text + ' ' + events_years[x].text + ' ' + events_location[x].text # generate final view of data
	events.append(s)
	
for c in events:
	print(c)

