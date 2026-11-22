#!/usr/bin/env python3
"""Exact automaton and independent finite trace checks for 000/011 avoidance."""
from collections import deque
from itertools import product
from math import comb

FORBIDDEN=('000','011')
TRANS=((1,0),(2,3),(-1,3),(1,-1))

def step(P,b):
    ans=0
    for s in range(4):
        if (P>>s)&1:
            j=TRANS[s][b]
            if j>=0: ans|=1<<j
    return ans

def antichain(a):
    u=set(a)
    return tuple(sorted(x for x in u if not any(y!=x and (y&x)==y for y in u)))

def advance(F,s):
    parts=[]
    for P in F:
        if s==0: parts.append(step(P,0)|step(P,1))
        else: parts.extend((step(P,0),step(P,1)))
    if 0 in parts: return None
    return antichain(parts)

def build():
    states=[(1,)]; index={(1,):0}; transitions=[]
    for F in states:
        row=[]
        for s in (0,1):
            next_F=advance(F,s)
            if next_F is not None and next_F not in index:
                index[next_F]=len(states);states.append(next_F)
            row.append(index.get(next_F,-1))
        transitions.append(tuple(row))
    return states,transitions

def automaton_counts(n,rows):
    cur={(0,0):1}
    for _ in range(n):
        nxt={}
        for (state,k),mult in cur.items():
            for s,dest in enumerate(rows[state]):
                if dest>=0:
                    key=(dest,k+s)
                    nxt[key]=nxt.get(key,0)+mult
        cur=nxt
    counts={}
    for (state,k),mult in cur.items(): counts[k]=counts.get(k,0)+mult
    return counts

def brute_counts(n):
    words=[''.join(x) for x in product('01',repeat=n) if all(f not in ''.join(x) for f in FORBIDDEN)]
    ans={}
    for mask in range(1<<n):
        support=[i for i in range(n) if mask>>i&1]
        traces={tuple(w[i] for i in support) for w in words}
        if len(traces)==1<<len(support):
            k=len(support);ans[k]=ans.get(k,0)+1
    return ans

def verify():
    states,rows=build()
    assert len(states)==14
    assert rows==[(1,2),(3,4),(5,6),(3,4),(5,6),(7,8),(8,-1),(9,10),(11,-1),(9,10),(11,-1),(12,13),(7,8),(8,-1)]
    D=[4,4,2,4,2,3,0,3,1,3,1,2,3,0]
    assert all(D[i]>=3*s-1+D[j] for i,row in enumerate(rows) for s,j in enumerate(row) if j>=0)
    for n in range(13):
        c=automaton_counts(n,rows)
        assert c==brute_counts(n), (n,c,brute_counts(n))
        dim=max(c)
        assert dim==(0 if n==0 else (n+4)//3)
    # Exact rational GF identity: denominator = (1-t)(1-t-2t^3 z+t^4 z).
    # Numerator = 1-t+tz+t^2z^2-2t^3z+t^3z^2+t^4z-t^4z^2.
    pol=[automaton_counts(n,rows) for n in range(28)]
    lhs_terms={(0,0):1,(1,0):-2,(2,0):1,(3,1):-2,(4,1):3,(5,1):-1}
    rhs_terms={(0,0):1,(1,0):-1,(1,1):1,(2,2):1,(3,1):-2,(3,2):1,(4,1):1,(4,2):-1}
    for n in range(28):
        got={}
        for (nt,k),a in lhs_terms.items():
            if n>=nt:
                for j,v in pol[n-nt].items():
                    got[k+j]=got.get(k+j,0)+a*v
        got={k:v for k,v in got.items() if v}
        expected={k:v for (nt,k),v in rhs_terms.items() if nt==n}
        assert got==expected,(n,got,expected)
    # Exact transfer resolvent reduction with symbolic rational arithmetic.
    try:
        import sympy as sp
    except ImportError:
        print('Symbolic matrix-elimination check omitted: install sympy')
    else:
        t,z=sp.symbols('t z'); N=len(rows);M=sp.zeros(N)
        for i,row in enumerate(rows):
            for s,j in enumerate(row):
                if j>=0:M[i,j]+=(t*z if s else t)
        f=(sp.eye(N)-M).inv()*sp.ones(N,1)
        expected=(1-t+t*z+t*t*z*z-2*t**3*z+t**3*z*z+t**4*z-t**4*z*z)/((1-t)*(1-t-2*t**3*z+t**4*z))
        assert sp.cancel(f[0]-expected)==0
        print('Symbolic rational identity: PASS')
    print('14-state transitions and potential certificate: PASS')
    print('Independent direct trace comparison n=0..12: PASS')
    print('Generating-function coefficient identity n=0..27: PASS')
    print('VC dimension and constructive path bound: PASS')

if __name__=='__main__':verify()
