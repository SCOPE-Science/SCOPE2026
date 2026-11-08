#!/usr/bin/env python3
"""Independent finite-state and algebra checks for leaf-degree-driven random trees.

The analytic limit theorems require their separate proofs; finite checks are not proofs.
Run: python3 check_leafpa.py
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import sqrt

ASSERTIONS = 0

def check(condition, explanation):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(explanation)


def leaves_degrees(edges, n):
    deg=[0]*(n+1)
    neighbours=[[] for _ in range(n+1)]
    for u,v in edges:
        deg[u]+=1;deg[v]+=1
        neighbours[u].append(v);neighbours[v].append(u)
    ld=[0]*(n+1)
    for v in range(1,n+1):
        ld[v]=sum(deg[w]==1 for w in neighbours[v])
    return deg,ld


def full_tree_distribution(a, maxn=8):
    # Independent calculation using the FULL labelled tree (no leaf-count reduction).
    trees={((1,2),):Q(1)}
    dist={3:{2:Q(1)}}
    for n in range(2,maxn):
        nexttrees=defaultdict(Q)
        for edges, prob in trees.items():
            deg,ld=leaves_degrees(edges,n)
            normalizer=sum((ld[v]+a for v in range(1,n+1)),Q(0))
            check(normalizer==sum(deg[v]==1 for v in range(1,n+1))+n*a,
                  f'weight normalization, n={n}')
            for v in range(1,n+1):
                nexttrees[edges+((v,n+1),)] += prob*(ld[v]+a)/normalizer
            if n>=3:
                count=sum(deg[v]==1 for v in range(1,n+1))
                leaf_weight=sum((ld[v]+a for v in range(1,n+1) if deg[v]==1),Q(0))
                check(leaf_weight==a*count,f'leaf attachment weight, n={n}')
        trees=nexttrees
        check(sum(trees.values(),Q(0))==1,f'full-tree probability, n={n+1}')
        if n>=3:
            observed=defaultdict(Q)
            for edges,p in trees.items():
                deg,_=leaves_degrees(edges,n+1)
                observed[sum(deg[v]==1 for v in range(1,n+2))]+=p
            dist[n+1]=dict(observed)
    return dist


def reduced_distribution(a, maxn=8):
    state={2:Q(1)}
    out={3:state}
    for n in range(3,maxn):
        nextstate=defaultdict(Q)
        for leaf,p in state.items():
            gain=1-(a*leaf)/(leaf+a*n)
            check(0<=gain<=1,f'probabilities, {a}, {n}, {leaf}')
            nextstate[leaf]+=p*(1-gain)
            nextstate[leaf+1]+=p*gain
        state=dict(nextstate)
        check(sum(state.values(),Q(0))==1,f'reduced mass n={n+1}')
        out[n+1]=state
    return out

for a in (Q(1,5),Q(1,2),Q(1),Q(2),Q(5)):
    original=full_tree_distribution(a)
    reduced=reduced_distribution(a)
    for n in range(4,9):
        check(original[n]=={k:v for k,v in reduced[n].items() if v},
              f'exact distribution comparison: a={a}, n={n}')

# Polynomial arithmetic: derivative of r^3(1-r)/(3r^2-4r+2)
# has numerator -r^2(6r^3-15r^2+16r-6).
def multiply(x,y):
    z=[Q(0)]*(len(x)+len(y)-1)
    for i,u in enumerate(x):
        for j,v in enumerate(y):
            z[i+j]+=u*v
    return z

def diff(x): return [i*x[i] for i in range(1,len(x))]

def subtract(x,y):
    n=max(len(x),len(y));return [(x[i] if i<len(x) else Q(0))-(y[i] if i<len(y) else Q(0)) for i in range(n)]

N=[Q(0),Q(0),Q(0),Q(1),Q(-1)]
D=[Q(2),Q(-4),Q(3)]
dnum=subtract(multiply(diff(N),D),multiply(N,diff(D)))
check(dnum==[Q(0),Q(0),Q(6),Q(-16),Q(15),Q(-6)], 'derivative identity')

def H(r): return 6*r**3-15*r**2+16*r-6
check(H(Q(1,2))<0 and H(Q(1))>0,'root existence')
check(H(Q(7244360,10000000))<0 and H(Q(7244361,10000000))>0,
      'root bracket')
# H'(r)=18 r^2-30 r+16>0 because its discriminant is negative.
check(30**2-4*18*16<0,'uniqueness of root')

def parameters(a):
    r=.5-a+sqrt(a*a+.25)
    kap=(a/(a+r))**2
    variance=r*(1-r)/(1+2*kap)
    return r,kap,variance

def variance_in_r(r): return r**3*(1-r)/(3*r*r-4*r+2)

for a in (.01,.1,.2,.44473363454726733,1,2,10,1000):
    r,kap,v=parameters(a)
    check(abs(r-(1-a*r/(a+r)))<1e-12, 'fixed point')
    check(abs(kap-((1-r)/r)**2)<1e-11, 'drift coefficient')
    check(abs(v-variance_in_r(r))<1e-12, 'variance parameterization')
    check(.5<r<1 and v>0,'domain')

check(abs(variance_in_r(.5)-1/12)<1e-15,'recursive-tree endpoint')
check(abs(variance_in_r(1))<1e-15,'star endpoint')
_,_,peak=parameters(.44473363454726733)
check(peak>parameters(1)[-1]>1/12 and peak>parameters(.1)[-1],
      'nonmonotone variance observed at rational test parameters')
print('PASS:',ASSERTIONS,'exact state-distribution and algebra checks')
print('a*=0.4447336345... gives variance=',peak)
print('a=1 gives variance=',parameters(1)[-1])
