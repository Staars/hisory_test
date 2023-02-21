#!/usr/bin/python
import sys
import json

with open('env.txt') as f:
    data = json.load(f)
    print(data)

with open('commit_history.txt', 'a') as fd:
    fd.write(f'\n{s}')
print("Did it",s)
with open('commit_history.txt') as f:
    text = f.read()
    print(text)
