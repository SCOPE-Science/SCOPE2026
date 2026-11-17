#!/usr/bin/env python3
"""Exact automorphism and extremal-state orbit check on the Chvatal graph."""
from pathlib import Path
E = [(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),
     (2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),
     (5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)]
n = 12
A = [[False]*n for _ in range(n)]
for u,v in E: A[u][v]=A[v][u]=True

def automorphisms():
    im = [-1]*n
    used = [False]*n
    out = []
    def go(k):
        if k==n:
            out.append(tuple(im));return
        # Map the vertex with the most already mapped neighbours first.
        remain = [i for i in range(n) if im[i]<0]
        u = max(remain,key=lambda i:(sum(A[i][j] for j in range(n) if im[j]>=0),-i))
        for v in range(n):
            if used[v]:continue
            if any(A[u][j]!=A[v][im[j]] for j in range(n) if im[j]>=0):continue
            used[v]=True; im[u]=v
            go(k+1)
            im[u]=-1;used[v]=False
    go(0)
    return out

# The exact 48 states were obtained by exhaustive first-entry classification.
text = Path('census_with_reps.out').read_text()
line = next(s for s in text.splitlines() if s.startswith('maximal_states '))
states = set(map(int,line.split()[1:]))
autos = automorphisms()
assert len(autos)==8
assert len(states)==48
assert len(E)==24 and all(sum(r)==4 for r in A)
assert all(all(A[i][j]==A[p[i]][p[j]] for i in range(n) for j in range(n)) for p in autos)
seen = set(); reps=[]
for s in sorted(states):
    if s in seen:continue
    orbit = {sum(((s>>(2*i))&3)<<(2*p[i]) for i in range(n)) for p in autos}
    assert orbit<=states
    seen|=orbit; reps.append((s,len(orbit)))
assert seen==states and len(reps)==6 and all(k==8 for _,k in reps)
print('graph=Chvatal n=12 edges=24 automorphism_order=',len(autos),sep='')
print('max_first_entry=12 maximal_states=',len(states),sep='')
print('spatial_orbits=',len(reps),sep='')
for r,k in reps:print(f'representative={r} orbit_size={k}')
print('SIX_MAXIMAL_ORBITS_VERIFIED')
