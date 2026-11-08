"""Exact check of prime-polynomial unit classification over F_2[t]."""
from math import gcd

def rem(a,b):
    while a and a.bit_length()>=b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

def pgcd(a,b):
    while b:
        a,b=b,rem(a,b)
    return a

def irreducible(a):
    if a<2:return False
    d=a.bit_length()-1
    for e in range(1,d//2+1):
        for p in range(1<<e,1<<(e+1)):
            if rem(a,p)==0:return False
    return True

def product_small(n):
    k=(n-1)//2
    p=1
    for d in range(1,k+1):
        for x in range(1<<d,1<<(d+1)):
            if irreducible(x):
                z=0
                while x:
                    bit=x&-x
                    z^=p<<(bit.bit_length()-1)
                    x-=bit
                p=z
    return p

for n in range(1,11):
    Q=product_small(n)
    predicted=[]
    actual=[]
    for f in range(1<<n,1<<(n+1)):
        if rem(f,Q)==0:predicted.append(f)
        if n<=8 and all((x==1 or irreducible(x)) for x in range(1,1<<n) if pgcd(x,f)==1):
            actual.append(f)
    if n<=8: assert predicted==actual,(n,predicted,actual)
    print('degree',n,'sieve_degree',Q.bit_length()-1,'predicted_count',len(predicted),'verified',n<=8)
assert sum(len([f for f in range(1<<n,1<<(n+1)) if rem(f,product_small(n))==0]) for n in range(1,7))==18
expected = {1:[1,1], 2:[1,2,2,3], 3:[2,2], 4:[3,4,4,4], 5:[6,6], 6:[12,12,12,12]}
for n in range(1,7):
    fs=[f for f in range(1<<n, 1<<(n+1)) if rem(f,product_small(n))==0]
    orders=sorted(sum(pgcd(x,f)==1 for x in range(1,1<<n)) for f in fs)
    assert orders == expected[n], (n, orders)
print('CHECKED_GROUP_ORDER_DISTRIBUTION', expected)
print('VERIFY_OK')
