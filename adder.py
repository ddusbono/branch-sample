def add_numbers(num1, num2):
    """
    두 개의 숫자를 받아 그 합계를 반환하는 함수.
    """
    # 두 숫자를 더하여 결과를 반환합니다.
    return num1 + num2

# --- 함수 사용 예시 ---

# 1. 정수형 숫자 더하기
result_int = add_numbers(10, 5)
print(f"10 + 5 = {result_int}") # 출력: 10 + 5 = 15

# 2. 실수형 숫자 더하기
result_float = add_numbers(3.5, 2.1)
print(f"3.5 + 2.1 = {result_float}") # 출력: 3.5 + 2.1 = 5.6
