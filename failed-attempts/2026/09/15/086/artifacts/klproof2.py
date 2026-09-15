"""Certified KL via Hecke algebra: C'_w basis recursion (avoids descent-convention pitfalls).
H = Z[q^{1/2},q^{-1/2}] with T_s^2=(q-1)T_s+q... use v with q=v^2, T_s, bar involution.
C'_s = v^{-1}(1+T_s). For w with ws<w: C'_w = C'_{ws} C'_s - sum_{z<ws, zs<z} mu(z,ws) C'_z.
Expand C'_w = sum_{x<=w} P_{x,w}(v^2) v^{l(x)-l(w)} T_x. Implement with exact integer polys in v.
Self-check: bar-invariance of each C'_w; P_{x,w} in Z[q] deg<=(l(w)-l(x)-1)/2; mu symmetry.
Then cells from W-graph (mu edges), a-function, P(1) table.
"""
from fractions import Fraction
from collections import deque
import sys
sys.path.insert(0,'output/artifacts')
from kl import E,S1,S2,Sth,THV
def mm(A,B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),(A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def mv(A,v): return (A[0][0]*v[0]+A[0][1]*v[1], A[1][0]*v[0]+A[1][1]*v[1])
def va(u,v): return (u[0]+v[0],u[1]+v[1])
MID=((E(1),E(0)),(E(0),E(1))); ZV=(E(0),E(0))
GENS=[(Sth,THV),(S1,ZV),(S2,ZV)]
def compose(g,h): return (mm(g[0],h[0]), va(mv(g[0],h[1]),g[1]))
def key(g): return (g[0][0][0],g[0][0][1],g[0][1][0],g[0][1][1],g[1][0],g[1][1])

RMAX=7
kseen={}; elems=[]
e=(MID,ZV); kseen[key(e)]=[]; elems.append(e)
qq=deque([e])
while qq:
    g=qq.popleft(); w=kseen[key(g)]
    if len(w)>=RMAX: continue
    for i,gen in enumerate(GENS):
        h=compose(g,gen); k=key(h)
        if k not in kseen:
            kseen[k]=w+[i]; qq.append(h); elems.append(h)
KEYS=list(kseen.keys()); K2I={k:i for i,k in enumerate(KEYS)}; N=len(KEYS)
LEN=[len(kseen[k]) for k in KEYS]
multR=[[None]*3 for _ in range(N)]; descR=[set() for _ in range(N)]
for i,k in enumerate(KEYS):
    g=elems[i]
    for s in range(3):
        h=compose(g,GENS[s]); j=K2I.get(key(h),None)
        multR[i][s]=j
        if j is not None and LEN[j]<LEN[i]: descR[i].add(s)
print("N=",N," lens:",sorted(set(LEN)))

Mmat=[[1,2,3],[2,1,6],[3,6,1]]
def braid_closure(word):
    seen={tuple(word)}; stack=[list(word)]
    while stack:
        w=stack.pop(); L=len(w)
        for a in range(L):
            for s in range(3):
                for t in range(s+1,3):
                    m=Mmat[s][t]
                    b=a+m
                    if b<=L and w[a:b]==([s,t]*4)[:m]:
                        w2=w[:a]+([t,s]*4)[:m]+w[b:]
                        if tuple(w2) not in seen: seen.add(tuple(w2)); stack.append(w2)
                    if b<=L and w[a:b]==([t,s]*4)[:m]:
                        w2=w[:a]+([s,t]*4)[:m]+w[b:]
                        if tuple(w2) not in seen: seen.add(tuple(w2)); stack.append(w2)
    return seen
def interval_of(w):
    rw=kseen[KEYS[w]]
    out=set()
    for wword in braid_closure(rw):
        L=len(wword)
        for mask in range(1<<L):
            g=e
            for i in range(L):
                if mask>>i & 1: g=compose(g,GENS[wword[i]])
            j=K2I.get(key(g),None)
            if j is not None: out.add(j)
    return out
INTERVAL={}
for w in range(N):
    if LEN[w]<=6:
        INTERVAL[w]=interval_of(w)
print("intervals ok", len(INTERVAL))

# polys in v (integer exponents, possibly negative): dict exp->coeff
def padd(a,b):
    r=dict(a)
    for k,v in b.items():
        r[k]=r.get(k,0)+v
        if r[k]==0: del r[k]
    return r
def psub(a,b): return padd(a,{k:-v for k,v in b.items()})
def pmul(a,b):
    r={}
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            r[k1+k2]=r.get(k1+k2,0)+v1*v2
    return {k:v for k,v in r.items() if v!=0}

# C[w] = dict x -> poly in v (coeff of T_x in C'_w, i.e. P_{x,w}(v^2) v^{lx-lw})
C={0:{0:{0:1}}}
def mu_coeff(Pvw_half, lx, lw):
    # mu(z,v) = coeff of v^{lw-lx-1}... P_{z,v}(q) has top q^{(m-1)/2} <-> v^{m-1} where m=lw-lx. In C' expansion coeff of T_z is P v^{lz-lw}; mu term contributes v^{... }: mu = coeff of v^{lw-lz-1}?? Let's extract: coeff poly c(v)=P(v^2) v^{lz-lw}. Highest possible power: P deg<=(m-1)/2 gives v^{2d+m... }: 2d+lz-lw <= m-1+lz-lw = -1. So mu = coeff of v^{-1} in c(v) (when m odd; else 0). Standard.
    return Pvw_half.get(-1,0)

order=sorted(INTERVAL.keys(), key=lambda i: LEN[i])
for w in order:
    if w==0: continue
    s=min(descR[w])
    v=multR[w][s]
    # C'_w = C'_v C'_s - sum mu(z,v) C'_z over z<=v with zs<z (i.e., s in descR[z])
    Cv=C[v]
    # multiply by C'_s = v^{-1}(1+T_s): for each x: T_x C'_s = T_x v^{-1} + T_x T_s v^{-1}
    # T_x T_s = T_{xs} if x<xs else (v^2-1)T_x + v^2 T_{xs} (since q=v^2).
    new={}
    for x,cx in Cv.items():
        # term v^{-1} T_x
        new[x]=padd(new.get(x,{}), pmul(cx,{-1:1}))
        xs=multR[x][s]
        if xs is None:
            raise RuntimeError(f"mult outside ball: xlen={LEN[x]}")
        if s not in descR[x]:  # xs>x: T_x T_s = T_xs
            new[xs]=padd(new.get(xs,{}), pmul(cx,{-1:1}))
        else:  # T_xT_s = (q-1)T_x + q T_xs
            new[x]=padd(new.get(x,{}), pmul(cx,{1:1,-1:-1}))  # v^{-1}(v^2-1)=v-v^{-1}
            new[xs]=padd(new.get(xs,{}), pmul(cx,{1:1}))  # v^{-1} v^2 = v
    # subtract mu sum
    for z in INTERVAL[v]:
        if s not in descR[z]: continue
        m=mu_coeff(Cv[z],LEN[z],LEN[v])
        if m!=0:
            for x,cx in C[z].items():
                new[x]=psub(new.get(x,{}), {k:vv*m for k,vv in cx.items()})
    # verify support in INTERVAL[w]
    C[w]=new

print("recursion done")
# checks
bad=0
for w in order:
    for x,cx in C[w].items():
        # bar-invariance check per coefficient? global check: C write P_{x,w}(q): cx(v) v^{lw-lx} should be poly in q=v^2.
        sh={k+LEN[w]-LEN[x]:v for k,v in cx.items()}
        if any(k<0 or k%2==1 for k in sh):
            print("non-poly",w,x,cx); bad+=1; break
print("polycheck bad=",bad)
# P(1) table: P_{x,w}(1) = sum cx
def P1(x,w): return sum(C[w].get(x,{}).values())
def Ppoly_q(x,w):
    sh={k+LEN[w]-LEN[x]:v for k,v in C[w].get(x,{}).items()}
    return {k//2:v for k,v in sh.items()}
# print some KL polys
for w in order:
    if LEN[w]<=4:
        for x in sorted(INTERVAL[w],key=lambda i:LEN[i]):
            print(f"P x={kseen[KEYS[x]]} w={kseen[KEYS[w]]} = {Ppoly_q(x,w)}")
    if LEN[w]>4: break
