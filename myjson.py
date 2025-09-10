import json

jsonString = "{\"funktion\":\"plus\", \"values\": [2,4]}"
print("JSON: " + jsonString)

pythonDictionary = json.loads(jsonString)
print("Dictionary: " + str(pythonDictionary))

print(pythonDictionary["funktion"])