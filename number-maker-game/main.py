import random

random_number = random.randint(1, 100)  # 랜덤 넘버 생성 변수

game_count = 1 # 게임 카운트 변수

# 무한 반복
while True:
    try:
        my_number = int(input("1과 100 사이의 숫자를 입력하세요: "))
        
        # 조건 작성
        if my_number > random_number:
            print("다운")
        elif my_number < random_number:
            print("업")
        else:
            print(f"축하합니다! {game_count}번 만에 맞추셨습니다.")
            break
        
        game_count += 1  # 게임 카운트 증가

    except ValueError:
        print("유효한 숫자를 입력하세요.") # 예외 처리
