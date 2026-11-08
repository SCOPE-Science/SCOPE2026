"""Independent slow checks of exact arithmetic predicate at small widths and sampled width 14.
Only evidence for full width-14 count is exhaustive verify.cpp, not this spot check.
"""
from math import gcd
from random import Random

def rev(n,k):
    return int(bin(n)[2:].zfill(k)[::-1],2)

def direct_can(t,r,k):
    H=1 << (k-1)
    Q=2*H
    for b in range(H,Q):
        a=rev((r*rev(b,k))%Q,k)
        for divisor in (H,2*H):
            lb=t*b
            ub=(t+1)*(b+1)
            if max(lb, a*divisor) < min(ub,(a+1)*divisor):
                return True
    return False

def optimized_can(t,r,k):
    H=1 << (k-1)
    Q=2*H
    for b in range(H,Q):
        inv=pow(rev(b,k),-1,Q)
        lo=t*b
        hi=(t+1)*(b+1)
        for step in (H,2*H):
            start=max(H,lo//step)
            stop=min(Q-1,(hi-1)//step)
            for a in range(start,stop+1):
                if rev(a,k)*inv%Q == r and max(lo, a*step)<min(hi,(a+1)*step):
                    return True
    return False

for k in range(3,9):
    H=1<<(k-1)
    count=0
    for t in range(H,2*H):
        for r in range(1,2*H,2):
            # Direct O(8^k) check, independently phrased via a forced prefix.
            flag=direct_can(t,r,k)
            assert flag==optimized_can(t,r,k)
            count+=not flag
    print('small',k,count)

rng=Random(20261105)
k=14
H=1<<(k-1)
for i in range(200):
    t=rng.randrange(H,2*H)
    r=rng.randrange(1,2*H,2)
    assert direct_can(t,r,k)==optimized_can(t,r,k)
print('width14 crosschecks',200)
