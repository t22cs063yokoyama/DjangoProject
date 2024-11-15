import random

def janken():
    hands = ["グー", "チョキ", "パー"]
    
    # プレイヤーの手をランダムに選択
    player_hand = random.randint(0, 2)
    
    # コンピューターの手をランダムに選択
    computer_hand = random.randint(0, 2)
    
    print("プレイヤーの手: ", hands[player_hand])
    print("コンピューターの手: ", hands[computer_hand])
    
    # 勝敗判定
    if player_hand == computer_hand:
        print("引き分けです！")
    elif (player_hand == 0 and computer_hand == 1) or (player_hand == 1 and computer_hand == 2) or (player_hand == 2 and computer_hand == 0):
        print("プレイヤーの勝ちです！")
    else:
        print("コンピューターの勝ちです！")

# じゃんけんを実行
janken()
