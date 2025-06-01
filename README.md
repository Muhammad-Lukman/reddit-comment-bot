# Reddit Reply Bot 🤖
A Python bot that monitors Reddit comments and automatically replies to specific triggers.

## Features
- Monitors comments in real-time using PRAW (Python Reddit API Wrapper)
- Replies to comments containing specific keywords ("hello", "hi")
- Graceful shutdown handling (Ctrl+C)
- Error handling and automatic reconnection
- Configurable through a separate config file

## Prerequisites
- Python 3.6+
- PRAW library (`pip install praw`)
- Reddit account with developer credentials

## Installation 
1. Clone this repository:
   ```bash
   git clone https://github.com/Muhammad-Lukman/reddit-comment-bot.git
   cd reddit-reply-bot
