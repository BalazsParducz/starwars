import requests
response = requests.get('https://swapi.co/api/planets').json()

def all_planets():
    return response['results']
