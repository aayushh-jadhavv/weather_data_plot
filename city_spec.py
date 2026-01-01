from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import sys

csv = pd.read_csv('data/weather_data.csv', usecols=['Location', 'Date_Time', 'Temperature_C'])

# filtering cities: San Diego, New York, San Jose, Philadelphia
condition_SD = csv['Location'] == 'San Diego'
condition_NY = csv['Location'] == 'New York'
condition_SJ = csv['Location'] == 'San Jose'
condition_PA = csv['Location'] == 'Philadelphia'

sd_data = csv[condition_SD].reset_index(drop=True).head(20)
ny_data = csv[condition_NY].reset_index(drop=True).head(20)
sj_data = csv[condition_SJ].reset_index(drop=True).head(20)
pa_data = csv[condition_PA].reset_index(drop=True).head(20)

#sorting by date time and resetting index for each city
for data in [sd_data, ny_data, sj_data, pa_data]:
    data.sort_values(by='Date_Time', inplace=True, axis=0)
    data.reset_index(drop=True, inplace=True)

#plotting
fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(10, 8))

datas = [sd_data, ny_data, sj_data, pa_data]

for i in range(4):
    row = i // 2
    col = i % 2

    data = datas[i]

    x_data = data.index.to_frame()
    y_data = data['Temperature_C']

    # plotting rolling average
    data['rolling'] = data['Temperature_C'].rolling(window=5).mean()

    ax[row, col].plot(x_data, data['rolling'], linewidth=5)
    ax[row, col].set_title(f'{["San Diego", "New York", "San Jose", "Philadelphia"][i]}')
    ax[row, col].set_xlabel("Index")
    ax[row, col].set_ylabel("Temperature in C")
    ax[row, col].grid(True)

if len(sys.argv) != 2:
    print("No data")
else :
    city = sys.argv[1]
    if city == 'sd':
        print(sd_data)
    elif city == 'ny':
        print(ny_data)
    elif city == 'sj':
        print(sj_data)
    elif city == 'pa':
        print(pa_data)
    else:
        raise Exception("wrong city")

fig.tight_layout()
fig.subplots_adjust(hspace=0.35, wspace=0.25)
plt.show()