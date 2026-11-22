#!/usr/bin/env python3
"""Exact alternative integer checks of the sink-profile cycle Fourier theorem.
Standard-library only; finite tests supplement, not replace, the all-size proof.
"""
from itertools import product
from math import prod

checks=0

def check(cond, details=''):
    global checks
    checks+=1
    if not cond:raise AssertionError(details)

def q(k):
    a,b=2,2
    if k==0:return a
    for _ in range(1,k):a,b=b,2*b-2*a
    return b

def formula_cycle(n,S):
    check(n>=3)
    if not S:return (1<<n)-2
    if len(S)==n:return q(n)-2
    z=n-len(S)
    begin=next(i for i in range(n) if i not in S)
    runs=[]; ell=0
    for j in range(1,n+1):
        v=(begin+j)%n
        if v in S:ell+=1
        elif ell:
            runs.append(ell);ell=0
    check(ell==0 and sum(runs)==len(S))
    return (1<<(z-len(runs)))*prod(q(ell) for ell in runs)-2

def measure_from_edges(N,edges):
    # Orient each edge (u,v), with 0 meaning u->v, 1 meaning v->u.
    out=[0]*(1<<N)
    for orientation in product((0,1),repeat=len(edges)):
        indeg=[0]*N; outdeg=[0]*N
        adj=[[] for _ in range(N)]
        for bit,(u,v) in zip(orientation,edges):
            if bit:u,v=v,u
            outdeg[u]+=1;indeg[v]+=1
            adj[u].append(v)
        # Kahn algorithm, independent generic acyclicity test.
        rem=indeg[:];stack=[i for i,d in enumerate(rem) if d==0];seen=0
        while stack:
            u=stack.pop();seen+=1
            for v in adj[u]:
                rem[v]-=1
                if not rem[v]:stack.append(v)
        if seen<N:continue
        mask=sum(1<<i for i,d in enumerate(outdeg) if d==0)
        out[mask]+=1
    return out

def spectrum(f):
    f=f[:];N=(len(f)).bit_length()-1
    for b in range(N):
        for m in range(len(f)):
            if not m>>b&1:
                u,v=f[m],f[m|(1<<b)]
                f[m],f[m|(1<<b)]=u+v,u-v
    return f

def direct_character(f,S):
    return sum(w*(-1 if (S&j).bit_count()%2 else 1) for j,w in enumerate(f))

def cycle(n,shift=0):
    return [((shift+i),(shift+(i+1)%n)) for i in range(n)]

def path(n,shift=0):
    return [((shift+i),(shift+i+1)) for i in range(n-1)]

for n in range(3,15):
    f=measure_from_edges(n,cycle(n))
    check(sum(f)==(1<<n)-2,f'orientation count n={n}')
    spectrum_n=spectrum(f)
    check(all(v!=0 and v%2==0 for v in spectrum_n),f'nonzero/parity n={n}')
    check(min(map(abs,spectrum_n))==2,f'gap n={n}')
    check(max(map(abs,spectrum_n))==(1<<n)-2,f'max n={n}')
    for mask,weight in enumerate(spectrum_n):
        S={i for i in range(n) if mask>>i&1}
        check(weight==formula_cycle(n,S),f'n={n}, S={mask}, {weight}!={formula_cycle(n,S)}')
    if n<=9:
        for mask in range(1<<n):
            check(direct_character(f,mask)==spectrum_n[mask])

# Independent leaf test for every path through eleven vertices.
for n in range(2,12):
    f=measure_from_edges(n,path(n))
    F=spectrum(f)
    check(sum(f)==1<<(n-1))
    check(F[1]==0, f'leaf mode n={n}')

# Both disconnected cyclic products and a path obstruction are tested.
for N,edges,cycles,expect_invertible in [
    (4,cycle(3)+[],[3],True),
    (6,cycle(3)+cycle(3,3),[3,3],True),
    (7,cycle(3)+cycle(4,3),[3,4],True),
    (8,cycle(3)+cycle(3,3),[3,3],True),
    (8,cycle(4)+cycle(4,4),[4,4],True),
    (5,path(2)+cycle(3,2),[3],False),
    (6,path(3)+cycle(3,3),[3],False),
    (5,path(4),[],False),
]:
    f=measure_from_edges(N,edges)
    F=spectrum(f)
    check(all(v!=0 for v in F)==expect_invertible)
    if expect_invertible:
        check(min(map(abs,F))==(1<<len(cycles)))
        check(max(map(abs,F))==prod((1<<m)-2 for m in cycles))
    else:
        check(any(v==0 for v in F))

for k in range(1,1001):
    v=q(k)
    check(v==0 if k%4==2 else abs(v)>=2)
    if k>=3:check(v==0 or abs(v)>=4)
print(f'PASS: {checks} exact integer assertions; cycles 3..14, paths 2..11, disconnected examples, recurrence 1..1000')
