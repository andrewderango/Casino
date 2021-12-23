#Link to repl.it: https://repl.it/@kotkaniemi15/Casino#main.py

#casino.py
#Author: Andrew D.
#Date: November 11, 2020
#Description: The user is given $100 000 to start the game, and they can pick between a variety of games to play and attempt to build up their balance. This program relies heavily on random integers to randomize odds.

import random
import time
import math
import sys
import os #Needed to delete the jelly bean jar.

def slowPrint(message): #Allows flush text to make the program look cleaner.
  for char in message: #This function applies to every character that is to be typed.
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(printTime) #The amount of time the program waits before each letter is typed, in seconds.

def moneyCheck(): #Will be applied after the user loses money. This function checks if the user ran out of money.
  if money < 1: #If the user drops below $1, they leave the casino.
    slowPrint('\nYou no longer have enough money to gamble. You have lost your $100 000!\nYou left the casino.\n')
    raise SystemExit #The program is terminated.
 
def yesNoQuestion(question): #Will be applied when the user is being asked a yes or no question.
  yesNoResp = '' #Assures that the following loop is entered.
  while yesNoResp not in yes_no:
    slowPrint(question)
    yesNoResp = input()
    if yesNoResp not in yes_no:
      slowPrint("Please type 'yes' or 'no'.\n") #This should only occur if the user enters an invalid response.
    else:
      if yesNoResp in yes:
        return True
      elif yesNoResp in no:
        return False
      elif yesNoResp in menuVocab:
        if menuOptions(True,True,True,True) == 'Quit': #Menu is displayed.
          slowPrint('\n\n')
          raise SystemExit
        yesNoResp = '' #Assures that if the user opens the menu, the question will still appear once the menu is closed by the user.
      else:
        slowPrint('This should not happen #1.') #The only strings in yes_no are contained in the menuVocab, yes, and no lists.
 
def multipleChoices(question,opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9,opt10): #This function will be applied when the user should answer a question by using integers to denote the option. Up to 10 options are possible.
  slowPrint(question)
  slowPrint('1. ' + opt1 + '\n')
  slowPrint('2. ' + opt2 + '\n')
  if opt3 != False: #Options that are not being used should be denoted as False.
    slowPrint('3. ' + opt3 + '\n')
    if opt4 != False:
      slowPrint('4. ' + opt4 + '\n')
      if opt5 != False:
        slowPrint('5. ' + opt5 + '\n')
        if opt6 != False:
          slowPrint('6. ' + opt6 + '\n')
          if opt7 != False:
            slowPrint('7. ' + opt7 + '\n')
            if opt8 != False:
              slowPrint('8. ' + opt8 + '\n')
              if opt9 != False:
                slowPrint('9. ' + opt9 + '\n')
                if opt10 != False:
                  slowPrint('10. ' + opt10 + '\n')
  
  valid = False
  while valid == False:
    slowPrint('Enter the number beside the option you would like to select: ')
    userChoiceMultiple = input()
    if userChoiceMultiple in menuVocab: #The user attempts to enter the menu.
      menuOptions(True,True,True,True) #All menu options should appear.
    else:
      try:
        userChoiceMultiple = int(userChoiceMultiple) #Value entered by user should be an integer.
        if userChoiceMultiple < 1:
          slowPrint('Please enter an integer above 0.\n')
        else:
          if opt3 == False:
            if userChoiceMultiple > 2:
              slowPrint('Please enter an integer under 3.\n') #There are only 2 valid options in this case.
            else:
              valid = True #Loop is exited.
              return userChoiceMultiple #Returns the integer representing the user's choice.
          elif opt4 == False:
            if userChoiceMultiple > 3:
              slowPrint('Please enter an integer under 4.\n')
            else:
              valid = True
              return userChoiceMultiple
          elif opt5 == False:
            if userChoiceMultiple > 4:
              slowPrint('Please enter an integer under 5.\n')
            else:
              valid = True
              return userChoiceMultiple
          elif opt6 == False:
            if userChoiceMultiple > 5:
              slowPrint('Please enter an integer under 6.\n')
            else:
              valid = True
              return userChoiceMultiple
          elif opt7 == False:
            if userChoiceMultiple > 6:
              slowPrint('Please enter an integer under 7.\n')
            else:
              valid = True
              return userChoiceMultiple
          elif opt8 == False:
            if userChoiceMultiple > 7:
              slowPrint('Please enter an integer under 8.\n')
            else:
              valid = True
              return userChoiceMultiple
          elif opt9 == False:
            if userChoiceMultiple > 8:
              slowPrint('Please enter an integer under 9.\n')
            else:
              valid = True
              return userChoiceMultiple
          elif opt10 == False:
            if userChoiceMultiple > 9:
              slowPrint('Please enter an integer under 10.\n')
            else:
              valid = True
              return userChoiceMultiple
          else:
            if userChoiceMultiple > 10:
              slowPrint('Please enter an integer under 11.\n')
            else:
              return userChoiceMultiple
      except:
        slowPrint('Please enter an integer.\n')
 
def gameOptions(): #This function is applied when the user chooses what game they would like to play.
  slowPrint('Which game would you like to play?')
  time.sleep(0.5)
  slowPrint('\n1. Roulette')
  time.sleep(0.5)
  slowPrint('\n2. Jelly bean guesser')
  time.sleep(0.5)
  slowPrint('\n3. Horse race')
  time.sleep(0.5)
  slowPrint('\n4. Blackjack')
  time.sleep(0.5)
  slowPrint('\n5. Slots')
  time.sleep(0.5)
  slowPrint('\n6. NHL betting')
  time.sleep(0.5)
  slowPrint('\n7. Leave casino\n') #7 different options for the user, including to leave the casino/quit.
  time.sleep(0.5)
  valid = False
  while valid == False:
    slowPrint('\nPlease select the number beside the game you would like to play. (1-7): ')
    gameChoiceUser = input()
    try:
      if gameChoiceUser in menuVocab:
        if menuOptions(True,True,True,True) == 'Quit': #Menu is displayed.
          return 'Quit'
        else:
          valid = False #Assures that if the user opens the menu, the question will still appear once the menu is closed by the user.
      else:
        gameChoiceUser = int(gameChoiceUser) #Value entered must be an integer.
        if gameChoiceUser < 1:
          slowPrint('Please ensure that the value you entered is equal to or above 1.\n')
        elif gameChoiceUser > 7:
          slowPrint('Please ensure that the value you entered is equal to or below 7.\n') #There are only 7 options.
        else:
          if gameChoiceUser == 1:
            return 'Roulette' #The name of the desired game is returned, rather than the integer representing it.
          elif gameChoiceUser == 2:
            return 'Jelly bean guesser'
          elif gameChoiceUser == 3:
            return 'Horse race'
          elif gameChoiceUser == 4:
            return 'Blackjack'
          elif gameChoiceUser == 5:
            return 'Slots'
          elif gameChoiceUser == 6:
            return 'NHL betting'
          elif gameChoiceUser == 7:
            return 'Leave casino'
          else:
            slowPrint('This should not happen #16.')
    except:
      slowPrint('Please ensure that the value you entered is an integer.\n')
 
