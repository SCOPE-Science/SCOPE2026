#!/usr/bin/env python3
"""Exhaustive exact-arithmetic certificate for two rounded remainder maps.

Python 3.10+. Only the standard library is required.
Run: python3 check.py
"""
from bisect import bisect_left
from collections import Counter, deque
from fractions import Fraction

S = 1 << 133
TOP = 0x4000
EXT = 0x4380

def scaled(code):
    e, f = code >> 7, code & 127
    return f if e == 0 else (128 + f) << (e - 1)

V = [scaled(i) for i in range(TOP + 1)]
VEXT = [scaled(i) for i in range(EXT + 1)]
assert V[0] == 0 and V[0x3f80] == S and V[TOP] == 2*S
assert VEXT[EXT] == 256*S

def rnd_int(num, den, table):
    """Rounded code for num/(den*S), ties to EVEN bfloat16 code."""
    assert num >= 0 and den > 0
    # No floating arithmetic is used in finding either neighbor or tie.
    # bisect operates on exact integers after cross-multiplication.
    lo, hi = 0, len(table)
    while lo < hi:
        mid = (lo + hi) // 2
        if den * table[mid] < num: lo = mid + 1
        else: hi = mid
    k = lo
    if k == 0: return 0
    if k == len(table): return k-1
    dleft = num - den*table[k-1]
    dright = den*table[k] - num
    return k-1 if dleft < dright or (dleft == dright and (k-1)%2 == 0) else k

def succ_integer():
    one, stage = [], []
    for X in V:
        residue = (100*X) % S
        # Once-rounded exact x/10 + frac(100x)
        a = rnd_int(X + 10*residue, 10, V)
        # Staged rounded division, rounded product, exact remainder,
        # then final rounded sum.
        k = rnd_int(100*X, 1, VEXT)
        l = rnd_int(X, 10, V)
        b = rnd_int(V[l] + (VEXT[k] % S), 1, V)
        one.append(a); stage.append(b)
    return one, stage

def code_value(i):
    return Fraction(scaled(i), S)

def round_fraction(z, limit):
    # Independent arithmetic route, using Fraction and bisect on fractions.
    table = [Fraction(scaled(i), S) for i in range(limit + 1)]
    k = bisect_left(table, z)
    if k == 0: return 0
    if k == len(table): return k-1
    da,db = z-table[k-1],table[k]-z
    return k-1 if da < db or (da==db and (k-1)%2==0) else k

def independent_rounding_check(A, B):
    # A second implementation of every exact edge. Reusing neither the
    # integer rounding search nor the integer modulo implementation.
    tbl = [Fraction(x,S) for x in VEXT]
    def round_r(z, limit):
        k=bisect_left(tbl,z,0,limit+1)
        if k==0:return 0
        if k==limit+1:return limit
        delta0=z-tbl[k-1];delta1=tbl[k]-z
        return k-1 if delta0<delta1 or (delta0==delta1 and (k-1)%2==0) else k
    for j in range(TOP+1):
        x=tbl[j];v=100*x
        rem=v-(v.numerator//v.denominator)
        a=round_r(x/10+rem,TOP)
        prod=tbl[round_r(v,EXT)]
        rp=prod-(prod.numerator//prod.denominator)
        b=round_r(tbl[round_r(x/10,TOP)]+rp,TOP)
        assert A[j]==a and B[j]==b,(j,A[j],a,B[j],b)

def dfs_graph(edges):
    n=len(edges);where=[-1]*n;distance=[-1]*n;cycles=[]
    for start in range(n):
        if where[start]!=-1:continue
        path=[];pos={};q=start
        while where[q]==-1 and q not in pos:
            pos[q]=len(path);path.append(q);q=edges[q]
        if q in pos:
            i=len(cycles);members=path[pos[q]:];cycles.append(members)
            for v in members:where[v]=i;distance[v]=0
            path=path[:pos[q]]
        for v in reversed(path):
            where[v]=where[edges[v]];distance[v]=distance[edges[v]]+1
    return cycles, Counter(where),max(distance)

def kahn_graph(edges):
    n=len(edges);degree=[0]*n
    for j in edges:degree[j]+=1
    Q=deque(i for i,d in enumerate(degree) if d==0)
    removed=[]
    while Q:
        v=Q.popleft();removed.append(v)
        w=edges[v];degree[w]-=1
        if degree[w]==0:Q.append(w)
    where=[-1]*n;distance=[0]*n;cycles=[]
    for start in range(n):
        if degree[start]==0 or where[start]>=0:continue
        j=len(cycles);cycle=[];v=start
        while where[v]<0:
            where[v]=j;cycle.append(v);v=edges[v]
        assert v==start
        cycles.append(cycle)
    for v in reversed(removed):
        where[v]=where[edges[v]];distance[v]=distance[edges[v]]+1
    return cycles,Counter(where),max(distance)

def verify():
    A,B=succ_integer()
    assert len(A)==len(B)==16385
    assert all(0<=q<=TOP for q in A+B)
    independent_rounding_check(A,B)
    for name,edges,periods,basins,depth in [
      ('once-rounded',A,[1,18,24],[1,2040,14344],51),
      ('staged',B,[1,1,3,3,3,3,3,3,3,3],
       [1,1326,11103,3221,537,117,58,8,7,7],44),
    ]:
        c,b,m=dfs_graph(edges)
        e,f,h=kahn_graph(edges)
        assert sorted(map(len,c))==periods
        assert sorted(b.values())==sorted(basins)
        assert sorted(map(len,e))==periods
        assert sorted(f.values())==sorted(basins)
        assert m==h==depth
        assert sum(b.values())==len(edges)
        # Independently compare the cycle member sets, not ordering.
        assert {frozenset(z) for z in c}=={frozenset(z) for z in e}
        print(name,'periods',sorted(map(len,c)),
              'basins',sorted(b.values(),reverse=True),'max-preperiod',m)
        for i,z in enumerate(c):
            print('  cycle',min(z),'period',len(z),'basin',b[i],
                  'members',','.join('%04x'%q for q in z))
    assert sum(x!=y for x,y in zip(A,B))==3545
    assert A[0]==B[0]==0
    print('changed successor edges',3545,'of',len(A))
    print('complete independent exact-rational edge and graph checks PASS')

if __name__=='__main__':verify()
