import json

with open('array_of_followers','r') as file:
    file = json.load(file)
print(len(file['usernames']))
print(len(file['bio']))
print(len(file['influencer_status']))
