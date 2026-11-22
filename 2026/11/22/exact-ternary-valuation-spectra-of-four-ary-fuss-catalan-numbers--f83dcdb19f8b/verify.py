#!/usr/bin/env python3
"""Reproducibility checks for ternary valuation counts of 4-ary Fuss-Catalan numbers.
No external dependencies. Finite checks complement, but do not replace, the proof.
"""
from collections import Counter
from fractions import Fraction
from math import comb

STATES = [(a,c) for a in range(3) for c in range(2)]

def count_base3_carries(n):
    prev=carry=total=0
    while n:
        a=n%3;n//=3
        cur=a+prev+carry
        carry=cur//3
        total+=carry
        prev=a
    total+=(prev+carry)//3
    return total

def valuation3(n):
    out=0
    while n and n%3==0:
        n//=3;out+=1
    return out

def polyadd(a,b):
    c=Counter(a)
    for k,v in b.items():c[k]+=v
    return +c

def poly_mul(a,b):
    c=Counter()
    for i,x in a.items():
        for j,y in b.items():c[i+j]+=x*y
    return dict(c)

def scaled_shift(a,scale,shift):
    return Counter({k+shift:scale*x for k,x in a.items() if scale*x})

def automaton_counts(level):
    dp={(0,0):Counter({0:1})}
    for _ in range(level):
        nd={}
        for (prev,carry),p in dp.items():
            for a in range(3):
                cur=a+prev+carry
                nxt=(a,cur//3)
                q=nd.setdefault(nxt,Counter())
                for j,x in p.items():q[j+cur//3]+=x
        dp=nd
    out=Counter()
    for (prev,carry),p in dp.items():
        for j,x in p.items():out[j+(prev+carry)//3]+=x
    return +out

# Denominator of the bivariate rational generating function, grouped by z powers.
DEN=[Counter({0:1}),Counter({0:-2,1:-2}),Counter({0:-1,1:4,2:-1}),
     Counter({0:1,1:1,2:1,3:1}),Counter({1:-1,2:-1,3:-1})]
# Numerator (1-tz)(1+(1-t)z-z^2).
NUM=[Counter({0:1}),Counter({0:1,1:-2}),Counter({0:-1,1:-1,2:1}),Counter({1:1})]

def main():
    checks=0
    P=[]
    for L in range(10):
        hist=automaton_counts(L)
        P.append(hist)
        assert sum(hist.values())==3**L
        checks+=1
        assert hist==Counter(count_base3_carries(n) for n in range(3**L))
        checks+=3**L
        # For integer C_4(n) the denominator 3n+1 is a 3-adic unit.
        if L<=4:
            for n in range(3**L):
                C=comb(4*n,n)//(3*n+1)
                assert C*(3*n+1)==comb(4*n,n)
                assert count_base3_carries(n)==valuation3(C)
                checks+=2
        conv=Counter()
        for j in range(min(L,4)+1):
            val=poly_mul(DEN[j],P[L-j])
            for k,x in val.items():conv[k]+=x
        lhs={k:v for k,v in conv.items() if v}
        rhs={k:v for k,v in NUM[L].items() if v} if L<len(NUM) else {}
        assert lhs==rhs, (L,lhs,rhs)
        checks+=1
        if L>=2:
            assert max(hist)==L
            checks+=1
        mean=Fraction(sum(k*v for k,v in hist.items()),3**L)
        theoretical=Fraction(L-1,2)+Fraction(1+(-1)**L,4*3**L)
        assert mean==theoretical
        checks+=1
        variance=Fraction(sum(k*k*v for k,v in hist.items()),3**L)-mean*mean
        expected=Fraction(2*L,3)-Fraction(3,4)+Fraction(5+3*(-1)**L,8*3**L)-Fraction((1+(-1)**L)**2,16*9**L)
        assert variance==expected
        checks+=1
    a=[P[L][L] for L in range(2,10)]
    assert a[:5]==[2,3,8,17,39]
    for j in range(3,len(a)):
        assert a[j]==2*a[j-1]+a[j-2]-a[j-3]
        checks+=1
    # Add distinct high-index Legendre checks without computing enormous binomial numbers.
    for n in [10**6+39,3**17+41,3**23-1,10**15+34521,10**18+33]:
        def legendre_val_factorial(k):
            s=0
            while k:k//=3;s+=k
            return s
        v=legendre_val_factorial(4*n)-legendre_val_factorial(n)-legendre_val_factorial(3*n)
        assert v==count_base3_carries(n)
        checks+=1
    print(f'VERIFY_OK checks={checks} depths=0..9 max_depth=9')

if __name__=='__main__':main()
