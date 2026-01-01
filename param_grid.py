from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

csv_file = pd.read_csv('data/sample_weather_data.csv', usecols=['Location', 'Temperature_C', 'Humidity_pct', 'Precipitation_mm', 'Wind_Speed_kmh'], nrows=100)

# extracting relevant columns
temp = csv_file['Temperature_C']
humi = csv_file['Humidity_pct']
precip = csv_file['Precipitation_mm']
wind_speed = csv_file['Wind_Speed_kmh']

# creating dataset for scatter plots and ease of access
dataset = np.array([[precip, humi],
                    [temp, wind_speed],
                    [precip, wind_speed],
                    [temp, humi]])

# plotting
fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(10, 8))

for i in range(4):
    row = i // 2
    col = i % 2
    x_data = dataset[i][0]
    y_data = dataset[i][1]

    ax[row, col].scatter(x_data, y_data, marker='o')
    ax[row,col].set_title(f'{["Precipitation vs Humidity", "Temperature vs Wind Speed", "Precipitation vs Wind Speed", "Temperature vs Humidity"][i]}')
    x_label = ["Precipitation", "Temperature", "Precipitation", "Temperature"][i]
    y_label = ["Humidity", "Wind Speed", "Wind Speed", "Humidity"][i]
    ax[row, col].set_xlabel(f'{x_label} ({"mm" if x_label == "Precipitation" else "%" if x_label == "Humidity" else "°C" if x_label == "Temperature" else "km/h"})')
    ax[row, col].set_ylabel(f'{y_label} ({"mm" if y_label == "Precipitation" else "%" if y_label == "Humidity" else "°C" if y_label == "Temperature" else "km/h"})')
    ax[row, col].grid(True)

fig.tight_layout()
fig.subplots_adjust(hspace=0.35, wspace=0.25)

plt.show()
