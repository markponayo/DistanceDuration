# Interacting with Googlemaps API to find driving time and distance between cities
#User to dynamically input start and end of destination

import googlemaps
API = open ("Google Maps Platform API key.txt", "r")
APIKey = API.read()

Maps = googlemaps.Client(key = APIKey)

StartDestination = input ("Where will you start your drive?\n")
EndDestination = input ("Where will you end your drive?\n")

#Calculate distance using API 
Distance = Maps.directions(StartDestination, EndDestination)

KMDistance = (Distance[0]['legs'][0]['distance']['text'])
HrsMinsDuration = (Distance[0]['legs'][0]['duration']['text'])
print("Your drive will cover a total distance of "+ KMDistance+", taking the total time of "+ HrsMinsDuration+ ".")

