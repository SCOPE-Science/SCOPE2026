#!/usr/bin/env python3
"""Standalone finite checks for bounded-binary-run cyclic window extremizers.
Python 3 standard library only; run: python verify.py
"""
from collections import defaultdict, deque
from itertools import product


def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def admissible(s):
    return '000' not in s and '111' not in s


def whole_edges(n):
    return {''.join(p) for p in product('01',repeat=n) if admissible(''.join(p))}


def retained(n):
    return {w for w in whole_edges(n)
            if not (w[0]==w[1] and w[-1]==w[-2])}


def euler_cycle(edges,n):
    arcs=defaultdict(list)
    for w in sorted(edges,reverse=True):
        arcs[w[:-1]].append((w[1:],w))
    src=min(arcs)
    stack=[(src,None)];rev=[]
    while stack:
        node,_=stack[-1]
        if arcs[node]:
            nxt,w=arcs[node].pop()
            stack.append((nxt,w))
        else:
            _,w=stack.pop()
            if w is not None:rev.append(w)
    order=rev[::-1]
    assert len(order)==len(edges)
    assert all(order[i][1:]==order[(i+1)%len(order)][:-1]
               for i in range(len(order)))
    return ''.join(w[0] for w in order)


def is_strong(edges):
    f=defaultdict(set);r=defaultdict(set)
    for w in edges:
        f[w[:-1]].add(w[1:]);r[w[1:]].add(w[:-1])
    vs=set(f)|set(r)
    def reachable(G):
        start=next(iter(vs));seen={start};todo=[start]
        for u in todo:
            for v in G[u]:
                if v not in seen: seen.add(v);todo.append(v)
        return seen
    return reachable(f)==vs and reachable(r)==vs


def verify(n):
    E=whole_edges(n);R=retained(n)
    assert len(E)==2*fib(n+1)
    assert len(E-R)==2*fib(n-3)
    assert len(R)==2*(fib(n+1)-fib(n-3))
    vs={w[:-1] for w in E}|{w[1:] for w in E}
    full_in=defaultdict(int);full_out=defaultdict(int)
    inr=defaultdict(int);outr=defaultdict(int)
    for w in E:full_out[w[:-1]]+=1;full_in[w[1:]]+=1
    for w in R:outr[w[:-1]]+=1;inr[w[1:]]+=1
    plus={v for v in vs if full_out[v]-full_in[v]==1}
    assert len(plus)==2*fib(n-3)
    assert all(full_out[v]-full_in[v] == (v[0]==v[1])-(v[-2]==v[-1]) for v in vs)
    assert all(inr[v]==outr[v] for v in vs)
    assert is_strong(R)
    c=euler_cycle(R,n)
    assert len(c)==len(R)
    assert all(admissible(''.join(c[(i+j)%len(c)] for j in range(3))) for i in range(len(c)))
    windows=[''.join(c[(i+j)%len(c)] for j in range(n)) for i in range(len(c))]
    assert len(windows)==len(set(windows))
    assert set(windows)==R
    return c


def brute_small():
    # For n=4 and n=5, count all binary circular strings up to length |E|
    # and check that no cyclic run-constrained string with distinct n-windows
    # exceeds the formula. This does not certify the all-n assertion.
    for n in (4,5):
        bound=len(retained(n))
        for length in range(1,len(whole_edges(n))+1):
            for tup in product('01',repeat=length):
                s=''.join(tup)
                if any(not admissible(''.join(s[(i+j)%length] for j in range(3))) for i in range(length)):
                    continue
                wins=[''.join(s[(i+j)%length] for j in range(n)) for i in range(length)]
                if len(set(wins))==length:
                    assert length<=bound
                    if length==bound: assert set(wins)==retained(n)

if __name__=='__main__':
    for n in range(3,17):
        c=verify(n)
        if n<=8: print(f'n={n} optimum={len(c)} example={c}')
    brute_small()
    print('VERIFY_OK n=3..16; independently enumerated circles n=4,5')
