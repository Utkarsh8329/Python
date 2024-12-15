# #Practice Set 2

def game():
    return 444

score = game()
with open("history.txt", "r") as f:
    highscore = f.read()

if highscore == '':
    with open('history.txt','w') as f:
        f.write(str(score))

if int(highscore) < score:
    with open('history.txt','w') as f:
        f.write(str(score))