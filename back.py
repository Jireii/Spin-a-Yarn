import random

# Modern
mdNameM = ['Kane', 'Rick', 'Troy', 'Mike']
mdNameF = ['kaelyn', 'Natalie', 'Marie', 'Daisy']
mdPlace = ['Sowdence', 'Idletown', 'Plyport', 'Peasburg', 'Rancaster']
mdBuilding = ['cafe', 'street', 'school', 'alley', 'bookstore']
mdSenPlace = ['In a city of ', 'At city of ', 'In a district of ']

# Fantasy
ftNameM = ['Marsh', 'Ander', 'Red', 'Vop', 'Fyyrs']
ftNameF = ['Cala', 'Sera', 'Muko', 'Ruka', 'Mera']
ftPlace = ['Gatmedge', 'Pyrfield', 'Katbay', 'Wunvale', 'Jarncrest']
ftBuilding = ['inn', 'tavern', 'alley', 'road', 'market']
ftSenPlace = ['Somewhere at the ', 'Faraway at the ', 'In a town named ']

# Action
acMid = ['. After that, they realised that they are in a same competition, and challenged one another to meet at the finals']
acEndLT = ['. At the day of the competition, they worked hard and made it into the finals, but the result of they competition is draw.', ". Finally, it's the competition day. They both worked hard, and one of them wins but they become best friends."]
acEndDk = [". At the day of the competition, one of them finally reached the finals, but the other one didn't.", ". Finally, it's the competition day. They worked hard, but unfortunately they both didn't make it into the finals."]
# Romance
rmMid = ['. After that, somehow they get to know each other and getting closer day after day']
rmEndLt = ['.They have become life partners, and live a happy life after', "They're married, and they love each other for eternety."]
rmEndDk =  ['. After they are just becoming really close, one of them died because of the disease.', '. After they got to introduce themshelves to their families, one of them family does not approve their relationship.', '. After one of them confess to the other, one of them had to go with another person because of the tradition.']

# Universal
intro0 = [", there's someone called ", ', someone named ', ', a person called ']
intro1 = [' and walks out of ', ' and walks into ', ' is in a ']

prog0 = ['. While doing so ', '. At that time']
prog1 = [' then catches a glimpse of someone named ', ' then meet with ', ' then encountered with ']

# def story():
#     from main import setting, theme, tone

#     if setting == 0 and theme == 0 and tone == 0:
#         print(random.choice(ftSenPlace) + random.choice(ftPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(ftBuilding) + random.choice(prog1) + random.choice(acMid) + random.choice(acEndLT))

#     elif setting == 0 and theme == 0 and tone == 1:
#         print(random.choice(ftSenPlace) + random.choice(ftPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(ftBuilding) + random.choice(prog1) + random.choice(acMid) + random.choice(acEndDk))

#     elif setting == 0 and theme == 1 and tone == 0:
#         print(random.choice(ftSenPlace) + random.choice(ftPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(ftBuilding) + random.choice(prog1) + random.choice(rmMid) + random.choice(rmEndLt))
    
#     elif setting == 0 and theme == 1 and tone == 1:
#         print(random.choice(ftSenPlace) + random.choice(ftPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(ftBuilding) + random.choice(prog1) + random.choice(rmMid) + random.choice(rmEndDk))

#     elif setting == 1 and theme == 0 and tone == 0:
#         print(random.choice(mdSenPlace) + random.choice(mdPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(mdBuilding) + random.choice(prog1) + random.choice(acMid) + random.choice(acEndLT))

#     elif setting == 1 and theme == 0 and tone == 1:
#         print(random.choice(mdSenPlace) + random.choice(mdPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(mdBuilding) + random.choice(prog1) + random.choice(acMid) + random.choice(acEndDk))

#     elif setting == 1 and theme == 1 and tone == 0:
#         print(random.choice(mdSenPlace) + random.choice(mdPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(mdBuilding) + random.choice(prog1) + random.choice(rmMid) + random.choice(rmEndLt))

#     elif setting == 1 and theme == 1 and tone == 1:
#         print(random.choice(mdSenPlace) + random.choice(mdPlace) + random.choice(intro0) + random.choice(ftNameM) + random.choice(intro1) + random.choice(mdBuilding) + random.choice(prog1) + random.choice(rmMid) + random.choice(rmEndDk))
