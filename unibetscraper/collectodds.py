from scraper import UnibetScraper
import os

track = "Lingfield"
races_to_scrape = [1, 8] # a list provided as [start_race, until_race]
await_odds = False
send_mail = False
excel = False
recipients = ["example_1@gmail.com", "example_2@gmail.com"] # add recipients

############################################
############################################
############################################
############################################

# RUN THE PROGRAM

############################################
############################################
############################################
############################################

u = UnibetScraper(track = track, countrycode = "GBR")

"""
AWAIT NEW ODDS
"""
if await_odds:
    s = u.awaitnewodds(races = races_to_scrape, delta = 5)

"""
SCRAPE THE DATA
"""
scraped_races = u.scrape_wp(races = races_to_scrape)
scraped_h2h = u.scrape_h2h(races = races_to_scrape)

"""
PRINT THE RESULT IN THE CONSOLE
"""
for race in scraped_races:
    print(race)
    print()

for h2h in scraped_h2h:
    print(h2h)
    print()

"""
WRITE TO EXCEL
"""
if excel:
    u.to_excel(pd_list = scraped_races, pd_list_name = "scraped_races",
        file_path = os.path.expanduser("~/Desktop/unibetodds.xlsx"), sheet_name = "Unibet - W&P")
    u.to_excel(pd_list = scraped_h2h, pd_list_name = "scraped_h2h",
        file_path = os.path.expanduser("~/Desktop/unibetodds.xlsx"), sheet_name = "Unibet - H2H")

"""
SEND MAIL
"""
if send_mail:
    u.send_mail(recipients=recipients, result=scraped_races)
