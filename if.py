age=(int(input("年齢を入力してください: ")))

print('---')

if age<18:
    print('まだ選挙権はありません。')
    print('18歳になったら選挙に行きましょう。')

else:
    print('選挙に行けます。')
    print('投票を忘れずに行きましょう。')      

print('プログラムを終了します。')    

print('---')

if age<4:
    print('入場料は無料です。')
elif age<13:
    print('子ども料金で入場できます。')
else:
    print('大人料金で入場できます。')    

print('---')

if age<13 or age>=65:
    print('入場料は無料です。')
else:
    print('入場料が必要です。')