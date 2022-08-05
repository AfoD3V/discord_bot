from bs4 import BeautifulSoup
from requests import get


def status_check():
    url = 'https://www.playlostark.com/en-us/support/server-status'

    page = get(url)
    bs = BeautifulSoup(page.content, 'html.parser')

    status = {}

    for server in bs.find_all('div', class_='ags-ServerStatus-content-responses-response-server'):

        good = server.find('div',
                           class_='ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--good')
        busy = server.find('div',
                           class_='ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--busy')
        full = server.find('div',
                           class_='ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--full')
        maintenance = server.find('div',
                                  class_='ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--maintenance')

        if good:
            status.update({f'{server.get_text().strip()}': 'Good'})
        elif busy:
            status.update({f'{server.get_text().strip()}': 'Busy'})
        elif full:
            status.update({f'{server.get_text().strip()}': 'Full'})
        elif maintenance:
            status.update({f'{server.get_text().strip()}': 'Maintenance'})

    return status


if __name__ == '__main__':
    status_check()
