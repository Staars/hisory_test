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

with open('commit_history.txt', 'a') as fd:
    fd.write(f'\n{hash}')
    
print("Did it:",hash)


