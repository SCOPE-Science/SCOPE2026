"""Reproduce exact ear-covariance counts and harmonic crossover certificates.
Self-contained proof supplement; Python 3 standard library only.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import comb, cos, pi

count=0
def verify(x, reason):
    global count
    assert x, reason
    count+=1

def catalan(k):
    return comb(2*k,k)//(k+1)

def probs(n):
    a=F(catalan(n-3),catalan(n-2))
    b=F(catalan(n-4),catalan(n-2))
    return a,b

def eigen0(n):
    return F((n-5)*(n-4)*(n-1),2*(2*n-7)*(2*n-5)**2)

@lru_cache(None)
def triangulate(verts):
    """Ordered triangles of all triangulations of a convex vertex chain."""
    if len(verts)<=2:
        return ((),)
    if len(verts)==3:
        return ((verts,),)
    output=[]
    for j in range(1,len(verts)-1):
        for l in triangulate(verts[:j+1]):
            for r in triangulate(verts[j:]):
                output.append(((verts[0],verts[j],verts[-1]),)+l+r)
    return tuple(output)

for n in range(5,12):
    all_tr=triangulate(tuple(range(n)))
    verify(len(all_tr)==catalan(n-2), ('Catalan',n))
    occ=Counter()
    pair=Counter()
    for tr in all_tr:
        ts={frozenset(t) for t in tr}
        ears=[i for i in range(n) if frozenset(((i-1)%n,i,(i+1)%n)) in ts]
        for i in ears: occ[i]+=1
        for i in ears:
            for j in ears:
                pair[(i,j)]+=1
    p,q=probs(n)
    for i in range(n):
        verify(F(occ[i],len(all_tr))==p, ('marginal',n,i))
        for j in range(n):
            expected=p if j==i else (F(0) if (i-j)%n in (1,n-1) else q)
            verify(F(pair[(i,j)],len(all_tr))==expected,('joint',n,i,j))
    # Independent direct covariance-matrix Fourier test from enumerated events.
    for j in range(n):
        raw = 0j
        for d in range(n):
            second = F(pair[(0,d)],len(all_tr))
            raw += float(second-p*p)*complex(cos(2*pi*j*d/n), -__import__('math').sin(2*pi*j*d/n))
        expected = float(eigen0(n)) if j==0 else float(p-q)-2*float(q)*cos(2*pi*j/n)
        verify(abs(raw-expected)<1e-10,('direct Fourier',n,j,raw,expected))
    # Parseval: constant Fourier eigenvalue equals variance of ear count / n.
    variance = F(sum(sum(1 for i in range(n) if frozenset(((i-1)%n,i,(i+1)%n)) in {frozenset(t) for t in tr})**2 for tr in all_tr), len(all_tr)) - F(n)**2*p*p
    verify(variance==n*eigen0(n),('variance',n))

# Exact finite crossover proof: 223/71 < pi < 22/7,
# 1-cos(t) >= t^2/2-t^4/24 on 0<t<=2pi/5.
# Thus 1-cos(2pi/n) > 19.72/n^2 - (196/3)/n^4 for 5<=n<=20.
for n in range(5,21):
    lower=F(986,50*n*n)-F(196,3*n**4)
    rhs=F(3*n,2*(n-2)*(2*n-5))
    verify(lower>rhs,('rational crossover below',n,lower,rhs))
# For n>=21, 1-cos(2pi/n)<2pi^2/n^2, so it suffices that
# 3n^3>4(22/7)^2(n-2)(2n-5). With n=21+t this becomes
# 147t^3+5389t^2+49281t+359>0, t>=0.
for t in range(0,500):
    verify(147*t**3+5389*t**2+49281*t+359>0,('cubic',t))

for n in range(5,1001):
    p,q=probs(n)
    mean0=float(eigen0(n))
    spectrum=[mean0 if j==0 else float(p-q)-2*float(q)*cos(2*pi*j/n) for j in range(n)]
    verify(abs((min(spectrum[1:]) if n==5 else min(spectrum))-(min(spectrum[1:]) if n==5 else min(mean0,spectrum[1])))<1e-8,('min',n))
    verify(all(s>0 for s in spectrum[1:]),('all nonzero frequencies',n))
    verify((mean0==0)==(n==5),('constant null',n))
    if n>=6:
        verify((mean0<spectrum[1])==(n<=20),('switch',n))
    verify(abs(max(spectrum)-float(p-q-2*q*cos(2*pi*(n//2)/n)))<1e-8,('max',n))

p,q=probs(6)
verify(p+q==F(1,2), 'six maximal eigen')
verify(eigen0(6)==F(1,49), 'six minimal eigen')
verify((p+q)/eigen0(6)==F(49,2),'six sharp condition')
print('PASS',count,'assertions (exact Catalan enumeration, rational crossover, finite spectral stress tests)')
