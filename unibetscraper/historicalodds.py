from scraper import UnibetScraper

track = "Lingfield"
race = 1
horse = "Royal Athena"

u = UnibetScraper(track)
hist_odds = u.get_historical_odds(race, horse)
u.plot_historical_odds(hist_odds, horse)