# Ext^{3,t} via kernel of d: C^3_t -> C^4_t over F2 with sparse Gaussian elimination.
# Uses reduced coproduct from cobar_s3 (recompute here). Rank over F2 via bitsets (Python ints).
import sys
from collections import defaultdict

mons=[]; idx={}
for i in range(8):
    for j in range(4):
        for k in range(2):
            idx[(i,j,k)]=len(mons); mons.append((i,j,k))
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
bydeg=defaultdict(list)
for m in non1: bydeg[deg(m)].append(m)

def solve_stem(stem, verbose=True):
    t3=stem+3; t4=stem+4
    # C^3 basis
    B3=[(a,b,c) for a in non1 for b in non1 for c in non1 if deg(a)+deg(b)+deg(c)==t3]
    n=len(B3); col={x:i for i,x in enumerate(B3)}
    # C^4 basis index (rows)
    B4=[(a,b,c,d) for a in non1 for b in non1 for c in non1 for d in non1
        if deg(a)+deg(b)+deg(c)+deg(d)==t4]
    m=len(B4); row={x:i for i,x in enumerate(B4)}
    if verbose: print(f"stem {stem}: dim C^3={n}, dim C^4={m}", flush=True)
    # matrix rows as bitsets over n cols: row r = set of cols j with d(e_j)[r]=1
    rows=[0]*m
    # d[a|b|c] = [da|b|c]+[a|db|c]+[a|b|dc] with [u|v] expanded via red
    for j,(a,b,c) in enumerate(B3):
        for (u1,u2) in red[a]:
            # [u1|u2|b|c]: only if deg sums match (automatic)
            r=row.get((u1,u2,b,c))
            if r is not None: rows[r]^=(1<<j)
        for (v1,v2) in red[b]:
            r=row.get((a,v1,v2,c))
            if r is not None: rows[r]^=(1<<j)
        for (w1,w2) in red[c]:
            r=row.get((a,b,w1,w2))
            if r is not None: rows[r]^=(1<<j)
    # rank of m x n matrix over F2 (row reduction on bitsets)
    M=list(rows); rank=0
    # find pivots by column: use standard algorithm with row ops
    # transpose approach: elimination over columns using highest-bit
    pivoted=[-1]*n
    r=0
    # order rows; use dict pivot col -> row
    piv={}
    for i in range(m):
        x=M[i]
        while x:
            hb=x.bit_length()-1
            if hb in piv:
                x^=piv[hb]
            else:
                piv[hb]=x; rank+=1; break
    dimker=n-rank
    if verbose: print(f"  rank d = {rank}, dim ker = {dimker} (= dim Ext^3 since C^2=0)", flush=True)
    # kernel basis: solve M x = 0. Build from row-echelon? Use nullspace via column elimination.
    # n <= 1014 fits in Python ints for rows; for nullspace, do Gauss-Jordan on transpose:
    # Represent as m equations; do elimination to row-echelon with pivot cols, then back-substitute.
    # Recompute echelon keeping transformation: standard nullspace algorithm.
    import copy
    A=list(rows)  # m bitsets of width n
    pivcol=[-1]*m; colpiv={}
    rr=0
    order=list(range(m))
    # forward elimination choosing lowest set bit as pivot for stability
    used=[False]*m
    # convert to list of ints; pivot on columns from 0..n-1 using row with that bit
    # Build col->rows incidence via scanning (m up to ~400k, n ~ 1000): use sparse approach.
    # Sparse: for each row store sorted col list.
    srows=[]
    for x in A:
        cols=[]; xx=x
        while xx:
            lsb=(xx & -xx).bit_length()-1
            cols.append(lsb); xx^=(1<<lsb)
        srows.append(cols)
    colrows=defaultdict(list)
    for i,cols in enumerate(srows):
        for c in cols: colrows[c].append(i)
    # Gaussian elimination with row XORs, tracking row bitsets
    alive=[True]*m
    pivot_row_for_col={}
    for c in range(n):
        # find alive row containing c
        cand=None
        for i in colrows[c]:
            if alive[i] and (A[i]>>c)&1:
                cand=i; break
        if cand is None: continue
        pivot_row_for_col[c]=cand
        alive[cand]=False
        # eliminate c from all other alive rows containing c
        for i in list(colrows[c]):
            if alive[i] and (A[i]>>c)&1:
                A[i]^=A[cand]
                # update incidence for new bits (cheap: rescan row)
                # remove i from old cols? Instead rescan lazily: check membership by bit test.
                # Add i to colrows for newly added cols:
                new=A[i]^0
                # for cols in cand row, toggle membership
                cc=A[cand]
                q=0
                while cc:
                    lsb=(cc & -cc).bit_length()-1
                    if lsb!=c and ((A[i]>>lsb)&1) and i not in colrows[lsb]:
                        colrows[lsb].append(i)
                    cc^=(1<<lsb)
    pivots=set(pivot_row_for_col.keys())
    free=[c for c in range(n) if c not in pivots]
    if verbose: print(f"  free vars: {len(free)} (nullity {dimker})", flush=True)
    assert len(free)==dimker
    # kernel basis vectors as col-index lists
    ker=[]
    prow=pivot_row_for_col
    for f in free:
        vec={f}
        for c in pivots:
            if (A[prow[c]]>>f)&1: vec.add(c)
        ker.append(sorted(vec))
    return B3, ker
if __name__=="__main__":
    stem=int(sys.argv[1]) if len(sys.argv)>1 else 55
    B3,ker=solve_stem(stem)
    print(f"EXT stem {stem}: dim={len(ker)}")
    for v in ker:
        print("  cocycle support size", len(v), ":", [B3[c] for c in v][:12])
