import praw
import time
from keep_alive import keep_alive
reddit = praw.Reddit(client_id="NGbw1N6Q354uiLxF6Xtn3w",
                     client_secret="8nSWsQCK6dgdogx9AQFHjpFOYZQOaw",
                     user_agent="<console:amazingbot:2.0",
                     username="notthebottest",
                     password="Amazingbob9")
subreddit = reddit.subreddit("memes")

keep_alive()
#
#for comment in subreddit.stream.comments():
#    if comment.author.name == reddit.user.me().name:
#        continue
#    if "1984" in comment.body.lower():
#        print(f"https://reddit.com{comment.permalink}")
#        comment.reply('1984 by george orwell 1949')
#        comment.upvote()

#for post in subreddit.new(limit=1):
#    print("*************")
#    print(post.title)

#    for comment in post.comments:
#        if hasattr(comment, "body"):
#            comment_lower = comment.body.lower()
#            if " weak " in comment_lower:
#                print("-------------")
#               print(comment.body)
#                time.sleep(60)

top = subreddit.top(limit = 5)
for submission in top:
    print(submission.title)