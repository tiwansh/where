import pandas as pd

from DBTables.GDPTable import HistoricalGDP
from sqlalchemy_globals import postgres_session

df = pd.read_csv("csv_data/gdp_historical.csv")

years = sorted([int(column) for column in df.columns if column != "Region"])

for index, row in df.iterrows():
    print(f"Starting row : {row['Region']}")
    if row['Region'] == "World Total":
        continue
    for year in years:
        historical_gdp_object = HistoricalGDP(region = row['Region'], year = year, gdp = row[str(year)],
                                              percent = (float)(row[str(year)]) / (float)(df.iloc[-1][str(year)]))
        postgres_session.add(historical_gdp_object)
        postgres_session.commit()
