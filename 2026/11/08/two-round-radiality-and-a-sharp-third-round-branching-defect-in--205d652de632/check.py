#!/usr/bin/env python3
"""Exact finite-state checks for iterated probabilistic triadic closure.
Standard library only. No external data or dependencies. Scientific, not certification.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations, product
from math import comb

# Polynomials over Z[p] stored in coefficient tuples, exact arithmetic.
def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,c in enumerate(a):z[i]+=c
    for i,c in enumerate(b):z[i]+=c
    while len(z)>1 and z[-1]==0:z.pop()
    return tuple(z)
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    while len(z)>1 and z[-1]==0:z.pop()
    return tuple(z)
def powpoly(a,n):
    b=(1,)
    for _ in range(n):b=mul(b,a)
    return b

def graph_pairs(n):return list(combinations(range(n),2))
def mask_of(n, edges):
    idx={x:i for i,x in enumerate(graph_pairs(n))}
    return sum(1<<idx[tuple(sorted(x))] for x in edges)
def eligible(n,mask):
    pairs=graph_pairs(n); adj=[0]*n
    for i,(a,b) in enumerate(pairs):
        if mask>>i&1:adj[a]|=1<<b;adj[b]|=1<<a
    return [i for i,(a,b) in enumerate(pairs)
            if not mask>>i&1 and adj[a]&adj[b]]

def symbolic_transition(n,edges,rounds):
    states={mask_of(n,edges):(1,)}
    for _ in range(rounds):
        new=defaultdict(lambda:(0,))
        for mask,weight in states.items():
            eligible_edges=eligible(n,mask);m=len(eligible_edges)
            for subset in range(1<<m):
                next_mask=mask
                for j,edge_index in enumerate(eligible_edges):
                    if subset>>j&1:next_mask|=1<<edge_index
                # p^selected (1-p)^rejected; integer coefficients.
                k=subset.bit_count()
                factor=(0,)*k+tuple((-1)**i*comb(m-k,i) for i in range(m-k+1))
                new[next_mask]=add(new[next_mask],mul(weight,factor))
        states=dict(new)
    mass=(0,)
    for poly in states.values():mass=add(mass,poly)
    assert mass==(1,),('probability mass not one',mass)
    return states

def prob(states,n,pair):
    i=graph_pairs(n).index(tuple(sorted(pair)))
    z=(0,)
    for mask,weight in states.items():
        if mask>>i&1:z=add(z,weight)
    return z

def evaluate(a,p):
    return sum((c*(p**i) for i,c in enumerate(a)),Fraction())

def distances(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    all_dist=[]
    for s in range(n):
        d=[None]*n;d[s]=0;queue=deque([s])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if d[v] is None:d[v]=d[u]+1;queue.append(v)
        all_dist.append(d)
    return all_dist

def prufer_edges(n,code):
    if n==2:return [(0,1)]
    d=[1]*n
    for u in code:d[u]+=1
    e=[]
    for u in code:
        v=next(i for i in range(n) if d[i]==1)
        e.append((u,v));d[u]-=1;d[v]-=1
    u,v=[i for i in range(n) if d[i]==1]
    e.append((u,v));return e

def test_exact():
    runs=0
    # Every labelled tree of sizes 2..5 at p=1/2, all pair probabilities after 2 rounds.
    expected={1:Fraction(1),2:Fraction(3,4),3:Fraction(3,8),4:Fraction(1,8)}
    for n in range(2,6):
        for code in product(range(n),repeat=n-2):
            edges=prufer_edges(n,code)
            d=distances(n,edges)
            states=symbolic_transition(n,edges,2)
            for a,b in combinations(range(n),2):
                assert evaluate(prob(states,n,(a,b)),Fraction(1,2))==expected[d[a][b]],(n,code,a,b)
                runs+=1
    # Explicit symbolic check, all real p, for the minimal branched counterexample.
    path=[(0,1),(1,2),(2,3)]
    branch=path+[(1,4)]
    bare=prob(symbolic_transition(4,path,3),4,(0,3))
    unbranched=prob(symbolic_transition(5,path+[(0,4)],3),5,(0,3))
    assert unbranched==bare, (unbranched,bare)
    leafy=prob(symbolic_transition(5,branch,3),5,(0,3))
    diff=add(leafy,tuple(-x for x in bare))
    expected_diff=mul(powpoly((0,1),4),mul((2,-1),powpoly((1,-1),4)))
    assert diff==expected_diff,(diff,expected_diff)
    assert evaluate(diff,Fraction(1,2))==Fraction(3,512)
    # Two-step path distance kernels are exact polynomials, not only samples.
    q2=(0,2,-1)
    q3=(0,0,2,-1)
    q4=(0,0,0,1)
    s=symbolic_transition(5,[(i,i+1) for i in range(4)],2)
    assert prob(s,5,(0,2))==q2
    assert prob(s,5,(0,3))==q3
    assert prob(s,5,(0,4))==q4
    print('PASS: all',runs,'tree/pair finite checks on n<=5;')
    print('PASS: symbolic p-polynomials of distance 2,3,4 after two rounds;')
    print('PASS: same-order five-vertex path reproduces four-vertex path law;')
    print('PASS: symbolic third-round branch defect',diff, '= p^4 (2-p)(1-p)^4;')
    print('PASS: defect at p=1/2 = 3/512, total probability = 1.')

if __name__=='__main__':test_exact()
