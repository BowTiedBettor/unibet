from scraper import UnibetScraper
import matplotlib.pyplot as plt
from datetime import timedelta

track = "Lingfield"
race = 3

############################################
############################################
############################################
############################################

# RUN THE PROGRAM

############################################
############################################
############################################
############################################

u = UnibetScraper(track, countrycode="GBR")

raceobj = u.scrape_wp(races = [race, race])

horses = raceobj[0]['Horse']

num_horses = len(horses)

num_cols = min(num_horses, 3)
num_rows = (num_horses + num_cols - 1) // num_cols

# Create the subplots
fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))
fig.tight_layout(pad=3.0)

# Loop through each horse
for i, horse in enumerate(horses):
    # Get historical odds for the horse
    hist_odds = u.get_historical_odds(race, horse)

    # Determine the subplot position
    row = i // num_cols
    col = i % num_cols

    # Set the subplot for the current horse
    if num_rows == 1:
        ax = axes[col]
    else:
        ax = axes[row, col]

    timestamps = []
    prices = []
    for fluc in hist_odds: 
        timestamps.append((fluc['timestamp'] + timedelta()).strftime("%H:%M"))
        prices.append(fluc['price'])

    ax.plot(timestamps, prices)
    ax.set_title(f'{horse} - Historical Odds')
    ax.set_ylabel("Odds")
    ax.set_xlabel("Timestamp")

# Show the plot
fig.suptitle(f"{track} - Race {race}")
plt.show()

