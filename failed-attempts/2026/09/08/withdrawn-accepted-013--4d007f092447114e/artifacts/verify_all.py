"""Independent verifier (different code path, brute-force line tables):
1. rebuilds PG(2,9), conic C;
2. checks committed A (17 pts) has max line-occupancy 3, spectrum sums to 91;
3. checks weight enumerator by direct 9^3 codeword enumeration;
4. checks GLOBAL maximality of off-size 7 by independent clique-style DFS with
   correct model (bisecant pairs + unisecant triples + exterior quads), in
   natural (unpermuted) order with forward checking. Prints certificate.
"""
import itertools, json
from collections import Counter
def add(x,y): return ((x%3)+(y%3))%3 + 3*(((x//3)+(y//3))%3)
def neg(x): return ((-x)%3)+3*((-(x//3))%3)
def mul(x,y):
    u1,v1=x%3,x//3; u2,v2=y%3,y//3
    return (u1*u2-v1*v2)%3+3*((u1*v2+u2*v1)%3)
def inv(x):
    for z in range(1,9):
        if mul(x,z)==1: return z
pts=[]; seen=set()
for x in range(9):
    for y in range(9):
        for z in range(9):
            if x==y==z==0: continue
            v=(x,y,z)
            for c in v:
                if c: s=inv(c); break
            key=(mul(x,s),mul(y,s),mul(z,s))
            if key not in seen: seen.add(key); pts.append(key)
N=91
def on_line(p,L): return add(add(mul(L[0],p[0]),mul(L[1],p[1])),mul(L[2],p[2]))==0
lines=set()
for i in range(N):
    for j in range(i+1,N):
        x1,y1,z1=pts[i]; x2,y2,z2=pts[j]
        a=add(mul(y1,z2),neg(mul(z1,y2))); b=add(mul(z1,x2),neg(mul(x1,z2))); c=add(mul(x1,y2),neg(mul(y1,x2)))
        for v in (a,b,c):
            if v: s=inv(v); break
        lines.add((mul(a,s),mul(b,s),mul(c,s)))
lines=list(lines); assert len(lines)==91
line_pts=[[i for i,p in enumerate(pts) if on_line(p,L)] for L in lines]
W=json.load(open("output/artifacts/witness_analysis.json"))
A=W["A"]; C=set(W["C"]); S=W["S"]
assert len(A)==17 and len(C)==10 and len(S)==7
occ=Counter(len(set(LP)&set(A)) for LP in line_pts)
assert max(occ)<=3 and sum(occ.values())==91
print("VERIFY witness arc: spectrum",dict(sorted(occ.items())))
G=[[pts[i][r] for i in A] for r in range(3)]
Wc=Counter()
for a in range(9):
    for b in range(9):
        for c in range(9):
            if a==b==c==0: continue
            Wc[sum(1 for j in range(17) if add(add(mul(a,G[0][j]),mul(b,G[1][j])),mul(c,G[2][j]))!=0)]+=1
assert dict(sorted(Wc.items()))=={int(k):v for k,v in W["weight_raw"].items()}
print("VERIFY weight enumerator:",dict(sorted(Wc.items())),"d=14" if min(Wc)==14 else ("d="+str(min(Wc))))
# independent global-max DFS in natural order
off=sorted(i for i in range(N) if i not in C); n=len(off); pos={v:k for k,v in enumerate(off)}
pair_line={}
for li,LP in enumerate(line_pts):
    for a,b in itertools.combinations(LP,2): pair_line[(min(a,b),max(a,b))]=li
co=[len(set(LP)&C) for LP in line_pts]
bad2=set()
for k1 in range(n):
    for k2 in range(k1+1,n):
        if co[pair_line[(min(off[k1],off[k2]),max(off[k1],off[k2]))]]>=2: bad2.add((k1,k2))
bad3=set()
extlines=[]
for li,LP in enumerate(line_pts):
    so=sorted(pos[x] for x in LP if x not in C)
    if co[li]==1:
        for t in itertools.combinations(so,3): bad3.add(t)
    if co[li]==0: extlines.append(so)
import sys; sys.setrecursionlimit(100000)
best=[7]; nodes=[0]
exte=[set(e) for e in extlines]
def feas(v,cur):
    for j in cur:
        if (min(v,j),max(v,j)) in bad2: return False
    for j1,j2 in itertools.combinations(cur,2):
        if tuple(sorted((v,j1,j2))) in bad3: return False
    for E in exte:
        if v in E and len(cur & E)>=3: return False
    return True
def dfs(cand,cur):
    nodes[0]+=1
    while cand:
        if len(cur)+len(cand)<=best[0]: return
        v=cand.pop(0)
        if feas(v,cur):
            nc=[u for u in cand if (min(v,u),max(v,u)) not in bad2]
            if len(cur)+1+len(nc)>best[0]: dfs(nc,cur|{v})
        if len(cur)+len(cand)<=best[0]: return
    if len(cur)>best[0]: best[0]=len(cur); print("BEATEN:",len(cur))
dfs(list(range(n)),set())
print("VERIFY global max: optimum off-size <=" , best[0], "nodes:",nodes[0])
assert best[0]==7
print("VERIFY PASS: max conic-plus (n,3)-arc in PG(2,9) has n=17; no 8th off-conic point exists.")
