import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

wanna_play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
player = []
dealer = []


def DealCard(ans):
    global next_dealer, next_res
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    if ans == 'y':
        print(logo)
        player_card = random.choice(cards)
        dealer_card = random.choice(cards)

        player.append(player_card)
        dealer.append(dealer_card)

        player_result = sum(player)
        dealer_result = sum(dealer)

        print(f'Your cards is {player} your current score is: {player_result}')
        print(f'Computer first card is {dealer_result}')

        take_answer = True

        while take_answer:
            take_another = input("Type 'y' to take another card and type 'n' to pass ")
            if take_another == 'y':
                player_another_card = random.choice(cards)
                player.append(player_another_card)
                next_res = sum(player)
                dealer.append(dealer_card)
                next_dealer = sum(dealer)
                print(f'You current score is: {next_res} \n Want to take another card?')

                if next_res > 21 >= next_dealer:
                    take_answer = False
                    print(f'You have too much:{next_res} Computer is the winner  with score: {next_dealer}')

                elif next_dealer > 21 >= next_res:
                    take_answer = False
                    print(f'Computer have too much {next_dealer}! You win! With result: {next_res}!')

                elif next_dealer == 21:
                    take_answer = False
                    print(f'You lose:{next_res} Computer is the winner  with score: {next_dealer}!')

                elif next_res == 21:
                    take_answer = False
                    print(f'You lose:{next_dealer} Human is the winner  with score: {next_res}!')

                elif next_res > 21:
                    take_answer = False
                    print(f'You lose with score {next_res} and your opponent score is: {next_dealer}')

                elif next_dealer > 21:
                    take_answer = False
                    print(f'You lose with score {next_dealer} and your opponent score is: {next_res}')

                elif next_dealer > 21 and next_res > 21:
                    if next_dealer > next_res:
                        take_answer = False
                        print(f'Winner is {next_res}.Computer score is: {next_dealer}')

                elif next_dealer > 21 and next_res > 21:
                    if next_dealer < next_res:
                        take_answer = False
                        print(f'Winner is {next_dealer}.Human score is: {next_res}')

                elif next_res <= 21 and next_res == next_dealer and next_dealer <= 21:
                    take_answer = False
                    print(f'You have DRAW! With result: {next_res} and {next_dealer}!')


            elif take_another == 'n':
                take_answer = False
                if 21 >= next_dealer > next_res:
                    print(f'You lose dude:{next_res} Computer is the winner  with score: {next_dealer}!')

                elif 21 >= next_res > next_dealer:
                    print(f'You lose robot:{next_dealer} Human is the winner  with score: {next_res}!')

                elif next_res <= 21 and next_res == next_dealer and next_dealer <= 21:
                    print(f'You have DRAW! With result: {next_res} and {next_dealer}!')


DealCard(wanna_play)