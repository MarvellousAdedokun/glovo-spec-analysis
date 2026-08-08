from google_play_scraper import reviews, Sort
import pandas as pd

APP_ID = "com.glovo"
COUNTRY = "ng"          # Nigeria store
LANG = "en"
TARGET_COUNT = 500 

def pull_reviews():
    all_reviews = []
    continuation_token = None

    while len(all_reviews) < TARGET_COUNT:
        batch, continuation_token = reviews(
            APP_ID,
            lang=LANG,
            country=COUNTRY,
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token,
        )
        if not batch:
            break
        all_reviews.extend(batch)
        if continuation_token is None:
            break

    df = pd.DataFrame(all_reviews)
    # keep the columns that actually matter for analysis
    df = df[["reviewId", "userName", "score", "at", "content", "thumbsUpCount"]]
    df.columns = ["review_id", "user", "rating", "date", "text", "thumbs_up"]
    return df

if __name__ == "__main__":
    df = pull_reviews()
    print(f"Pulled {len(df)} reviews")
    print(df["rating"].value_counts().sort_index())
    df.to_csv("glovo_reviews_raw.csv", index=False)
    print("Saved to glovo_reviews_raw.csv")
