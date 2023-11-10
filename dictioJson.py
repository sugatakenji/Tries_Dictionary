import json


if __name__ == "__main__":
    jsonfile = open("b.json","r")
    dictionary = json.load(jsonfile)
    print(dictionary["b"]["a"]["n"]["a"]["n"]["a"]["meaning"])