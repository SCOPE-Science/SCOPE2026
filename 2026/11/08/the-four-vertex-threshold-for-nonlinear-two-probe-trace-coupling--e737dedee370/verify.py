"""Exact checks for two-probe Rademacher trace coupling on complete graphs.

Run with Python 3 standard library: python verify.py
The analytic proof in RESULT.md establishes all dimensions; checks are finite.
"""
from fractions import Fraction
from itertools import product
from math import comb
import random

checks = 0

def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def antitone_covariance(values):
    """Uniform finite law, sorted anti-pairing. Values may be rational."""
    vals = sorted(values)
    n = len(vals)
    m = sum(vals, Fraction(0)) / n
    return sum((vals[i]-m)*(vals[n-1-i]-m) for i in range(n)) / n


def compressed_covariance(n):
    """Exact binomial lumping; O(n) arithmetic and no sign-vector list."""
    counts = {}
    for j in range(n+1):
        x = ((n-2*j)**2-n)//2
        counts[x] = counts.get(x,0)+comb(n,j)
    ascending = sorted(counts.items())
    descending = ascending[::-1]
    i=j=0
    left=right=0
    total=0
    while i<len(ascending) and j<len(descending):
        if left == 0:
            left=ascending[i][1]
        if right == 0:
            right=descending[j][1]
        common=min(left,right)
        total += common*ascending[i][0]*descending[j][0]
        left -= common
        right -= common
        if not left:
            i+=1
        if not right:
            j+=1
    check(i==len(ascending) and j==len(descending), "all cumulative counts consumed")
    return Fraction(total,2**n)


def full_probe_values(n, edges):
    vals=[]
    signs=list(product((-1,1),repeat=n))
    for s in signs:
        vals.append(sum(Fraction(w)*s[u]*s[v] for u,v,w in edges))
    return signs, vals


def best_flip_covariance(n, edges):
    signs,vals=full_probe_values(n,edges)
    mean=sum(vals,Fraction(0))/len(vals)
    indexed=dict(zip(signs,vals))
    best=None
    for flip in product((-1,1),repeat=n):
        c=sum((indexed[s]-mean)*(indexed[tuple(s[i]*flip[i] for i in range(n))]-mean) for s in signs)/len(signs)
        if best is None or c<best:
            best=c
    return best

# Low-dimensional theorem: all 2x2 and 3x3 symmetric weighted edge patterns.
rng=random.Random(640219)
for n in (1,2,3):
    eidx=[(u,v) for u in range(n) for v in range(u+1,n)]
    for iteration in range(100):
        edges=[(u,v,rng.randint(-9,9)) for u,v in eidx]
        _,vals=full_probe_values(n,edges)
        check(antitone_covariance(vals)==best_flip_covariance(n,edges), f"n={n}, case {iteration}")

# Verify every binomial-valued scalar distribution for n<=12 in two independent ways.
for n in range(2,13):
    s,vals=full_probe_values(n,[(i,j,1) for i in range(n) for j in range(i+1,n)])
    c=compressed_covariance(n)
    check(c==antitone_covariance(vals),f"n={n} compressed quantile law")
    v=Fraction(n*(n-1),2)
    check(sum(vals)==0,f"n={n} centered")
    check(sum(x*x for x in vals)/len(vals)==v,f"n={n} Walsh variance")
    for k in range(n+1):
        flip=(-1,)*k+(1,)*(n-k)
        tab=dict(zip(s,vals))
        cc=sum(tab[z]*tab[tuple(z[i]*flip[i] for i in range(n))] for z in s)/len(s)
        check(cc==v-2*k*(n-k),f"n={n}, k={k} flip covariance")
    if n>=4:
        check(c < v-2*(n*n//4),f"n={n} strict nonlinear benefit")
    if n==3:
        check(c==v-2*(n*n//4),"triangle equality")

# All n up to 128: exact integer binomial recurrence and strict dominance.
for n in range(4,129):
    c=compressed_covariance(n)
    v=Fraction(n*(n-1),2)
    optimum=2*(v+c)              # variance for (zAz + z'Az')/2
    best_fixed=4*(v-(n*n//4))
    check(0<=optimum<best_fixed,f"n={n} exact rational benchmark")

# Explicit four-vertex witness (A is the unweighted K4 adjacency).
n=4
c=compressed_covariance(n)
v=Fraction(n*(n-1),2)
check(c==-3,"K4 antitone covariance")
check(2*(v+c)==6,"K4 optimal trace-estimator variance")
check(4*(v-n*n//4)==8,"K4 best fixed flip variance")
check(2*v==12,"K4 independent variance")

# Analytic strictness witness, evaluated exactly for a large finite range.
for n in range(4,129):
    k=n//2
    f=n-2*k
    qa=Fraction((n-4)**2-n,2)
    qb=Fraction((n-2)**2-n,2)
    pa=Fraction(f*f-n,2)
    pb=Fraction((f+2)**2-n,2)
    check(qb>qa and pb>pa,f"n={n} crossed-order witness")

print("K4: independent=12; best_fixed_flip=8; global_optimum=6")
for n in (3,4,5,6,7,8,10,12,16,32):
    c=compressed_covariance(n)
    v=Fraction(n*(n-1),2)
    print(f"K{n}: global={2*(v+c)}, fixed={4*(v-n*n//4)}, independent={2*v}")

print(f"PASS: {checks} exact assertions")
