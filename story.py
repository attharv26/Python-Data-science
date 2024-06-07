kahani = ''
while True:
    line=input('>>>')
    if not line: #line mai data nhi h ( blank entry)
        break
    kahani += line + '\n'
print('story is:')
print(kahani)