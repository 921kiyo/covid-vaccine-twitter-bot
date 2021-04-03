import tweepy
from read_output import extract_total_num

access_token = "1378443057620729859-q0hwpZdfDtdCwQP3PSaGNKEuyIhab0"
access_token_secret = "trrEROXZUaBkwkc8VfxPR4OnYGtRsqL8u9Y82iNgsUOS6"

consumer_key = "eBiOzvAcDcz9vWqIO9IxBk94G"
consumer_secret = "Giz20R0HhtF8WxnNANYzH813Og1dcuf47uaCPBUH2twCnqQUWg"
# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

vaccinated_num = extract_total_num()
print("vaccinated_num ", vaccinated_num)

# source: https://www.stat.go.jp/data/jinsui/new.html
# 15-64: 74492000
# over 65: 36191000
# total: 110683000
total_population = 110683000

ratio = vaccinated_num / total_population * 100
total_bar = 20
num_done = int(ratio / 5)
tweet = "▓" * num_done
tweet += "░" * (total_bar - num_done)
tweet += f" {round(ratio, 1)}%"

# Create a tweet
api.update_status(tweet)
