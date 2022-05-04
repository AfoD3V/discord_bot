from bs4 import BeautifulSoup
from requests import get


def server_status():
    url = 'https://www.playlostark.com/en-us/support/server-status'

    page = get(url)
    bs = BeautifulSoup(page.content, 'html.parser')

    status = {}

    for server in bs.find_all('div', class_='ags-ServerStatus-content-responses-response-server'):
        good = server.find('div',
                           class_='ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--good')
        busy = server.find('div',
                           class_='ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--busy')
        if good:
            status.update({f'{server.get_text().strip()}': 'Good'})
        elif busy:
            status.update({f'{server.get_text().strip()}': 'Busy'})

    procyon = str(status['Procyon'])
    if procyon == 'Good':
      return f'Procyon:  :white_check_mark:'
    else:
      return 'May be down'