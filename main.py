# Request a project at https://ixdoge.com/request/

import requests, time
import sys
pastebin = 'https://pastebin.com/raw/WBbkF6hC'

username = input('Enter Your Username > ') # Doge
password = input('Enter Your Password > ') # 123

response = requests.get(pastebin).text

# Code below

def start():
  print('''
  [1]: Option 1
  [2]: Option 2
  [3]: Option 3
  ''')
  while True:
    input('Select: ')

#######################

for line in response.split('\n'):
  if username and password in line:
    print('Correct password and username')
    start()
print('Invalid password or username.')
sys.exit()
