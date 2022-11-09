import phonenumbers
from test import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, 'en')


from opencage.geocoder import OpenCageGeocode

key = 'a3876c9e6f884abf92fb21d6d401d50d'

geocoder = OpenCageGeocode(key)
query =str(location)
results = geocoder.geocode(query)
print(results)