# # # # # # from xgoogle.search import GoogleSearch
# # # # # # gs = GoogleSearch("quick")
# # # # # # gs.results_per_page = 50
# # # # # # results = gs.get_results()
# # # # # # print gs

# # # # # from google import google
# # # # # num_page = 3
# # # # # search_results = google.search("define probable", 1)
# # # # # for result in search_results:
# # # # #     print(result.description)

# # # # import webbrowser
# # # # chrome = webbrowser.get('google-chrome') # or webbrowser.get('chrome')
# # # # chrome.open_new_tab('chrome://newtab')
# # # import webbrowser

# # # url = 'http://docs.python.org/'

# # # # MacOS
# # # chrome_path = 'gksu -u nihal google-chrome %s'

# # # # Windows
# # # # chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

# # # # Linux
# # # # chrome_path = '/usr/bin/google-chrome %s'

# # # webbrowser.get(chrome_path).open(url)
# # import json
# # from PyDictionary import PyDictionary
# # dictionary=PyDictionary()

# # n = dictionary.meaning("indentation")
# # print "--------------------------------------"

# # print(json.dumps(n, indent=2))
# # print "--------------------------------------"
# # if n['Noun']:
# # 	print n['Noun']
# # if 'Verb' in n:
# # 	print n['Verb']
# # print len(n['Noun'])

# from weather import Weather
# weather = Weather()

# # Lookup WOEID via http://weather.yahoo.com.

# lookup = weather.lookup(560743)
# condition = lookup.condition()
# print(condition['text'])

# # Lookup via location name.

# location = weather.lookup_by_location('chicago')
# condition = location.condition()
# print(condition['text'])

# # Get weather forecasts for the upcoming days.

# forecasts = location.forecast()
# for forecast in forecasts:
#     print(forecasts.text())
#     print(forecasts.date())
#     print(forecasts.high())
#     print(forecasts.low())
from weather import Weather
weather = Weather()

# Lookup WOEID via http://weather.yahoo.com.

lookup = weather.lookup(560743)
condition = lookup.condition()
print condition['text']

# Lookup via location name.

location = weather.lookup_by_location('dublin')
condition = location.condition()
print condition['text']