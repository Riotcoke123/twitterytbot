<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Twitter YouTube Bot</title>
</head>
<body>
    <h1>Twitter YouTube Bot</h1>
    <p>
        This Python bot monitors specified YouTube channels and tweets when the channels go live.
        The bot uses Twitter's API v2 and YouTube's Data API v3 to track the live status of YouTube channels
        and posts updates on Twitter accordingly.
    </p>
    <h2>Features</h2>
    <ul>
        <li>Monitor multiple YouTube channels for live streaming.</li>
        <li>Tweet updates to a specified Twitter account when a channel goes live.</li>
        <li>Rate-limited to a maximum number of tweets per day to avoid exceeding API limits.</li>
    </ul>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3.6+</li>
        <li><code>tweepy</code> (Twitter API library)</li>
        <li><code>google-api-python-client</code> (YouTube API library)</li>
    </ul>
    <h2>Setup Instructions</h2>
    <ol>
        <li>
            Clone this repository:
            <pre><code>git clone https://github.com/Riotcoke123/twitterytbot.git</code></pre>
        </li>
        <li>
            Install the required packages:
            <pre><code>pip install tweepy google-api-python-client</code></pre>
        </li>
        <li>
            Create a Twitter Developer account and generate the API credentials:
            <ul>
                <li>API Key</li>
                <li>API Key Secret</li>
                <li>Bearer Token</li>
                <li>Access Token</li>
                <li>Access Token Secret</li>
            </ul>
        </li>
        <li>
            Get a YouTube Data API v3 key by creating a project in the Google Cloud Console and enabling the YouTube Data API.
        </li>
        <li>
            Update the <code>API_KEY</code>, <code>API_KEY_SECRET</code>, <code>BEARER_TOKEN</code>, <code>ACCESS_TOKEN</code>, 
            <code>ACCESS_TOKEN_SECRET</code>, and <code>YOUTUBE_API_KEY</code> variables with your credentials in the script.
        </li>
        <li>
            Specify the YouTube channel IDs you want to monitor in the <code>CHANNEL_IDS</code> list.
        </li>
        <li>
            Run the bot:
            <pre><code>python bot.py</code></pre>
        </li>
    </ol>
    <h2>Configuration</h2>
    <p>
        The following configuration options are available within the script:
    </p>
    <ul>
        <li><code>CHANNEL_IDS</code>: A list of YouTube Channel IDs to monitor.</li>
        <li><code>MAX_TWEETS_PER_DAY</code>: The maximum number of tweets allowed per day (default: 50).</li>
        <li>Check frequency: The bot checks YouTube channels every minute by default, this can be adjusted using the <code>time.sleep()</code> function in the script.</li>
    </ul>
    <h2>Usage</h2>
    <p>
        The bot continuously monitors the specified YouTube channels for live streams. When a channel goes live, the bot tweets the update with a link to the YouTube channel.
        The tweet count resets after 24 hours to comply with the Twitter API limits.
    </p>
    <h2>Limitations</h2>
    <ul>
        <li>The bot can only post up to the maximum number of tweets specified in <code>MAX_TWEETS_PER_DAY</code> per day.</li>
        <li>YouTube API quotas may limit the number of requests the bot can make daily.</li>
    </ul>
    <h2>Contributing</h2>
    <p>
        Contributions are welcome! Feel free to submit a pull request or open an issue to improve this project.
    </p>
    <h2>License</h2>
    <p>
        This project is licensed under the GNU General Public License v3.0. See the <a href="LICENSE">LICENSE</a> file for more information.
    </p>

</body>
</html>
