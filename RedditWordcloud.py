import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json
import requests

class Reddit:

  def __init__(self, subreddit, limit):
    self.subreddit = subreddit
    self.limit = limit
    self.timeframe = 'month'
    self.listing = 'top'
    
  def get_reddit(self):
      try:
          base_url = f'https://www.reddit.com/r/{self.subreddit}/{self.listing}.json?limit={self.limit}&t={self.timeframe}'
          request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
      except:
          print('Um erro ocorreu!')
      return request.json()
  
  def get_post_titles(self, r):
      '''
      Pega os posts
      '''
      posts = []
      for post in r['data']['children']:
          x = post['data']['title']
          posts.append(x)
      return posts

  def wordcloud(self):
    r = self.get_reddit()
    posts = self.get_post_titles(r)

    # Nuvem de palavras
    wc = WordCloud(background_color="white", max_words=2000, contour_width=1)

    # inclui as palavras na nuvem
    tweets_texts = ' '.join(posts) # converte lista de textos em um único texto
    wc.generate(tweets_texts)

    # mostra a nuvem de palavras
    plt.figure(figsize = (10,10))
    plt.imshow(wc); 
    plt.axis("off");
