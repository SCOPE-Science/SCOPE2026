# Scan Ext^{s,t} proxy for stems 52..56, all s with C^s_t nonzero (t-s=stem).
# Reports dim C^s_t and dim ker(d: C^s_t -> C^{s+1}_t) via sparse F2 rank.
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

def basis(s,t):
    # compositions of t into s positive-degree parts from non1
    res=[]
    def rec(k,rem,acc):
        if k==1:
            for m in non1:
                if deg(m)==rem: res.append(tuple(acc+[m]))
            return
        for m in non1:
            d=deg(m)
            if d<rem: rec(k-1,rem-d,acc+[m])
    rec(s,t,[])
    return res

def ker_dim(s,t):
    B=basis(s,t); n=len(B)
    if n==0: return 0,0,0
    rows=defaultdict(int)  # rowkey -> bitmask
    for j,e in enumerate(B):
        e=list(e)
        for p in range(s):
            for (u1,u2) in red[e[p]]:
                f=tuple(e[:p]+[u1,u2]+e[p+1:])
                rows[f]^=(1<<j)
    piv={}; rank=0
    for r,x in rows.items():
        while x:
            hb=x.bit_length()-1
            if hb in piv: x^=piv[hb]
            else: piv[hb]=x; rank+=1; break
    return n,len(rows),n-rank

for stem in [52,53,54,55,56]:
    print(f"== stem {stem} ==", flush=True)
    for s in range(1,10):
        t=stem+s
        # skip huge
        import math
        n,nr,kd=ker_dim(s,t)
        print(f"  s={s} t={t}: dimC={n} nnzrows={nr} dimker={kd}", flush=True)
        if n>3000: print("   (stop: too big)"); break
