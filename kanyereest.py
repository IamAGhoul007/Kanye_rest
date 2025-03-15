import tweepy
import requests
import time

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHzJzwEAAAAASIedkSDOkQQGYREjTExXinz3K1E%3DdYXmbkZlOWdbt1yzR3Gx2GGsxZRUMu9ro9oK0BPjanWPczsjms"
CONSUMER_KEY = "EkkITG0572Pr0lsW5qzXFPF87"
CONSUMER_SECRET = "ZWlgYxdfD5SlBMBkbeluLlh0viQT1lIusdJsuonTEBfSlQpcIL"
ACCESS_TOKEN = "1425294546359906311-Zn8shUFxRC6rcqobhwPQ0uKahetQ7I"
ACCESS_TOKEN_SECRET = "Pbpw4SVjMH5KQXMLQUhiCxs4pfMp9jm2wGGcACSA06MFc"


client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def get_kanye_quote():
    response = requests.get("https://api.kanye.rest").json()
    return response.get("quote", "No quote found")

def tweet_kanye_quote():
    """Fetches a quote and posts it to Twitter."""
    quote = get_kanye_quote()
    try:
        client.create_tweet(text=quote) 
        print(f"Tweeted: {quote}")
    except tweepy.TweepyException as e:
        print(f"Error tweeting: {e}")

if __name__ == "__main__":
    while True:
        tweet_kanye_quote()
        time.sleep(3600) 
