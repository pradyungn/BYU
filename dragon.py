import random
import time

def nameChooser():#Asks user's nameyboi
    name=input('What is your name?')
    return name
nameyboi=nameChooser()
def displayIntro():
    print(''+nameyboi+' is in a land full of dragons. In front of '+nameyboi+',')
    print(nameyboi+' sees three caves. In one cave, the dragon is friendly')
    print('and will share his treasure with '+nameyboi+'. The other dragon')
    print('is greedy and hungry, and will eat '+nameyboi+' on sight.')
    print('There also exists a third cave where there is a sword and a large dragon. \n'+nameyboi+' can take up the sword an slay the dragon.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave will '+nameyboi+' go into? (1, 2, or 3?)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print(''+nameyboi+' approaches the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of '+nameyboi+'! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 3)
    slayerCave = random.randint(1, 3)
    while slayerCave == friendlyCave:
        slayerCave=random.randint(1, 3)
    meanyCave=random.randint(1, 3)
    while meanyCave==friendlyCave or meanyCave==slayerCave:
        meanyCave=random.randint(1, 3)

    if chosenCave == str(friendlyCave):
         print('Gives '+nameyboi+' his treasure!')
    elif chosenCave == str(meanyCave):
         print('Gobbles '+nameyboi+' down in one bite!')
    elif chosenCave == str(slayerCave):
        print(nameyboi+' is able to slay the dragon!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
