def get_string(msg):
    while True:
        # 공백 제거한 문자 input (입력 행위는 항상 True, 입력 무한 반복)
        value = input(msg).strip()

        if value:        # value에 값이 있으면 (value = True)
            return value # 입력된 value 반환하고 무한 반복 탈출 (함수 탈출)

        # value에 값이 없으면 (value = False) 원래대로 입력 무한 반복
        print('[경고] 입력값이 없습니다. 정확한 정보를 입력하세요.')            

def get_int(num, error_msg='[경고] 공백 없이 숫자(정수)만 입력하세요.'):
    while True:

        try:
            value = int(input(num)) # 숫자(정수) input
            return value            # 반환하고 무한 반복 탈출 (함수 탈출)

        except ValueError:          # 숫자(정수) 아닌 값 input
            print(error_msg)        # 중단 없이 오류 알림, 입력 무한 반복