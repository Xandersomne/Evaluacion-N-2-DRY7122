import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "p8jdTickB2dPJ8QPittm8Uz4lm5kEmxv"
while True:
    print("Si desea cerrar el programa, escriba q y enter")
    orig = input("Indique el origen: ")
    if orig == "q":
        break
    dest = input("Indique el destino: ")
    if dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest,"unit":"k", "locale": "es_ES"})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")

        print("=============================================")
        print("Indicaciones desde: " + (orig) + " hacia " + (dest))
        print("Tiempo de viaje:   " + (json_data["route"]["formattedTime"]))
        print("Distancia total:  " + str("{:.2f}".format(json_data["route"]["distance"])))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])) + " km)"))
        print("=============================================\n")
