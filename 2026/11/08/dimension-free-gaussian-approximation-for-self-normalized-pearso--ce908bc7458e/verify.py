"""Finite exact identities and sampling diagnostics for high-dimensional Pearson radial fluctuations."""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial, sqrt, gamma, isclose
import numpy as np

checks = 0

def ok(value):
    global checks
    assert value
    checks += 1

def double_factorial_odd(k):
    return factorial(2*k)//(2**k*factorial(k))

def spherical_monomial_moment(counts, d):
    if any(q % 2 for q in counts):
        return F(0)
    half = [q//2 for q in counts]
    m = sum(half)
    denom = 1
    for j in range(m):
        denom *= d+2*j
    numerator = 1
    for h in half:
        numerator *= double_factorial_odd(h)
    return F(numerator,denom)

def exact_edge_product(edges, d):
    result = F(0)
    for cc in product(range(d),repeat=len(edges)):
        degrees = [[0]*d for _ in range(max(max(e) for e in edges)+1)]
        for (i,j),k in zip(edges,cc):
            degrees[i][k] += 1
            degrees[j][k] += 1
        prob = F(1)
        for counts in degrees:
            prob *= spherical_monomial_moment(counts,d)
            if not prob: break
        result += prob
    return result

for d in (2,3,4):
    for n in (2,3,4):
        ee=list(combinations(range(n),2))
        for i,e in enumerate(ee):
            for j,f in enumerate(ee):
                ok(exact_edge_product((e,f),d)==(F(1,d) if e==f else 0))
            for j,f in enumerate(ee):
                for k,g in enumerate(ee):
                    is_triangle=len({*e,*f,*g})==3 and len({e,f,g})==3
                    ok(exact_edge_product((e,f,g),d)==(F(1,d*d) if is_triangle else 0))

for n in range(2,11):
    for typ in range(4):
        a=[F(1+i if typ==0 else 1 if typ==1 else (i+1)**2 if typ==2 else (i%3)+1) for i in range(n)]
        Q=sum((a[i]*a[j])**2 for i,j in combinations(range(n),2))
        T=sum(a[i]**2*a[j]**2*a[k]**2 for i,j,k in combinations(range(n),3))
        ee=list(combinations(range(n),2))
        second=sum(a[i]*a[j]*a[u]*a[v] for i,j in ee for u,v in ee if (i,j)==(u,v))
        third=sum(6*a[i]**2*a[j]**2*a[k]**2 for i,j,k in combinations(range(n),3))
        ok(second==Q and third==6*T)
        # Gaussian quadratic-form identity: 2 tr(B^2)=1 and E Y^4<=15.
        B=np.zeros((n,n))
        for i,j in ee:
            B[i,j]=B[j,i]=float(a[i]*a[j])/(2*sqrt(float(Q)))
        tr2=float(np.trace(B@B)); tr4=float(np.trace(B@B@B@B))
        ok(abs(2*tr2-1)<1e-10)
        ok(3+48*tr4 <= 15+1e-10)
        ok(6*float(T)/float(Q)**1.5<=6)

for d in range(2,401):
    # Use log-gamma for numerical stability in large dimension.
    import math
    eta=math.exp(0.5*math.log(2/d)+math.lgamma((d+1)/2)-math.lgamma(d/2))
    ok(0 <= 2*(1-eta*eta) <= 2/d+1e-10)

rng=np.random.default_rng(714209)
for d,n in [(3,2),(12,3),(40,6),(80,80),(120,3),(120,150)]:
    a=np.array([1.0+(i%7)/5.0 for i in range(n)])
    Q=((a*a).sum()**2-(a**4).sum())/2
    vals=[]
    for t in range(900):
        G=rng.standard_normal((n,d))
        U=G/np.linalg.norm(G,axis=1)[:,None]
        S=a@U
        Z=sqrt(d)*(S@S-np.dot(a,a))/(2*sqrt(Q))
        vals.append(Z)
    vals=np.array(vals)
    ok(abs(vals.mean()) < .2)
    ok(.76 < vals.var() < 1.25)

print(f"PASS: {checks} exact/structural and seeded numerical assertions")
