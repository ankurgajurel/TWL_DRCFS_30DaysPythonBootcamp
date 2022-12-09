arr = [3, 5, 15, 30]

for i in arr:
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        # print(i)
    elif i % 3 == 0:
        print("fizz")
        # pass
    elif i % 5 == 0:
        print("buzz")
        # pass
    else:
        print(i)
        # pass