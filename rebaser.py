#!/usr/bin/python
import sys
import json

new_hash = ""
oldest_hash = ""
hash_list = []

with open('env.txt') as f:
    data = json.load(f)
    new_hash = data["after"]
    
with open('commit_history.txt') as f:
    hash_list = f.readlines()
    for hash in hash_list:
        hash = hash.strip()
    oldest_hash = hash_list[0]
    print(hash_list,oldest_hash)
hash_list.append(new_hash)
print(hash_list)

with open('.git/info/grafts', 'w') as f:
    f.write(f'{oldest_hash}')

with open('commit_history.txt', 'w') as f:
    for h in hash_list[1:]:
        if len(h) > 8:
            f.write(f'{h}'\n)
    
print("Did it:",hash_list)


