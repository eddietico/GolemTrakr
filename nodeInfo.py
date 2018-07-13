import requests
import json
from bs4 import BeautifulSoup
import pandas as pd


def get_latest_stats():
	url = "https://stats.golem.network/show"
	response = requests.get(url)
	node_soup = BeautifulSoup(response.text, 'html.parser')
	containers_strdict = node_soup.find('div',{'id':'modalMessage','data':True})['data']
	node_dicts = json.loads(containers_strdict)
	return node_dicts

def main():
	'''
	Main method to retrieve and information from stats.golem.network
	'''
	node_dicts = get_latest_stats()
	print(node_dicts[0])
	
if __name__ == "__main__":
	main()