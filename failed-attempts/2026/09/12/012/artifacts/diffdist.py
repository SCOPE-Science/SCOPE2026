"""Deeper probe: does a 'suffix-swap' structure force equality?
Key numerical fact to examine: counts agree to n=13 while difference classes at
each n>=6 are BOTH nonempty. Track:
 (a) joint distribution: nA_only, nB_only at each n (are difference sets equal size?)
 (b) whether there is a natural involution: test if complement-of-suffix or
     'swap last two values' style maps could pair A_only with B_only.
First: compute difference-set sizes to n=11 with the DFS engine approach in Python
(using incremental pattern detection), small-n only, to see diff sizes.
"""
import sys
sys.setrecursionlimit(10000)

def endings(p, v):
    # p: list of values (permutation of 1..n using values 1..n+1 minus v-slot), detect 1342/1423/1432
    n = len(p)
    e2=e3=e4=False
    pref=min(p) if p else 10**9
    # NOTE values in p use 1..n+1 excluding v; comparisons vs v are order-based, fine
    for j in range(n):
        pj=p[j]
        if pref < v <= pj:  # p[j] >= v since pj != v
            for k in range(j+1,n):
                pk=p[k]
                if pk>pj: e2=True; break
            for k in range(j+1,n):
                pk=p[k]
                if v < pk < pj: e4=True; break
            for k in range(j+1,n):
                pk=p[k]
                if pref < pk < v: e3=True; break
            if e2 and e3 and e4: break
        if pj<pref: pref=pj
    return e2,e3,e4

counts={}
diffs={}
def dfs(p, h23, h32, nmax):
    n=len(p)
    counts.setdefault(n,[0,0])
    if not h23: counts[n][0]+=1
    if not h32: counts[n][1]+=1
    if n>=6:
        d=diffs.setdefault(n,[0,0])
        if (not h23) and h32: d[0]+=1
        if (not h32) and h23: d[1]+=1
    if n==nmax: return
    for v in range(1,n+2):
        e2,e3,e4=endings(p,v)
        if e2: continue
        q=[x+(1 if x>=v else 0) for x in p]+[v]
        dfs(q, h23 or e3, h32 or e4, nmax)

dfs([], False, False, 10)
for n in range(0,11):
    print(n, counts[n], "Aonly,Bonly=",diffs.get(n))
