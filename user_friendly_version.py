import praw
import config
import time
import datetime
import signal

class RedditBot:
    def __init__(self):
        self.running = True
        signal.signal(signal.SIGINT, self.graceful_shutdown)
        
    def graceful_shutdown(self, signum, frame):
        print("\nShutting down gracefully...")
        self.running = False

    def reddit_login(self):
        print(f"{self.current_time()} - Logging in...")
        try:
            reddit = praw.Reddit(
                client_id=config.client_id,
                client_secret=config.client_secret,
                username=config.username,
                password=config.password,
                user_agent=f"script:RedditReplyBot:v1.0 (by /u/{config.username})"
            )
            # Verify authentication
            print(f"{self.current_time()} - Logged in as: {reddit.user.me()}")
            return reddit
        except Exception as e:
            print(f"{self.current_time()} - Login failed: {str(e)}")
            raise

    def current_time(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def run_bot(self, reddit):
        print(f"{self.current_time()} - Bot started. Monitoring /r/test...")
        print(f"{self.current_time()} - Test by commenting 'hello' or 'hi' in /r/test")
        
        while self.running:
            try:
                for comment in reddit.subreddit("test").stream.comments(skip_existing=True):
                    if not self.running:
                        break
                        
                    comment_text = comment.body.lower()
                    author = comment.author.name if comment.author else "[deleted]"
                    
                    print(f"{self.current_time()} - New comment from u/{author}: {comment.body[:50]}...")
                    
                    if "hello" in comment_text:
                        self.reply_to_comment(comment, "Hi there! How can I help you today?")
                    elif "hi" in comment_text:
                        self.reply_to_comment(comment, "Hello! Nice to see you here!")
                        
                    time.sleep(10)  # Rate limiting
                    
            except Exception as e:
                print(f"{self.current_time()} - Error: {str(e)}")
                print(f"{self.current_time()} - Reconnecting in 60 seconds...")
                time.sleep(60)

    def reply_to_comment(self, comment, reply_text):
        try:
            print(f"{self.current_time()} - Replying to comment by u/{comment.author} (ID: {comment.id})")
            comment.reply(reply_text)
            print(f"{self.current_time()} - Reply sent! Link: https://reddit.com{comment.permalink}")
            print(f"{self.current_time()} - Waiting for new comments...")
        except Exception as e:
            print(f"{self.current_time()} - Failed to reply: {str(e)}")

if __name__ == "__main__":
    bot = RedditBot()
    try:
        reddit = bot.reddit_login()
        bot.run_bot(reddit)
    except Exception as e:
        print(f"{bot.current_time()} - Fatal error: {str(e)}")
        print(f"{bot.current_time()} - Bot stopped.")