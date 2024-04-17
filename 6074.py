'''
영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
'''

n = ord(input())
p = 'a'
while ord(p)<=n:
    print(p,end=' ')
    p = ord(p)
    if p<n:
        p = chr(p+1)