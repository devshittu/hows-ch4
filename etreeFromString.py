from lxml import html
import requests
response = requests.get('http://httpbin.org/forms/post')
print(type(response.text))
