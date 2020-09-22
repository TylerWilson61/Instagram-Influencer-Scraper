import json

file = open('users.txt', 'r')
lines = file.read()
file.close()
file_lines = lines.split('>')
usernames = []
end = " "

for line in file_lines:
    if 'title' in line:
        idx = line.index('title') + 7
        user = ""
        while line[idx] != '"':
            user += line[idx]
            idx +=1
        
        usernames.append(user)

obj = {"usernames":usernames}
with open ('array_of_followers','w') as file:
    file.write(json.dumps(obj))
