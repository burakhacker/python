import requests

def get_address_info(address):
    api_key = 'jouw_api_sleutel'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    if 'results' in data and len(data['results']) > 0:
        result = data['results'][0]
        return result
    else:
        return None

# Voorbeeld: Adres om informatie op te halen
adres = 'Isaac Huberstraat 92, 3034CT Rotterdam'

# Informatie ophalen via het adres
adres_informatie = get_address_info(adres)
if adres_informatie:
    print("Informatie gevonden:")
    print(adres_informatie)
else:
    print("Geen informatie gevonden voor dit adres.")
