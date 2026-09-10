# Sparse-bitset version (chunked ints) for s>=4. Column j -> sparse row incidence.
from collections import defaultdict
mons=[]
for i in range(8):
    for j in range(4):
        for k in range(2):
            mons.append((i,j,k))
def deg(m): return m[0]+3*m[1]+7*m[2]
def add(m1,m2):
    a=(m1[0]+m2[0],m1[1]+m2[1],m1[2]+m2[2])
    if a[0]>=8 or a[1]>=4 or a[2]>=2: return None
    return a
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
bydeg=defaultdict(list)
for m in non1: bydeg[deg(m)].append(m)

def ker_dim_sparse(s,t, cap_rows=4000000):
    # enumerate domain basis lazily; build equation rows sparsely: eq -> list of cols
    # enumerate compositions via recursion with index assignment on the fly
    col_index={}; cols=[]  # basis elements
    rows=defaultdict(list)
    def get_col(e):
        i=col_index.get(e)
        if i is None:
            i=len(cols); col_index[e]=i; cols.append(e)
        return i
    # enumerate domain basis
    def rec(k,rem,acc):
        if k==1:
            for m in bydeg.get(rem,()):
                e=tuple(acc+[m]); get_col(e)
            return
        for m in non1:
            d=deg(m)
            if d<rem and rem-d>= (k-1)*1:
                rec(k-1,rem-d,acc+[m])
    rec(s,t,[])
    n=len(cols)
    for j,e in enumerate(cols):
        e=list(e)
        for p in range(s):
            for (u1,u2) in red[e[p]]:
                f=tuple(e[:p]+[u1,u2]+e[p+1:])
                rows[f].append(j)
    # sparse F2 rank: rows as sorted col lists; elimination with pivot col
    piv={}  # col -> row (as set)
    rank=0
    # order rows by length
    rlist=sorted(rows.values(), key=len)
    rowsets=[set(r) for r in rlist]
    # maintain col->pivot row index mapping with symmetric-difference elimination
    pivrow={}
    for rs in rowsets:
        x=set(rs)
        while x:
            c=max(x)
            if c in pivrow:
                x^=pivrow[c]
            else:
                pivrow[c]=x; rank+=1; break
    return n,len(rows),n-rank

import sys
stem=int(sys.argv[1]); s=int(sys.argv[2])
t=stem+s
n,nr,kd=ker_dim_sparse(s,t)
print(f"stem {stem} s={s} t={t}: dimC={n} nnzrows={nr} dimker={kd}", flush=True)
