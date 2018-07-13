import requests
import json
from bs4 import BeautifulSoup
import pandas as pd


def dataframe_to_excel(df):
	"""
	Function to take generic dataframe and output to excel
	"""
	out_name = 'output.xlsx'
	writer = pd.ExcelWriter(out_name)
	df.to_excel(writer,'Sheet1')
	writer.save()
	print('Saving dataframe to %s' % out_name)

def get_latest_stats():
	url = "https://stats.golem.network/show"
	response = requests.get(url)
	node_soup = BeautifulSoup(response.text, 'html.parser')
	containers_strdict = node_soup.find('div',{'id':'modalMessage','data':True})['data']
	node_dicts = json.loads(containers_strdict)
	node_df = pd.DataFrame(node_dicts)
	return node_df

def main():
	'''
	Main method to retrieve and information from stats.golem.network
	'''
	node_df = get_latest_stats()
	dataframe_to_excel(node_df)
	print(list(node_df))
	
if __name__ == "__main__":
	main()