import cmath
import random
import init
init.Ini()

'''
a = float(input( ))
b = float(input( ))
a = cmath.sqrt(a)
b = cmath.sqrt(b)
print("a = {:.2f}, b = {:.1f}".format(a, b))

a = random.randint(2, 4)
b = random.randint(2,10000)
print("{:} {:}".format(a, b))

a = int(input())
b = int(input())
c = a**b
d = a%b
print('哈哈哈是 %d, 嘿嘿嘿是 %d' %(c, d))

a = input()
if init.Is_num(a)==True:
    print("这是一个数字")
else :
    print("这不是一个数字")

a = int(input())
ans = 1
for i in range(1,a+1):
    ans *= i
print("{:}".format(ans))

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}\t".format(i, j, i*j), end='')
    print()


class One():

    a = ''

    def __init__(self, aa):

        self.a = aa

    def yaya(self):
        print("%s" %(self.a))


name = input()
a = One(name)
a.yaya()

'''


A = [x ** 2 for x in range(a, b+1)]
b = 12