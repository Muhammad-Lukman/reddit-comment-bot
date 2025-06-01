# pip install praw --q

# import libraries

import praw
import config
import time

def reddit_login():
    print("Logging in...")
    try:
        r = praw.Reddit(
            client_id=config.client_id,
            client_secret=config.client_secret,
            username=config.username,
            password=config.password,
            user_agent=f"script:redit_bot:v1.0 (by /u/{config.username})"
        )
        # Verify login
        print(f"Logged in as: {r.user.me()}")
        return r
    except Exception as e:
        print(f"Login error: {str(e)}")
        raise

def run_bot(r):
    print("Bot started. Monitoring /r/test...")
    while True:
        try:
            for comment in r.subreddit("test").stream.comments(skip_existing=True):
                body = comment.body.lower()
                
                if "hello" in body:
                    print(f"Replying to {comment.id}")
                    comment.reply("Hi there! [Example](https://www.youtube.com/)")
                    
                time.sleep(10)  # Avoid rate limits
                
        except Exception as e:
            print(f"Error: {e}. Retrying in 60s...")
            time.sleep(60)

if __name__ == "__main__":
    while True:
        try:
            r = reddit_login()
            run_bot(r)
        except KeyboardInterrupt:
            print("Bot stopped by user")
            break
        except Exception as e:
            print(f"Fatal error: {e}. Restarting in 60s...")
            time.sleep(60)
