"""
version
@author varlamov.a
@email warlamovav@yandex.ru
@date 22.05.2023
@time 12:51
"""

import configparser

config = configparser.ConfigParser()
config.read('./settings.ini')

chromedriver_path = config['EXEC_PATH']['chrome_driver_path']
port = int(config['NETWORK']['port'])

