import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from wordcloud import WordCloud


subs = ['circlejerk', 'FloridaMan', 'gaming', 'movies',
			'science', 'Seahawks', 'totallynotrobots', 
			'uwotm8', 'videos', 'worldnews']

for sub in subs:
	text = open('text_files/%s.txt' % sub).read()
	reddit_mask = np.array(Image.open('reddit_mask.jpg'))
	wc = WordCloud(background_color="black", mask=reddit_mask)
	wc.generate(text)
	wc.to_file('wordclouds/%s.jpg' % sub)

