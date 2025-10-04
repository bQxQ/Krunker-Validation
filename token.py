import requests

p = requests.get('https://token-api67.vercel.app/generate-token') #free token gen
print(p.json())
