"""Deterministic finite checks of weighted-quorum identities.

This program verifies exact finite-size combinatorial identities used in the
analytic argument; it does not prove weak convergence or literature priority.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import factorial

checks=0

def check(x, text):
    global checks
    assert x, text
    checks += 1


def weights(n, power):
    v=[F(1,(j+1)**power) for j in range(n)]
    z=sum(v)
    return [a/z for a in v]


def subset_law(w, q):
    d={F(0):F(1)}
    for wi in w:
        e=defaultdict(F)
        for v,p in d.items():
            e[v]+=(1-q)*p
            e[v+wi]+=q*p
        d=dict(e)
    return d


def brute_law(w,q):
    n=len(w)
    d=defaultdict(F)
    for mask in range(1<<n):
        k=mask.bit_count()
        y=sum((w[j] for j in range(n) if mask>>j&1),F(0))
        d[y]+=q**k*(1-q)**(n-k)
    return dict(d)

for n in range(2,10):
    for power in (0,1,2):
        w=weights(n,power)
        s2=sum((a*a for a in w),F(0))
        check(sum(w)==1, 'weights normalization')
        check(0 < s2 <= 1, 'positive sum squares')
        for q in (F(1,4),F(1,3),F(1,2),F(2,3),F(3,4)):
            d=subset_law(w,q)
            brute=brute_law(w,q)
            check(d==brute,'recursion against independent subset enumeration')
            check(sum(d.values(),F(0))==1,'probabilities sum to one')
            m=sum((v*p for v,p in d.items()),F(0))
            check(m==q,'weighted mass mean')
            var=sum((p*(v-q)**2 for v,p in d.items()),F(0))
            check(var==q*(1-q)*s2,'weighted mass variance')
            for theta in (F(1,3),F(1,2),F(2,3)):
                cdf=sum((p for v,p in d.items() if v>theta),F(0))
                reverse=sum((p for v,p in brute.items() if v<=theta),F(0))
                check(cdf+reverse==1,'strict quorum CDF exactly equals positive weighted tail')

# The third and fourth cumulant identities of a weighted Bernoulli sum,
# checked by exact fourth moments for small arrays.
for n in range(2,9):
    for power in (0,1,2):
        w=weights(n,power)
        s2=sum(a*a for a in w)
        for q in (F(1,4),F(1,2),F(3,4)):
            d=subset_law(w,q)
            v=sum((p*(y-q)**2 for y,p in d.items()),F(0))
            k3=sum((p*(y-q)**3 for y,p in d.items()),F(0))
            k4=sum((p*(y-q)**4 for y,p in d.items()),F(0))-3*v*v
            check(k3==q*(1-q)*(1-2*q)*sum(a**3 for a in w), 'third cumulant')
            check(k4==q*(1-q)*(1-6*q*(1-q))*sum(a**4 for a in w),'fourth cumulant')

# Zipf normalization scale identities exact at finite n.
for n in (5,10,20,100,500):
    w=weights(n,1)
    h1=sum((F(1,j) for j in range(1,n+1)),F(0))
    h2=sum((F(1,j*j) for j in range(1,n+1)),F(0))
    check(sum(a*a for a in w)==h2/(h1*h1),'Zipf scale')

print('PASS',checks,'exact rational checks')
