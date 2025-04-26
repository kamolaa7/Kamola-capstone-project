# Purpose/Problem Statement 
This program helps users find fun and simple activities when they are bored by reccomending an idea based on whether they want to do something by themselves or socially with others. It addresses the common conflict people have of not knowing what to do during their free time.

# Target Audience 
teens looking to find ways to have fun with their friends or anyone who wants quick and easy ways to have fun or be entertained

# Solution + Limitations  
The project solves the problem by pulling suggestions from the Bored API which includes the number of participants the user selects (solo or social). It uses an easy user interface with just one input, "What type of activity would you like?" making it very beginner-friendly and intuiative. However, there are some limitations such as not being able to filter the actvity type such as the user wanting something to do with going outside or inside. It also gives only 1 activity at a time, making it less quick to find an intresting activity.

# Key Features / Key Components 
Some key features include the input, API request, the ouput, and status code that ensures the API response was successful. If not, it lets the user know it failed. 
Input: ```
solo_or_social = int(input("What type of activity would you like? (1 for solo, 2 for social)"))```
API Request: ```
response = requests.get(url, params=params)```
Output for User: ```
print("Activity: " + data['activity'])
print("Type: " + data['type'])```
Status Check:```
if response.status_code == 200:
#code block
else:
    print("Oops! Failed to fetch activity.")```
    
# Technical Challenges + Future Plans  
Learning how to use the resquest library and pulling out information from the Bored API was something I was new to. I was stuck majority of the time learning how get information such as the activty and type of activty from the dictionary as seen here: ```
print("\nActivity: " + data['activity'])
print("Type: " + data['type'])```
Although simple, this part was difficult to figure out for me and fully understand how it is being used, hence why I used Chatgpt to explain step by step how it worked. I wish I could've given 5 different type of activities in one go so that it's quicker to make a decision for the user. I hope in the future with more experience with request library, I will filter the activity types and give user the topic they want such as "outside acitivty" or "educational activty." 

# Project Timeline
I spent my frist week thinking of exactly what I will code - I wanted to code something that would help teens my age who love to try new things like me. By the end of the first week, I tried searching for web apis that relate to activities and found the Bored API which convientatntly worked out. The following week, I started planning and began coding. However this week I ran into trouble figuring out how I can pull out information from the api. Upon learning about the request library and using AI to understand how to pull information from an api and call it, I finally coded the whole thing. This whole process took me about 2.5 weeks, all to learn, undertsnad, and code this project. 

# Tools and Resources Used  
Techsmart - platform to code the project
Bored API Documentation
Python Requests Library
AI - to explain how to pull the activity and type of activty from the documentation


