"""Exact rational diagnostics for Gini variation under bipartite Markov heat.

Run: python verify.py. No external dependencies are required.
"""
from fractions import Fraction as F
from random import Random


def gini(v):
    return sum(abs(v[i]-v[j]) for i in range(len(v)) for j in range(i+1,len(v)))


def heat(v,p,q,a):
    assert len(v)==p+q and 0 <= a <= 1
    u=sum(v[:p])/p; w=sum(v[p:])/q
    z=(u+w)/2; d=(u-w)*a*a/2
    return [z+d+a*(x-u) for x in v[:p]]+[z-d+a*(x-w) for x in v[p:]]


def cut_coefficient(p,q,r,s):
    k=r+s
    if k==0 or k==p+q:
        raise ValueError('constant cut')
    d=F(r,p)-F(s,q)
    eq=r*s+(p-r)*(q-s)
    e=-p*q*d*d+eq*abs(d)
    return e/F(k*(p+q-k))


def best_coefficient(p,q):
    return max((cut_coefficient(p,q,r,s),r,s) for r in range(p+1)
               for s in range(q+1) if 0<r+s<p+q)


def norm_formula(p,q,a):
    return a*(1+(1-a)*best_coefficient(p,q)[0])


count=0
for p in range(1,11):
    for q in range(1,11):
        n=p+q
        for a in (F(1,4),F(1,2),F(3,4),F(1)):
            expected=norm_formula(p,q,a)
            direct=F(-1)
            for r in range(p+1):
                for s in range(q+1):
                    if not 0<r+s<n:continue
                    v=[F(1)]*r+[F(0)]*(p-r)+[F(1)]*s+[F(0)]*(q-s)
                    ratio=gini(heat(v,p,q,a))/gini(v)
                    direct=max(direct,ratio)
                    count+=1
            assert direct==expected, (p,q,a,direct,expected)
print('EXACT_FULL_CUT_OPERATOR_NORMS_PASSED',count)

rng=Random(836171)
count=0
for p in range(1,12):
    for q in range(1,12):
        for a in (F(1,5),F(2,5),F(3,5),F(4,5)):
            bound=norm_formula(p,q,a)
            for trial in range(12):
                x=[F(rng.randint(-7,7)) for _ in range(p+q)]
                if gini(x)==0:continue
                assert gini(heat(x,p,q,a)) <= bound*gini(x)
                count+=1
print('EXACT_SIGNED_INPUT_TESTS_PASSED',count)

for p in range(1,25):
    for q in range(1,25):
        C,r,s=best_coefficient(p,q)
        assert C < 1 and C>=-1
        for a in (F(1,7),F(1,2),F(6,7)):
            assert norm_formula(p,q,a) <= a*(2-a)
print('STRICT_FINITE_CONTRACTION_AND_UNIFORM_ENVELOPE_PASSED',24*24)

for p in (10,20,40,80,160):
    q=p*p
    lower=F(q*(p-2),p*(p+q-1))
    print('SHARP_ENVELOPE_APPROXIMATION',p,q,str(lower))
print('ALL_BIPARTITE_GINI_HEAT_DIAGNOSTICS_PASSED')
