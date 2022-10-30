x, y = map(input().split())

y = int(y)

if x == "OCT":
    if y == 31:
        print("yup")
    else:
        print("nope")
elif x == "DEC":
    if y == 25:
        print("yup")
    else:
        print("nope")
else:
    print("nope")


