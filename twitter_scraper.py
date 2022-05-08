import datetime
import os
# import twint
import pathlib


DATE_START = str(datetime.datetime.today().date() - datetime.timedelta(days=1))
DATA_PATH = pathlib.Path("data/")
DATA_PATH.mkdir(parents=True, exist_ok=True)
# MAX_RESULT = 100
# DATE_END = '2020-05-08'
HASHTAG = 'depression'
JSON_FILENAME = DATA_PATH / str(datetime.datetime.today().date())

def sns_scrape():
    os.system(f'snscrape --jsonl --progress --since {DATE_START} twitter-hashtag "{HASHTAG}" > {JSON_FILENAME}.json')

    # with end date
    # os.system(f'snscrape --jsonl --progress --since {DATE_START} twitter-hashtag "{HASHTAG} until:{DATE_END}" > {JSON_FILENAME}.json')

def scrape_twint():
    c = twint.Config()
    # c.Until = str(datetime.datetime.today().date() + datetime.timedelta(days=1))
    c.Since = str(datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1))
    # c.Username = "test"
    c.Search = "#depression"
    c.Location=True
    c.Images = True
    # c.Limit = 50
    # c.Custom["user"] = ["id", "tweet", "user_id", "username", "hashtags", "mentions"]
    c.User_full = True
    c.Store_csv = True
    c.Output = "test3.csv"
    c.Debug = True
    twint.run.Search(c)



if __name__ == "__main__":
    # scrape_twint()
    sns_scrape()


# reference
# https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af
# https://github.com/hansheng0512/tweets-scrapping-using-python
# https://github.community/t/can-github-actions-directly-edit-files-in-a-repository/17884/7
