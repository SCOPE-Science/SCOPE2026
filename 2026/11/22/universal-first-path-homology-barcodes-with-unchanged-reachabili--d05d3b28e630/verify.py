#!/usr/bin/env python3
"""Exact, dependency-free checks for finite path-homology birth/death gadgets.
Run: python verify.py
The analytic theorem in RESULT.md establishes all cases; tests are finite sanity checks.
"""
from itertools import product
from fractions import Fraction

def qrank(rows, cols):
    """Exact rank from a list of integer row lists (Gaussian elimination over Q)."""
    if not rows or cols == 0: return 0
    a = [[Fraction(z) for z in row] for row in rows]
    r = 0
    for j in range(cols):
        p = next((i for i in range(r, len(a)) if a[i][j] != 0), None)
        if p is None: continue
        a[r], a[p] = a[p], a[r]
        lead = a[r][j]
        a[r] = [v/lead for v in a[r]]
        for i in range(r+1, len(a)):
            if a[i][j]:
                c=a[i][j]
                a[i]=[u-c*v for u,v in zip(a[i],a[r])]
        r += 1
        if r == len(a): break
    return r

def kernel_basis(rows, n):
    """Exact basis of solutions Ax=0."""
    if not rows: return [[Fraction(int(i==j)) for i in range(n)] for j in range(n)]
    a = [[Fraction(v) for v in row] for row in rows]
    piv=[];r=0
    for j in range(n):
        i=next((i for i in range(r,len(a)) if a[i][j]),None)
        if i is None:continue
        a[r],a[i]=a[i],a[r]
        v=a[r][j];a[r]=[x/v for x in a[r]]
        for k in range(len(a)):
            if k!=r and a[k][j]:
                c=a[k][j];a[k]=[x-c*y for x,y in zip(a[k],a[r])]
        piv.append(j);r+=1
        if r==len(a):break
    return [[(Fraction(1) if j==f else -a[piv.index(j)][f] if j in piv else Fraction(0)) for j in range(n)] for f in range(n) if f not in piv]

def graph(states):
    k=len(states); n=3*k+1
    E={(v,v+1) for v in range(n-1)}
    for i,s in enumerate(states):
        x=3*i
        if s>=1:E.add((x,x+3))
        if s>=2:E.add((x,x+2))
    return n,E

def bettis(states):
    n,E=graph(states); maximum=n-1
    paths={0:[(v,) for v in range(n)]}
    for p in range(1,maximum+1):
        paths[p]=[t+(j,) for t in paths[p-1] for j in range(n) if (t[-1],j) in E]
        if not paths[p]:maximum=p-1;break
    bases={0:[[Fraction(int(i==j)) for i in range(n)] for j in range(n)]}
    ranks={0:0}
    for p in range(1,maximum+1):
        cur=paths[p];pr=paths[p-1]; idx={x:i for i,x in enumerate(pr)}
        allfaces={tuple(t[:j]+t[j+1:]) for t in cur for j in range(p+1)}
        outside=sorted(allfaces-set(pr))
        forbid=[[sum((-1)**j for j in range(p+1) if t[:j]+t[j+1:]==f) for t in cur] for f in outside]
        kb=kernel_basis(forbid,len(cur))
        bases[p]=kb
        allowed=[[sum((-1)**j for j in range(p+1) if t[:j]+t[j+1:]==f) for t in cur] for f in pr]
        induced=[[sum(Fraction(row[i])*b[i] for i in range(len(cur))) for b in kb] for row in allowed]
        ranks[p]=qrank(induced,len(kb))
    b={}
    for p in range(maximum+1):
        bet=len(bases[p])-ranks.get(p,0)-ranks.get(p+1,0)
        b[p]=bet
    return b

def check():
    count=0
    for k in range(1,4):
        for state in product((0,1,2),repeat=k):
            n,E=graph(state)
            assert all(u<v for u,v in E)
            # Covers force exactly the total reachability relation, independent of state.
            assert all((j,j+1) in E for j in range(n-1))
            got=bettis(state)
            expected=sum(s==1 for s in state)
            assert got[0]==1 and got.get(1,0)==expected and all(not v for j,v in got.items() if j>=2),(state,got)
            count+=1
    # Representative two-bar timeline: [1,3) and [2,4).
    for t,want in [(0,0),(1,1),(2,2),(3,1),(4,0)]:
        state=tuple(0 if t<b else 1 if t<d else 2 for b,d in [(1,3),(2,4)])
        assert bettis(state).get(1,0)==want
    print(f'PASS: {count} exact rational-chain states and 5 timeline stages; arbitrary-parameter integral proof is in RESULT.md')
if __name__=='__main__':check()
