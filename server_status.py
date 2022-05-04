from bs4 import BeautifulSoup
from requests import get


def status_check():
    url = 'https://www.playlostark.com/en-us/support/server-status'

    page = get(url)
    bs = BeautifulSoup(page.content, 'html.parser')

    status = {}

    for server in bs.find_all(
            'div',
            class_='ags-ServerStatus-content-responses-response-server'):
        good = server.find(
            'div',
            class_=
            'ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--good'
        )
        busy = server.find(
            'div',
            class_=
            'ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--busy'
        )
        if good:
            status.update({f'{server.get_text().strip()}': 'Good'})
        elif busy:
            status.update({f'{server.get_text().strip()}': 'Busy'})

    return status


if __name__ == '__main__':
    status_check()
