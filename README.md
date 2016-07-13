# Daniel Donohue: Webscraping Project

My third project here at NYCDS was to write a webscraping script in Python.  I used the scrapy library to scrape post titles, number of votes, dates, links, and top comments for a selection of subreddits on reddit.com.  The pipeline.py file then dictates that these data be saved to a MongoDB database.  I wrote the titles and top comments to txt files, and then used the Python module <a href="https://github.com/amueller/word_cloud">wordcloud</a> (thanks Andreas!) to generate word clouds for each subreddit.  
