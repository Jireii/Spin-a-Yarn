#Spin a Yarn
import time
import random

print('\nWelcome to the Spin a Yarn program.\n\n')
# time.sleep(0.75)

print('Spinning a yarn is a proccess which involves spinning and twisting fiber to form a yarn.')
print('As an idiom, Spin a yarn is defined as when the one tells a story.\n')
print('In this program, you will choose(spinning) some words(fibers) to form a story(yarn).')
print('The program will generate a story based on your choices.\n')
# time.sleep(7.5)

print('Now you shall choose the pieces to form the story :\n')
# time.sleep(1)

nsetting = ['fantasy', 'modern']
print('Please choose your desired story setting.')
print('1. Fantasy')
print('2. Modern')
while  True:
    setting = int(input('Insert here based on the number :'))
    if 1 <= setting <= 2:
        print('')
        break
    print('Please try again, insert the correct number.')
setting = setting -1

ntheme = ['action', 'romance']
print('Please choose your desired story theme.')
print('1. Action')
print('2. Romance')
while True:
    theme = int(input('Insert here based on the number :'))
    if 1 <= theme <= 2:
        print('')
        break
    print('Please try again, insert the correct number.')
theme = theme -1

ntone = ['light', 'dark']
print('Please choose your desired story tone.')
print('1. Light')
print('2. Dark')
while True:
    tone = int(input('Insert here based on the number :'))
    if 1 <= tone <= 2:
        print('')
        break
    print('Please try again, insert the correct number.')
tone = tone -1

time.sleep(0.5)
print('You have choosen :')
print('The story which has ' + nsetting[setting] +' setting with ' + ntheme[theme] + ' themed, and a ' + ntone[tone] + ' story.')

print('\nAnd here is the story :')

def story():
    from back import mdNameM, mdNameF, mdPlace, mdBuilding, mdSenPlace, ftNameM, ftNameF, ftPlace, ftBuilding, ftSenPlace, acMid, acEndLT, acEndDk, rmMid, rmEndLt, rmEndDk, intro0, intro1, prog0, prog1

    if setting == 0 and theme == 0 and tone == 0:
        print(random.choice(ftSenPlace) + random.choice(ftPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(ftBuilding) + random.choice(prog1) + random.choice(ftNameF) + random.choice(acMid) + random.choice(acEndLT))

    elif setting == 0 and theme == 0 and tone == 1:
        print(random.choice(ftSenPlace) + random.choice(ftPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(ftBuilding) + random.choice(prog1) + random.choice(ftNameM) + random.choice(acMid) + random.choice(acEndDk))

    elif setting == 0 and theme == 1 and tone == 0:
        print(random.choice(ftSenPlace) + random.choice(ftPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(ftBuilding) + random.choice(prog1) + random.choice(ftNameM) + random.choice(rmMid) + random.choice(rmEndLt))
    
    elif setting == 0 and theme == 1 and tone == 1:
        print(random.choice(ftSenPlace) + random.choice(ftPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(ftBuilding) + random.choice(prog1) + random.choice(ftNameF) + random.choice(rmMid) + random.choice(rmEndDk))

    elif setting == 1 and theme == 0 and tone == 0:
        print(random.choice(mdSenPlace) + random.choice(mdPlace) + random.choice(intro0) + random.choice(mdNameF) + random.choice(intro1) + random.choice(mdBuilding) + random.choice(prog1) + random.choice(mdNameM) + random.choice(acMid) + random.choice(acEndLT))

    elif setting == 1 and theme == 0 and tone == 1:
        print(random.choice(mdSenPlace) + random.choice(mdPlace) + random.choice(intro0) + random.choice(mdNameF) + random.choice(intro1) + random.choice(mdBuilding) + random.choice(prog1) + random.choice(mdNameF) + random.choice(acMid) + random.choice(acEndDk))

    elif setting == 1 and theme == 1 and tone == 0:
        print(random.choice(mdSenPlace) + random.choice(mdPlace) + random.choice(intro0) + random.choice(mdNameM) + random.choice(intro1) + random.choice(mdBuilding) + random.choice(prog1) + random.choice(mdNameF) + random.choice(rmMid) + random.choice(rmEndLt))

    elif setting == 1 and theme == 1 and tone == 1:
        print(random.choice(mdSenPlace) + random.choice(mdPlace) + random.choice(intro0) + random.choice(mdNameF) + random.choice(intro1) + random.choice(mdBuilding) + random.choice(prog1) + random.choice(mdNameM) + random.choice(rmMid) + random.choice(rmEndDk))

    return

story()
