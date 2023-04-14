# import requests
# import pandas as pd

# # Send GET request to API endpoint
# url = "https://nodeumcu-clientserver.onrender.com/api/data"
# response = requests.get(url)

# # Convert JSON response to DataFrame
# data = response.json()
# df = pd.DataFrame(data)

# # Save DataFrame to CSV file
# df.to_csv("data.csv", index=False)



import requests
import pandas as pd

# Send GET request to API endpoint
url = "https://nodeumcu-clientserver.onrender.com/api/data"
response = requests.get(url)

# Convert JSON response to DataFrame
data = response.json()
df = pd.DataFrame(data)

# Append DataFrame to CSV file
df.to_csv("data.csv", mode='a', header=False, index=False)
