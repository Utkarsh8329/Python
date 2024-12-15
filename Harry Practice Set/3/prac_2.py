letter = '''Dear <|NAME|> 
You are Selected!ut
Date: <|DATE|>'''
name = input('Enter your name: ')
date = input('Enter your date: ')
letter = letter.replace('<|NAME|>',name)
letter = letter.replace('<|DATE|>',date)
print(letter)