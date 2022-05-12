from github import Github
import requests
from bs4 import BeautifulSoup
import json 


def main():
	articles_dict = {}

	token = "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"
	g = Github(token)
	acc = g.get_user().get_repo("shqipanon.github.io")
	files = acc.get_contents("/articles")
	for file in files:
		url = "https://raw.githubusercontent.com/shqipanon/shqipanon.github.io/main/articles/"+file.name
		content = requests.get(
			url,
			headers={
				'accept': 'application/vnd.github.v3.raw',
				'authorization': 'token {}'.format(token)
	            }
	    	)
		soup = BeautifulSoup(content.text, "lxml")
		time = soup.find("time")["datetime"]

		articles_dict[file.name] = time

	json_object = json.dumps(articles_dict)

	return json_object