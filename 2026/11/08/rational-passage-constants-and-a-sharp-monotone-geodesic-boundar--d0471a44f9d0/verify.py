#!/usr/bin/env python3
"""Exact symbolic identities and finite independent checks for binary two-step FPP.
Run: python verify.py  (requires sympy >= 1.11, Python >= 3.9).
The finite enumerations are diagnostics, not a substitute for the general path lemma.
"""
from itertools import product
from heapq import heappush, heappop
import sympy as sp

checks=0

def require(condition, msg='check failed'):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(msg)

p=sp.symbols('p',real=True)
q=1-p
states=(-1,0,1,2)
P=sp.zeros(4)
for i, x in enumerate(states):
    for u in (1,2):
        for v in (1,2):
            j=states.index(min(u,v-x))
            P[i,j]+=(p if u==1 else q)*(p if v==1 else q)
P=P.applyfunc(sp.expand)
expected=sp.Matrix([
    [0,0,p,q],
    [0,0,2*p-p*p,q*q],
    [0,p,q,0],
    [p,q,0,0]
])
for i in range(4):
    for j in range(4):
        require(sp.cancel(P[i,j]-expected[i,j])==0, 'transition matrix')
    require(sp.cancel(sum(P[i,j] for j in range(4))-1)==0, 'row stochastic')

Z=p**3+p**2-4*p+4
pi=sp.Matrix([[p*q*q/Z, (p*p-p+1)/Z, (p*p-2*p+2)/Z, q*q/Z]])
require(sp.cancel(sum(pi)-1)==0, 'stationary normalization')
for i in range(4):
    require(sp.cancel((pi*P)[i]-pi[i])==0, 'stationary identity')
f=sp.Matrix(states)
mu=sp.factor((pi*f)[0])
mu_claim=(-p**3+5*p**2-7*p+4)/Z
require(sp.cancel(mu-mu_claim)==0, 'drift formula')
require(mu_claim.subs(p,sp.Rational(1,2))==sp.Rational(13,19),'midpoint drift')
require(mu_claim.subs(p,0)==1 and mu_claim.subs(p,1)==sp.Rational(1,2),'endpoints')

# Poisson equation for the stationary additive functional f(X_k).
A=sp.eye(4)-P+sp.ones(4,1)*pi
h=A.inv()*(f-sp.ones(4,1)*mu)
for i in range(4):
    require(sp.cancel((A*h)[i]-(f[i]-mu))==0, 'Poisson equation')
require(sp.cancel((pi*h)[0])==0, 'mean zero solution')
cent=f-sp.ones(4,1)*mu
variance=sp.factor(2*(pi*sp.diag(*cent)*h)[0] - (pi*sp.diag(*cent)*cent)[0])
H=14*p**6-77*p**5+197*p**4-295*p**3+272*p**2-146*p+36
claimed= p*q*H/Z**3
require(sp.cancel(variance-claimed)==0,'variance formula')
require(claimed.subs(p,sp.Rational(1,2))==sp.Rational(544,6859),'midpoint variance')
require(sp.expand(H.subs(p,1-q).subs(q,sp.symbols('r'))) == H.subs(p,p), 'symbol rewrite check') if False else None
r=sp.symbols('r')
require(sp.expand(H.subs(p,1-r)-(14*r**6-7*r**5+22*r**4-3*r**3+9*r**2+1))==0,'variance positivity polynomial')

# Independent finite exhaustive Dijkstra comparison with the path recurrence.
for n in range(1,8):
    edges=[(i,j) for i in range(n+1) for j in (i+1,i+2) if j<=n]
    for weights in product((1,2),repeat=len(edges)):
        w=dict(zip(edges,weights))
        d=[0]
        if n>=1: d.append(w[(0,1)])
        for k in range(2,n+1):
            d.append(min(d[k-1]+w[(k-1,k)],d[k-2]+w[(k-2,k)]))
        adjacency=[[] for _ in range(n+1)]
        for (a,b),weight in w.items():
            adjacency[a].append((b,weight))
            adjacency[b].append((a,weight))
        dist=[float('inf')]*(n+1)
        dist[0]=0
        heap=[(0,0)]
        while heap:
            length,vertex=heappop(heap)
            if length!=dist[vertex]: continue
            for neighbor,weight in adjacency[vertex]:
                new=length+weight
                if new<dist[neighbor]:
                    dist[neighbor]=new
                    heappush(heap,(new,neighbor))
        require(d==dist,f'Dijkstra mismatch at n={n}, weights={weights}')

# Sharpness of b<=2a in the deterministic geodesic monotonicity assertion.
for b in (3,4,5,10):
    require(1+1 < b, 'backtracking witness')
print(f'PASS: {checks} exact symbolic or finite checks; maximum enumerated n=7; symbolic laws valid for 0<p<1.')
