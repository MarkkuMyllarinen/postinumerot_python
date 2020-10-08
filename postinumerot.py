import json


def main():
    lista = postinumero_lista()
    postipaikka = input("Kirjoita postitoimipaikka: ").upper()
    try:
        print("Postinumerot:", ", ".join(lista[postipaikka]))
    except:
        print("Väärä input")


def postinumero_lista():
    with open("postcode_map_light.json", "r") as read_file:
        postinumerolista = json.load(read_file)
        inv_map = {}
        for k, v in postinumerolista.items():
            inv_map[v] = inv_map.get(v, []) + [k]
        return inv_map


def etsi_postinumerot(postitoimipaikka, postinumerot_sanakirja):
    try:
        lista = postinumerot_sanakirja[postitoimipaikka.upper()]
        return lista
    except KeyError:
        return []  # Palautetaan tyhjä lista jos sanakirjasta ei löydy kaupunkia vastaavia postinumeroita 
    

if __name__ == '__main__':
    main()