def menuOptions(one,two,three,four): #This function opens the menu. The menu can only be opened during certain parts of the game.
  lastMenuNumber = 0 #Assures the first valid menu option is declared by pressing key 1.
  menuOption1 = False
  menuOption2 = False
  menuOption3 = False
  menuOption4 = False
  slowPrint('\nYou have opened the menu.')
  
  if one == True:
    slowPrint('\n' + str(lastMenuNumber+1) + '. Resume')
    menuOption1 = lastMenuNumber + 1
    lastMenuNumber += 1
  
  if two == True:
    slowPrint('\n' + str(lastMenuNumber+1) + '. Check stats')
    menuOption2 = lastMenuNumber + 1
    lastMenuNumber += 1
  
  if three == True:
    slowPrint('\n' + str(lastMenuNumber+1) + '. View instructions')
    menuOption3 = lastMenuNumber + 1
    lastMenuNumber += 1
  
  if four == True:
    slowPrint('\n' + str(lastMenuNumber+1) + '. Leave casino')
    menuOption4 = lastMenuNumber + 1
    lastMenuNumber += 1
  
  valid = False #Assures the following loop is entered.
  while valid == False: #Process will repeat until the user enters a valid response.
    slowPrint('\nSelect an option by typing the number beside it: ') #The user can select an option provided from the menu by typing the integer correlated with the desired option.
    userMenuOption = input()
    try:
      userMenuOption = int(userMenuOption) #The selected menu option must be an integer.
      if userMenuOption < 1 or userMenuOption > 4: #The selected menu option must be between 1 and 5.
        slowPrint('Please select an integer between 1 and 4.\n')
      else:
        valid = True #The selected menu option meets all criteria and can thus proceed.
    except:
      slowPrint('Please enter an integer here.\n')
  
  if userMenuOption == menuOption1:
    slowPrint('You have resumed the game.\n\n') #The user resumes the game and just exits the menu.
  
  elif userMenuOption == menuOption2: #User can see how they have done so far in the casino.
    slowPrint('\nStarting balance: $100000\n')
    if money % 1 == 0: #If the money value is on the dollar. 
      slowPrint('Current balance: $' + str(int(money)) + '\n') #Money is converted to integer so that no decimals appear.
    elif money % 1 != 0:
      slowPrint('Current balance: ${:.2f}'.format(money) + '\n') #Money is rounded to 2 decimals no matter what (unless it is on the dollar.)
    else:
      slowPrint('This should not happen #14.')
    netGainMoney = money - 100000 #The net gain of money is the amount of money the user and gained/lost since starting the game.  
    if netGainMoney >= 0: #If the net gain is positive.
      if netGainMoney % 1 == 0:
        slowPrint('Net gain: $' + str(int(netGainMoney)) + '\n')
      elif netGainMoney % 1 != 0:
        slowPrint('Net gain: ${:.2f}'.format(netGainMoney) + '\n') 
      else:
        slowPrint('This should not happen #15.')
    else: #If the net gain is negative. This needed to be separated from the previous if statement so that the negative sign could be before the dollar sign.
      if netGainMoney % 1 == 0:
        slowPrint('Net gain: -$' + str(int(netGainMoney*-1)) + '\n') #Net gain money is converted to its positive value because the negative is already printed before.
      elif netGainMoney % 1 != 0:
        slowPrint('Net gain: -${:.2f}'.format(netGainMoney*-1) + '\n')
      else:
        slowPrint('This should not happen #40.')
    slowPrint('Percentage increase: ' + str(round(netGainMoney / 100000 * 100,2)) + '%\n') #The percentage increase is the relative gain of money compared to the starting value.
    slowPrint('Bets won: ' + str(betsWon) + '\n')
    slowPrint('Bets lost: ' + str(betsLost) + '\n\n')
  
  elif userMenuOption == menuOption3: #User wants to see the instructions of the game.
    slowPrint("You're in a virtual casino, and your only goal is to win as much money as possible! You start with $100 000, and can gain money through a variety of games and bets. The menu is accessible throughout the game by typing 'menu.'\n\n")
  
  elif userMenuOption == menuOption4: #User wants to leave the casino.
    if money % 1 == 0:
      slowPrint('\nYou left the casino with $' + str(int(money)) + ', which is a percentage increase of ' + str(round((money - 100000) / 100000 * 100,2)) + '%.\nFarewell!\n')
    elif money % 1 != 0:
      slowPrint('\nYou left the casino with ${:.2f}'.format(money) + ', which is a percentage increase of ' + str(round((money - 100000) / 100000 * 100,2)) + '%.\nFarewell!\n')
    return 'Quit'
 
def distributionCurveProbability(min,max,standardDeviation,arithmeticMean,vertexTimes100000):
  valid = False #Assures the following loop is entered.
  while valid == False: #Process will repeat until the randomly selected coordinates fit inside the distribution curve.
    randomX = float(random.randint(min,max))
    fxCordForRandX = (1/(standardDeviation*math.sqrt(2*math.pi)))*math.e**(-((randomX-arithmeticMean)**2)/(2*standardDeviation**2)) #Formula for the normal distribution curve.
    if fxCordForRandX >= float(random.randint(0,vertexTimes100000))/100000: #Picks a random decimal between 0 and the vertex of the distribution curve.
      valid = True #This should only occur if the randomly selected coordinates are inside of the distribution curve.
  return randomX #The final randomized value selected.
 
def drawCardBlackjack(player): #This function is applied when the user or the dealer needs to draw a card from the deck in Blackjack.
  if player == 'user': #If it is the user's turn.
    userDrawBlackjack = random.choice(cardsProbabilitiesBlackjack)
    userHandBlackjack.append(userDrawBlackjack)
    if userDrawBlackjack == 'Ace':
      userHandValuesBlackjack.append(1)
    elif userDrawBlackjack == 'Jack' or userDrawBlackjack == 'Queen' or userDrawBlackjack == 'King':
      userHandValuesBlackjack.append(10) #Jacks, Queens and Kings are all worth 10.
    elif userDrawBlackjack >= 2 and userDrawBlackjack <= 10:
      userHandValuesBlackjack.append(int(userDrawBlackjack)) #All of these cards use their pip value.
    else:
      slowPrint('This should not happen #30.')
    return userDrawBlackjack #The card that the user acquired.
  elif player == 'dealer': #If it is the dealer's turn.
    dealerDrawBlackjack = random.choice(cardsProbabilitiesBlackjack[1:])
    dealerHandBlackjack.append(dealerDrawBlackjack)
    if dealerDrawBlackjack == 'Ace':
      dealerHandValuesBlackjackAces1.append(1)
      dealerHandValuesBlackjackAces11.append(11) #Aces can have a value of 1 or 11.
    elif dealerDrawBlackjack == 'Jack' or dealerDrawBlackjack == 'Queen' or dealerDrawBlackjack == 'King':
      dealerHandValuesBlackjackAces1.append(10) #Jacks, Queens and Kings are all worth 10.
      dealerHandValuesBlackjackAces11.append(10)
    elif dealerDrawBlackjack >= 2 and dealerDrawBlackjack <= 10:
      dealerHandValuesBlackjackAces1.append(int(dealerDrawBlackjack))
      dealerHandValuesBlackjackAces11.append(int(dealerDrawBlackjack))
    else:
      slowPrint('This should not happen #31.')
  else:
    slowPrint('This should not happen #32.') #It must either be the user's or the dealer's turn.
  return dealerDrawBlackjack #The card that the dealer acquired.
 
yes = ['yes', 'Yes', 'y', 'Y', 'y.', 'ya', 'sure', 'ok', 'OK', 'yes.', 'YES'] #Possible responses for approval.
no = ['no', 'No', 'n', 'N', 'n.', 'nope', 'no.', 'NO'] #Possible responses for disapproval.
menuVocab = ['menu', 'Menu', 'menu.', 'Menu.', 'quit', 'pause', 'Pause', 'Quit', 'MENU', 'QUIT', 'PAUSE', 'open menu', 'leave', 'Leave', 'Leave casino'] #Possible inputs to open the menu.
yes_no = yes + no + menuVocab #All total valid responses for a yes or no question.
betsWon = 0 #Before the game starts, the user has not lost or won any bets in the casino. Must be set to 0.
betsLost = 0
printTime = 0.03
 
money = 100000 #The user enters the casino with $100,000.
slowPrint('Welcome to my casino!')
time.sleep(1)
slowPrint('\nPlease enter your name: ')
name = input().capitalize() #First letter of name is capitalized.
slowPrint('Hello, ' + name + '.\n\n')
 
