import os
from datetime import datetime

template = os.getcwd()+"/articles/template.txt" 


def main(img_src, title, date_time, date, content):
	split_content = content.split("\n")
	content = ""
	for s in split_content:
		paragraph = "<p>"+s+"</p>"
		content+=paragraph

	with open(template) as file:
		source = file.read()
		final = source.format(img_src, title, date_time, date, content)

	split_title = title.lower().split(" ")
	title = ""
	for s in split_title:
		title+=s+"_"
	
	dest = open(title[:-1]+".html", "w")
	dest.write(final)
	dest.close()


main("../img/article_img/test.png", "very cool title", datetime.now().strftime("%m-%d-%Y %H:%M:%S"), "1 prill 2022", "i love shqip\nalbania is great\nyou are awesome")