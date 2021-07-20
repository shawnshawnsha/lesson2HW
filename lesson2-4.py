math = input('數學成績')
math = int(math)
eng = input('英文成績')
eng = int(eng)

if math > 90 and eng > 90:
    print('有獎品')
elif math == 60 or eng == 60:
    print('再加油')
else:
    print('要處罰')