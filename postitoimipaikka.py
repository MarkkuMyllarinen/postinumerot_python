import json

with open("postcode_map_light.json", "r") as read_file:
    postinumerolista = json.load(read_file)
    postinumero = input("Kirjoita postinumero: ")
    print(postinumerolista[postinumero])