import requests
from requests.exceptions import HTTPError

r = requests.get('https://api.github.com', auth=('user', 'pass'))

print (r.status_code)
print (r.headers['content-type'])

try:
    response = requests.get('https://api.github.com/users')

    # If the response was successful, no Exception will be raised
    print(response)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
else:
    print('Success!')