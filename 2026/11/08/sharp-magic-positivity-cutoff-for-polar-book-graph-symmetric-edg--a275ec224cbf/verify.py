"""Exact-arithmetic checks for polar book-graph magic coefficients.
Standard-library Python 3; run: python verify.py
"""
from fractions import Fraction as F
from math import comb

POSITIVE = {
  1: ['1','1','1'],
  2: ['1','4/3','4/3','1'],
  3: ['1','2','3/2','2','1'],
  4: ['1','44/15','34/15','34/15','44/15','1'],
  5: ['1','4','9/2','2','9/2','4','1'],
  6: ['1','106/21','61/7','71/21','71/21','61/7','106/21','1'],
}
NEGATIVE = {7:(4,'-5/4'),8:(4,'-14/15'),9:(5,'-198/5'),
  10:(5,'-662/11'),11:(6,'-399'),12:(6,'-286772/455'),
  13:(7,'-156612/35'),14:(7,'-35441/5'),15:(8,'-548685/8'),
  16:(8,'-5493182/51')}

def count(q,t):
    return (2*t+1)**q + 2*sum((2*t+1-s)**q for s in range(1,t+1))

def interpolate(q):
    """Newton forward difference interpolation of count(q,t)."""
    d=q+1
    vals=[F(count(q,t)) for t in range(d+1)]
    delta=[]
    while vals:
        delta.append(vals[0]); vals=[vals[j+1]-vals[j] for j in range(len(vals)-1)]
    coeffs=[F(0)]*(d+1)
    product=[F(1)]
    fact=1
    for k,dk in enumerate(delta):
        for j,v in enumerate(product): coeffs[j]+=dk*v/fact
        product=[F(0)]+product
        for j in range(len(product)-1): product[j]-=k*product[j+1]
        fact*=k+1
    return coeffs

def magic(ordinary):
    d=len(ordinary)-1; out=[]
    for j in range(d+1):
        out.append(ordinary[j]-sum(out[k]*comb(d-k,j-k) for k in range(j)))
    return out

def bernoulli(n):
    """Exact B_n in the conventional convention B_1=-1/2."""
    A=[F(0)]*(n+1)
    for m in range(n+1):
        A[m]=F(1,m+1)
        for j in range(m,0,-1): A[j-1]=j*(A[j-1]-A[j])
    return -A[0] if n==1 else A[0]

def run():
    checks=0
    for q in range(1,17):
        d=q+1
        ordinary=interpolate(q)
        a=magic(ordinary)
        # Test interpolation outside its defining d+1 evaluation points.
        for t in [d+1,d+2,2*d+3]:
            assert sum(v*t**j for j,v in enumerate(ordinary)) == count(q,t)
            checks+=1
        # Independently test both ordinary and magic expansions at t=0..d+2.
        for t in range(d+3):
            assert sum(a[j]*t**j*(t+1)**(d-j) for j in range(d+1)) == count(q,t)
            checks+=1
        # Reflexive reciprocity gives palindromic magic coefficients here.
        assert all(a[j]==a[d-j] for j in range(d+1)); checks+=1
        if q<=6:
            assert a == list(map(F,POSITIVE[q]));checks+=1
            assert all(z>0 for z in a);checks+=1
        else:
            j,z=NEGATIVE[q]
            assert a[j]==F(z) and a[j]<0;checks+=1
        if q>=5:
            B0=bernoulli(q);B1=bernoulli(q-1);B2=bernoulli(q-2)
            assert a[1]==q-1+2*B0;checks+=1
            assert a[2]==F(q*(q-3),2)+3*q*B1-2*q*B0;checks+=1
            assert a[3]==F(q*(q-1),6)*(q-5+6*B0-18*B1+14*B2);checks+=1
    # Check crucial Bernoulli initial conditions and strict growth at finite sampled indices.
    assert bernoulli(14)==F(7,6);checks+=1
    assert bernoulli(16)==-F(3617,510);checks+=1
    assert bernoulli(18)==F(43867,798);checks+=1
    assert bernoulli(20)==-F(174611,330);checks+=1
    for n in range(14,49,2):
        assert abs(bernoulli(n+4))>2*abs(bernoulli(n)); checks+=1
    print('VERIFY_OK',checks,'exact assertions')
if __name__=='__main__': run()
