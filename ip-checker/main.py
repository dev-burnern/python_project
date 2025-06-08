import socket  # 소켓을 사용하여 IP 주소를 확인하기 위한 모듈
import requests  # HTTPS를 사용하기 위한 requests 모듈
# import re  # 정규 표현식을 사용하기 위한 re 모듈

input_addr = input("IP 주소를 입력하세요: ")  # 사용자로부터 IP 주소 입력 받기

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 주소를 사용하기 위한 소켓 생성
# in_addr.connect((input_addr, 443))  # 구글 서버에 연결하여 IP 주소를 확인
in_addr.connect(('www.google.co.kr', 443))  # 구글 서버에 연결하여 IP 주소를 확인
print("내부 IP 주소:", in_addr.getsockname()[0])  # 연결된 소켓의 IP 주소 출력

req = requests.get('https://api.ipify.org')  # 외부 IP 주소를 확인하기 위한 API 요청

# out_addr = re.search(r'IP Address: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]  # 정규 표현식을 사용하여 IP 주소 추출
# print("외부 IP 주소:", out_addr)  # 추출한 외부 IP 주소 출력

out_addr = req.text.strip()
print("외부 IP 주소:", out_addr)