# Glovo Nigeria — Spec Analysis

Part of **Actually with Marvellous** — a weekly data analysis series that uses real,
published data to settle actual arguments people have (civic and business).

## What this is

A spec-work piece: a small, sharp analysis of a real Nigerian business using their
public-facing data (in this case, Google Play reviews), built to test a specific claim
people make about them.

**The claim being tested:** "Glovo is unreliable" — is the real problem delivery speed,
or is it something else (order accuracy, refunds/payment)?

## Status

🚧 In progress — built step by step as a learning project (Forge Method: exposure,
execution, feedback, refinement, repetition).

## Plan

- [ ] Pull real review data from Google Play (`com.glovo`, Nigeria store)
- [ ] Save raw data to CSV
- [ ] Categorize reviews by keyword (order accuracy / payment & refunds / delivery time / support)
- [ ] Count mentions + average rating per category
- [ ] One chart, one finding
- [ ] Build the episode caption + hook around the finding
- [ ] Post + tag/DM Glovo Nigeria

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Data source

Google Play reviews via the `google-play-scraper` Python package — public review data,
no auth required.

---
*More detail added as the project develops.*
