import requests
from dotenv import load_dotenv
import os
import json

# id of search engine
engine_id = '2325fc50983544745'

#load api key for search engine
load_dotenv()
api_key = os.environ['SEARCH']

# searches site:stackoverflow.com/questions/tagged/cobol currently
api_url = "https://customsearch.googleapis.com/customsearch/v1?key=" + api_key + "&cx=" + engine_id + "&q=site:stackoverflow.com/questions/tagged/cobol"

# get the request in other words the results from the search
response = requests.get(api_url)

#print(response.json())

# store request in a dictionary - key value pairs structure
res_dict = response.json()

# search holds search information which has number of search results somewhere
search = res_dict["searchInformation"]

# prints the total results for search
# is intention at least must only get the number of search results
print(json.dumps(search["totalResults"], indent=4, sort_keys=True))