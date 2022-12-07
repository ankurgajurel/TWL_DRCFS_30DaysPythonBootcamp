'''
divisible by 3 then display fizz
divisible by 5 then display buzz
divisible by 3 and 5 both, display fizzbuzz
divisible by none then display the number
'''

#solution 

for i in range(20):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        # print(i)
    elif i % 3 == 0:
        print("fizz")
        pass
    elif i % 5 == 0:
        print("buzz")
        pass
    else:
        print(i)
        pass