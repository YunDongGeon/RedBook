# 문서를 읽어 저장 배열 생성
array = []
count = 0
# 문서 읽어 들이기
f = open("python.txt", 'rt', encoding='UTF8')
# 문서 얽고 변수에 저장
gi = f.read()
# 변수에 저장한 읽은 파일을 공백을 기준으로 잘라서 배열에 각각 저장
array = gi.split(' ')
# 베열에 저장되어 있는 내용을 확인차 출력
n = len(array)
print("배열 안의 단어 개수 :", n)
for i in range(n):
    for j in range(len(array[i])// 2):
        if array[i][j] != array[i][-1-j]:
            isPalindrome = False
        else:
            isPalindrome = True
            count += 1
            print(isPalindrome, "array[",i,"]", array[i])
print(n,"개의 단어들 중 회문은" ,count, "개 입니다.")
