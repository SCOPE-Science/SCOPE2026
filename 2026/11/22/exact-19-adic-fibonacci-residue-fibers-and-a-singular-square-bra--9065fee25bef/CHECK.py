#!/usr/bin/env python3
"""Exhaustive finite-level fiber audit for Fibonacci residues modulo 19**k.
Independent from the theoretical matrix-isometry proof; Python standard library.
"""
from collections import Counter

P=19
REGULAR=[0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17]
FIB=[0,1]
for _ in range(2,18): FIB.append(FIB[-1]+FIB[-2])
assert [FIB[r]%P for r in REGULAR]==[0,1,1,2,3,5,8,13,2,17,13,11,5,16,2,18,1]


def center(k):
    # Hensel lift 5*c^2=4 with c=15 mod 19.
    c=15
    m=P
    for _ in range(1,k):
        v=next(i for i in range(P) if (5*(c+m*i)**2-4)%(m*P)==0)
        c+=m*v
        m*=P
    return c


def expected(k):
    m=P**k
    e=[0]*m
    for r in REGULAR:
        u=FIB[r]%P
        for y in range(u,m,P):
            e[y]+=1
    if k==1:
        e[15]+=1
        return e
    c=center(k)
    a=(c*pow(8,-1,m))%m
    mod=P**(k-2)
    qcnt=Counter((x*x)%mod for x in range(mod))
    for sq,cnt in qcnt.items():
        e[(c+P**2*a*sq)%m]+=P*cnt
    return e


def observed(k):
    m=P**k
    T=18*P**(k-1)
    e=[0]*m
    a,b=0,1
    for _ in range(T):
        e[a]+=1
        a,b=b,(a+b)%m
    assert (a,b)==(0,1)
    # Confirm that the period is minimal by testing prime-divisor reductions.
    for d in [2,3,19]:
        if T%d: continue
        x,y=0,1
        for _ in range(T//d): x,y=y,(x+y)%m
        assert (x,y)!=(0,1), (k,d)
    return e


def main():
    for k in range(1,5):
        e=expected(k)
        o=observed(k)
        assert o==e,(k,next((i,o[i],e[i]) for i in range(len(e)) if o[i]!=e[i]))
        print('PASS',k,'modulus',P**k,'least period',18*P**(k-1),
              'attained',sum(x>0 for x in o),'maximum fiber',max(o),
              'center',center(k))
    print('All finite tests passed; infinite claims are proven mathematically in RESULT.md.')


if __name__=='__main__':main()
