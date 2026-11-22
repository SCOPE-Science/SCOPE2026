#!/usr/bin/env python3
"""Direct exact permutation-model checks for split-graph normal cones."""
from itertools import permutations, product
from collections import Counter
from math import factorial, comb
from fractions import Fraction

def parts(s,k):
    if k==1:
        yield (s,)
    else:
        for j in range(s+1):
            for p in parts(s-j,k-1):
                yield (j,)+p

def graph_edges(r,s):
    return [(i,j) for i in range(r+s) for j in range(i+1,r+s) if i<r or j<r]

def exact_check(r,s):
    n=r+s; E=graph_edges(r,s)
    hist=Counter()
    for order in permutations(range(n)):
        rank={v:i for i,v in enumerate(order)}
        key=tuple(rank[u]<rank[v] for u,v in E)
        hist[key]+=1
    predicted=Counter()
    for pi in permutations(range(r)):
        for a in product(range(r+1),repeat=s):
            m=Counter(a)
            cnt=1
            for j in range(r+1):cnt*=factorial(m[j])
            rank_clique={v:i for i,v in enumerate(pi)}
            sign=[]
            for u,v in E:
                if v<r: sign.append(rank_clique[u]<rank_clique[v])
                elif u<r: sign.append(rank_clique[u]<a[v-r])
                else: raise AssertionError('independent edges unexpected')
            key=tuple(sign)
            assert key not in predicted
            predicted[key]=cnt
    assert hist==predicted,(r,s,'orientation mismatch')
    assert len(hist)==factorial(r)*(r+1)**s
    S=sum(__import__('math').prod(factorial(m) for m in p) for p in parts(s,r+1))
    C=Fraction(sum(v*v for v in hist.values()),factorial(n)**2)
    assert C==Fraction(factorial(r)*factorial(s)*S,factorial(n)**2)
    for t in (2,3,4):
        S_t=sum(__import__('math').prod(factorial(m)**(t-1) for m in pp) for pp in parts(s,r+1))
        observed=Fraction(sum(v**t for v in hist.values()),factorial(n)**t)
        expected=Fraction(factorial(r)*factorial(s)*S_t,factorial(n)**t)
        assert observed==expected,(r,s,t)
    return n,len(hist),C

def bipartite_pair_check(s):
    n=s+2
    E=[(i,j) for i in range(2) for j in range(2,n)]
    hist=Counter()
    for order in permutations(range(n)):
        rank={v:i for i,v in enumerate(order)}
        hist[tuple(rank[u]<rank[v] for u,v in E)]+=1
    direct=Fraction(sum(v*v for v in hist.values()),factorial(n)**2)
    split_C=exact_check(2,s)[-1]
    correction=Fraction(2*factorial(s)*sum(factorial(a)*factorial(s-a) for a in range(s+1)),factorial(n)**2)
    assert direct==split_C+correction
    return direct

def asymptotic_check():
    for r in range(2,5):
        vals=[]
        for s in (12,25,50,100):
            S=sum(__import__('math').prod(factorial(m) for m in p) for p in parts(s,r+1)) if s<=25 else None
            if S is not None:
                vals.append((s,float(Fraction(S,(r+1)*factorial(s)))))
        assert all(v>1 for _,v in vals)
    return True

if __name__=='__main__':
    tested=[]
    for r,s in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)]:
        tested.append(exact_check(r,s))
    assert asymptotic_check()
    for s in (2,3,4,5): bipartite_pair_check(s)
    print('SPLIT_ANGULAR_CONE_EXACT_PASS cases=%d' % len(tested))
    for n,v,c in tested: print('n=%d vertices=%d collision=%s' %(n,v,c))
