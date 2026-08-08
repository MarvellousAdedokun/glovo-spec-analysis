#lets better understand it - copy and pasted from documentation
from google_play_scraper import app
result1 = app(
    'com.glovo',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)


#This only prints meta data, info about the app, lets try geting the reviews part

from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'com.glovo',
    lang='en', 
    country='ng',
    sort=Sort.NEWEST,
    count=3, 
    filter_score_with=5
)
print(result)

