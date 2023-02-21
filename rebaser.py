#!/usr/bin/python
import sys
import json

hash = ""

with open('env.txt') as f:
    data = json.load(f)
    hash = data["after"]

with open('commit_history.txt', 'a') as fd:
    fd.write(f'\n{hash}')
    
print("Did it:",hash)

with open('commit_history.txt') as f:
    text = f.read()
    print(text)
