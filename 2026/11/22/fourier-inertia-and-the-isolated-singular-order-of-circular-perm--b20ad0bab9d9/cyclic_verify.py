"""Independent exact-integer finite checks for circular-successions Walsh convolution.
Run: python cyclic_verify.py. Finite checks are supplementary to the all-order proof.
"""
from itertools import permutations
from math import comb, factorial
from fractions import Fraction

checks=0

def check(test, why):
    global checks
    checks+=1
    if not test:
        raise AssertionError(why)

def closed(n,k):
    assert 2<=n and 0<=k<=n
    return sum(comb(k,j)*(-2)**j*(factorial(n) if j==0 else (n*factorial(n-j-1) if j<n else n)) for j in range(k+1))

for n in range(2,10):
    N=1<<n
    profile=[0]*N
    for p in permutations(range(n)):
        mask=0
        for i in range(n):
            if p[(i+1)%n]==(p[i]+1)%n:
                mask|=1<<i
        profile[mask]+=1
    check(sum(profile)==factorial(n),('mass',n))
    # Walsh transform via exactly integral butterfly.
    fw=profile[:]
    for i in range(n):
        bit=1<<i
        for a in range(N):
            if not (a&bit):
                u,v=fw[a],fw[a|bit]
                fw[a]=u+v;fw[a|bit]=u-v
    for mask in range(N):
        value=closed(n,mask.bit_count())
        check(fw[mask]==value,('spectrum',n,mask,fw[mask],value))
    for k in range(n+1):
        check(sum(1 for a in range(N) if a.bit_count()==k and fw[a]==closed(n,k))==comb(n,k),('exchangeable',n,k))

for n in range(2,201):
    fac=factorial(n)
    f=[closed(n,k) for k in range(n+1)]
    check(f[0]==fac,('trivial',n))
    check(f[n-1]==n*sum(comb(n-1,j)*(-2)**j*factorial(n-j-1) for j in range(n)),('terminal',n))
    for k in range(n):
        check(f[k]==n*sum(comb(k,j)*(-2)**j*factorial(n-j-1) for j in range(k+1)),('proper',n,k))
    if n==3:
        check(f[1]==0 and f[3]==0 and f[0]>0 and f[2]>0,('exception n3',f))
    elif n==2:
        check([1 if v>0 else -1 for v in f]==[1,-1,1],('n2',f))
    elif n==4:
        check([1 if v>0 else -1 for v in f]==[1,1,1,-1,-1],('n4',f))
    elif n==6:
        check(all(v>0 for v in f[:-1]) and f[-1]<0,('n6',f))
    else:
        check(all(v>0 for v in f),('positive',n))

# Exact rational generating-function recurrence for cyclic terminal character.
b=Fraction(1)
s=Fraction(-1)
for n in range(2,201):
    b=(s-2*b)/n
    target=Fraction(closed(n,n),factorial(n))
    check(target==n*(b+Fraction((-2)**n,factorial(n))),('terminal recurrence',n))
    s+=Fraction((-2)**n,factorial(n))

print('PASS:',checks,'exact assertions; direct all-permutation Walsh n<=9; full exact formula/sign n<=200.')
