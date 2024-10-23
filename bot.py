import tweepy
import time
from googleapiclient.discovery import build

# Your Twitter API credentials
API_KEY = ''
API_KEY_SECRET = ''
BEARER_TOKEN = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Your YouTube API Key and Channel IDs
YOUTUBE_API_KEY = ''
CHANNEL_IDS = ['', '']

# Max number of requests allowed per day
MAX_TWEETS_PER_DAY = 50

# Create the client object (v2)
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Track the number of tweets sent
tweet_count = 0  # Change from 7 to 0 for actual tracking
start_time = time.time()

# Track live statuses of the channels
live_status = {channel_id: False for channel_id in CHANNEL_IDS}
channel_names = {}  # Dictionary to store channel names

# Function to reset the count after 24 hours
def reset_count():
    global tweet_count, start_time
    elapsed_time = time.time() - start_time
    if elapsed_time >= 24 * 60 * 60:  # 24 hours in seconds
        tweet_count = 0
        start_time = time.time()

# Function to tweet a status update, with rate limiting
def tweet(message):
    global tweet_count
    reset_count()
    if tweet_count < MAX_TWEETS_PER_DAY:
        try:
            client.create_tweet(text=message)  # This uses API v2
            tweet_count += 1
            print(f"Tweeted successfully! ({tweet_count}/{MAX_TWEETS_PER_DAY} tweets used)")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Tweet limit reached. Please wait until the 24-hour limit resets.")

# Function to get the current tweet count
def get_tweet_count():
    return tweet_count

# Function to get channel name by ID
def get_channel_name(channel_id):
    try:
        request = youtube.channels().list(
            part='snippet',
            id=channel_id
        )
        response = request.execute()
        if response['items']:
            return response['items'][0]['snippet']['title']
        else:
            print(f"Channel ID {channel_id} not found.")
            return None
    except Exception as e:
        print(f"Error getting channel name: {e}")
        return None

# Function to check if a YouTube channel is live
def is_channel_live(channel_id):
    try:
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            type='video',
            eventType='live'
        )
        response = request.execute()

        # If the items list is not empty, the channel is live
        return len(response['items']) > 0
    except Exception as e:
        print(f"Error checking YouTube live status: {e}")
        return False

# Main function to monitor YouTube live status and tweet
def monitor_youtube():
    for channel_id in CHANNEL_IDS:
        is_live = is_channel_live(channel_id)

        if is_live and not live_status[channel_id]:
            # The channel just went live
            channel_name = get_channel_name(channel_id)
            if channel_name:
                # Updated tweet format with the live link
                tweet(f"🎥 {channel_name} is now LIVE on YouTube! Check it out: https://www.youtube.com/channel/{channel_id}/")
                live_status[channel_id] = True
        elif not is_live:
            # The channel is offline
            live_status[channel_id] = False

if __name__ == "__main__":
    # Pre-fetch channel names
    for channel_id in CHANNEL_IDS:
        channel_names[channel_id] = get_channel_name(channel_id)

    # Continuously check the YouTube live status
    while True:
        monitor_youtube()
        # Optionally print the current tweet count every 10 iterations
        if tweet_count % 10 == 0:  # or any interval you prefer
            print(f"Current tweet count: {get_tweet_count()}")
        # Wait for 1 minute before checking again
        time.sleep(60)
