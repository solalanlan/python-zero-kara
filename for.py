for i in [10,20,30,40,50]:
    print(i)

for i in range(10):
    print(i)

print(list(range(1,10)))

for i in range(1,10):
    print(i)

print('---')

for i in range(1,10):
    i = i * 7
    print(i)

for i in range(7,64,7):
    print(i)

total=0
for i in range(10):
    total+=i
    print(total)    
    if total>20:
        break

print('---')

total=0
for i in range(1,20):
    if i%3 >= 1:
        continue
    print(i)
    total+=i

print('---')

for a in range(1,4):
    print('a=',a)
    for b in range(1,4):
        print('    b=',b)