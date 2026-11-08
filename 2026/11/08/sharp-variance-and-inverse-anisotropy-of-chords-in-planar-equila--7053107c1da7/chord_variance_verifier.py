"""Exact finite-population verification of a planar chord-variance identity.
Run: python chord_variance_verifier.py. Uses the Python standard library only.
Exact tests are diagnostics; the full theorem follows from the proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def unit(t):
    t=F(t)
    return ((1-t*t)/(1+t*t),2*t/(1+t*t))
def dot(x,y): return x[0]*y[0]+x[1]*y[1]
def neg(x): return tuple(-v for v in x)
def variance_formula(edges,k):
    n=len(edges)
    assert n>=4 and 2<=k<=n-2 and n%2==0
    assert sum(x[0] for x in edges)==0 and sum(x[1] for x in edges)==0
    assert all(dot(x,x)==1 for x in edges)
    p=sum(x[0]*x[0]-x[1]*x[1] for x in edges)
    q=sum(2*x[0]*x[1] for x in edges)
    f2=p*p+q*q
    a=F(k*n*(k-1)*(n-k)*(n-k-1),(n-2)*(n-1)**2)
    c=F(k*(k-1)*(n-k)*(n-k-1),n*(n-1)*(n-2)*(n-3))
    return a+c*f2,a,c,f2

def enumerate_variance(edges,k):
    n=len(edges)
    vals=[]
    for inds in combinations(range(n),k):
        vec=(sum(edges[i][0] for i in inds),sum(edges[i][1] for i in inds))
        vals.append(dot(vec,vec))
    mean=sum(vals,F(0))/len(vals)
    second=sum((v*v for v in vals),F(0))/len(vals)
    return mean,second-mean*mean

tests=0
for params in [[0,1],[0,F(1,2),2],[0,1,2,F(3,2)],[0,F(1,2),1,2,F(3,2)]]:
    es=[]
    for t in params:
        x=unit(t)
        es.extend([x,neg(x)])
    n=len(es)
    vmin=None
    for k in range(2,n-1):
        empirical_mean,empirical_var=enumerate_variance(es,k)
        formula,a,c,f2=variance_formula(es,k)
        assert empirical_mean==F(k*(n-k),n-1)
        assert empirical_var==formula
        assert a<=formula<=F(2*k*n*(k-1)*(n-k)*(n-k-1),(n-3)*(n-1)**2)
        tests+=1

# n=4 exact equality geometries
es=[(F(1),F(0)),(F(-1),F(0)),(F(0),F(1)),(F(0),F(-1))]
assert variance_formula(es,2)[0]==F(8,9)
es=[(F(1),F(0)),(F(1),F(0)),(F(-1),F(0)),(F(-1),F(0))]
assert variance_formula(es,2)[0]==F(32,9)
print('VERIFY_OK exact_subsets=%s geometry_equalities=2'%tests)
