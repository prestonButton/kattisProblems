x = "Knuth-Morris-Pratt"

testChar = "-"

result = []

result.append(x[0]) 

y=1

while y<len(x):
    if y == testChar:
        result.append(x[y])
        y+=1
    else:
        y+=1


for a in result:
    print(result[a])