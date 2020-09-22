import json
with open ("followers", "r") as flrs:
    iter_followers =  json.loads(flrs.read())["followers"]
print(type(iter_followers))
