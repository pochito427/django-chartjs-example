import pandas as pd
from mysite.core.models import Country

# dataset from https://en.wikipedia.org/wiki/All-time_table_of_the_FIFA_World_Cup 

def csv_to_db():
    df = pd.read_csv('world_teams_appeared.csv') # use pandas to read the csv file
    records = df.to_records() # convert to records

    # loop through and create a country object using django
    for record in records:
        country = Country(
          name = record[1],
          code = record[2],
          appeared = record[3],
        )
        country.save()
