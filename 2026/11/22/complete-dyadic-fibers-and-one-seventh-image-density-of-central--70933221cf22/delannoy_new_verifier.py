#!/usr/bin/env python3
"""Independent exact-arithmetic tests for Delannoy dyadic fiber theorem.
No external dependencies. Finite tests do not replace the all-level proof.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def delannoy(n, bits):
    return sum((1 << j) * comb(n,j)**2 for j in range(min(n,bits-1)+1)) % (1 << bits)

def v2(x):
    assert x
    return (x & -x).bit_length() - 1

def predicted_hist(k):
    assert k >= 4
    h = Counter({1: 1 << (k-3)})
    for r in range(2, (k-1)//3+1):
        h[1 << (2*r-2)] += 1 << (k-3*r)
    h[1 << (k-2-(k+2)//3)] += 2
    return h


def coefficient_checks():
    # The coefficient p_{j,1}=-2H_{j-1}; p_{j,2}=2H_{j-1}^2-H^{(2)}_{j-1}.
    for j, linear, quad in [(4,Fraction(-11,3),Fraction(193,36)),
                            (8,None,Fraction(2105161,176400))]:
        h=sum((Fraction(1,i) for i in range(1,j)),Fraction())
        h2=sum((Fraction(1,i*i) for i in range(1,j)),Fraction())
        if linear is not None: assert -2*h == linear
        assert 2*h*h-h2 == quad
    # Explicit finite valuation bounds for the only sensitive coefficient ranges.
    def w(j):
        vv = sorted([((i & -i).bit_length()-1) for i in range(1,j) for _ in range(2)], reverse=True)
        return [j-2*v2(j)+2*(m-1)-sum(vv[:m]) for m in range(2,2*j-1)]
    assert [min(w(j)) for j in range(2,9)] == [2,3,0,3,2,5,0]
    for j in range(9,32):
        B=j-2*v2(j)-2-2*sum((j-1)//(1<<a) for a in range(3,10))
        assert B>=4
        assert min(w(j))>=B
    # Critical pair has even sum of 2-adic units.
    a=Fraction(193,9)+Fraction(2105161,11025)
    assert v2(a.numerator)-v2(a.denominator)>=1


def finite_fibers():
    num=0
    for k in range(4,16):
        T=1<<(k-2)
        vals=[delannoy(n,k) for n in range(T)]
        hist=Counter(Counter(vals).values())
        expected=predicted_hist(k)
        assert hist==expected, (k,hist,expected)
        image=set(vals)
        # Full singletons in the two claimed congruence classes.
        for y in range(1<<k):
            if y%16 in (3,13): assert vals.count(y)==1, (k,y)
        for y in image:
            if y%16 in (3,13): continue
            c=(y-1)%(1<<k) if y%16 == 1 else (y+1)%(1<<k)
            assert y%16 in (1,15)
            if c:
                a=v2(c)
                assert a>=6 and a%3==0, (k,y,a)
        assert len(image)==(1<<(k-3))+sum(1<<(k-3*r) for r in range(2,(k-1)//3+1))+2
        num+=len(vals)
    return num


def dyadic_differences():
    checks=0
    bits=30
    for r in range(2,8):
        for n in range(0,200):
            x=delannoy(n,bits)
            y=delannoy(n+(1<<r),bits)
            d=(y-x)%(1<<bits)
            assert d % (1<<(r+3)) == ((1<<(r+2))*(n+comb(n,2)))%(1<<(r+3)),(n,r,d)
            checks+=1
    # Critical-shell pairwise isometries, modulo a large safe power.
    for r in range(2,7):
        for a in range(1,20,2):
            for b in range(a+2,24,2):
                n=(1<<r)*a; m=(1<<r)*b
                d=(delannoy(m,bits)-delannoy(n,bits))%(1<<bits)
                expected=v2(m-n)+2*r
                if expected < bits:
                    assert v2(d)==expected,(n,m,r,expected,v2(d) if d else None)
                    checks+=1
    return checks

if __name__=='__main__':
    coefficient_checks()
    print('coefficient bounds: OK')
    print('finite fiber indices:',finite_fibers())
    print('shift and shell tests:',dyadic_differences())
    print('PASS')
