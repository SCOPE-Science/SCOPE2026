"""Exact support-enumeration certificate for perfect Roman labelings of the Heawood graph."""
from collections import Counter, defaultdict
from math import comb

n = 7
lines = [frozenset((j,(j+1)%n,(j+3)%n)) for j in range(n)]
assert len(lines)==7 and len(set(lines))==7
assert all(sum({p,q}<=L for L in lines)==1 for p in range(n) for q in range(p+1,n))
N = [set() for _ in range(14)]
for j,L in enumerate(lines):
    for p in L:
        N[p].add(7+j)
        N[7+j].add(p)
assert all(len(a)==3 for a in N)

hist = Counter()
max_u = defaultdict(lambda:-1)
num_max_u = Counter()
minweight = 100
minimum = []
for T in range(1<<14):
    p = (T&127).bit_count()
    l = (T>>7).bit_count()
    eligible = sum(1<<v for v in range(14) if not (T>>v&1) and sum(bool(T>>w&1) for w in N[v])==1)
    u=eligible.bit_count()
    typ=(p,l)
    if u>max_u[typ]:max_u[typ]=u;num_max_u[typ]=1
    elif u==max_u[typ]:num_max_u[typ]+=1
    for c in range(u+1):
        hist[14+p+l-u+c]+=comb(u,c)
    w=14+p+l-u
    if w<minweight: minweight=w;minimum=[]
    if w==minweight: minimum.append((T,eligible))
expect = {10:133,11:1064,12:4578,13:12530,14:23913,15:34664,16:40803,17:40138,18:33607,19:24360,20:15813,21:9312,22:4977,23:2422,24:1043,25:364,26:91,27:14,28:1}
assert hist==expect, (hist,expect)
assert minweight==10 and len(minimum)==133
best=Counter()
for T,U in minimum:
    p=(T&127).bit_count();l=(T>>7).bit_count()
    assert all(not ((T>>q)&1) for i in range(7) if T>>i&1 for q in [7+j for j,L in enumerate(lines) if i in L])
    best[p,l]+=1
assert best==Counter({(1,1):28,(2,1):42,(1,2):42,(2,2):21}),best
print("PRD_SUPPORT_EXACT_OK min_weight=10 min_count=133")
print("coefficients",sorted(hist.items()))
print("min_types",sorted(best.items()))
print("max_unique_by_selected_parts", [(p,l,max_u[p,l],num_max_u[p,l]) for p in range(6) for l in range(6-p) if p+l in (2,3,4,5)])
