# Glovo Nigeria Review Analysis

A data analysis of Glovo Nigeria's Google Play reviews, testing whether delivery speed
is actually the biggest driver of negative ratings.

## Finding

Delivery speed is not the main issue. Payment and refund complaints are both the most
frequently mentioned problem and the most damaging to rating — a bigger drop than
delivery time, order accuracy, or support.

| Category | Reviews mentioning (of 600) | Avg. rating when mentioned | Drop vs. baseline |
|---|---|---|---|
| Payment/Refund | 73 | 1.34★ | -2.47★ |
| Order Accuracy | 17 | 1.41★ | -2.16★ |
| Delivery Time | 30 | 1.50★ | -2.12★ |
| Support | 49 | 1.78★ | -1.89★ |

## Method

1. Pulled 600 recent Google Play reviews for Glovo Nigeria using `google-play-scraper`
2. Categorized reviews by keyword matching (payment/refund, order accuracy, delivery
   time, support)
3. Compared average rating for reviews mentioning each category against the baseline
   average for reviews that don't
4. Visualized the rating drop per category

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Files

- `scrape.py` — pulls and saves raw review data
- `glovo analysis.ipynb` — categorizes reviews by keyword, computes category-level stats
- `glovo_chart.py` — generates the final chart (`glovo_chart.png`)
- `glovo_reviews_raw.csv` — raw pulled review data

## Data source

Google Play reviews, Nigeria store, `com.glovo`. Public data, no authentication
required. Sample: 600 reviews, newest-first.
