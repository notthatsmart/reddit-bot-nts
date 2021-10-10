import praw
import time
reddit = praw.Reddit(client_id="xx1xbGxR1hbDCe1NoXjxQQ",
                     client_secret="b6w50lVs3-v87ywTToOWl8C2Ogxy7g",
                     user_agent="<console:amazingbot:1.0",
                     username="allbotsaregood",
                     password="Amazingbob9")
subreddit = reddit.subreddit("memes")

for comment in subreddit.stream.comments():
    if comment.author.name == reddit.user.me().name:
        continue
    if "!attack" in comment.body.lower():
        print(f"https://reddit.com{comment.permalink}")
        comment.reply('bad human')
        comment.upvote()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
