# # # from google import google
# # # num_page = 3
# # # search_results = google.search("define probable", 1)
# # # for result in search_results:
# # #     print(result.description)


# # from pprint import pprint
# # import requests
# # r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=530d603cdf40e5478531d1f027fb13b4')
# # pprint(r.json())
# # {u'base': u'cmc stations',
# #  u'clouds': {u'all': 68},
# #  u'cod': 200,
# #  u'coord': {u'lat': 51.50853, u'lon': -0.12574},
# #  u'dt': 1383907026,
# #  u'id': 2643743,
# #  u'main': {u'grnd_level': 1007.77,
# #            u'humidity': 97,
# #            u'pressure': 1007.77,
# #            u'sea_level': 1017.97,
# #            u'temp': 282.241,
# #            u'temp_max': 282.241,
# #            u'temp_min': 282.241},
# #  u'name': u'London',
# #  u'sys': {u'country': u'GB', u'sunrise': 1383894458, u'sunset': 1383927657},
# #  u'weather': [{u'description': u'broken clouds',
# #                u'icon': u'04d',
# #                u'id': 803,
# #                u'main': u'Clouds'}],
# #  u'wind': {u'deg': 158.5, u'speed': 2.36}}
# from time import ctime
# a = (ctime())
# print int(a[11:13]) > 2
# # import datetime
# # a =  datetime.datetime.now().time()
# # print a[0]

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'JASS'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


if __name__ == '__main__':
    main()
