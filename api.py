import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ['SEARCH']
api_url = "https://customsearch.googleapis.com/customsearch/v1?key=" + api_key + "&cx=" + engine_id + "&q=site:stackoverflow.com/questions/tagged/cobol"

response = requests.get(api_url)

print(response.json())

search = res_dict["searchInformation"]