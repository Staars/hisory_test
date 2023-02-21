#!/usr/bin/python
import sys
import json

hash = ""
oldest_hash = ""
hash_list = []

with open('env.txt') as f:
    data = json.load(f)
    hash = data["after"]
    
with open('commit_history.txt') as f:
    hash_list = f.readlines()
    oldest_hash = hash_list[0]
    print(hash_list,oldest_hash)

with open('commit_history.txt', 'a') as fd:
    fd.write(f'\n{hash}')
    
print("Did it:",hash)


