import json
with open ("array_of_followers", "r") as json_file:
    csv = json.loads(json_file.read())
        
        #ADD NEW COLS
csv['influencer_status'] = []
csv['bio'] = []
with open ("array_of_followers", "w") as json_file:
    json_file.write(json.dumps(csv))
