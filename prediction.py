import pandas as pd
import numpy as np


def rainfall():

    # Set the date range
    start_date = "2023-02-22"
    end_date = "2023-03-22"
    date_range = pd.date_range(start=start_date, end=end_date, freq="D")

    # Generate random rainfall data for each date
    rain_data = pd.DataFrame({
        "Date": date_range,
        "Rainfall": np.random.choice([0, 1], size=len(date_range), p=[0.9, 0.1])
    })
    rain_data.loc[(rain_data["Date"] == "2023-03-02") | (rain_data["Date"] == "2023-03-10"), "Rainfall"] = np.random.choice([0, 1], size=2, p=[0.5, 0.5])

    # Define a function to calculate random rainfall amounts between 1mm and 3mm
    def get_rainfall_amount():
        return round(np.random.uniform(1, 3), 1)

    # Add a Rain Status column indicating whether it's raining or not
    rain_data["Rain Status"] = np.where(rain_data["Rainfall"] == 1, "Raining", "Not Raining")

    # Add a Rainfall Amount column with random values between 1mm and 3mm for dates that have rain
    rain_data["Rainfall Amount"] = np.where(rain_data["Rainfall"] == 1, [get_rainfall_amount() if x == 1 else 0 for x in rain_data["Rainfall"]], 0)

    # Print the rainfall data for each date
    for i, row in rain_data.iterrows():
        if row["Rainfall"] == 1:
            print(f"{row['Date'].strftime('%Y-%m-%d')}: Raining ({row['Rainfall Amount']} mm)")
        else:
            print(f"{row['Date'].strftime('%Y-%m-%d')}: Not raining")

    # Save the data to a CSV file
    rain_data.to_csv("kerala_rainfall.csv", index=False)
