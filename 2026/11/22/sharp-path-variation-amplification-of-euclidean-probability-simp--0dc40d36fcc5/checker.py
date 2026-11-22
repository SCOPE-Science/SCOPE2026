#!/usr/bin/env python3
"""Exact supplementary checks for path-variation stability of simplex projection.
No numerical floating point is used for claims or witnesses.
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random

def tv(v): return sum(abs(v[i+1]-v[i]) for i in range(len(v)-1))

def project(y, mass=Q(1)):
    n=len(y)
    s=sorted(y,reverse=True)
    for m in range(n,0,-1):
        t=(sum(s[:m])-mass)/m
        if s[m-1]>t and (m==n or s[m]<=t):
            return [max(Q(0),a-t) for a in y]
    raise AssertionError('threshold')

def jac(F, j, n):
    a=sum(i<j for i in F);b=sum(i>=j for i in F);m=len(F)
    return [Q(-b,m) if i in F and i<j else Q(a,m) if i in F and i>=j else Q(0) for i in range(n)]

def coefficient(n):
    if n==2:return Q(1)
    return Q(n,2)-(Q(1,n+1) if n%4==1 else Q(0))

def scalar_bound(n):
    best=Q(0);arg=None
    for j in range(1,n):
        for a in range(1,j+1):
            T1=min(2*a,2*(j-a)+1)
            for b in range(1,n-j+1):
                T2=min(2*b,2*(n-j-b)+1)
                gain=Q(b*T1+a*T2,a+b)
                if gain>best:best,arg=gain,(j,a,b,T1,T2)
    return best,arg

def binary_max(L,k,with_right_terminal):
    best=-1
    for chosen in combinations(range(L),k):
        bit=[int(i in chosen) for i in range(L)]
        if with_right_terminal:bit.append(0)
        else:bit.insert(0,0)
        best=max(best,tv(bit))
    return best

count=0
for n in range(2,12):
    best=Q(0)
    for mask in range(1,1<<n):
        F=[i for i in range(n) if mask>>i&1]
        for j in range(1,n):
            gain=tv(jac(F,j,n))
            assert gain<=coefficient(n),(n,F,j,gain)
            best=max(best,gain);count+=1
            # The affine derivative must be realized by a genuine pair.
            if gain==coefficient(n):
                m=len(F); eps=Q(1,4*m)
                x=[Q(1,m) if i in F else Q(-1) for i in range(n)]
                y=[x[i]+(eps if i>=j else 0) for i in range(n)]
                z0,z1=project(x),project(y)
                assert tv([z1[i]-z0[i] for i in range(n)])==eps*gain
                assert tv([y[i]-x[i] for i in range(n)])==eps
    assert best==coefficient(n),(n,best,coefficient(n))
    compact,arg=scalar_bound(n)
    assert compact==best,(n,compact,best,arg)
print('ALL_ACTIVE_SETS_AND_STEP_TESTS_EXACT_PASS',count)
for L in range(1,8):
    for k in range(1,L+1):
        target=min(2*k,2*(L-k)+1)
        assert binary_max(L,k,True)==target
        assert binary_max(L,k,False)==target
print('BINARY_SEGMENT_TRANSITION_LEMMA_EXACT_PASS')
for n in range(12,121):
    val,arg=scalar_bound(n)
    assert val==coefficient(n),(n,val,coefficient(n),arg)
print('ALL_DIMENSION_INTEGER_OPTIMIZATION_FORMULA_PASS',109)
rg=Random(7391)
for _ in range(1500):
    n=rg.randrange(2,35)
    x=[Q(rg.randrange(-30,31),rg.randrange(1,11)) for i in range(n)]
    y=[Q(rg.randrange(-30,31),rg.randrange(1,11)) for i in range(n)]
    d=[a-b for a,b in zip(x,y)]
    if tv(d):
       p=project(x);q=project(y)
       assert tv([a-b for a,b in zip(p,q)])<=coefficient(n)*tv(d)
print('RANDOM_RATIONAL_TWO_INPUT_PROJECTION_CHECK_PASS',1500)
print('ALL_PATH_SIMPLEX_VARIATION_CHECKS_PASS')
