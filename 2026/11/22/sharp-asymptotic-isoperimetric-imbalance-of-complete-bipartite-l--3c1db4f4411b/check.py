"""Independent numerical checks for the Euclidean geometry of the full-column
complete-bipartite Laplacian simplex. Requires NumPy; no external data.
"""
import math
import numpy as np


def formula(p, q):
    n = p + q
    d = n - 1
    a, b = p / n, q / n
    va = n**1.5 * (p ** (q - 1)) * (q ** (p - 1)) / math.factorial(d)
    fa = math.sqrt(1 - (1 + b + b*b) / n) / q
    fb = math.sqrt(1 - (1 + a + a*a) / n) / p
    sa = d * va * (p * fa + q * fb)
    return va, sa, fa, fb


def direct(p, q):
    n=p+q
    L=np.zeros((n,n), dtype=float)
    for i in range(p):
        for j in range(p,n):
            L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    vertices=L.T
    def vol(v):
        E=v[1:]-v[0]
        sign, logdet=np.linalg.slogdet(E@E.T)
        assert sign>0
        return math.exp(logdet/2-math.lgamma(len(v)))
    va=vol(vertices)
    facets=[vol(np.delete(vertices,i,axis=0)) for i in range(n)]
    return va,sum(facets),facets


def iso(p,q):
    n=p+q;d=n-1;a=p/n;b=q/n
    T=(p/q)*math.sqrt(1-(1+b+b*b)/n)+(q/p)*math.sqrt(1-(1+a+a*a)/n)
    # compute log volume stably
    logv=1.5*math.log(n)+(q-1)*math.log(p)+(p-1)*math.log(q)-math.lgamma(n)
    return d*T*math.exp(logv/d)


def H(a):
    if a == 0 or a == 0.5:return 1.0
    b=1-a
    return (a/b+b/a)*a**b*b**a

for n in range(3,11):
    for p in range(1,n):
        q=n-p
        v,s,fa,fb=formula(p,q)
        v0,s0,areas=direct(p,q)
        assert math.isclose(v,v0,rel_tol=2e-9), (n,p,v,v0)
        assert math.isclose(s,s0,rel_tol=2e-9), (n,p,s,s0)
        for i,area in enumerate(areas):
            exp=(n-1)*v*(fa if i<p else fb)
            assert math.isclose(area,exp,rel_tol=2e-9), (n,p,i,area,exp)
print('DIRECT_VOLUME_FACET_AREA_PASS: 44 bipartitions n=3..10')

# Independent asymptotic calculation, using only stable log gamma and exact
# finite formula, tests the mathematical predictions but does not prove them.
for n in [100,200,400,800,1600,3200]:
    values=[iso(p,n-p)/(n-1) for p in range(1,n//2+1)]
    p=1+max(range(len(values)),key=lambda i:values[i])
    print('n=%d best_p=%d fraction=%.9f quotient_scaled=%.9f balanced=%.9f' %
          (n,p,p/n,max(values),values[-1]))
    assert abs(max(values)-3.0955144919803804)<8/n+0.03
print('BIPARTITE_ISOPERIMETRIC_PROFILE_PASS')
