import configparser

import requests

conf = configparser.ConfigParser()
conf.read('config.ini')

ACCESS_TOKEN = conf['linenotify']['access_token']


def pprint(message):
    s = ''
    if isinstance(message, dict):
        for k, v in message.items():
            s += f'{k}:{v}\n'
        message = s
    return '\n' + message


def send_message_to_line(message):
    access_token = ACCESS_TOKEN
    header = {
        'Authorization': f'Bearer {access_token}'
    }
    data = {'message': pprint(message)}
    requests.post('https://notify-api.line.me/api/notify',
                  headers=header, data=data)


if __name__ == '__main__':
    send_message_to_line({'amount': 0.05, 'rate': 620})
