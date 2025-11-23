import random

answer = random.randint(1 , 100)
print("1~100の数をあててね！")

count = 0

while True:
    guess = int(input("あなたの予想は："))
    count += 1

    if guess > answer:
        print("もっと小さいよ")
    elif guess < answer:
        print("もっと大きいよ")
    else:
        print(f"正解！{count}回で当たったよ")
        break