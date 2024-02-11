import random

print("ヌメロンを始めます。")
#答えを生成する関数
def generate_answer():
    return [random.randint(0, 9) for _ in range(6)]

#ユーザーから3桁の数字を取得する関数
def get_user_input():
    while True:
        usernum = input("6桁の数字を入力してください>>>")
        if len(usernum) != 6:
            print("6桁の数字以外の数字が入力されました。6桁の数字を入力してください")
        else:
            valid = True
            for i in range(6):
                if not usernum[i].isdigit():
                    print("数字ではありません")
                    valid = False
                    break
            if valid:
                break
    return usernum

#EATの数を数える関数
def count_eat(answer, usernum):
    eat = 0
    for i in range(6):
        if answer[i] == int(usernum[i]):
            eat += 1
    return eat

#BITEの数を数える関数
def count_bite(answer, usernum):
    bite = 0
    for i in range(6):
        for j in range(6):
            if (int(usernum[i]) == answer[j] and int(usernum[i]) != answer[i] and int(usernum[j]) != answer[i]):
                bite += 1
    return bite

#ゲームをプレイする関数
def play_game():
    # 答えの生成
    answer = generate_answer()

    while True:
        # ユーザーの数字入力
        usernum = get_user_input()

        # EATとBITEの数を計算
        eat = count_eat(answer, usernum)
        bite = count_bite(answer, usernum)

        # 結果の出力
        print("EAT:", eat)
        print("BITE:", bite)

        # eatが3の場合、おめでとうメッセージを表示
        if eat == 6:
            print("おめでとうございます！")

        # プレイを続けるかどうかを尋ねる
        choice = input("ゲームを続けますか？(1: 続ける, 2: やめる)>>> ")
        if choice == '2':
            print("答えは", ''.join(map(str, answer)) + " でした!")
            break

if __name__ == "__main__":
    play_game()
