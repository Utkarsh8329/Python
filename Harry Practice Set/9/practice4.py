words = ['sale','bsdk']
with open('gali.txt','r') as f:
    content=f.read()
for word in words:
    content = content.replace(word,"#$@#")
    with open('gali.txt','w') as f:
        f.write(content)
