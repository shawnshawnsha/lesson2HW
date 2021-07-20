math = input('數學成績')
math = int(math)
eng = input('英文成績')
eng = int(eng)

if math >= 90 and eng >= 90:
    print('有獎學金')
elif math == 100 or eng == 100:
    print('有獎學金')
else:
    print('沒獎學金')