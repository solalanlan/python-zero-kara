#問題1

a=int(input("aの値を入力してください: "))
b=int(input("bの値を入力してください: "))
c=int(input("cの値を入力してください: "))

print(a==b)
print(a!=b)
print(c>b)
print(a<=b)
print(c>=b)

print('---')

#問題2
a=int(input("aの値を入力してください: "))
if a%3==0:
    print("3で割り切れます")
else:
    print("3で割り切れません")

print('---')

#問題3-1
total=0
for i in range(10,21):
    total+=i
    print(total)    

print('---')

total=0
i=10
while i<=20:
    total+=i
    print(total)    
    i+=1

#問題5
scores=[65,80,40,92,76,52]
count=0
for score in scores:
    if score>=60:
        count+=1
        print(f'{score}点は合格です。')
    else:
        print(f'{score}点は不合格です。')
print(count)