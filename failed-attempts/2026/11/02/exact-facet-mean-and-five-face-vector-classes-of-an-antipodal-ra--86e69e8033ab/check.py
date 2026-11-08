#!/usr/bin/env python3
"""Reproduce the facet-count theorem for antipodal spherical four-polytopes.
Scientific verification only; universal assertions use the accompanying proof.
Requires Python 3, numpy, scipy, sympy.
"""
from fractions import Fraction as F
from itertools import combinations, product
import math
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull

CASES = [
    ('e0', (F(1,5),)*5, 0),
    ('e1', tuple(F(v,1000) for v in (300,215,180,160,145)), 1),
    ('e2', tuple(F(v,100) for v in (32,21,19,14,14)), 2),
    ('e3', tuple(F(v,100) for v in (37,18,17,16,12)), 3),
    ('e4', tuple(F(v,100) for v in (40,15,15,15,15)), 4),
]

def exact_counts(a):
    if sum(a)!=1 or not all(F(0)<v<F(1,2) for v in a):
        raise AssertionError('invalid unit-vector circuit length weights')
    if any(sum(a[i] for i in J)==F(1,2) for k in range(1,5) for J in combinations(range(5),k)):
        raise AssertionError('non-generic circuit')
    winning_pairs=sum(a[i]+a[j]>F(1,2) for i,j in combinations(range(5),2))
    facet_count=0
    for j in range(5):
        ix=[i for i in range(5) if i!=j]
        for s in product((-1,1),repeat=4):
            r=sum((a[i]*s[k] for k,i in enumerate(ix)),F(0))
            facet_count+=(abs(r)<a[j])
    return winning_pairs,facet_count

def make_vectors(a):
    a=list(map(float,a))
    k=a[0]/(1-a[0]); rho=math.sqrt(1-k*k)
    tt=.2
    def pair(p,q,sgn,axis):
        cp=(tt*tt+p*p-q*q)/(2*tt*p)
        cq=(tt*tt+q*q-p*p)/(2*tt*q)
        sp=math.sqrt(max(0,1-cp*cp)); sq=p*sp/q
        u=np.zeros(3);v=np.zeros(3)
        u[0]=sgn*cp;v[0]=sgn*cq
        u[axis]=sp;v[axis]=-sq
        assert abs(np.linalg.norm(u)-1)<1e-11 and abs(np.linalg.norm(v)-1)<1e-11
        return u,v
    y2,y3=pair(a[1],a[2],+1,1)
    y4,y5=pair(a[3],a[4],-1,2)
    x=[np.array([1.,0.,0.,0.])]
    x.extend(np.r_[[-k],rho*y] for y in (y2,y3,y4,y5))
    x=np.array(x)
    assert np.linalg.matrix_rank(x)==4
    assert np.max(np.abs(np.linalg.norm(x,axis=1)-1))<1e-10
    assert np.linalg.norm(np.array(a)@x)<1e-10
    return x

for name,a,e in CASES:
    found,f3=exact_counts(a)
    assert found==e and f3==30-2*e, (name,found,f3)
    x=make_vectors(a)
    hull=ConvexHull(np.vstack([x,-x]))
    assert len(hull.simplices)==f3,(name,len(hull.simplices),f3)
print('EXACT_FIVE_SHARP_F_VECTOR_CLASSES_AND_INSCRIBED_REALIZATIONS_PASSED')

th=sp.Symbol('t',real=True,nonnegative=True)
I=sp.integrate(th*sp.cos(th)**8,(th,0,sp.pi/2))
assert sp.simplify(I-(35*sp.pi**2/sp.Integer(1024)-sp.Rational(2,9)))==0
J=sp.integrate(sp.sin(th)*sp.cos(th)**9,(th,0,sp.pi/2))
assert J==sp.Rational(1,10)
normalization=sp.integrate(sp.cos(th)**8,(th,0,sp.pi/2))
assert normalization==sp.Rational(35,256)*sp.pi
EQ=sp.simplify(sp.Rational(512,35)/sp.pi**2*(I+J))
target_EQ=sp.Rational(1,2)-sp.Rational(2816,1575)/sp.pi**2
assert sp.simplify(EQ-target_EQ)==0
EF=sp.simplify(80*EQ)
assert sp.simplify(EF-(40-sp.Rational(45056,315)/sp.pi**2))==0
print('EXACT_SPHERICAL_HYPERPLANE_DENSITY_AND_FACET_MEAN_PASSED')

rng=np.random.default_rng(20261029)
N=8000
samples=[]
for j in range(N):
    x=rng.normal(size=(5,4));x/=np.linalg.norm(x,axis=1)[:,None]
    singular= np.linalg.svd(x.T)[2][-1]
    w=np.abs(singular);w/=sum(w)
    e=sum((w[i]+w[k]>.5) for i,k in combinations(range(5),2))
    f3=ConvexHull(np.vstack([x,-x])).simplices.shape[0]
    assert f3==30-2*e
    samples.append(f3)
observed=np.mean(samples)
se=np.std(samples,ddof=1)/math.sqrt(N)
target=float(EF)
assert abs(observed-target)<5*se, (observed,target,se)
print('INDEPENDENT_RANDOM_SPHERE_CONVEX_HULL_AND_CIRCUIT_CHECKS_PASSED',N,round(observed,5),round(target,5),round(se,5))
print('ALL_CHECKS_PASSED')
