# ker(d: C^4_t -> C^5_t) for t = stem+4, stems 52..56 (t=56..60), sparse F2 rank.
# C^4 dims ~272k-404k; equations = C^5 basis count ~31-33M worst case but only nonzero rows stored.
# Use streaming: enumerate domain basis, accumulate rows as sorted col lists; rank via sparse elimination.
from collections import defaultdict
import sys
mons=[(i,j,k) for i in range(8) for j in range(4) for k in range(2)]
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
print("building red coproduct...", flush=True)
red={}
for m in mons:
    if m==(0,0,0): continue
    P=psi_mon(m)
    red[m]=[(a,b) for (a,b) in P if a!=(0,0,0) and b!=(0,0,0)]
non1=[m for m in mons if m!=(0,0,0)]
bydeg=defaultdict(list)
for m in non1: bydeg[deg(m)].append(m)
print("red built.", flush=True)
def ker4(t):
    # enumerate C^4 basis as integer cols; stream equations into dict row->list
    cols=[]  # list of tuples
    # iterative composition enumeration to avoid recursion overhead
    # s=4: nested loops over bydeg
    count=0
    rows=defaultdict(list)
    j=0
    for a in non1:
        da=deg(a)
        for b in non1:
            dab=da+deg(b)
            for c in non1:
                dabc=dab+deg(c)
                rem=t-dabc
                if rem<1: continue
                for d in bydeg.get(rem,()):
                    e=(a,b,c,d)
                    # d(e) = 4 terms groups
                    for (u1,u2) in red[a]: rows[(u1,u2,b,c,d)].append(j)
                    for (v1,v2) in red[b]: rows[(a,v1,v2,c,d)].append(j)
                    for (w1,w2) in red[c]: rows[(a,b,w1,w2,d)].append(j)
                    for (z1,z2) in red[d]: rows[(a,b,c,z1,z2)].append(j)
                    j+=1
    n=j; print(f"t={t}: dimC4={n} nnzrows={len(rows)}", flush=True)
    pivrow={}; rank=0
    for r in sorted(rows.values(), key=len):
        x=set(r)
        while x:
            c=max(x)
            if c in pivrow: x^=pivrow[c]
            else: pivrow[c]=x; rank+=1; break
    print(f"t={t}: rank={rank} dimker={n-rank}", flush=True)
    return n,rank,n-rank
if __name__=="__main__":
    for t in [int(x) for x in sys.argv[1:]]:
        ker4(t)
