#!/usr/bin/env python3
"""Exact rational spot checks for the weighted two-moment BV embedding identity.
This is a finite consistency check, not an infinite-dimensional proof.
Python 3, standard library only.
"""
from fractions import Fraction as Q
from itertools import product

def integrate_poly(coeffs, l, r):
    return sum(c*(r**(k+1)-l**(k+1))/Q(k+1) for k,c in enumerate(coeffs))

def two_point_check(coeffs, s, t):
    assert Q(0)<s<t<Q(1)
    Z=integrate_poly(coeffs,Q(0),Q(1))
    assert Z>0
    mean=integrate_poly([Q(0)]+list(coeffs),Q(0),Q(1))/Z
    def prob(l,r):return integrate_poly(coeffs,l,r)/Z
    def m1(l,r):return integrate_poly([Q(0)]+list(coeffs),l,r)/Z
    hs=m1(s,Q(1))-mean*prob(s,Q(1))
    ht=m1(t,Q(1))-mean*prob(t,Q(1))
    assert hs>0 and ht>0
    a=ht/(hs+ht); b=hs/(hs+ht)
    # Center the derivative profile of a 1_{x>=s}-b 1_{x>=t}.
    c=-(a*prob(s,Q(1))-b*prob(t,Q(1)))
    q0=c; q1=c+a; q2=c+a-b
    avg=sum(q*p for q,p in zip((q0,q1,q2),(prob(Q(0),s),prob(s,t),prob(t,Q(1)))))
    moment=sum(q*m1(l,r) for q,(l,r) in zip((q0,q1,q2),((Q(0),s),(s,t),(t,Q(1)))))
    assert avg==0 and moment==0
    actual=sum(q*q*prob(l,r) for q,(l,r) in zip((q0,q1,q2),((Q(0),s),(s,t),(t,Q(1)))))
    Fs=prob(Q(0),s); Ft=prob(Q(0),t)
    predicted=(ht*ht*Fs*(1-Fs)+hs*hs*Ft*(1-Ft)-2*hs*ht*Fs*(1-Ft))/(hs+ht)**2
    assert actual==predicted
    if coeffs==[Q(1)]:
        Hs=s*(1-s); Ht=t*(1-t); d=t-s
        unweighted=Hs*Ht*d*(1-d)/(Hs+Ht)**2
        gap=(d-Q(1,2))**2/Q(4)+(Hs-Ht)**2*d*(1-d)/(Q(4)*(Hs+Ht)**2)
        assert actual==unweighted
        assert Q(1,16)-actual==gap
        assert actual<=Q(1,16)
        assert (actual==Q(1,16)) == (s==Q(1,4) and t==Q(3,4))
    return 1

count=0
for coeffs in ([Q(1)], [Q(1),Q(1)], [Q(1),Q(0),Q(1)], [Q(2),Q(3),Q(1)]):
    for N in (5,8,12,16,24):
        for i in range(1,N):
            for j in range(i+1,N):
                count+=two_point_check(coeffs,Q(i,N),Q(j,N))
# Degenerate boundary and calibrated exact extremizer.
a=Q(1,4); b=Q(3,4)
assert two_point_check([Q(1)],a,b)==1
assert sum((Q(-1,4)**2*Q(1,4),Q(1,4)**2*Q(1,2),Q(-1,4)**2*Q(1,4)))==Q(1,16)
assert (Q(-1,4)*Q(1,4)+Q(1,4)*Q(1,2)+Q(-1,4)*Q(1,4))==0
assert (Q(-1,4)*Q(1,32)+Q(1,4)*Q(1,4)+Q(-1,4)*Q(7,32))==0
print('PASS:',count+4,'exact rational assertions (pair identities, moments, gap and equality).')
