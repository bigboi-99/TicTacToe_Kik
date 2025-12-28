import random

box = [" "," "," "," "," "," "," "," "," "]
empty_area = [0,1,2,3,4,5,6,7,8]
move_count = 0
winner_type = ""

game_end = False

def play_area ():
    print(" " + box[0] + " | " +  box[1] + " | " + box[2] + " ")
    print("---+---+---")
    print(" " + box[3] + " | " + box[4] + " | " + box[5] + " ")
    print("---+---+---")
    print(" " + box[6] + " | " + box[7] + " | " + box[8] + " ")

def check_winner():
    global game_end
    global winner_type

    if box[0]==box[1]==box[2]!=" ":
        game_end = True
        winner_type = box[0]
    elif box[3]==box[4]==box[5]!=" ":
        game_end = True
        winner_type = box[3]
    elif box[6]==box[7]==box[8]!=" ":
        game_end = True
        winner_type = box[6]
    elif box[0]==box[4]==box[8]!=" ":
        game_end = True
        winner_type = box[0]
    elif box[2]==box[4]==box[6]!=" ":
        game_end = True
        winner_type = box[2]
    elif box[0]==box[3]==box[6]!=" ":
        game_end = True
        winner_type = box[0]
    elif box[1]==box[4]==box[7]!=" ":
        game_end = True
        winner_type = box[1]
    elif box[2]==box[5]==box[8]!=" ":
        game_end = True
        winner_type = box[2]
    elif move_count == 9:
        game_end = True
        winner_type = "draw"

turn_who = 1

def player_1():
    pos_1 = random.choice(empty_area)
    empty_area.remove(pos_1)
    box[pos_1] = "O"
    global move_count
    move_count += 1

def player_2():
    pos_2 = random.choice(empty_area)
    empty_area.remove(pos_2)
    box[pos_2] = "X"
    global move_count
    move_count += 1


while not(game_end):
    if turn_who == 1:
        player_1()
        print("Turn " + str(move_count) + ". Player 1 plays.")
        play_area()
        check_winner()
        turn_who = 2
    elif turn_who == 2:
        player_2()
        print("Turn " + str(move_count) + ". Player 2 plays.")
        play_area()
        check_winner()
        turn_who = 1

print("Game has Ended on turn " + str(move_count) + ".")

if winner_type=="O":
    print("Player 1 wins.")
elif winner_type=="X":
    print("Player 2 wins")
elif winner_type=="draw":
    print("It was a draw.")