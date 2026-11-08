"""Independent exact-arithmetic checks for two-power fourth-moment phase theorem.
Run: python check_muntz.py
"""
from fractions import Fraction as F
from itertools import product

def avgpow(k):
    return F(0) if k % 2 else F(1, k+1)

def ratio_direct(l,h,a,b):
    # Independent binomial polynomial integration for real coefficients a,b.
    v2 = a*a*avgpow(2*l) + 2*a*b*avgpow(l+h) + b*b*avgpow(2*h)
    v4 = sum(F([1,4,6,4,1][j])*a**(4-j)*b**j*avgpow((4-j)*l+j*h) for j in range(5))
    return v4/(v2*v2)

def scalars(l,h):
    A=F((2*l+1)**2,4*l+1)
    B=F((2*h+1)**2,4*h+1)
    C=F(3*(2*l+1)*(2*h+1),2*l+2*h+1)
    return A,B,C

count=0
for l in range(0,45):
    for h in range(l+1,6*l+21):
        A,B,C=scalars(l,h)
        assert B>A
        if (l+h)%2==1:
            mix=h<=5*l+1
            assert (C>B)==mix,(l,h)
            assert (C<=B)==(h>=5*l+3),(l,h)
            if mix:
                D=2*C-A-B
                assert D>0
                upper=(C*C-A*B)/D
                x=(C-A)/D
                assert 0<x<1 and upper>B
                assert upper-B==(C-B)**2/D
                # Optimize energy split x by hand, using rational quadratic.
                assert upper==A*(1-x)**2+B*x*x+2*C*x*(1-x)
                for t in (F(0),F(1),F(1,3),F(4,5),F(19,37)):
                    q=A*(1-t)**2+B*t*t+2*C*t*(1-t)
                    assert q<=upper
            else:
                assert C<B
                for t in (F(0),F(1),F(1,3),F(4,5),F(19,37)):
                    q=A*(1-t)**2+B*t*t+2*C*t*(1-t)
                    assert q<=B
            for a,b in product((F(1),F(-2),F(3,2)),(F(1),F(-3),F(2,3))):
                direct=ratio_direct(l,h,a,b)
                L2a=a*a/F(2*l+1)
                L2b=b*b/F(2*h+1)
                x=L2b/(L2a+L2b)
                model=A*(1-x)**2+B*x*x+2*C*x*(1-x)
                assert direct==model,(l,h,a,b)
            count+=1
        else:
            # The first variation at the pure higher monomial is strictly nonzero.
            numer=-2*h*(h-l)
            assert numer<0
            # Independent rational finite-difference witness for one sign.
            pure=B
            for k in range(1,14):
                if ratio_direct(l,h,-F(1,10**k),F(1))>pure:
                    break
            else: raise AssertionError(('not found',l,h))
print('EXACT_PARITY_AND_MIXTURE_CLASSIFICATION_PASSED',count,'opposite-parity pairs')
print('EXACT_SAME_PARITY_LOCAL_OBSTRUCTION_PASSED')
print('ALL_MUNTZ_TWO_POWER_CHECKS_PASSED')
