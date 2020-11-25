n = int(input())
if (n % 4 != 0):
    print("NO")
elif (n % 4 == 0) & (n % 100 != 0):
    print("YES")
elif (n % 100 == 0) & (n % 400 != 0):
    print("NO")
else:
    print("YES")
