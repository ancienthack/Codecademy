import random

money = 50

#Write your game of chance functions here

# def coin_flip(guess, bet):
#     if bet <= 0:
#         print('You must make a bet above 0.')
#         return 0
#     elif bet > money:
#         print('You don\'t have enough for that bet.')
#         return 0

#     print('Let\'s flip! You chose ' + guess + '.')
#     result = random.randint(1,2)

#     if result == 1:
#         print('Heads!')
#     elif result == 2:
#         print('Tails!')

#     if (guess == 'Heads' and result == 1) or (guess == 'Tails' and result == 2):
#         print('Congratulations! You won ' + str(bet) + ' dollars!')
#         return bet
#     else:
#         print('Sorry. You lost ' + str(bet) + ' dollars.')
#         return -bet

# def cho_han(guess, bet):
#     if bet <= 0:
#         print('You must make a bet above 0.')
#         return 0
#     elif bet > money:
#         print('You don\'t have enough for that bet.')
#         return 0

#     print('Let\'s roll! You chose ' + guess + '.')
#     d1 = random.randint(1,6)
#     d2 = random.randint(1,6)
#     d_total = d1 + d2

#     if d_total % 2 == 0:
#         print(str(d_total) + ' is Even!')
#     elif d_total % 2 != 0:
#         print(str(d_total) + ' is Odd!')

#     if (guess == 'Even' and d_total % 2 == 0) or (guess == 'Odd' and d_total % 2 != 0):
#         print('You won ' + str(bet) + ' dollars!')
#         return bet
#     else:
#         print('You lost ' + str(bet) + ' dollars!')
#         return -bet

# def war(bet):
#     if bet <= 0:
#         print('You must make a bet above 0.')
#         return 0
#     elif bet > money:
#         print('You don\'t have enough for that bet.')
#         return 0

#     print('The bet is ' + str(bet) + ' each.')
#     print('Each of you draw a card.')
#     deck_of_cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
#     result_one = random.choice(deck_of_cards)
#     deck_of_cards.remove(result_one)
#     result_two = random.choice(deck_of_cards)
#     deck_of_cards.remove(result_two)

#     if result_one == 1:
#         print('You pulled an Ace.')
#     elif result_one == 11:
#         print('You pulled a Jack.')
#     elif result_one == 12:
#         print('You pulled a Queen.')
#     elif result_one == 13:
#         print('You pulled a King.')
#     else:
#         print('You pulled a ' + str(result_one) + '.')

#     if result_two == 1:
#         print('You\'re opponent pulled an Ace.')
#     elif result_two == 11:
#         print('You\'re opponent pulled a Jack.')
#     elif result_two == 12:
#         print('You\'re opponent pulled a Queen.')
#     elif result_two == 13:
#         print('You\'re opponent pulled a King.')
#     else:
#         print('You\'re opponent pulled a ' + str(result_two) + '.')

#     if result_one > result_two:
#         print('You win! Here is your ' + str(bet) + ' dollars.')
#         return bet
#     elif result_one < result_two:
#         print('Your opponent wins ' + str(bet) + ' dollars!')
#         return -bet
#     else:
#         print('A tie! Bets returned!')
#         return 0

def roulette(guess, bet):
    if bet <= 0:
        print('You must make a bet above 0.')
        return 0
    elif bet > money:
        print('You don\'t have enough for that bet.')
        return 0

    print('Let\'s play roulette!')
    print('You have put ' + str(bet) + ' dollars on ' + guess + '.')
    result = random.randint(0, 37)

    if result == 37:
        print('The ball landed on 00.')
    else:
        print('The ball landed on ' + str(result) + '.')

    if guess == 'Even' and result%2 == 0 and result != 0 and result != 37:
        print(str(result) + ' is even! You win ' + str(bet) + ' dollars.')
        return bet
    elif guess == 'Odd' and result%2 == 1 and result != 0 and result != 37:
        print(str(result) + ' is odd! You win ' + str(bet) + ' dollars.')
        return bet
    elif guess == 'Low' and result <= 18 and result != 0 and result != 37:
        print(str(result) + ' is low! You win ' + str(bet) + ' dollars.')
        return bet
    elif guess == 'High' and result >= 19 and result != 0 and result != 37:
        print(str(result) + ' is high! You win ' + str(bet) + ' dollars.')
        return bet
    elif guess == str(result):
        print(str(result) + ' matches your guess of ' + str(guess) + '! You win ' + str(bet) + ' dollars.')
        return bet*35
    else:
        print(str(result) + ' doesn\'t match your guess. Sorry, you lose.')
        return -bet

#Call your game of chance functions here

# coin_guess = input('Heads or Tails?')
# while coin_guess != 'Heads' and coin_guess != 'Tails':
#     coin_guess = input('Heads or Tails?')
#     if coin_guess == 'Heads' or coin_guess == 'Tails':
#         break
# coin_bet = int(input('The bet?'))
# money += coin_flip(coin_guess, coin_bet)
# print(money)

# dice_guess = input('Even or Odd?')
# while dice_guess != 'Even' and dice_guess != 'Odd':
#     coin_guess = input('Even or Odd?')
#     if coin_guess == 'Even' or coin_guess == 'Odd':
#         break
# dice_bet = int(input('The bet?'))
# money += cho_han(dice_guess, dice_bet)
# print(money)

# war_bet = int(input('War it is. The bets?'))
# money += war(war_bet)
# print(money)

roulette_guess = ''
while roulette_guess != 'Even' and roulette_guess != 'Odd' and roulette_guess != 'High' and roulette_guess != 'Low' and roulette_guess != 'Straight':
    roulette_guess = input('Even, Odd? High, Low? Or call it Straight?')
    if roulette_guess == 'Straight':
        roulette_guess = input('Pick a number between 0 and 37.')
        while int(roulette_guess) < 0 or int(roulette_guess) > 37:
            roulette_guess = input('Pick a number between 0 and 37.')
            if int(roulette_guess) >= 0 and int(roulette_guess) <= 37:
                break
    if roulette_guess == 'Even' or roulette_guess == 'Odd' or roulette_guess == 'High' or roulette_guess == 'Low':
        break
# if roulette_guess == 'Straight':
#         roulette_guess = input('Pick a number between 0 and 37.')
#         while int(roulette_guess) < 0 or int(roulette_guess) > 37:
#             roulette_guess = input('Pick a number between 0 and 37.')
#             if int(roulette_guess) >= 0 and int(roulette_guess) <= 37:
#                 break
roulette_bet = int(input('The bet?'))
money += roulette(roulette_guess, roulette_bet)
print(money)