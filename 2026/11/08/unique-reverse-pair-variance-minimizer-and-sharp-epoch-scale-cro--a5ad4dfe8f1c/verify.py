"""Finite consistency checks for exact reverse-epoch variance identities.

Run: python3 verify.py
The exhaustive tests below check finite cases, not an all-size proof.
"""
from fractions import Fraction as F
from itertools import permutations
from math import exp, factorial

checks = 0

def verify(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def weights(n, q):
    return [(1-q)*q**(n-j-1) for j in range(n)]

def perm_variance(weights, centers):
    n = len(weights)
    s = sum(centers, F(0))/n
    ss = sum((c-s)**2 for c in centers)/n
    total = sum(weights)
    return ss * (n*sum(x*x for x in weights)-total*total)/(n-1)

def direct_variance(weights, centers):
    n = len(weights)
    values = [sum((weights[j]*centers[p[j]] for j in range(n)),F(0)) for p in permutations(range(n))]
    m = sum(values,F(0))/len(values)
    return sum(((v-m)**2 for v in values),F(0))/len(values)

def reverse_weights(w):
    return [(w[j]+w[-1-j])/2 for j in range(len(w))]

def permuted_coupling_weights(w, sig):
    # A permuted traversal pi(sig(j)) puts positional weight w[j] on pi(sig(j)).
    v = list(w)
    for j,k in enumerate(sig):
        v[k] += w[j]
    return [x/2 for x in v]

def closed_variances(n,q,centers):
    s = sum(centers,F(0))/n
    ss = sum((x-s)**2 for x in centers)/n
    r = 1-q
    g = sum(q**(2*j) for j in range(n))
    W = 1-q**n
    U = r*r*g-W*W/n
    B = (r*r/2)*(g+n*q**(n-1))-W*W/n
    return ss*n*U/(n-1),ss*n*B/(n-1)

for n in range(2,8):
    centers = [F((3*i*i + 2*i + 1) % 19, 7) for i in range(n)]
    for q in (F(0), F(1,3), F(2,3)):
        w = weights(n,q)
        a,b = closed_variances(n,q,centers)
        verify(perm_variance(w,centers)==a, f'unpaired closed n={n}')
        verify(perm_variance(reverse_weights(w),centers)==b, f'paired closed n={n}')
        verify(direct_variance(w,centers)==a, f'unpaired exhaustive n={n}')
        verify(direct_variance(reverse_weights(w),centers)==b, f'paired exhaustive n={n}')
        verify(0<=b*2<a if q !=1 else True,f'negative covariance n={n}')
        if n==2:
            verify(b==0,'two-term exact cancellation')
        elif all(c==centers[0] for c in centers):
            verify(b==0,'degenerate centers')
        else:
            verify(b>0,'strict positive noise n>=3')

for n in range(2,6):
    centers = [F(i*i+3*i,7) for i in range(n)]
    q = F(2,5)
    w = weights(n,q)
    rev = tuple(reversed(range(n)))
    opt = perm_variance(reverse_weights(w),centers)
    for sig in permutations(range(n)):
        v = perm_variance(permuted_coupling_weights(w,sig),centers)
        verify(v>=opt, f'failed minimax n={n},sig={sig}')
        verify((v==opt)==(sig==rev),f'failed unique n={n},sig={sig}')

# Exact finite-time AR(1) second-moment recurrence for independently reshuffled epochs.
n=5
centers=[F(-2),F(1),F(7),F(3),F(0)]
q=F(3,5)
a,b=closed_variances(n,q,centers)
for innovation in (a,b):
    acc=F(0)
    for t in range(1,18):
        acc=q**(2*n)*acc+innovation
        verify(acc==innovation*(1-q**(2*n*t))/(1-q**(2*n)),'stationary recurrence')

# n -> infinity crossover and fixed-q half-variance limit.
def ratio(n,q):
    r=1-q
    W=1-q**n
    g=(1-q**(2*n))/(1-q*q)
    u=r*r*g-W*W/n
    v=r*r/2*(g+n*q**(n-1))-W*W/n
    return v/u

def continuum(L):
    z=exp(-L)
    u=L/2*(1-z*z)-(1-z)**2
    v=L/4*(1-z*z)+(L*L/2)*z-(1-z)**2
    return v/u
for L in (.5,1.,2.,5.,10.):
    verify(abs(ratio(10000,1-L/10000)-continuum(L))<0.003,'large-epoch crossover')
for q in (.1,.3,.7,.9):
    verify(abs(ratio(10000,q)-.5)<.006,'fixed-step half-variance limit')
for n in (3,4,5,8,12):
    r=F(1,10000)
    predicted=(n*n-4)*r*r/60
    verify(abs(ratio(n,1-r)/predicted-1)<.01,'small-step coefficient')

print(f'PASS {checks} exact/numerical assertions')
