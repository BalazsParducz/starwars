import requests

pages = ['https://swapi.co/api/planets/?page=1',
             'https://swapi.co/api/planets/?page=2',
             'https://swapi.co/api/planets/?page=3',
             'https://swapi.co/api/planets/?page=4',
             'https://swapi.co/api/planets/?page=5',
             'https://swapi.co/api/planets/?page=6',
             'https://swapi.co/api/planets/?page=7']


def all_planets(counter):

        response = requests.get(pages[counter]).json()
        return response['results']



# page1 = 'https://swapi.co/api/planets/?page=1'
# page2 = 'https://swapi.co/api/planets/?page=2'
# page3 = 'https://swapi.co/api/planets/?page=3'
# page4 = 'https://swapi.co/api/planets/?page=4'
# page5 = 'https://swapi.co/api/planets/?page=5'
# page6 = 'https://swapi.co/api/planets/?page=6'
# page7 = 'https://swapi.co/api/planets/?page=7'