"""Exact independent checks of the wheel parking comparison theorem.

Run: python verify.py  (Python standard library only).
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations
from math import comb

checks = 0

def check(test, why):
    global checks
    checks += 1
    if not test:
        raise AssertionError(why)

def convolution(a, b):
    out = defaultdict(Q)
    for j, p in a.items():
        for k, q in b.items():
            out[j+k] += p*q
    return dict(out)

# Independent first-choice recursion on all paths.
P = {-1: {0: Q(1)}, 0: {0: Q(1)}}
for m in range(1, 65):
    law = defaultdict(Q)
    for j in range(m):
        for k, p in convolution(P[j-1], P[m-j-2]).items():
            law[k+1] += p/Q(m)
    P[m] = dict(law)
    check(sum(P[m].values()) == 1, 'path probability normalization')

# Gaps of 2 and 3 between selected vertices characterize all
# inclusion-maximal independent sets of a cycle.
def static_cycle(n):
    a = {}
    for k in range((n+2)//3, n//2 + 1):
        t = n-2*k
        if 0 <= t <= k:
            a[k] = n*comb(k,t)//k
            check(n*comb(k,t)%k == 0, 'integral cycle count')
    M = sum(a.values())
    return {k:Q(c,M) for k,c in a.items()}, M

def seq_cycle(n):
    return {k+1:v for k,v in P[n-3].items()}

def wheel_laws(n):
    s=seq_cycle(n)
    t,M=static_cycle(n)
    ws=defaultdict(Q, {k:Q(n,n+1)*v for k,v in s.items()})
    ws[1]+=Q(1,n+1)
    wt=defaultdict(Q, {k:Q(M,M+1)*v for k,v in t.items()})
    wt[1]+=Q(1,M+1)
    return dict(ws),dict(wt),M

# Independent generic graph enumeration: label permutations, greedy
# inclusion-maximal set sizes, and all maximal independent subsets.
def graph_laws(n):
    N=n+1
    neighbors=[]
    for v in range(n):
        neighbors.append((1<<n) | (1<<((v-1)%n)) | (1<<((v+1)%n)))
    neighbors.append((1<<n)-1)
    all_sets=[]
    for mask in range(1<<N):
        if any((neighbors[v]&mask) for v in range(N) if mask>>v&1):
            continue
        if all((mask>>v&1) or (neighbors[v]&mask) for v in range(N)):
            all_sets.append(mask)
    stats=defaultdict(int)
    for mask in all_sets: stats[mask.bit_count()]+=1
    out_static={k:Q(v,len(all_sets)) for k,v in stats.items()}
    counts=defaultdict(int)
    from math import factorial
    for order in permutations(range(N)):
        mask=0
        for v in order:
            if not mask & neighbors[v]: mask|=1<<v
        counts[mask.bit_count()]+=1
    out_seq={k:Q(v,factorial(N)) for k,v in counts.items()}
    return out_seq,out_static

# Brute all labeled orderings through a seven-vertex wheel (7! cases).
for n in range(3,7):
    seq,sta,M=wheel_laws(n)
    s2,t2=graph_laws(n)
    check(seq==s2, f'independent sequential enumeration W_{n+1}')
    check(sta==t2, f'independent static enumeration W_{n+1}')

# Exhaustive finite boundary comparison, with exact rational arithmetic.
min_gap=None
for n in range(3,44):
    seq,sta,M=wheel_laws(n)
    check(sum(seq.values())==sum(sta.values())==1, f'wheel normalized {n}')
    check(M>=1, 'cycle MIS nonempty')
    dist=[sum(v for k,v in seq.items() if k<=j)-sum(v for k,v in sta.items() if k<=j)
          for j in range(n//2+1)]
    if n in (3,5,7):
        check(all(q==0 for q in dist), f'exact equality n={n}')
    elif n in (4,6):
        check(all(q<=0 for q in dist) and any(q<0 for q in dist), f'dominance n={n}')
    else:
        check(dist[1]>0, f'hub CDF reversed at n={n}')
        mean_diff=sum(k*v for k,v in seq.items())-sum(k*v for k,v in sta.items())
        check(mean_diff>0, f'positive mean gap n={n}')
        check(any(x<0 for x in dist), f'negative CDF witness n={n}')
        min_gap=mean_diff if min_gap is None or mean_diff<min_gap else min_gap

# Rigorous rational certificates used for n>=44: the real root
# rho of lambda^3-lambda-1 is in (33/25, 133/100).
def f(x): return x*x*x-x-1
check(f(Q(33,25))<0<f(Q(133,100)), 'plastic root interval')
# c_0<0.413 from c_0=1/(3-rho^{-2}).
check(Q(1)/(3-Q(1)/Q(33,25)**2)<Q(413,1000), 'dominant derivative')
check(Q(1)/(3-Q(133,100))<Q(3,5), 'complex derivative')
check(Q(33,25)**3>Q(9,4), 'complex root ratio <2/3')
r=Q(2,3)**20
check((Q(413,1000)+Q(6,5)*r)/(1-2*r)<Q(42,100), 'static density bound')
# e^2>22/3 by truncation of its positive exponential series.
from math import factorial
check(sum(Q(2**j,factorial(j)) for j in range(7))>Q(22,3),'exp bound')
# Bound absolute coefficient-tail error in the cycle mean, for n>=20.
error=Q(2**19,2*factorial(19))/(1-Q(1,5))
check(error<Q(1,10**9), 'mean remainder bound')
check(Q(19,44)*20-Q(1,10**9)>Q(43,100)*20,'sequential density bound')
check(Q(1,100)*44-Q(43,100)>0,'all larger wheel mean gaps')
print(f'PASS: {checks} exact assertions; smallest finite mean gap = {min_gap}')
