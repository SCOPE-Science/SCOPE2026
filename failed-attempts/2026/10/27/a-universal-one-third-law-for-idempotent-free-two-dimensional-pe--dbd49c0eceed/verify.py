#!/usr/bin/env python3
"""Check exact nonzero-idempotent distributions in dimension two.

All enumerations are exhaustive at the stated field sizes. For q <= 5,
independent direct enumeration of solutions x = M(x_1^2,x_2^2)^T
cross-checks the projective fixed-point count.
"""
from collections import Counter
from itertools import product
from fractions import Fraction

FIELDS = [
    (2, (0, 1)), (3, (0, 1)), (5, (0, 1)),
    (7, (0, 1)), (11, (0, 1)),
    (2, (1, 1, 1)),  # F_4 = F_2[t]/(t^2+t+1)
    (2, (1, 1, 0, 1)),  # F_8 = F_2[t]/(t^3+t+1)
    (3, (1, 0, 1)),  # F_9 = F_3[t]/(t^2+1)
]

def arithmetic(p, modulus):
    e = len(modulus)-1
    q = p**e
    def mul(a,b):
        poly=[0]*(2*e-1)
        for i in range(e):
            ai=(a//p**i)%p
            for j in range(e):
                poly[i+j]=(poly[i+j]+ai*((b//p**j)%p))%p
        for k in range(2*e-2,e-1,-1):
            c=poly[k]
            for j in range(e):
                poly[k-e+j]=(poly[k-e+j]-c*modulus[j])%p
        return sum(poly[i]*p**i for i in range(e))
    def add(a,b):
        return sum((((a//p**i)%p+(b//p**i)%p)%p)*p**i for i in range(e))
    def sub(a,b):
        return sum((((a//p**i)%p-(b//p**i)%p)%p)*p**i for i in range(e))
    # Verify the finite-field multiplication used in the enumeration.
    assert all(len({mul(a,b) for b in range(1,q)}) == q-1 for a in range(1,q))
    return q,add,sub,mul

def expected_distribution(q,p):
    if p == 2:
        return (Fraction(1,3),Fraction(1,2),Fraction(0),Fraction(1,6))
    return (Fraction(1,3),
            Fraction(q*q+1,2*q*(q+1)),
            Fraction(q-1,q*(q+1)),
            Fraction(q*q-2*q+3,6*q*(q+1)))

def exhaustive_case(p,modulus):
    q,add,sub,mul=arithmetic(p,modulus)
    counts=Counter()
    nonsingular=0
    for a,b,c,d in product(range(q),repeat=4):
        if sub(mul(a,d),mul(b,c))==0:
            continue
        nonsingular += 1
        n = int(c==0)  # infinity is a fixed projective point
        for t in range(q):
            t2=mul(t,t)
            numerator=add(mul(a,t2),b)
            denominator=add(mul(c,t2),d)
            if numerator == mul(t,denominator):
                n += 1
        assert n <= 3
        if q <= 5:
            direct=0
            for x,y in product(range(q),repeat=2):
                if x==0 and y==0:
                    continue
                xs,ys=mul(x,x),mul(y,y)
                if x==add(mul(a,xs),mul(b,ys)) and y==add(mul(c,xs),mul(d,ys)):
                    direct+=1
            assert n==direct,(q,a,b,c,d,n,direct)
        counts[n]+=1
    size=q*(q*q-1)*(q-1)
    assert nonsingular==size,(q,size,nonsingular)
    predicted=expected_distribution(q,p)
    for i in range(4):
        assert Fraction(counts[i],size)==predicted[i],(q,i,counts[i],size,predicted[i])
    print('q=%d matrices=%d counts(N=0,1,2,3)=%s' %
          (q,size,tuple(counts[i] for i in range(4))))

if __name__=='__main__':
    for params in FIELDS:
        exhaustive_case(*params)
    print('VERIFY_OK')
