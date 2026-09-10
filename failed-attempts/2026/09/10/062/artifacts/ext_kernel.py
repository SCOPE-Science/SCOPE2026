# Correct cobar homology: d: C^s_t -> C^{s+1}_t preserves internal degree t (stem = t-s drops by 1).
# Compute ker(d: C^3_t -> C^4_t) for t = stem+3, stems 52..56, over F2 (sparse).
import sys
from collections import defaultdict

mons=[]
for i in range(8):
    for j in range(4):
        for k in range(2):
            mons.append((i,j,k))
def deg(m): return m[0]+3*m[1]+7*m[2]
def add(m1,m2):
    i=m1[0]+m2[0]; j=m1[1]+m2[1]; k=m1[2]+m2[2]
    if i>=8 or j>=4 or k>=2: return None
    return (i,j,k)
def psi_gen(g):
    if g==(1,0,0): return [((1,0,0),(0,0,0)),((0,0,0),(1,0,0))]
    if g==(0,1,0): return [((0,1,0),(0,0,0)),((2,0,0),(1,0,0)),((0,0,0),(0,1,0))]
    if g==(0,0,1): return [((0,0,1),(0,0,0)),((0,2,0),(1,0,0)),((4,0,0),(0,1,0)),((0,0,0),(0,0,1))]
def mul_GxG(P,Q):
    R=defaultdict(int)
    for (a1,b1),c1 in P.items():
        for (a2,b2),c2 in Q.items():
            na=add(a1,a2); nb=add(b1,b2)
            if na is None or nb is None: continue
            R[(na,nb)]^=(c1&c2)
    return {k:v for k,v in R.items() if v}
def psi_mon(m):
    R={((0,0,0),(0,0,0)):1}
    for g,n in [((1,0,0),m[0]),((0,1,0),m[1]),((0,0,1),m[2])]:
        if n==0: continue
        Pg={k:1 for k in psi_gen(g)}
        Pn={((0,0,0),(0,0,0)):1}
        for _ in range(n): Pn=mul_GxG(Pn,Pg)
        R=mul_GxG(R,Pn)
    return R
red={}
for m in mons:
    if m==(0,0,0): continue
    P=psi_mon(m)
    red[m]=[(a,b) for (a,b) in P if a!=(0,0,0) and b!=(0,0,0)]
non1=[m for m in mons if m!=(0,0,0)]

def kernel_dim(t):
    B3=[(a,b,c) for a in non1 for b in non1 for c in non1 if deg(a)+deg(b)+deg(c)==t]
    n=len(B3); col={x:i for i,x in enumerate(B3)}
    # rows keyed by C^4 basis element, sparse: row -> set of cols
    rows=defaultdict(set)
    for j,(a,b,c) in enumerate(B3):
        for (u1,u2) in red[a]:
            rows[(u1,u2,b,c)].add(j)
        for (v1,v2) in red[b]:
            rows[(a,v1,v2,c)].add(j)
        for (w1,w2) in red[c]:
            rows[(a,b,w1,w2)].add(j)
    # sparse F2 rank over n cols
    # elimination: pivot[col] = row-set (as bitmask int over rows? use col-indexed)
    # Standard: process rows, keep pivots by leading col.
    piv={}  # leadcol -> row bitset(int over cols)
    rank=0
    for r,cols in rows.items():
        x=0
        for c in cols: x^=(1<<c)
        while x:
            hb=x.bit_length()-1
            if hb in piv: x^=piv[hb]
            else: piv[hb]=x; rank+=1; break
    return n, len(rows), rank, n-rank, B3, piv

if __name__=="__main__":
    import json
    out={}
    for stem in [52,53,54,55,56]:
        t=stem+3
        n,nrows,rank,null,B3,piv=kernel_dim(t)
        print(f"stem {stem} (t={t}): dim C^3={n}, nonzero d-rows={nrows}, rank={rank}, dim ker={null}", flush=True)
        out[stem]=dict(dimC3=n, nnzrows=nrows, rank=rank, dimker=null)
    json.dump(out, open("output/artifacts/ext3_summary.json","w"), indent=1)
