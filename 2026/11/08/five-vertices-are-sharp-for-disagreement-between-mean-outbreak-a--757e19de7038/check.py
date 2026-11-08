#!/usr/bin/env python3
"""Exact finite-graph certificate for four-person postvaccination bond outbreaks.
Public research code. Python >=3.10; requires SymPy >=1.11.
No numerical sampling is used in certification.
"""
from itertools import combinations, permutations
from fractions import Fraction
from math import comb
from collections import defaultdict
import sympy as sp
p=sp.Symbol('p')

def edges(n):
    return list(combinations(range(n),2))

def connected(n, E):
    seen={0}
    while True:
        nxt=seen|{v for u,v in E if u in seen}|{u for u,v in E if v in seen}
        if nxt==seen:return len(seen)==n
        seen=nxt

def permute_edges(E, perm):
    return tuple(sorted(tuple(sorted((perm[u],perm[v]))) for u,v in E))

def canonical(n,E):
    # Full permutation orbit: no external graph catalogue required.
    return min(permute_edges(E,perm) for perm in permutations(range(n)))

def all_connected_representatives(n):
    Eall=edges(n);rep={}
    for mask in range(1<<len(Eall)):
        E=tuple(e for i,e in enumerate(Eall) if mask>>i&1)
        if connected(n,E):
            key=canonical(n,E)
            rep.setdefault(key,E)
    return dict(sorted(rep.items()))

def component_sizes(nodes, E):
    adj={v:set() for v in nodes}
    for u,v in E:adj[u].add(v);adj[v].add(u)
    comps=[];seen=set()
    for v in nodes:
        if v in seen:continue
        q={v};seen.add(v)
        while q:
            u=q.pop()
            for w in adj[u]-seen:seen.add(w);q.add(w)
        comps.append(len(seen)-sum(comps))
    return comps

def epidemic_polynomials(n,E,v):
    remain=tuple(u for u in range(n) if u!=v)
    EE=tuple(e for e in E if v not in e)
    kmax=n-1
    D={k:sp.Integer(0) for k in range(1,kmax+1)}
    for mask in range(1<<len(EE)):
        O=[e for i,e in enumerate(EE) if mask>>i&1]
        probability=p**len(O)*(1-p)**(len(EE)-len(O))
        for k in component_sizes(remain,O):
            D[k]+=sp.Rational(k,kmax)*probability
    M=sp.expand(sum(k*D[k] for k in D))
    T=sp.expand(sum(D[k] for k in D if k>=3))
    return M,T


def independent_induced_component_polys(n,E,v):
    # Different combinatorial decomposition: enumerate the infected vertex
    # set S, require that the induced random graph on S be connected and
    # every edge leaving S be closed. Edges outside S are marginalized.
    V=tuple(u for u in range(n) if u!=v)
    F=tuple(e for e in E if v not in e)
    out={k:sp.Integer(0) for k in range(1,n)}
    for bits in range(1,1<<len(V)):
        S={V[i] for i in range(len(V)) if bits>>i&1}
        inside=tuple(e for e in F if set(e)<=S)
        boundary=sum(1 for a,b in F if (a in S)!=(b in S))
        prob=sp.Integer(0)
        for emask in range(1<<len(inside)):
            chosen=[e for j,e in enumerate(inside) if emask>>j&1]
            if connected_on_set(S,chosen):
                k=len(chosen)
                prob+=p**k*(1-p)**(len(inside)-k)
        out[len(S)]+=sp.Rational(len(S),len(V))*prob*(1-p)**boundary
    return sp.expand(sum(k*out[k] for k in out)),sp.expand(sum(out[k] for k in out if k>=3))

def connected_on_set(nodes,E):
    if len(nodes)==1:return True
    start=next(iter(nodes));seen={start}
    while True:
        nxt=seen|{v for u,v in E if u in seen}|{u for u,v in E if v in seen}
        if nxt==seen:return len(seen)==len(nodes)
        seen=nxt

