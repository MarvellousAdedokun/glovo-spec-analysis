#lets better understand it - copy and pasted from documentation
from google_play_scraper import app
result = app(
    'com.glovo',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

print(result)

