#!/usr/bin/env python3
"""Exact gap-moment identities and independent facet-simplex comparisons for top-k balls.

Requires Python 3.10+, sympy, numpy and scipy for the independent convex-hull checks.
Run `python check.py`.
"""
import math
from fractions import Fraction as F
from itertools import product
from math import factorial
from scipy.spatial import ConvexHull
import numpy as np
import sympy as s


def c_list(d,k):
    return [min(F(i),k) for i in range(1,d+1)]

def exact_gap(d,k):
    cs=c_list(d,k)
    vol=F(2**d,1)
    for c in cs:vol/=c
    inv=[1/c for c in cs]
    H=sum(min(i,j)*inv[i-1]*inv[j-1] for i in range(1,d+1) for j in range(1,d+1))
    H+=sum(i*inv[i-1]**2 for i in range(1,d+1))
    rad=H/F((d+1)*(d+2))
    return vol,rad

def determinant(M):
    M=[[F(x) for x in row] for row in M]
    n=len(M); a=F(1)
    for j in range(n):
        p=next((i for i in range(j,n) if M[i][j]),None)
        if p is None:return F(0)
        if p!=j: M[j],M[p]=M[p],M[j];a=-a
        t=M[j][j]; a*=t
        for i in range(j+1,n):
            q=M[i][j]/t
            for h in range(j+1,n):M[i][h]-=q*M[j][h]
            M[i][j]=F(0)
    return a

def exact_hull(d,k):
    one=F(1)
    vertices=set()
    for bits in product((-1,1),repeat=d): vertices.add(tuple(F(v,1)/k for v in bits))
    for i in range(d):
        for sign in (-1,1):
            row=[F(0)]*d;row[i]=F(sign);vertices.add(tuple(row))
    vertices=sorted(vertices)
    hull=ConvexHull(np.array([[float(t) for t in p] for p in vertices]),qhull_options='Qx')
    total=F(0); weighted=F(0)
    seen=set()
    for simplex in hull.simplices:
        key=tuple(sorted(int(x) for x in simplex))
        if key in seen:continue
        seen.add(key)
        vs=[vertices[i] for i in key]
        det=abs(determinant(vs))
        vol=det/factorial(d)
        total+=vol
        sum_norm=sum(sum(x*x for x in v) for v in vs)
        vector_sum=[sum(v[j] for v in vs) for j in range(d)]
        ss=sum(x*x for x in vector_sum)
        weighted+=vol*(sum_norm+ss)/F((d+1)*(d+2))
    return total,weighted/total, len(seen)

def check_symbolic():
    k,d,m=s.symbols('k d m', positive=True)
    n=d-m
    H=2*m+2*m*n/k+n*(n+1)*(d+2*m+2)/(3*k*k)
    P=2*m*k*k+2*m*n*k+n*(n+1)*(d+2*m+2)/3
    assert s.simplify(H-P/k**2)==0
    q=2*k*k+(d-2*m)*k-(n+1)*(d+2*m+2)/3
    assert s.simplify(d*k*s.diff(P,k)-2*m*P-2*m*n*q)==0
    for D in range(2,15):
        for M in range(1,D):
            K=F(2*M+1,2)
            cs=c_list(D,K)
            vol,rad=exact_gap(D,K)
            v_formula=F(2**D,1)/(F(factorial(M))*K**(D-M))
            h_formula=F(2*M)+F(2*M*(D-M))/K+F((D-M)*(D-M+1)*(D+2*M+2),3)/K**2
            assert vol==v_formula and rad==h_formula/F((D+1)*(D+2))
    print('SYMBOLIC_AND_RATIONAL_CHAMBERS',sum(range(1,14)))

def verify_limits():
    # Symbolic asymptotic h(alpha) and unique critical point of limiting profile.
    a=s.symbols('a',positive=True)
    h=s.simplify(2+(1-a)**2*(1+2*a)/(3*a*a))
    assert s.simplify(h-(1+3*a*a+2*a**3)/(3*a*a))==0
    f=s.exp(-2*a)*(1+3*a*a+2*a**3)/12
    deriv=s.factor(s.diff(f,a))
    assert s.simplify(deriv+s.exp(-2*a)*(a-1)*(2*a*a+2*a-1)/6)==0
    alpha=(s.sqrt(3)-1)/2
    assert s.simplify((1+3*alpha**2+2*alpha**3)-s.Rational(3,2))==0
    assert s.simplify(f.subs(a,alpha)-s.exp(1-s.sqrt(3))/8)==0
    for D in [10,50,100,500,1000]:
        m=int(float(alpha)*D); k=F(2*m+1,2)
        volume,rad=exact_gap(D,k)
        isotropic=math.exp(math.log(float(rad/D))-(2/D)*(math.log(volume.numerator)-math.log(volume.denominator)))
        assert 0.055<isotropic<0.083334
    print('ASYMPTOTIC_POLYNOMIAL_IDENTITY_PASSED')


def check_candidate_classification():
    from scipy.optimize import minimize_scalar
    def q(d,m,k):
        return 2*k*k+(d-2*m)*k-F((d-m+1)*(d+2*m+2),3)
    count=0
    for d in range(2,71):
        candidates=[]
        for m in range(1,d):
            lo=q(d,m,F(m)); hi=q(d,m,F(m+1))
            if lo<0<hi:
                candidates.append(m)
        assert 1<=len(candidates)<=2 and (len(candidates)<2 or candidates[1]==candidates[0]+1),(d,candidates)
        if d<=28:
            def val(k):
                cs=np.minimum(np.arange(1,d+1),float(k))
                inv=1/cs
                ix=np.arange(1,d+1)
                H=sum(min(i,j)*inv[i-1]*inv[j-1] for i in ix for j in ix)+sum(i*inv[i-1]**2 for i in ix)
                return math.exp(math.log(float(H))-math.log(4*d*(d+1)*(d+2))+(2/d)*np.log(cs).sum())
            opt=[]
            for m in range(1,d):
                z=minimize_scalar(val,bounds=(m,m+1),method='bounded',options={'xatol':1e-11})
                opt.append((z.fun,z.x))
            best=min(opt)
            assert any(m<best[1]<m+1 for m in candidates), (d,best,candidates)
        count+=1
    print('CHAMBER_MINIMA_BOUND_TESTS_PASSED',count)

def compare_hull():
    cases=[]
    for d in (2,3,4):
        for k in (F(6,5),F(3,2),F(7,4),F(2,1)):
            if k>d:continue
            expect=exact_gap(d,k)
            got=exact_hull(d,k)
            assert expect[0]==got[0],(d,k,'volume',expect,got)
            assert expect[1]==got[1],(d,k,'moment',expect,got)
            cases.append((d,str(k),got[2]))
    print('INDEPENDENT_EXACT_HULL_SIMPLEX_TESTS_PASSED',len(cases),'facets',sum(z[2] for z in cases))

if __name__=='__main__':
    check_symbolic()
    verify_limits()
    check_candidate_classification()
    compare_hull()
    print('TOP_K_NORM_ISOTROPY_CHECKS_PASSED')
