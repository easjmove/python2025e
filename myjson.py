import json
import morsecode

jsonString = "{\"funktion\":\"plus\", \"values\": [2,4]}"
print("JSON: " + jsonString)

pythonDictionary = json.loads(jsonString)
print("Dictionary: " + str(pythonDictionary))

print(pythonDictionary["funktion"])

print(morsecode.encrypt("test der".upper()))