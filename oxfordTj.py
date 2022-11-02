import requests

app_id = "a85cce0e"
app_key = "b231da37670ac66f15336bac38c9e472"
language = 'en-gb'


def getDefinition(word_id):
    url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + '/' + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"👉{sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output


if __name__ == "__main__":
    from pprint import pprint as print
    print(getDefinition('Great Britain'))
    print(getDefinition('amdwdwwdwdwd'))
