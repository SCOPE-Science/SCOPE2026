#!/usr/bin/env python3
"""Exact rational interval certificate for a trinomial sixth-moment extremum.

No external dependencies. The finite collision check is supplementary;
the interval-Hessian test proves the asserted strict concavity on a full
continuum of coefficient magnitudes.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from collections import defaultdict
from math import isqrt, factorial

class I:
    def __init__(self, lo, hi=None):
        self.lo = Q(lo)
        self.hi = Q(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, y):
        y = y if isinstance(y, I) else I(y)
        return I(self.lo+y.lo, self.hi+y.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, y): return self + (-y if isinstance(y,I) else -Q(y))
    def __rsub__(self,y): return -self+y
    def __mul__(self,y):
        y = y if isinstance(y, I) else I(y)
        z = [a*b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,y):
        y = y if isinstance(y, I) else I(y)
        assert y.lo > 0
        return self * I(Q(1,y.hi),Q(1,y.lo))
    def square(self):
        return I(0 if self.lo<=0<=self.hi else min(self.lo**2,self.hi**2),
                 max(self.lo**2,self.hi**2))

def sqrt_bounds(z,places=16):
    assert z>0
    unit=10**places
    k=isqrt((z.numerator*unit**2)//z.denominator)
    return Q(k,unit),Q(k+1,unit)

def certificate():
    # Cover all (A,B,C) in [1/5,1/2]^3, A+B+C=1.
    cells=0; min_det=None
    for ia in range(20):
        A=I(Q(ia,20),Q(ia+1,20))
        if A.hi < Q(1,5) or A.lo > Q(1,2):continue
        A=I(max(A.lo,Q(1,5)),min(A.hi,Q(1,2)))
        for ib in range(20):
            B=I(Q(ib,20),Q(ib+1,20))
            if B.hi < Q(1,5) or B.lo > Q(1,2):continue
            B=I(max(B.lo,Q(1,5)),min(B.hi,Q(1,2)))
            C=I(1)-A-B
            if C.hi<Q(1,5) or C.lo>Q(1,2):continue
            C=I(max(C.lo,Q(1,5)),min(C.hi,Q(1,2)))
            tl,_=sqrt_bounds(B.lo/C.hi)
            _,th=sqrt_bounds(B.hi/C.lo)
            t=I(tl,th)
            # The entries of the Hessian of P(A,B,1-A-B), with t=sqrt(B/C):
            h11=I(-12)-24*B-6*B*t-Q(3,2)*A*t*t*t
            h12=I(-18)+24*C+t*(9*C-3*B-Q(9,2)*A)-Q(3,2)*A*t*t*t
            h22=I(-12)-24*A+Q(9,2)*A/t-9*A*t-Q(3,2)*A*t*t*t
            # Sylvester criterion for -H-I positive definite. It certifies
            # H <= -I on the whole covered simplex, not only at grid nodes.
            minor=(-h11-I(1))*(-h22-I(1))-h12.square()
            assert h11.hi < -1 and h22.hi < -1 and minor.lo > 0, (ia,ib)
            cells+=1
            min_det=minor.lo if min_det is None else min(min_det,minor.lo)
    assert cells==51 and min_det>180
    return cells,min_det

def moment_collision_check():
    # Three frequencies 0,1,3. Enumerate all ordered triples exactly.
    D=defaultdict(lambda:defaultdict(int))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                ct=(sum(z==0 for z in (i,j,k)),sum(z==1 for z in (i,j,k)),sum(z==2 for z in (i,j,k)))
                freq=sum((0,1,3)[z] for z in (i,j,k))
                D[freq][ct]+=1
    # Diagonal monomials and one off-diagonal collision at total frequency 3.
    assert len(D)==9 and sum(sum(v.values()) for v in D.values())==27
    collisions=[]
    for freq,terms in D.items():
        if len(terms)>1:collisions.append((freq,sorted(terms.items())))
    assert collisions==[(3,[((0,3,0),1),((2,0,1),3)])],collisions
    # Equal coefficients yield 99; the generic nonresonant case yields 93.
    assert sum(sum(v.values())**2 for v in D.values())==99
    return len(D)

def sharp_interval():
    # Rational near-maximizer. Strong concavity (H<=-I) implies
    # P(x*) <= P(x0)+||grad P(x0)||^2/2, for x0 in the K simplex.
    A=Q(3342205,10**7);B=Q(3628166,10**7);C=1-A-B
    assert Q(1,5)<min(A,B,C) and max(A,B,C)<Q(1,2)
    tl,th=sqrt_bounds(B/C,places=24);t=I(tl,th)
    base=6-9*(A*A+B*B+C*C)+4*(A**3+B**3+C**3)
    P=I(base)+6*A*B*C*t
    ga=(C-A)*(6+12*B)+3*B*t*(2*C-A)
    gb=(C-B)*(6+12*A)+3*A*t*(3*C-B)
    grad2=ga.square()+gb.square()
    upper=P.hi+grad2.hi/2
    assert P.lo > Q(367669,100000)
    assert upper < Q(367670,100000)
    # Makes an exact, reproducible rational bracket for the sharp constant.
    assert Q(367669,100000) < P.lo <= upper < Q(367670,100000)
    return (P.lo,upper)

if __name__=='__main__':
    nfreq=moment_collision_check()
    cells,det=certificate()
    lo,hi=sharp_interval()
    print('VERIFY_OK Fourier_fibers=%d Hessian_interval_cells=%d det_minus_identity_gt_180=PASS sharp_constant_interval=(%.11f,%.11f) exact_rational_certificate=PASS'%(nfreq,cells,float(lo),float(hi)))
