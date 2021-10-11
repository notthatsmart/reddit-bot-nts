import praw
import time
from keep_alive import keep_alive
reddit = praw.Reddit(client_id="NGbw1N6Q354uiLxF6Xtn3w",
                     client_secret="8nSWsQCK6dgdogx9AQFHjpFOYZQOa",
                     user_agent="<console:amazingbot:2.0",
                     username="notthebottest",
                     password="Amazingbob9")
subreddit = reddit.subreddit("kickopenthedoor")

keep_alive()

for comment in subreddit.stream.comments():
    if comment.author.name == reddit.user.me().name:
        continue
    if "weak" in comment.body.lower():
        print(f"https://reddit.com{comment.permalink}")
        #comment.reply('By george orwell 1949')
        comment.upvote()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
