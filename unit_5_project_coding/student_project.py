"""
Data Structures
Student Project
Project Title:
"""

import requests

# url link
url = "https://bored.api.lewagon.com/api/activity"

# ask user if they want solo or social activities 
solo_or_social = int(input("What type of activity would you like? (1 for solo, 2 for social)"))

# creates dictionary of social or solo parameter to show the user's input choice
params = {
    "participants": solo_or_social
}

# sends a get request to url with the parameter and stores into response variable
response = requests.get(url, params=params)

# checks if the request was successful
if response.status_code == 200: # 200 = successful
    data = response.json() # converting response to json file formate and stores into data variable
    print("\nHere's an activity you can try:")
    print("\nActivity: " + data['activity']) # adding type of activity
    print("Type: " + data['type']) # adding if activity is solo or social   
else:
    print("Oops! Failed to fetch activity.")
    

  
