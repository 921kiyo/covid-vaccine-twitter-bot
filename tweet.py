# -*- coding: utf-8 -*-
import tweepy
from scrape import extract_total_num

access_token = "1378443057620729859-q0hwpZdfDtdCwQP3PSaGNKEuyIhab0"
access_token_secret = "trrEROXZUaBkwkc8VfxPR4OnYGtRsqL8u9Y82iNgsUOS6"

consumer_key = "eBiOzvAcDcz9vWqIO9IxBk94G"
consumer_secret = "Giz20R0HhtF8WxnNANYzH813Og1dcuf47uaCPBUH2twCnqQUWg"
# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

(
    people_vaccinated,
    people_vaccinated_trend,
    people_fully_vaccinated,
    people_fully_vaccinated_trend,
    collect_date,
) = extract_total_num()


def get_progress_bar(num_vaccinated):
    """
    Source: https://www.stat.go.jp/data/jinsui/new.html
    - 15-64: 74492000
    - over 65: 36191000
    - total: 110683000
    """
    total_population = 110683000
    ratio = num_vaccinated / total_population * 100
    total_bar = 20
    num_done = int(ratio / 5)
    return "▓" * num_done + "░" * (total_bar - num_done), ratio


bar, ratio = get_progress_bar(people_vaccinated)

tweet = bar
tweet += f" {round(ratio, 1)}% "
tweet += f"(1回目接種回数, vaccinated {people_vaccinated}名, +{people_vaccinated_trend})\n"

bar_full, ratio_full = get_progress_bar(people_fully_vaccinated)
tweet += bar_full
tweet += f" {round(ratio_full, 1)}% "
tweet += f"(2回目接種回数, fully vaccinated {people_fully_vaccinated}名, +{people_fully_vaccinated_trend})\n"
tweet += "#新型コロナワクチン #CovidVaccines #covidjapan "
tweet += f"{collect_date} "
print(tweet)
# Create a tweet
# api.update_status(tweet)
