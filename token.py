import requests


# If you want free access to the api dm @cleanest on discord
p = requests.get('https://token-api67.vercel.app/generate-token') 
print(p.json())
