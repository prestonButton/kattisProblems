r1, s = map(int, input().split())

if r1<0:
    if r1<=s:
        r2 = s+(s-r1)
    else:
        r2 = s-(r1-s)
else:
    r2 = (s*2)-r1

print(r2)
