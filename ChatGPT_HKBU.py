import configparser
import logging
import os
import requests


class HKBU_ChatGPT():
    def __init__(self, config_='./config.ini'):
        if type(config_) == str:
            self.config = configparser.ConfigParser()
            self.config.read(config_)
        elif type(config_) == configparser.ConfigParser:
            self.config = config_

    def submit(self, message):
        print(f'Submitting message:{message}')
        # conversation = [{"role": "user", "content": message}]
        url = (os.getenv("CHATGPT_BASICURL") + "/deployments/" +
               os.getenv('CHATGPT_MODELNAME') + "/chat/completions/?api-version=" +
               os.getenv('CHATGPT_APIVERSION'))
        headers = {'Content-Type': 'application/json', 'api-key': os.getenv('CHATGPT_TOKEN')}
        payload = {'messages': message}
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(f'Response:{data}')
            return data['choices'][0]['message']
        else:
            logging.error(f'Error:{response.status_code} {response.text}'
                          f'\nPlease check your API key and network connection')


if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()

    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)

