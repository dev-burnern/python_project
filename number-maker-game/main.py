import random

# 무한 반복
def play_game():
    random_number = random.randint(1, 100)  # 랜덤 넘버 생성 변수
    game_count = 1  # 게임 카운트 변수
    
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

# 게임 시작
if __name__ == "__main__":
    print("1과 100 사이의 숫자를 맞추는 게임입니다.")
    play_game()
    print("게임을 종료합니다.")