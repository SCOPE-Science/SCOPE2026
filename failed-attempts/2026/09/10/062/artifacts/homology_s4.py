# Full homology at s=4: H = ker(d4)/im(d3) for stems 52..56.
# im(d3) rank: d3: C^3_t' -> C^4_t with t'=stem+3 maps... careful: d preserves t.
# d: C^3_t -> C^4_t and C^4_t -> C^5_t with SAME t. For stem-55 class at filtration f:
#   C^4 basis has t = 55+f. So compute per t: rank_in = rank(d: C^3_t->C^4_t), and
#   ker d4 at same t. H_t^4 = ker4 - rank_in.
# From ext_kernel: rank_in(t) for t=55..59 known (=full dimC3 since ker3=0).
# Need ker4(t) for t = stem+4 for relevant filtrations.
from collections import defaultdict
import sys
sys.path.insert(0,"output/artifacts")
# reuse code by import? replicate minimal
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

def image_rank(s_from,t):
    # rank of d: C^s_from_t -> C^{s_from+1}_t ; build column-sparse: eq->cols
    col_index={}; cols=[]
    def rec(k,rem,acc):
        if k==1:
            for m in bydeg.get(rem,()):
                e=tuple(acc+[m])
                if e not in col_index: col_index[e]=len(cols); cols.append(e)
            return
        for m in non1:
            d=deg(m)
            if d<rem and rem-d>=(k-1):
                rec(k-1,rem-d,acc+[m])
    rec(s_from,t,[])
    n=len(cols)
    rows=defaultdict(list)
    for j,e in enumerate(cols):
        e=list(e)
        for p in range(s_from):
            for (u1,u2) in red[e[p]]:
                f=tuple(e[:p]+[u1,u2]+e[p+1:])
                rows[f].append(j)
    pivrow={}; rank=0
    rlist=sorted(rows.values(), key=len)
    for r in rlist:
        x=set(r)
        while x:
            c=max(x)
            if c in pivrow: x^=pivrow[c]
            else: pivrow[c]=x; rank+=1; break
    return n,rank

# rank_in for H^4 at internal degree t is image_rank(3,t).
# We know ker3=0 so image_rank(3,t)=dimC3(t). Verify quickly for needed t values 56..64.
if __name__=="__main__":
    ts=[int(x) for x in sys.argv[1:]] or [59,60,61,62]
    for t in ts:
        n,r=image_rank(3,t)
        print(f"t={t}: dimC3={n} rank_in(d3)={r} (diff={n-r})", flush=True)
