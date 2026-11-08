"""Exact independent finite checks for the cubic modular moment collision theorem."""
from collections import Counter

def factor(n):
    p = 2
    while p*p <= n:
        if n % p == 0:
            k=0
            while n % p == 0:
                n//=p; k+=1
            yield p,k
        p += 1
    if n>1: yield n,1

def proposed(n):
    total=1
    for p,k in factor(n):
        if p==2:
            total *= (2 if k==1 else k)*2**(2*k)
        else:
            total *= p**(2*k-1)*(p+k*(p-1))
    return total

def exhaustive(n):
    buckets=Counter(((x+y)%n,(x*x+y*y)%n,(x**3+y**3)%n) for x in range(n) for y in range(n))
    return sum(v*v for v in buckets.values())

for n in range(1,85):
    lhs=exhaustive(n)
    rhs=proposed(n)
    assert lhs == rhs, (n,lhs,rhs)

for n in range(1,55):
    seen={}
    for a in range(n):
        for b in range(n):
            key=tuple((pow(a,j,n)+pow(b,j,n))%n for j in (1,2,3))
            higher=tuple((pow(a,j,n)+pow(b,j,n))%n for j in range(4,16))
            if key in seen: assert seen[key]==higher,(n,a,b)
            else: seen[key]=higher
    if n>=4 and n%4==0:
        a,b,x=1,n//2,0
        y=(-a-b)%n; z=(-a)%n; w=(-b)%n
        assert (x+y-z-w)%n==0
        assert (x*x+y*y-z*z-w*w)%n==0
        assert (x**3+y**3-z**3-w**3)%n!=0

print('VERIFY_OK exact_energy_moduli=1..84; all_higher_moments_moduli=1..54; power_degrees=4..15; minimality_witnesses=PASS')
