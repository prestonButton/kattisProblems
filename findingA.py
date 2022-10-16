def myfunction(y):
    if str[y] == "a":
        print(str[y:])
    else:
        y += 1
        myfunction(y)

y = 0
str = input()

myfunction(y)


