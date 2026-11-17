#!/usr/bin/env python3
"""Reproduce exact centered potential maxima and contact-normal ranks on mixed-arm trees."""
from fractions import Fraction
from itertools import product
from math import comb
from sympy import Matrix

def formula(p,q):
    N=1+p+2*q
    d=2 if p==1 and q%2==1 else ((p+q)%2)
    R=Fraction(p+5*q) - Fraction(d*d,N)
    sums_p=range(-p,p+1,2); sums_q=range(-q,q+1,2)
    S=[(a,b) for a in sums_q for b in sums_p if abs(3*a+b)==d]
    cnt=sum(comb(q,(q+a)//2)*comb(p,(p+b)//2) for a,b in S)
    iq=int(any(abs(a)<q for a,b in S)); ip=int(any(abs(b)<p for a,b in S))
    rm=Matrix(S).rank()
    rk=(q-1)*iq+(p-1)*ip+rm
    return R,cnt,rk,S

def direct(p,q):
    N=1+p+2*q
    rows=[]; mx=None; opts=[]
    for bits in product((-1,1),repeat=p+2*q):
        shorts=bits[:p]; inner=bits[p:p+q]; outer=bits[p+q:]
        u=list(shorts)+[v for v in inner]+[inner[i]+outer[i] for i in range(q)]
        sx=sum(u)
        Q=Fraction(sum(x*x for x in u))-Fraction(sx*sx,N)
        if mx is None or Q>mx: mx=Q;opts=[u]
        elif Q==mx:opts.append(u)
    M=Matrix(opts)
    return mx,len(opts),M.rank(),opts

checks=0;configs=0
for q in range(2,7):
    for p in range(1,12):
        if p+2*q>14:continue
        val,cnt,rk,S=formula(p,q)
        val2,cnt2,rk2,_=direct(p,q)
        assert (val,cnt,rk)==(val2,cnt2,rk2),(p,q,(val,cnt,rk),(val2,cnt2,rk2))
        checks+=1; configs+=2**(p+2*q)
print('EXACT_ALL_EDGE_POTENTIAL_CHECKS_PASS cases=%d signed_potentials=%d'%(checks,configs))
for p,q in [(3,2),(3,3),(3,4),(3,5),(1,2),(1,3),(4,4),(5,2),(4,2)]:
    R,contacts,rank,S=formula(p,q)
    print('PROFILE p=%d q=%d norm_squared=%s contacts=%d rank=%d center_dimension=%d class_pairs=%s'%(p,q,R,contacts,rank,p+2*q-rank,S))
print('MIXED_ARM_SPIDER_ALL_CHECKS_PASS')
