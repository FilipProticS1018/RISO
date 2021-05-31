import http.client
import json
import sys

conn = http.client.HTTPSConnection("getpantry.cloud")

class kontakt: 
    adresa = "Knez Mihajlova 6",
    mesto = "Beograd",
    telefon = "555 333"

kontakt = kontakt()

id = "Fica11"
if len(id) != 6:
    print("ID mora biti duzine 6 karaktera")
    sys.exit()
ime = "Filip"
prezime = "Protic"
smer = "Informacione tehnologije"
predmeti = ["Microsoft tehnologije za pristup podacima", "C# programiranje", "SQL programiranje"]
prosek = round(8.90, 2)
if prosek < 6.00 or prosek > 10.00:
    print("Prosek mora biti izmedju 6 i 10")
    sys.exit()

payload = json.dumps({
    "id":id,
    "ime":ime,
    "prezime":prezime,
    "smer":smer,
    "predmeti":predmeti,
    "prosek":prosek,
    "kontakt":[kontakt.adresa, kontakt.mesto, kontakt.telefon]

})

headers = {
    'Content-Type':'application/json'
}

conn.request("POST", "/apiv1/pantry/0ac9cb62-a8fb-48f4-8617-fcad9e1d49ca/basket/Prota", payload, headers)
result = conn.getresponse()
data = result.read()
print(data.decode("UTF-8"))
