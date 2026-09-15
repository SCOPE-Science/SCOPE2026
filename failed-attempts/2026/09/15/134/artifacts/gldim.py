"""Shape 4 (representative): a:0->1, b:1->0, c:0->1, rels ab=0, bc=0.
Nonzero paths: e0,e1,a,b,c,ba(1->1),cb(0->0),cba(0->1). dim=8.
Check forbidden cycles (all len-2 subpaths are relations) and compute
projective resolutions of simples S0,S1 -> global dimension."""
from itertools import product

# arrows with (source,target)
arrows={'a':(0,1),'b':(1,0),'c':(0,1)}
rels={'ab','bc'}
def composes(p,q):
    # path p then q: need t(p)==s(q); paths as strings of arrow names
    if not p: return q
    if not q: return p
    if arrows[p[-1]][1]!=arrows[q[0]][0]: return None
    s=p+q
    if 'ab' in s or 'bc' in s: return None  # zero
    return s

# all nonzero paths by BFS
paths={''}  # '' placeholders replaced below
import collections
nonzero=set()
frontier=['a','b','c']
nonzero.update(frontier)
seen=set(frontier)
while frontier:
    nxt=[]
    for p in frontier:
        for nm in 'abc':
            r=composes(p,nm)
            if r is not None and r not in seen:
                seen.add(r); nonzero.add(r); nxt.append(r)
    frontier=nxt
print("nonzero paths:",sorted(nonzero,key=lambda p:(len(p),p)),"count:",len(nonzero),"+2 lazy = dim",len(nonzero)+2)

# forbidden cycles: cyclic word w (len>=1) with every length-2 cyclic subpath in rels
def cyc_subs(w):
    n=len(w); return {w[i]+w[(i+1)%n] for i in range(n)}
# enumerate cyclic words up to length 6 over composable arrows
def cycles(n):
    out=[]
    def dfs(w):
        if len(w)==n:
            # check closed: t(last)==s(first)
            if arrows[w[-1]][1]==arrows[w[0]][0]:
                out.append(w)
            return
        for nm in 'abc':
            if not w or arrows[w[-1]][1]==arrows[nm][0]:
                dfs(w+nm)
    dfs('')
    return out
for n in range(1,7):
    forb=[w for w in cycles(n) if cyc_subs(w)<=rels]
    print(f"len-{n} closed cycles: {len(cycles(n))}, forbidden: {forb}")

# Projective reps: P0=e0A: paths from 0; P1: paths from 1
P0=sorted([p for p in nonzero if arrows[p[0]][0]==0]+['e0'])
P1=sorted([p for p in nonzero if arrows[p[0]][0]==1]+['e1'])
print("P0 basis:",P0,"dim",len(P0))
print("P1 basis:",P1,"dim",len(P1))
# radical maps: right mult by arrows. Minimal resolution of S0:
# P0 -> S0; ker = span of paths from 0 of len>=1 = {a,c,cb,cba}
# a*A: a followed by paths from 1: a*e1=a, a*b=0. so aA=span{a} (1-dim, top at 1, killed by b? a*b=0)
# c*A: c, cb, cba (c*e1=c, c*b=cb, c*ba=cba; c*b*b? bb invalid comp)
# ker = aA + cA, aA cap cA=0 (disjoint path sets) => ker = aA (+) cA.
# aA: module with top S1 (gen a, deg?), relations: a*b=0 => aA ~= P1/bA? bA = paths from 0?? b*e0? b starts at 1...
# Let's do linear algebra: represent right modules as dict path->coeff with mult.
