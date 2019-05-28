#  회문을 구분하는 매크로
def isPalindrome (string):
    return string[::-1] == string

# 문서를 읽어 저장할 배열 생성
array = []
count = 0
# 문서 읽어 들이기
f = open("gg.txt", 'rt', encoding='UTF8')
# 문서 얽고 변수에 저장
gi = f.read()

# 변수에 저장한 읽은 파일을 공백을 기준으로 잘라서 배열에 각각 저장
array = gi.split(' ')

# 베열에 저장되어 있는 내용을 확인차 출력
print(array)
# print(gi)

# 포문을 이용하여 배열에 들어있는 원소들을 위에 회문 구분하는 매크로로
# 회문을 구분하고 회문이면 True 회문이 아니면 False로 리턴을 받는다.
for array in array:
    # 조건문을 이용하여 매크로에서 회문으로 판별하여 True가 넘어오면
    # count변수에 +1을 하여 문서내의 회문이 몇개인지 카운팅한다.
    if isPalindrome(array) == True:
        count += 1
    # print(isPalindrome(array))

# 카운트한 회문의 갯수를 출력
print('문서내의 회문의 갯수는 총', count, '개 입니다.')
