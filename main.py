from bs4 import BeautifulSoup
import requests

# Get html file and make a soup
response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
soup = BeautifulSoup(response.text)

# Get hrefs
titles = soup.select(selector=".athing .title .titleline a")
links = [title.get("href").split("from")[0] for title in titles if title.get("href").split("from")[0] != ""]

# Get votes
votes = [int(upvote.getText().split(" ")[0]) for upvote in soup.select(selector=".subtext .subline .score")]

# Find most popular
most_popular = links[votes.index(max(votes))]
