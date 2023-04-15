import pandas as pd

# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
INPUT_FILE = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
OUTPUT_FILE = "sq_color_count.csv"
KEY = "Primary Fur Color"
OUTPUT_COLOR_COLUMN = "Fur Color"
OUTPUT_COUNT_COLUMN = "Count"

df = pd.read_csv(INPUT_FILE)
fur_color_series = df[KEY]
mask = fur_color_series.notna()
fur_color_array = fur_color_series[mask].unique()
print(fur_color_array)

list_of_color = []
list_of_counts = []
for color in fur_color_array:
    a = fur_color_series.where(fur_color_series == color)
    print(f"There were {a.count()} {color} squrrel(s).")
    list_of_color.append(color)
    list_of_counts.append(a.count())

results = {OUTPUT_COLOR_COLUMN: list_of_color, OUTPUT_COUNT_COLUMN: list_of_counts}
results_df = pd.DataFrame(results)
results_df.to_csv(OUTPUT_FILE)
