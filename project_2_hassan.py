# paper scissor stone game

def winner_pss(score1, score2):
    if score1 > score2:
        print('user1 is winner')
    elif score1 > score2:
        print('user2 is winner')
    else:
        print('tie!')

def pss_game():
    user1_count = 0
    user2_count = 0
    for item in range (0,2):
        user1 = input('User 1:\n wirte paper, stone or scissor :')
        user2 = input('User 2:\n wirte paper, stone or scissor :')
        if user1.upper() == user2.upper():
            user1_count += 1
            user2_count += 1
        elif user1.upper() =='PAPER' and user2.upper() =="STONE":
            user1_count += 1
        elif user1.upper() =='PAPER' and user2.upper() =="SCISSOR":
            user2_count += 1
        elif user1.upper() =='STONE' and user2.upper() =="SCISSOR":
            user1_count += 1
    winner_pss(user1_count,user2_count)

pss_game()