def nonpositive_all_01(expr):
    """Exact sign decision using rational real-root isolation, not sampling.

    Roots isolated by SymPy/Sturm in disjoint rational intervals. On each
    complementary open interval the polynomial has constant sign. Inside
    an isolating interval there is at most one distinct root: if both
    endpoint signs are nonpositive, no positive subinterval can exist.
    """
    expr=sp.factor(expr)
    if expr==0:return True
    P=sp.Poly(expr,p,domain=sp.QQ)
    rr=P.intervals(eps=sp.Rational(1,2**48))
    cuts=[sp.Rational(0),sp.Rational(1)]
    for (a,b),mult in rr:
        if 0<a<1:cuts.append(a)
        if 0<b<1:cuts.append(b)
    cuts=sorted(set(cuts))
    return (all(P.eval(x)<=0 for x in cuts)
            and all(P.eval((a+b)/2)<=0 for a,b in zip(cuts,cuts[1:])))

def dominates(vals,v,w):
    return all(nonpositive_all_01(vals[v][i]-vals[w][i]) for i in (0,1))

def positive_on_open01(expr):
    if not nonpositive_all_01(-expr):return False
    if sp.factor(expr)==0:return False
    rr=sp.Poly(expr,p,domain=sp.QQ).intervals(eps=sp.Rational(1,2**48))
    if any(0<=a<1 and 0<b<=1 for (a,b),mult in rr):return False
    return sp.Poly(expr,p).eval(sp.Rational(1,2))>0

def signature(G):
    return ';'.join(f'{u}{v}' for u,v in G)

EA=((0,1),(1,3),(1,4),(2,3),(2,4),(3,4))
EB=((0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,4))
keyA=canonical(5,EA);keyB=canonical(5,EB)
assert keyA!=keyB

def run():
    counts=[]
    for n in (2,3,4,5):counts.append(len(all_connected_representatives(n)))
    assert counts==[1,2,6,21],counts
    records=[]
    for key,E in all_connected_representatives(5).items():
        F={v:epidemic_polynomials(5,key,v) for v in range(5)}
        for v in range(5):
            independent=independent_induced_component_polys(5,key,v)
            assert all(sp.expand(F[v][i]-independent[i])==0 for i in (0,1)),(key,v)
        if key not in (keyA,keyB):
            dom=[v for v in range(5) if all(dominates(F,v,w) for w in range(5))]
            assert dom,(signature(key),'no universal dual optimizer')
            records.append((signature(key),'common',str(min(dom))))
        else:
            # Identify the two structurally different residual types by
            # graph isomorphism with the two explicitly labelled witnesses.
            if key==keyA: sample=EA; s=1;t=3
            else:sample=EB;s=0;t=2
            pairing=next(perm for perm in permutations(range(5))
                         if permute_edges(sample,perm)==key)
            v=pairing[s];w=pairing[t]
            # Every additional vertex is either a clone of one candidate
            # or is strictly worse on both outcomes throughout 0<p<1.
            for u in range(5):
                if u in (v,w):continue
                clone=any(all(sp.factor(F[x][i]-F[u][i])==0 for i in (0,1)) for x in (v,w))
                strict=any(all(positive_on_open01(F[u][i]-F[x][i]) for i in (0,1)) for x in (v,w))
                assert clone or strict,(key,u,F[u])
            dm=sp.factor(F[v][0]-F[w][0]);dt=sp.factor(F[v][1]-F[w][1])
            if key==keyA:
                assert sp.factor(dm-p**2*(1-4*p)/2)==0,(key,dm)
                assert sp.factor(dt-p**2*(3-4*p)/4)==0,(key,dt)
            else:
                assert sp.factor(dm-p**2*(p-1)*(4*p-1)/2)==0,(key,dm)
                assert sp.factor(dt-p**2*(p-1)*(4*p-3)/4)==0,(key,dt)
            records.append((signature(key),'exception',f'{v}/{w}'))
    assert len(records)==21
    assert sum(1 for r in records if r[1]=='exception')==2
    # At all p in (0, 1/4] and [3/4,1) each exception has
    # a shared optimizer; inside (1/4,3/4) the rankings oppose.
    print('Connected unlabeled classes n=2,3,4,5:',counts)
    print('105 two-method polynomial identity checks passed')
    print('All 19 nonexceptional 5-vertex types: universal dual optimizer certified')
    print('Exceptional types: exactly two, and exactly for 1/4 < p < 3/4')
    print('Canonical E_A:',signature(keyA))
    print('Canonical E_B:',signature(keyB))
    print('key;status;vertex_certificate')
    for row in records:print(';'.join(row))

if __name__=='__main__':run()
