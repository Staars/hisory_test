s = "12345678"
with open('commit_history.txt') as f:
    text = f.read()
    print(text)
with open('commit_history.txt', 'a') as fd:
    fd.write(f'\n{s}')
print("Did it",s)
with open('commit_history.txt') as f:
    text = f.read()
    print(text)