inCasino = True #User enters casino.
while inCasino == True:
  
  gameChoiceUserVariable = gameOptions()
  
  if gameChoiceUserVariable == 'Roulette': #If the user decides to play roulette.
    if yesNoQuestion('Welcome to Roulette! Are you familiar with this game? (Y/N): ') == False:
      slowPrint("The rules are simple for Roulette. A ball is rolled on a spinning wheel that has 37 slots, with numbers ranging from 0-36. The player attempts to guess the number that the ball will land on, or a set of numbers (Example: Evens, high numbers, etc.) Remember, a higher risk will reward a higher payout!\nLet's get started!\n\n") #Instructions/rules for roulette.
    else:
      slowPrint("Alright then, let's get started!\n\n")
  
    while gameChoiceUserVariable == 'Roulette': #This loop is required in case the user wants to keep playing roulette, which is determined later on.
      winningNumbersRoulette = [] #The possible winning numbers must be reset every time the user plays.
      slowPrint('Place your bets!\n\n')
      userChoiceRouletteGamble = multipleChoices('What would you like to bet for?\n','Over/Under','Even/Odd','One number','Reds/Blacks','Dozen bet',False,False,False,False,False) #Possible bets for roulette.
      if userChoiceRouletteGamble == 1: #User decides to bet on over/under.
        overOrUnderRoulette = multipleChoices('\nWhich would would you like to bet for?\n','Over','Under',False,False,False,False,False,False,False,False)
        valid = False
        while valid == False:
          if overOrUnderRoulette == 1:
            slowPrint('Fill in your guess: The selected number will be over ')
          elif overOrUnderRoulette == 2:
            slowPrint('Fill in your guess: The selected number will be under ')
          else:
            slowPrint('This should not happen #2.') #User must guess either over or under.
          overOrUnderNumberRoulette = input()
          try:
            overOrUnderNumberRoulette = int(overOrUnderNumberRoulette)
            if overOrUnderNumberRoulette < 1:
              slowPrint('Please enter a number equal to or above 1.\n')
            elif overOrUnderNumberRoulette > 35:
              slowPrint('Please enter an integer below 36.\n')
            else:
              valid = True
          except:
            slowPrint('Please enter an integer.\n')
        for ballProbabilities in range(0,37): #The ball can land on any number from 1 to 36.
          if overOrUnderRoulette == 1:
            if ballProbabilities > overOrUnderNumberRoulette:
              winningNumbersRoulette.append(ballProbabilities)
          elif overOrUnderRoulette == 2:
            if ballProbabilities < overOrUnderNumberRoulette:
              winningNumbersRoulette.append(ballProbabilities)
          else:
            slowPrint('This should not happen #3.')
  
      elif userChoiceRouletteGamble == 2: #The user decides to bet on even/odd numbers.
        userChoiceEvenOrOddRoulette = multipleChoices('Which type of number you would like to bet on?\n','Even','Odd',False,False,False,False,False,False,False,False)
        for allNumbersRoulette in range(0,37):
          if userChoiceEvenOrOddRoulette == 1:
            if allNumbersRoulette % 2 == 0: #If the number is even.
              winningNumbersRoulette.append(allNumbersRoulette)
          elif userChoiceEvenOrOddRoulette == 2: 
            if allNumbersRoulette % 2 != 0: #If the number is odd.
              winningNumbersRoulette.append(allNumbersRoulette)
          else:
            slowPrint('This should not happen #5.') #The number must be either even or odd.
      
      elif userChoiceRouletteGamble == 3: #The user decides to bet on a single integer.
        valid = False
        while valid == False:
          slowPrint('Enter your desired number: ')
          OneNumberPredictionRoulette = input()
          try:
            OneNumberPredictionRoulette = int(OneNumberPredictionRoulette)
            if OneNumberPredictionRoulette > 36: #Ball cannot land on a value higher than 36.
              slowPrint('Please enter an integer that is less than 37.\n')
            elif OneNumberPredictionRoulette < 0: #BAll cannot land on a value lower than 0.
              slowPrint('Please enter an integer greater than or equal to 0.\n')
            else:
              winningNumbersRoulette.append(OneNumberPredictionRoulette)
              valid = True
          except:
            slowPrint('Please enter an integer.\n')
  
      elif userChoiceRouletteGamble == 4: #The user decides to bet on a red or black number.
        userChoiceRedOrBlackRoulette = multipleChoices('What numbers would you like to bet on?\n', 'Reds', 'Blacks',False,False,False,False,False,False,False,False)
        if userChoiceRedOrBlackRoulette == 1:
          winningNumbersRoulette.extend([1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]) #The red numbers on the board.
        elif userChoiceRedOrBlackRoulette == 2:
          winningNumbersRoulette.extend([2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]) #The black numbers on the board.
        else:
          slowPrint('This should not happen #6.')
  
      elif userChoiceRouletteGamble == 5: #The user bets on a dozen.
        userChoiceWhichDozen = multipleChoices('Which dozen would you like to bet on?\n', '1 through 12', '13 through 24', '25 through 36',False,False,False,False,False,False,False)
        for dozensRange in range(0,37):
          if userChoiceWhichDozen == 1:
            if dozensRange >= 1 and dozensRange <= 12: #The first dozen.
              winningNumbersRoulette.append(dozensRange)
          elif userChoiceWhichDozen == 2:
            if dozensRange >= 13 and dozensRange <= 24: #The middle dozen
              winningNumbersRoulette.append(dozensRange)
          elif userChoiceWhichDozen == 3:
            if dozensRange >= 25 and dozensRange <= 36: #The last dozen.
              winningNumbersRoulette.append(dozensRange)
          else:
            slowPrint('This should not happen #8.') #The dozen selected must be either 1, 2, or 3.
  
      else:
        slowPrint('This should not happen #7.') #There are only 5 gambling methods for roulette.
  
      valid = False
      while valid == False:
        if money % 1 == 0: #If money is a whole number.
          slowPrint('\nHow much money are you willing to bet? Your current balance is $' + str(int(money)) + ': $')
        elif money % 1 != 0: #If money is not a whole number.
          slowPrint('\nHow much money are you willing to bet? Your current balance is ${:.2f}'.format(money) + ': $')
        else:
          slowPrint('This should not happen #9.')
        moneyBetRoulette = input()
        try:
          moneyBetRoulette = float(moneyBetRoulette) #Money bet must be a decimal.
          if moneyBetRoulette > money:
            slowPrint("You don't have that much money! Try to spend inside your limits.")
          elif moneyBetRoulette < 1:
            slowPrint('Your bet must be above $0.99')
          else:
            money -= moneyBetRoulette #Money is reduced by the bet, even before the outcome has been decided.
            valid = True
        except:
          slowPrint('Please enter a dollar amount, without units. Decimals are permitted.')
      
      oddsOfWinningRoulette = len(winningNumbersRoulette) / 37 * 100 #Percentage chance of winning their chosen bet.
      successfulPayoutRoulette = (100 / oddsOfWinningRoulette) * moneyBetRoulette #Money that would be gained if the user wins.
      moneyIfWinRoulette = successfulPayoutRoulette + money #Total user balance if they win the bet.
      moneyIfLossRoulette = money #Money bet has already been subtracted.
  
      if moneyIfWinRoulette % 1 == 0:
        slowPrint('Your balance if you win (' + str(round(oddsOfWinningRoulette,2)) + '%): $' + str(int(successfulPayoutRoulette + money)) + '\n')
      elif moneyIfWinRoulette % 1 != 0:
        slowPrint('Your balance if you win (' + str(round(oddsOfWinningRoulette,2)) + '%): ${:.2f}'.format(successfulPayoutRoulette + money,2) + '\n')
      else:
        slowPrint('This should not happen #10.')
  
      if moneyIfLossRoulette % 1 == 0:
        slowPrint('Your balance if you lose (' + str(round(100-oddsOfWinningRoulette,2)) + '%): $' + str(int(money)) + '\n')
      elif moneyIfLossRoulette % 1 != 0:
        slowPrint('Your balance if you lose (' + str(round(100-oddsOfWinningRoulette,2)) + '%): ${:.2f}'.format(money) + '\n')
      else:
        slowPrint('This should not happen #11.')
  
      randomIntegerRoulette = random.randint(0,36) #Possible landing spaces are all integers from 0-36.
      slowPrint('The ball lands on number ' + str(randomIntegerRoulette) + '. ') #The ball can only land on one number.
      if randomIntegerRoulette in winningNumbersRoulette: #User wins the bet.
        money = moneyIfWinRoulette
        betsWon += 1
        if money % 1 == 0:
          slowPrint('You win!\nYour new balance is $' + str(int(money)) + '!\n\n')
        elif money % 1 != 0:
          slowPrint('You win!\nYour new balance is ${:.2f}'.format(money) + '!\n\n')
        else:
          slowPrint('This should not happen #12.')
  
      elif randomIntegerRoulette not in winningNumbersRoulette: #User loses the bet.
        money = moneyIfLossRoulette
        betsLost += 1
        if money % 1 == 0:
          slowPrint('Unfortunately, you lose.\nYour new balance is $' + str(int(money)) + '.\n\n')
        elif money % 1 != 0:
          slowPrint('Unfortunately, you lose.\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
        else:
          slowPrint('This should not happen #13.')
        moneyCheck()
      else:
        slowPrint('This should not happen #4.') #The user must either win or lose the bet.
  
      if yesNoQuestion('Would you like to play roulette again? (Y/N): ') == True:
        slowPrint('\n') #The while statement is still true, so the roulette loop will repeat.
      else:
        gameChoiceUserVariable = False #The roulette loop is exited, and a new game can be selected to play.
  
  
  elif gameChoiceUserVariable == 'Jelly bean guesser': #If the user decides to play Jelly Bean Guesser.
    if yesNoQuestion('Welcome to the jelly bean guesser game! Are you familiar with this game? (Y/N): ') == False:
      slowPrint("Just like in every carnival, your objective for this game is to predict how many jelly beans (which will be represented as horizontal lines) are in the jar! Try to beat the host, and guess the number closer than them.\n\n")
      time.sleep(2)
    
    while gameChoiceUserVariable == 'Jelly bean guesser':
      valid = False
      while valid == False:
        if money % 1 == 0:
          slowPrint('\nHow much money are you willing to bet? Your current balance is $' + str(int(money)) + ': $')
        elif money % 1 != 0:
          slowPrint('\nHow much money are you willing to bet? Your current balance is ${:.2f}'.format(money) + ': $')
        else:
          slowPrint('This should not happen #17.') #Money value must either be a whole number or a decimal.
        moneyBetBeans = input() #User enters their betting amount.
        try:
          moneyBetBeans = float(moneyBetBeans)
          if moneyBetBeans > money:
            slowPrint("You don't have that much money! Try to spend inside your limits.")
          elif moneyBetBeans < 1:
            slowPrint('Your bet must be above $0.99')
          else:
            valid = True
        except:
          slowPrint('Please enter a dollar amount, without units. Decimals are permitted.')
  
      slowPrint('Press ENTER to see the jar. You only have a few seconds to look at it, so think fast! ')
      input() #Once the user presses enter, the program will continue. This assures that the user is ready because there is a timer for the jar.
      totalBeans = 0 #This variable must be defined before being added onto.
      printTime = 0 #Jar should appear at once, not slowly.
      slowPrint('______________________________________________________________\n') #Top of the jar.
      beanFrequency = random.randint(2,20)
      for beansRows in range(25):
        slowPrint('|') #Defines the right side of the jar every line.
        for beans in range(60): #The jar is 66 spaces wide.
          if random.randint(1,beanFrequency) <= random.randint(1,5): #Two random integers are included so that there is more variance in the jar.
            slowPrint('-') #A bean is printed.
            totalBeans += 1
          else:
            slowPrint(' ')
        slowPrint('|\n') #Defines the left side of the jar every line, and goes down a line.
      slowPrint('|____________________________________________________________|\n\n') #Bottom of the jar.
      printTime = 0.03
  
      time.sleep(2) #Countdown from 5 begins after 2 seconds. 
      slowPrint('5')
      time.sleep(1)
      slowPrint('4')
      time.sleep(1)
      slowPrint('3')
      time.sleep(1)
      slowPrint('2')
      time.sleep(1)
      slowPrint('1')
      time.sleep(1)
      os.system('clear') #Output screen is deleted once the countdown is over.
      valid = False
      while valid == False:
        slowPrint('Enter your estimate of jelly beans in the jar: ')
        try:
          userGuessBeans = int(input()) #The user's guess must be an integer.
          if userGuessBeans <= 0:
            slowPrint('Your estimate must be above 0.\n')
          else:
            valid = True
        except:
          slowPrint('Please enter an integer.\n')
      
      if totalBeans >= userGuessBeans:
        userImpreciseness = totalBeans - userGuessBeans #How many beans the user was off by.
      elif userGuessBeans > totalBeans:
        userImpreciseness = userGuessBeans - totalBeans
      
      hostGuessBeans = int(distributionCurveProbability(int(totalBeans/2),2*totalBeans,75,totalBeans,532)) #The host's guess, determined by a normal distribution curve. The mean is the correct amount of beans, with a standard deviation of 75.
      if totalBeans >= hostGuessBeans:
        hostImpreciseness = totalBeans - hostGuessBeans #How many beans the host was off by.
      elif hostGuessBeans > totalBeans:
        hostImpreciseness = hostGuessBeans - totalBeans
  
      slowPrint('There were ' + str(totalBeans) + ' jelly beans in the jar.\n')
      slowPrint('The host guessed ' + str(hostGuessBeans) + ' jellybeans in the jar.\n')
      if userImpreciseness != 0:
        slowPrint('You were ' + str(userImpreciseness) + ' jelly beans off from the actual number.\n')
      elif userImpreciseness == 0:
        slowPrint('You were right on! Awesome guess!\n')
      if userImpreciseness != 0:
        slowPrint('The host was ' + str(hostImpreciseness) + ' jelly beans off from the actual number.\n')
      elif userImpreciseness == 0:
        slowPrint('The host was right on, and guessed the number of jelly beans. \n')
  
      if hostImpreciseness > userImpreciseness:
        betsWon += 1 #The user was closer, and therefore wins the bet.
        money += moneyBetBeans #Odds of winning are considered 50/50, so a return of 100% of given.
        if money % 1 == 0:
          slowPrint('You win! Your new balance is $' + str(int(money)) + '!\n\n')
        elif money % 1 != 0:
          slowPrint('You win! Your new balance is ${:.2f}'.format(money) + '!\n\n')
        else:
          slowPrint('This should not happen #18.')
      elif hostImpreciseness < userImpreciseness:
        betsLost += 1 #The host was closer, and therefore the user loses the bet.
        money -= moneyBetBeans
        if money % 1 == 0:
          slowPrint('Unfortunately, you lose.\nYour new balance is $' + str(int(money)) + '.\n\n')
        elif money % 1 != 0:
          slowPrint('Unfortunately, you lose.\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
        else:
          slowPrint('This should not happen #19.')
        moneyCheck()
      elif hostImpreciseness == userImpreciseness:
        slowPrint('We have a tie, so the host gets the money. Better luck next time!\n\n') #The user and the host were off by the same amount. In this case, the user loses the bet.
        betsLost += 1
        money -= moneyBetBeans
        if money % 1 == 0:
          slowPrint('Unfortunately, you lose.\nYour new balance is $' + str(int(money)) + '.\n\n')
        elif money % 1 != 0:
          slowPrint('Unfortunately, you lose.\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
        else:
          slowPrint('This should not happen #20.')
        moneyCheck()
      else:
        slowPrint('This should not happen #21.')
  
      if yesNoQuestion('Would you like to play this game again? (Y/N): ') == False: #User does not want to play again.
        gameChoiceUserVariable = False #The bean loop is exited, so the user can go to the game choice screen.
  
  elif gameChoiceUserVariable == 'Horse race': #User decides to play horse race.
    if yesNoQuestion('Welcome to the horse race! Are you familiar with this game? (Y/N): ') == False:
      slowPrint("There are 5 horses in a race, and you have to predict which horse will win before the race starts for a payout. The higher risk you choose on a horse, the higher the reward!\n") #Instructions/rules for horserace.
      time.sleep(2)
  
    while gameChoiceUserVariable == 'Horse race':
      horseOddsList = [] #List must be defined before items are appended to it. This list will contain 100 items, each representing a 1% chance for a horse.
      sumOddsHorses = 0
      horse1odds = random.randint(1,70)
      for horse1OddsRange in range(horse1odds):
        horseOddsList.append('Horse 1') #These are the odds, in percentage, that horse 1 will win. The max is 70%.
      sumOddsHorses += horse1odds #This variable assures that each horse gets at least a 1% chance of winning.
      horse2odds = random.randint(1,90-sumOddsHorses)
      for horse2OddsRange in range(horse2odds):
        horseOddsList.append('Horse 2')
      sumOddsHorses += horse2odds
      horse3odds = random.randint(1,95-sumOddsHorses)
      for horse3OddsRange in range(horse3odds):
        horseOddsList.append('Horse 3')
      sumOddsHorses += horse3odds
      horse4odds = random.randint(1,98-sumOddsHorses)
      for horse4OddsRange in range(horse4odds):
        horseOddsList.append('Horse 4')
      sumOddsHorses += horse4odds
      horse5odds = 100-sumOddsHorses
      for horse5OddsRange in range(horse5odds):
        horseOddsList.append('Horse 5')
  
      slowPrint('\nPlace your bets!\n')
      userChoiceHorse = multipleChoices('Which horse would you like to bet for?\n','Horse 1 (' + str(horse1odds) + '%)','Horse 2 (' + str(horse2odds) + '%)','Horse 3 (' + str(horse3odds) + '%)','Horse 4 (' + str(horse4odds) + '%)','Horse 5 (' + str(horse5odds) + '%)',False,False,False,False,False) #User guesses which horse will win, and the odds are displayed.
  
      valid = False
      while valid == False:
        if money % 1 == 0:
          slowPrint('\nHow much money are you willing to bet? Your current balance is $' + str(int(money)) + ': $') 
        elif money % 1 != 0:
          slowPrint('\nHow much money are you willing to bet? Your current balance is ${:.2f}'.format(money) + ': $')
        else:
          slowPrint('This should not happen #25.')
        moneyBetHorses = input()
        try:
          moneyBetHorses = float(moneyBetHorses)
          if moneyBetHorses > money:
            slowPrint("You don't have that much money! Try to spend inside your limits.")
          elif moneyBetHorses < 1:
            slowPrint('Your bet must be above $1.00')
          else:
            money -= moneyBetHorses
            valid = True
        except:
          slowPrint('Please enter a dollar amount, without units. Decimals are permitted.')
      
      if userChoiceHorse == 1:
        oddsOfWinningHorses = horse1odds #This variable is needed to determine the user's payout if their selected horse wins the race.
      elif userChoiceHorse == 2:
        oddsOfWinningHorses = horse2odds
      elif userChoiceHorse == 3:
        oddsOfWinningHorses = horse3odds
      elif userChoiceHorse == 4:
        oddsOfWinningHorses = horse4odds
      elif userChoiceHorse == 5:
        oddsOfWinningHorses = horse5odds
      else:
        slowPrint('This should not happen #22.') #The chosen horse must be between 1 and 5.
  
      successfulPayoutHorses = (100 / oddsOfWinningHorses) * moneyBetHorses #The money gained by the user if they guess correctly.
      moneyIfWinHorses = successfulPayoutHorses + money #The total balance of the user if they guess correctly.
      moneyIfLossHorses = money #The bet money has already been deducted.
  
      if moneyIfWinHorses % 1 == 0:
        slowPrint('Your balance if you win (' + str(round(oddsOfWinningHorses,2)) + '%): $' + str(int(successfulPayoutHorses + money)) + '\n') #Odds of winning are displayed, along with their possible new balance.
      elif moneyIfWinHorses % 1 != 0:
        slowPrint('Your balance if you win (' + str(round(oddsOfWinningHorses,2)) + '%): ${:.2f}'.format(successfulPayoutHorses + money) + '\n')
      else:
        slowPrint('This should not happen #23.')
      
      if moneyIfLossHorses % 1 == 0:
        slowPrint('Your balance if you lose (' + str(round(100-oddsOfWinningHorses,2)) + '%): $' + str(int(money)) + '\n') #Odds of winning are displayed, along with their possible new balance.
      elif moneyIfLossHorses % 1 != 0:
        slowPrint('Your balance if you lose (' + str(round(100-oddsOfWinningHorses,2)) + '%): ${:.2f}'.format(money) + '\n')
      else:
        slowPrint('This should not happen #24.')
  
      try:
        horseWinner = int(random.choice(horseOddsList)[-1]) #Last letter of the item is added to the list. This should be the number of the horse.
      except:
        horseWinner = random.choice(horseOddsList)[-1]
      slowPrint('Horse ' + str(horseWinner) + ' won the race, ')
  
      if userChoiceHorse == horseWinner: #If the horse that the user chose is the horse that won.
        money = moneyIfWinHorses #User wins, guessed correct horse.
        betsWon += 1
        if money % 1 == 0:
          slowPrint('so you win!\nYour new balance is $' + str(int(money)) + '!\n')
        elif money % 1 != 0:
          slowPrint('so you win!\nYour new balance is ${:.2f}'.format(money) + '!\n')
        else:
          slowPrint('This should not happen #28.')
      elif userChoiceHorse != horseWinner: #If the horse that the user chose is not the horse that won.
        money = moneyIfLossHorses #User loses, guessed the wrong horse.
        betsLost += 1
        if money % 1 == 0:
          slowPrint('so you lose.\nYour new balance is $' + str(int(money)) + '.\n')
        elif money % 1 != 0:
          slowPrint('so you lose.\nYour new balance is ${:.2f}'.format(money) + '.\n')
        else:
          slowPrint('This should not happen #27.')
        moneyCheck()
      else:
        slowPrint('This should not happen #26.')
  
      if yesNoQuestion('Would you like to play horses again? (Y/N): ') == False:
        gameChoiceUserVariable = False #The loop of horses is exited, and therefore the user is able to choose a new game to play. If the user decides to play again, they will return to the top of this loop where new horse odds are defined.
  
  elif gameChoiceUserVariable == 'Blackjack': #If the user decides to play blackjack.
    if yesNoQuestion('Welcome to the blackjack! Are you familiar with this game? (Y/N): ') == False:
      slowPrint("You are playing against the dealer, and you both start with 2 cards being dealt to each of you. One of the dealer's cards is faced up. Your goal is to make your cards sum up to 21, but if you go over you lose. All cards are worth their pip value, and face cards are worth 10. This rule excludes aces, because they can be switched from 11 and 1 throughout the game.\n") #Instructions/rules of blackjack.
      time.sleep(2)
  
    while gameChoiceUserVariable == 'Blackjack':
      blackjackDone = False
      valid = False
      while valid == False:
        if money % 1 == 0:
          slowPrint('\nHow much money are you willing to bet? Your current balance is $' + str(int(money)) + ': $') #User decides how much they want to bet for this round of blackjack. This will be asked again if the user decides to play again because this is in the while blackjack loop.
        elif money % 1 != 0:
          slowPrint('\nHow much money are you willing to bet? Your current balance is ${:.2f}'.format(money) + ': $')
        else:
          slowPrint('This should not happen #33.')
        moneyBetBlackjack = input()
        try:
          moneyBetBlackjack = float(moneyBetBlackjack)
          if moneyBetBlackjack > money:
            slowPrint("You don't have that much money! Try to spend inside your limits.")
          elif moneyBetBlackjack < 1:
            slowPrint('Your bet must be above $0.99')
          else:
            money -= moneyBetBlackjack
            valid = True
        except:
          slowPrint('Please enter a dollar amount, without units. Decimals are permitted.')
  
      cardsProbabilitiesBlackjack = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'] #All cards that can possibly be pulled. This essentially acts as the deck when a random item is chosen.
  
      dealerHandBlackjack = [] #This list uses the names of the dealer's cards. It is for the user to read.
      dealerHandValuesBlackjackAces1 = [] #This list uses the ace value as 1.
      dealerHandValuesBlackjackAces11 = [] #This list uses the ace value as 11.
      drawCardBlackjack('dealer') #The dealer draws a card.
      if 'Ace' in dealerHandBlackjack or 8 in dealerHandBlackjack: #These 2 possibilities need 'an' instead of 'a'.
        slowPrint("The dealer's face up card is an " + str(dealerHandBlackjack[0]) + '.\n')
      else:
        slowPrint("\nThe dealer's face up card is a " + str(dealerHandBlackjack[0]) + '.\n') #The user gets to know this card.
  
      userHandBlackjack = [] #The user's hand is defined so items can be appended later on. This list stores the cards' names, for the user to understand.
      userHandValuesBlackjack = [] #This list stores the values of the cards. This list is used for adding and checking, rather than for the user.
      drawCardBlackjack('user') #User draws 2 cards to start.
      drawCardBlackjack('user')
      BlackjackRound = 1 #Allows for more options to be available later on.
      slowPrint('Your cards: ' + str(userHandBlackjack[0]) + ', ' + str(userHandBlackjack[1]) + '\n')
      time.sleep(2)
      if sum(userHandValuesBlackjack) == 11 and 'Ace' in userHandBlackjack: #If user gets blackjack on the first hand.
        slowPrint('You got blackjack on the first hand! You get 1.5x the amount you bet as a bonus!\n')
        betsWon += 1
        blackjackDone = True
        money += (moneyBetBlackjack*2.5)
        if money % 1 == 0:
          slowPrint('\nYour new balance is $' + str(int(money)) + '\n\n')
        elif money % 1 != 0:
          slowPrint('\nYour new balance is ${:.2f}'.format(money) + '\n\n')
      else:
        while sum(userHandValuesBlackjack) < 22:
          if BlackjackRound == 1:
            if money - moneyBetBlackjack >= 0:
              userDecisionBlackjack = multipleChoices('What would you like to do now?\n','Hit','Stand','Double down','Surrender',False,False,False,False,False,False) #Options like double down and surrender are only valid on the first turn.
              insufficientFundsBlackjack = False
            else:
              userDecisionBlackjack = multipleChoices('What would you like to do now?\n','Hit','Stand','Surrender',False,False,False,False,False,False,False) #The user cannot double down because they do not have enough money to do so.
              insufficientFundsBlackjack = True
          else:
            userDecisionBlackjack = multipleChoices('What would you like to do now?\n','Hit','Stand',False,False,False,False,False,False,False,False) #The user can only hit and stand if it is not the first turn.
    
          if userDecisionBlackjack == 1: #If the user hits.
            drawBlackjackCardVariable = drawCardBlackjack('user')
            if drawBlackjackCardVariable == 'Ace' or drawBlackjackCardVariable == 8:
              slowPrint('\nYou drew an ' + str(drawBlackjackCardVariable) + '.\n')
            else:
              slowPrint('\nYou drew a ' + str(drawBlackjackCardVariable) + '.\n')
            slowPrint('Your cards: ')
            for cardsInHand in range(len(userHandBlackjack)):
              slowPrint(str(userHandBlackjack[cardsInHand])) #User's cards are printed.
              if cardsInHand != len(userHandBlackjack)-1:
                slowPrint(', ')
            time.sleep(2)
            slowPrint('\n')
            slowPrint('Dealer card: ' + str(dealerHandBlackjack[0]) + '\n')
            BlackjackRound += 1

            if sum(userHandValuesBlackjack) > 21: #If the user's cards add up to more than 21.
              slowPrint('You went over 21. The dealer wins.\n')
              betsLost += 1 #User loses.
              blackjackDone = True
              userHandValuesBlackjack = [22]
              if money % 1 == 0:
                slowPrint('\nYour new balance is $' + str(int(money)) + '.\n\n')
              elif money % 1 != 0:
                slowPrint('\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
              moneyCheck()
            else:
              if 'Ace' in userHandBlackjack: #If the user has an ace.
                if sum(userHandValuesBlackjack)+10 == 21: #If the user's ace becoming an 11 makes the sum add up to 21.
                  finalStandValue = 21           
    
          elif userDecisionBlackjack == 2: #If the user stands.
            if 'Ace' in userHandBlackjack: #If the user has an ace.
              if sum(userHandValuesBlackjack)+10 <= 21:
                finalStandValue = sum(userHandValuesBlackjack)+10 #Attempting to maximize the score of the user by using the ace.
              else:
                finalStandValue = sum(userHandValuesBlackjack)
            else:
              finalStandValue = sum(userHandValuesBlackjack)
            slowPrint('You decided to stand with a hand value of ' + str(finalStandValue) + ". It is the dealer's turn now.\n")
            
            while sum(dealerHandValuesBlackjackAces1) < finalStandValue and sum(dealerHandValuesBlackjackAces11) < finalStandValue: #The dealer starts to draw now that the user stood. The dealer will draw until they go over 21 or they achieve a higher value than the user.
              if sum(dealerHandValuesBlackjackAces1) < 21:
                drawCardBlackjackVariable = drawCardBlackjack('dealer')
                if drawCardBlackjackVariable == 'Ace' or drawCardBlackjackVariable == 8:
                  slowPrint('\nThe dealer drew an ' + str(drawCardBlackjackVariable) + '.\n')
                else:
                  slowPrint('\nThe dealer drew a ' + str(drawCardBlackjackVariable) + '.\n')
                slowPrint("Dealer's cards: ")
                for cardsInDealerHand in range(len(dealerHandBlackjack)):
                  slowPrint(str(dealerHandBlackjack[cardsInDealerHand])) #The dealer's hand is printed.
                  if cardsInDealerHand != len(dealerHandBlackjack)-1:
                    slowPrint(', ')
                slowPrint('\n')
              
            if sum(dealerHandValuesBlackjackAces1) > 21:
              slowPrint('The dealer went over 21. You win!\n')
              betsWon += 1 #The user wins. 
              blackjackDone = True
              userHandValuesBlackjack = [22] #Exits a loop that is no longer required because the game is finished.
              money += (2*moneyBetBlackjack)
              if money % 1 == 0:
                slowPrint('\nYour new balance is $' + str(int(money)) + '.\n\n')
              elif money % 1 != 0:
                slowPrint('\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
    
            elif sum(dealerHandValuesBlackjackAces1) == finalStandValue or sum(dealerHandValuesBlackjackAces11) == finalStandValue:
              slowPrint('The dealer stands. You and the dealer tied, so you lose the bet.\n')
              betsLost += 1 #The user loses.
              blackjackDone = True
              userHandValuesBlackjack = [22]
              if money % 1 == 0:
                slowPrint('\nYour new balance is $' + str(int(money)) + '.\n\n')
              elif money % 1 != 0:
                slowPrint('\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
              moneyCheck()
    
            elif sum(dealerHandValuesBlackjackAces1) > finalStandValue or sum(dealerHandValuesBlackjackAces11) > finalStandValue:
              slowPrint('The dealer stands. The dealer was closer to 21, so you lose.\n')
              betsLost += 1 #The user loses.
              blackjackDone = True
              userHandValuesBlackjack = [22]
              if money % 1 == 0:
                slowPrint('\nYour new balance is $' + str(int(money)) + '.\n\n')
              elif money % 1 != 0:
                slowPrint('\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
              moneyCheck()
            else:
              slowPrint('This should not happen #35.')
    
          elif userDecisionBlackjack == 3 and insufficientFundsBlackjack == False: #The user doubles down.
            money -= moneyBetBlackjack #The user's money gets reduced once again by the amount they bet.
            drawBlackjackCardVariable = drawCardBlackjack('user')
            if drawBlackjackCardVariable == 'Ace' or drawBlackjackCardVariable == 8:
              slowPrint('\nYou drew an ' + str(drawBlackjackCardVariable) + '.\n')
            else:
              slowPrint('\nYou drew a ' + str(drawBlackjackCardVariable) + '.\n')
            slowPrint('Your cards: ')
            for cardsInHand in range(len(userHandBlackjack)):
              slowPrint(str(userHandBlackjack[cardsInHand]))
              if cardsInHand != len(userHandBlackjack)-1: #The user's full hand is printed.
                slowPrint(', ')
            time.sleep(2)
            slowPrint('\n')

            if sum(userHandValuesBlackjack) > 21: #If the sum of the user's hand exceeds 21.
              slowPrint('You went over 21. The dealer wins.\n')
              betsLost += 1 #The user loses.
              blackjackDone = True
              userHandValuesBlackjack = [22]
              if money % 1 == 0:
                slowPrint('\nYour new balance is $' + str(int(money)) + '.\n\n')
              elif money % 1 != 0:
                slowPrint('\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
              moneyCheck()
            else:
              if 'Ace' in userHandBlackjack:
                if sum(userHandValuesBlackjack)+10 == 21:
                  finalStandValue = 21 #Maximizing the user's points by using the ace.

            if blackjackDone == False: #If the game is still on.

              if 'Ace' in userHandBlackjack: #If the user has an ace.
                if sum(userHandValuesBlackjack)+10 <= 21: #Test if the ace puts them over 21.
                  finalStandValue = sum(userHandValuesBlackjack)+10 #If not, this gets them closer to 21.
                else:
                  finalStandValue = sum(userHandValuesBlackjack)
              else:
                finalStandValue = sum(userHandValuesBlackjack)
              slowPrint("It is the dealer's turn now. He must get equal to or more than " + str(finalStandValue) + " points to win.\n") #The user can only pick up one card after doubling down, so the dealer goes now until they reach 21 or surpass the score of the user.
              
              while sum(dealerHandValuesBlackjackAces1) < finalStandValue and sum(dealerHandValuesBlackjackAces11) < finalStandValue:
                if sum(dealerHandValuesBlackjackAces1) < 21:
                  drawCardBlackjackVariable = drawCardBlackjack('dealer')
                  if drawCardBlackjackVariable == 'Ace' or drawCardBlackjackVariable == 8:
                    slowPrint('\nThe dealer drew an ' + str(drawCardBlackjackVariable) + '.\n')
                  else:
                    slowPrint('\nThe dealer drew a ' + str(drawCardBlackjackVariable) + '.\n')
                  slowPrint("Dealer's cards: ")
                  for cardsInDealerHand in range(len(dealerHandBlackjack)):
                    slowPrint(str(dealerHandBlackjack[cardsInDealerHand])) #Dealer's full hand is printed.
                    if cardsInDealerHand != len(dealerHandBlackjack)-1:
                      slowPrint(', ')
                  slowPrint('\n')
                
              if sum(dealerHandValuesBlackjackAces1) > 21: #If the dealer's cards exceed 21.
                slowPrint('The dealer went over 21. You win!\n')
                betsWon += 1 #The user wins.
                money += moneyBetBlackjack*4
                blackjackDone = True
                userHandValuesBlackjack = [22]
                money += (2*moneyBetBlackjack)
                if money % 1 == 0:
                  slowPrint('\nYour new balance is $' + str(int(money)) + '.\n\n')
                elif money % 1 != 0:
                  slowPrint('\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
      
              elif sum(dealerHandValuesBlackjackAces1) == finalStandValue or sum(dealerHandValuesBlackjackAces11) == finalStandValue: #If the dealer is tied with the user.
                slowPrint('The dealer stands. You and the dealer tied, so you lose the bet.\n')
                betsLost += 1 #The user loses because the dealer was the same off from 21 than the user.
                blackjackDone = True
                userHandValuesBlackjack = [22]
                if money % 1 == 0:
                  slowPrint('\nYour new balance is $' + str(int(money)) + '.\n\n')
                elif money % 1 != 0:
                  slowPrint('\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
                moneyCheck()
      
              elif sum(dealerHandValuesBlackjackAces1) > finalStandValue and sum(dealerHandValuesBlackjackAces1) <= 21: #If the dealer is higher than the user and equal to or under 21.
                slowPrint('The dealer stands. The dealer was closer to 21, so you lose.\n')
                betsLost += 1 #The user loses because the dealer was closer to 21 without going over.
                blackjackDone = True #The game is finished.
                userHandValuesBlackjack = [22]
                if money % 1 == 0:
                  slowPrint('\nYour new balance is $' + str(int(money)) + '.\n\n')
                elif money % 1 != 0:
                  slowPrint('\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
                moneyCheck()

              else:
                slowPrint('This should not happen #37.')
              
          elif userDecisionBlackjack == 3 and insufficientFundsBlackjack == True or userDecisionBlackjack == 4: #The user surrenders.
            slowPrint('You surrendered your hand, and therefore you lose 50% of your bet.\n')
            money += moneyBetBlackjack*0.5 #The user has already lost their bet, so they get 50% back because they surrendered.
            betsLost += 1
            blackjackDone = True
            userHandValuesBlackjack = [22]
            if money % 1 == 0:
              slowPrint('\nYour new balance is $' + str(int(money)) + '.\n\n')
            elif money % 1 != 0:
              slowPrint('\nYour new balance is ${:.2f}'.format(money) + '.\n\n')
            moneyCheck()
    
          else:
            slowPrint('This should not happen #33.')
  
      if blackjackDone == True:
        if yesNoQuestion('Would you like to play Blackjack again? (Y/N): ') == False:
          gameChoiceUserVariable = False #The user can choose another game.
          userHandValuesBlackjack = [22]
          slowPrint('\n')
        else:
          userHandValuesBlackjack = [22] #The user decides to play blackjack again, the while gameChoiceUserVariable == 'Blackjack': loop condition is met again. Everything is reset.

  elif gameChoiceUserVariable == 'Slots': #If the user decides to play slots.
    if yesNoQuestion('Welcome to slots! Are you familiar with this game? (Y/N): ') == False:
      slowPrint('The rules for slots are simple. You bet a certain amount of money, and hope that all 3 slots are the same. This luck-based game requires no skill.\n') #Rules for slots.

    while gameChoiceUserVariable == 'Slots':
      valid = False
      while valid == False:
        if money % 1 == 0:
          slowPrint('\nHow much money are you willing to bet? Your current balance is $' + str(int(money)) + ': $')
        elif money % 1 != 0:
          slowPrint('\nHow much money are you willing to bet? Your current balance is ${:.2f}'.format(money) + ': $')
        else:
          slowPrint('This should not happen #38.')
        moneyBetSlots = input()
        try:
          moneyBetSlots = float(moneyBetSlots)
          if moneyBetSlots > money:
            slowPrint("You don't have that much money! Try to spend inside your limits.")
          elif moneyBetSlots < 0.25:
            slowPrint('Your bet must be above $0.24.') #The minimum bet for slots is cheaper. Other games are $1+ while slots is 25 cents or more.
          else:
            valid = True
            money -= moneyBetSlots
        except:
          slowPrint('Please enter a dollar amount, without units. Decimals are permitted.')

      slotsCherries = 0 #At the start, no items are picked from the slots machine yet. This variable is defined here to be modified later, and so that it resets if the user decides to play slots again right after.
      slotsLucky7 = 0
      slotsBell = 0
      slotsLemon = 0
      slotsGoldCoin = 0
      slowPrint('Press ENTER to spin the machine!\n')
      input() #Program will only continue if the user hits the ENTER key.
      for slotResults in range(3): #There are 3 slots.
        slotRandomNumber = random.randint(1,5) #There are 5 different symbols.
        if slotRandomNumber == 1:
          slowPrint('Cherries')
          slotsCherries += 1
        elif slotRandomNumber == 2:
          slowPrint('Lucky 7')
          slotsLucky7 += 1
        elif slotRandomNumber == 3:
          slowPrint('Bell')
          slotsBell += 1
        elif slotRandomNumber == 4:
          slowPrint('Lemon')
          slotsLemon += 1
        elif slotRandomNumber == 5:
          slowPrint('Gold coin')
          slotsGoldCoin += 1
        if slotResults < 2:
          slowPrint(' | ') #This key separates the items better.
          time.sleep(1) #After each of the first 2 items are printed, there is a one second delay.

      if slotsCherries == 3 or slotsLucky7 == 3 or slotsBell == 3 or slotsLemon == 3 or slotsGoldCoin == 3: #If 3 of the same items are chosen.
        slowPrint('\nYou got 3 of the same items! You win!\n') #User wins.
        money += 25*moneyBetSlots #User gets 24x the amount they bet back, plus the amount they bet. There is a 4% chance of winning.
        betsWon += 1
        slowPrint('You won ${:.2f}'.format(25*moneyBetSlots) + '.\n')
        if money % 1 == 0:
          slowPrint('Your new balance is $' + str(int(money)) + '.\n')
        elif money % 1 != 0:
          slowPrint('Your new balance is ${:.2f}'.format(money) + '.\n')
        else:
          slowPrint('This should not happen #38.')
      else: #The user loses.
        slowPrint('\nYou did not get 3 matching items. You lose.\n')
        slowPrint('\nYou lost ${:.2f}'.format(moneyBetSlots) + '.\n')
        betsLost += 1
        if money % 1 == 0:
          slowPrint('Your new balance is $' + str(int(money)) + '.\n')
        elif money % 1 != 0:
          slowPrint('Your new balance is ${:.2f}'.format(money) + '.\n')
        else:
          slowPrint('This should not happen #39.')
        moneyCheck()

      if yesNoQuestion('Would you like to play slots again? (Y/N): ') == False:
        slowPrint('\n')
        gameChoiceUserVariable = False #User chooses another game. If true, slots is played again.

  elif gameChoiceUserVariable == 'NHL betting':
    if yesNoQuestion('Welcome to NHL betting! Are you familiar with this game? (Y/N): ') == False:
      slowPrint('Your goal is to pick an NHL game, and guess which team will win the game. Better teams have better odds of winning the game, and guessing an underdog team will result in a higher payout if they win.\n') #Description for NHL betting.

    powerScoresNHL = {'Vegas Golden Knights': 61.264, 'Montreal Canadiens': 56.564, 'Colorado Avalanche': 56.36, 'Tampa Bay Lightning': 54.975, 'Minnesota Wild': 53.412, 'Carolina Hurricanes': 52.958, 'Boston Bruins': 52.94, 'St. Louis Blues': 52.614, 'New York Islanders': 52.454, 'Toronto Maple Leafs': 52.298, 'Dallas Stars': 51.65, 'Philadelphia Flyers': 51.476, 'Washington Capitals': 51.172, 'Nashville Predators': 50.683, 'Los Angeles Kings': 49.445, 'Edmonton Oilers': 49.412, 'Pittsburgh Penguins': 49.411, 'Calgary Flames': 49.349, 'Chicago Blackhawks': 	48.983, 'Columbus Blue Jackets': 48.844, 'Arizona Coyotes': 47.765, 'Vancouver Canucks': 47.563, 'New Jersey Devils': 46.968, 'Winnipeg Jets': 46.825, 'San Jose Sharks': 46.597, 'New York Rangers': 46.533, 'Florida Panthers': 46.33, 'Buffalo Sabres': 46.167, 'Ottawa Senators': 46.158, 'Anaheim Ducks': 44.695, 'Detroit Red Wings': 38.135} #All NHL teams with their respective power scores. The higher the score, the more likely they are to win the game.

    while gameChoiceUserVariable == 'NHL betting':
      NHLGameTeams = [0,0] #Two items must be in the list before the following line is ran to prevent index error. These two items will be modified in the next few lines.
      while NHLGameTeams[0] == NHLGameTeams[1]: #A team cannot play against themselves.
        NHLGameTeams[0] = (random.choice(list(powerScoresNHL.keys()))) #A random team is selected. This is the home team
        NHLGameTeams[1] = (random.choice(list(powerScoresNHL.keys()))) #This is the away team.
      slowPrint('\nTonight, the ' + NHLGameTeams[0] + ' play at home against the ' + NHLGameTeams[1] + '.\n')
      homeOdds = 1-(0.005*(25-0.2*((powerScoresNHL[NHLGameTeams[0]]/powerScoresNHL[NHLGameTeams[1]]*50*(2147/2002))-50)))+(powerScoresNHL[NHLGameTeams[0]]/powerScoresNHL[NHLGameTeams[1]]*50*(2147/2002)) #Odds of the home team winning, in percent chance.
      awayOdds = 100-homeOdds #Odds of the away team winning, in percent chance.
      userGuessNHL = multipleChoices('Which team would you like to bet on?\n',NHLGameTeams[0] + ' (' + str(round(homeOdds,2)) + '%)',NHLGameTeams[1] + ' (' + str(round(awayOdds,2)) + '%)',False,False,False,False,False,False,False,False)

      valid = False
      while valid == False:
        if money % 1 == 0:
          slowPrint('\nHow much money are you willing to bet? Your current balance is $' + str(int(money)) + ': $')
        elif money % 1 != 0:
          slowPrint('\nHow much money are you willing to bet? Your current balance is ${:.2f}'.format(money) + ': $')
        else:
          slowPrint('This should not happen #39.')
        moneyBetNHL = input()
        try:
          moneyBetNHL = float(moneyBetNHL)
          if moneyBetNHL > money:
            slowPrint("You don't have that much money! Try to spend inside your limits.")
          elif moneyBetNHL < 0.5:
            slowPrint('Your bet must be above $0.49')
          else:
            money -= moneyBetNHL
            valid = True
        except:
          slowPrint('Please enter a dollar amount, without units. Decimals are permitted.')

      randomNumberNHLGame = random.randint(1,10000)/100
      if randomNumberNHLGame <= homeOdds:
        homeGoals = distributionCurveProbability(1,12,1.07,3.5,37284) #Goals scored by home team.
        awayGoals = distributionCurveProbability(0,int(homeGoals)-1,1.07,2.5,37284) #Goals scored by away team
        slowPrint('The ' + NHLGameTeams[0] + ' won the game ' + str(int(homeGoals))+ '-' + str(int(awayGoals)) + '.\n') #Home team wins. Score is also displayed.
        if userGuessNHL == 1:
          money += moneyBetNHL*(100/homeOdds)
          betsWon += 1 #User guessed correctly.
          slowPrint('You guessed right! ')
        else:
          betsLost += 1 #User guessed incorrectly.
          slowPrint('You lost the bet. ')
      else:
        homeGoals = distributionCurveProbability(1,12,1.07,3.5,37284)
        awayGoals = distributionCurveProbability(0,int(homeGoals)-1,1.07,2.5,37284)
        slowPrint('The ' + NHLGameTeams[1] + ' won the game ' + str(int(homeGoals))+ '-' + str(int(awayGoals)) + '.\n')
        if userGuessNHL == 2:
          money += moneyBetNHL*(100/awayOdds)
          betsWon += 1
          slowPrint('You guessed right! ')
        else:
          betsLost += 1
          slowPrint('You lost the bet. ')
      if money % 1 == 0:
        slowPrint('Your new balance is $' + str(int(money)) + '\n\n')
      elif money % 1 != 0:
        slowPrint('Your new balance is ${:.2f}'.format(money) + '\n\n')
      moneyCheck()

      if yesNoQuestion('Would you like to bet on another NHL game? (Y/N): ') == False:
        gameChoiceUserVariable = False #If true, another game will be selected and the user can bet on it. If false, the user selects another place to gamble.
    
  elif gameChoiceUserVariable == 'Leave casino': #If the user wants to quit the game / leave the casino with their earnings.
    if yesNoQuestion('Are you sure you would like to leave the casino? (Y/N): ') == True:
      if money % 1 == 0:
        slowPrint('\nYou left the casino with $' + str(int(money)) + ', which is a percentage increase of ' + str(round((money - 100000) / 100000 * 100,2)) + '%.\nFarewell!\n') #Final balance and percentage increase is displayed before they leave.
      elif money % 1 != 0:
        slowPrint('\nYou left the casino with ${:.2f}'.format(money) + ', which is a percentage increase of ' + str(round((money - 100000) / 100000 * 100,2)) + '%.\nFarewell!\n')
      inCasino = False #The program ends.
    else:
      gameChoiceUserVariable = ''

  elif gameChoiceUserVariable == 'Quit': #Alternative of quitting the game, where the sign off has already been printed. This can only occur if the user opens the menu from the game selection screen.
    inCasino = False
