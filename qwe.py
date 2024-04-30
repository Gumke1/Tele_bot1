import requests

search_query = 'Черчилль,_Уинстон'
response = requests.get(f"https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&explaintext&titles={search_query}")
a = response.json()
print(a)
page_id = list(a['query']['pages'].keys())[0]
extract = a['query']['pages'][page_id]['extract']
print(extract)