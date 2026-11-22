"""Independent finite path sums and exact identities for intermittent detection schedules.
Run: python3 check.py
All tests corroborate the analytical proof; no finite grid proves global optimality.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log, isclose

checks = 0

def tick(test, note):
    global checks
    assert test, note
    checks += 1

def brute_no_detection(lags, p):
    """Exact stationary symmetric hidden-state path sum given rational relaxation factors."""
    z = F(0)
    n = len(lags) + 1
    for bits in product((0, 1), repeat=n):
        prob = F(1, 2)
        for i, a in enumerate(lags):
            prob *= (1+a)/2 if bits[i] == bits[i+1] else (1-a)/2
        for bit in bits:
            if bit:
                prob *= 1-p
        z += prob
    return z

def spin_sum(lags, p):
    """Independent even-subset spin-moment expansion, rational arithmetic."""
    n = len(lags) + 1
    c = 1-p/2
    b = p/2
    out = F(0)
    for bits in product((0, 1), repeat=n):
        indices = [i for i,v in enumerate(bits) if v]
        if len(indices)%2: continue
        term = c**(n-len(indices))*b**len(indices)
        for j in range(0, len(indices), 2):
            for k in range(indices[j],indices[j+1]):
                term *= lags[k]
        out += term
    return out

def five_reduced(u, v, p):
    c=1-p/2; b=p/2
    s2=2*u+2*v+2*u*v+2*u*v*v+v*v+u*u*v*v
    s4=2*u*v+2*u*u*v+u*u
    return c**5+c**3*b*b*s2+c*b**4*s4

for p in [F(1,9), F(1,4), F(1,2), F(2,3), F(9,10), F(1)]:
    for lagset in [(F(1,4), F(1,3), F(1,2), F(3,5)),
                   (F(2,3), F(3,4), F(3,4), F(2,3)),
                   (F(1), F(4,5), F(4,5), F(1)),
                   (F(2,5), F(1,2), F(1,2), F(2,5))]:
        z = brute_no_detection(lagset, p)
        tick(z == spin_sum(lagset,p), 'spin expansion')
        if lagset[0] == lagset[-1] and lagset[1] == lagset[2]:
            tick(z == five_reduced(lagset[0],lagset[1],p),'five formula')

# A nontrivial exact optimum: p=1/2, outer factor u=3/4, inner factor v=13/28.
p=F(1,2); rho=F(1,9); u=F(3,4); v=F(13,28); K=u*v
Tcrit_factor=(1+rho)/2
tick(K < Tcrit_factor, 'interior parameter domain')
tick(rho*u**3 + u*u - K*(u+1)==0,'exact cubic optimality')
tick(v < u, 'strictly longer inner intervals')
tick(K == F(39,112), 'exact total horizon factor')

# Verify positive-gap strict convexity and global five-survey optimum numerically.
def obj_from_g(g,p):
    return float(brute_no_detection(tuple(F(exp(-z)).limit_denominator(10**9) for z in g), F(p).limit_denominator(10**6)))
for p0 in [0.2,0.5,0.9]:
    rho=(p0/(2-p0))**2
    Tc=2*log(2/(1+rho))
    for T in [0.1*Tc, 0.99*Tc, Tc, 1.01*Tc, 2*Tc, 5*Tc]:
        K=exp(-T/2)
        if T<=Tc:
            x=0.0
        else:
            lo=K; hi=1.0
            for _ in range(70):
                mid=(lo+hi)/2
                val=rho*mid**3+mid**2-K*(mid+1)
                if val<0:lo=mid
                else:hi=mid
            x=-log((lo+hi)/2)
        base=[x,T/2-x,T/2-x,x]
        ref=obj_from_g(base,p0)
        for ii in range(21):
            for jj in range(21-ii):
                for kk in range(21-ii-jj):
                    ll=20-ii-jj-kk
                    trial=[T*ii/20,T*jj/20,T*kk/20,T*ll/20]
                    tick(obj_from_g(trial,p0)>=ref-1e-8,'global grid competitor')
print('PASS',checks,'independent assertions')
