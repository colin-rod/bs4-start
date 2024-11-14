from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_page = response.text

soup = BeautifulSoup(yc_page,"html.parser")
#print(soup.title)
article_text=[]
article_links=[]
article_votes=[]

link_tags = soup.find_all(class_="titleline")
for link_tag in link_tags:
    article_link = link_tag.find("a")
    text = article_link.getText()
    article_text.append(text)
    link = article_link.get("href")
    article_links.append(link)

article_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]


print(article_text)
print(article_links)
print(article_votes)

max_score_index = article_votes.index(max(article_votes))
print(article_text[max_score_index])
print(article_links[max_score_index])
print(article_votes[max_score_index])