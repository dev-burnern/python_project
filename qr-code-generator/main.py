# QR 코드 생성기
import qrcode

file_path = r'qr-code-generator/qr_code.txt'  # QR 코드 이미지 파일 경로
with open(file_path, 'rt', encoding='utf-8') as f:
    read_lines = f.readlines()  # 파일에서 줄 단위로 읽기
    
    for line in read_lines:
        line = line.strip()
        print(line)  # 읽은 줄 출력
        
        qr_data = line  # QR 코드에 저장할 데이터
        qr_img = qrcode.make(qr_data)  # QR 코드 생성

        # 파일명에 사용할 수 없는 문자 제거
        safe_line = ''.join(c for c in line if c not in '\/:*?"<>|')
        save_path = f'qr-code-generator/{safe_line}.png'  # QR 코드 이미지 저장 경로
        qr_img.save(save_path)  # QR 코드 이미지 저장