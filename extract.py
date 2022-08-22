import sys
import requests
x  = sys.argv[1]
#ophalen van
r = requests.get('https://jsonplaceholder.typicode.com/todos/'+ str(x))
text = r.json()
print(text['title'])
