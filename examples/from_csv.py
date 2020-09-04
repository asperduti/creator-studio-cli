import csv
from selenium.webdriver.common.keys import Keys
from creator_studio.creator_studio import CreatorStudio




cs_cli = CreatorStudio("YOUR_EMAIL", "YOUR_PASSWORD")
cs_cli.login()

file_name = "calendario.csv"
with open(file_name, "r") as file:
    posts = csv.reader(file)
    for post in posts:
        cs_cli.create_post(account=post[0],
                           message=post[2],
                           file=post[1],
                           schedule_options={
                               "date": post[3],
                               "time": post[4]
                           },
                           social_network="instagram")

