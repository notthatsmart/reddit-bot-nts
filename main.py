import praw
import time
from keep_alive import keep_alive
reddit = praw.Reddit(client_id="xx1xbGxR1hbDCe1NoXjxQQ",
                     client_secret="b6w50lVs3-v87ywTToOWl8C2Ogxy7g",
                     user_agent="<console:amazingbot:1.0",
                     username="allbotsaregood",
                     password="Amazingbob9")
subreddit = reddit.subreddit("All")

keep_alive()
for comment in subreddit.stream.comments():
    if comment.author.name == reddit.user.me().name:
        continue
    if "1984" in comment.body.lower():
        print(f"https://reddit.com{comment.permalink}")
        comment.reply('By george orwell 1949')
        comment.upvote()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
