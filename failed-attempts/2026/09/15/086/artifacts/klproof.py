"""Certified KL computation for affine Weyl G2 ball + cells.
Conventions: generators ordered (s0,s1,s2) with m01=2, m02=3, m12=6 (verified from faithful matrices).
- Enumerate group ball by BFS (exact, faithful affine representation over Q(sqrt3)).
- Bruhat order: x<=w iff some (=every?) subword of a fixed reduced word of w equals x. We use: fix one reduced word per element (BFS), then x<=w iff x equals subword of that word AND l(x) consistent... careful: single reduced word does NOT suffice for Bruhat membership in general (need existence over all reduced words). Correct approach: x<=w iff x can be obtained as subword of SOME reduced word of w. Using one fixed reduced word rw(w): the set of subwords gives a subset (the "subword" lower set of that word). To get full interval, must range over ALL reduced words of w (braid graph). We generate all reduced words via braid moves (m=2,3,6) up to closure, then take all subwords, then verify each subword's element and take lengths. Since braid moves connect all reduced words (Matsumoto/Tits), closure under the three braid relations gives all reduced words. Implement that.
- KL recursion: standard: for w with descent s (l(ws)<l(w)), for x<=ws: P_{x,w} = q^{...} ... Use classical formula:
  P_{x,w} = P_{x,ws}... precisely: let v=ws. Then for x<=v: P_{x,w} = P_{x,v} + ... hmm use standard recursion with mu:
  P_{x,w}(q) = P_{x,v}(q) + q*P_{xs,v}(q) - sum_{x<=z<v, zs<z} mu(z,v) q^{(l(w)-l(z))/2} P_{x,z}(q), with conventions P_{xs,v}=0 if xs not<= v or xs>x... (Klusener's formula / Kazhdan-Lusztig recursion). Implement with exact Laurent/integer polys.
- mu(x,w) = coeff of q^{(l(w)-l(x)-1)/2} in P_{x,w}.
- cells: left cells via KL graph (x-y if mu nonzero one way); two-sided via transitive closure. a-function via... For report: compute left-cell partition of ball + distinguished involutions + P(1) table constant on cells.
"""
from fractions import Fraction
import sys
sys.path.insert(0,'output/artifacts')
from kl import E,S1,S2,Sth,THV
from collections import deque

def mm(A,B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),(A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def mv(A,v): return (A[0][0]*v[0]+A[0][1]*v[1], A[1][0]*v[0]+A[1][1]*v[1])
def va(u,v): return (u[0]+v[0],u[1]+v[1])
MID=((E(1),E(0)),(E(0),E(1))); ZV=(E(0),E(0))
GENS=[(Sth,THV),(S1,ZV),(S2,ZV)]  # 0,1,2 = s0,s1,s2
def compose(g,h):
    return (mm(g[0],h[0]), va(mv(g[0],h[1]),g[1]))
def key(g):
    return (g[0][0][0],g[0][0][1],g[0][1][0],g[0][1][1],g[1][0],g[1][1])

RMAX=8
kseen={}; words={}  # key -> reduced word (list of ints 0..2), element mat
e=(MID,ZV); kseen[key(e)]=[]; words[key(e)]=[]
qq=deque([e])
elems=[e]
while qq:
    g=qq.popleft()
    w=kseen[key(g)]
    if len(w)>=RMAX: continue
    for i,gen in enumerate(GENS):
        h=compose(g,gen)
        k=key(h)
        if k not in kseen:
            kseen[k]=w+[i]; words[k]=w+[i]; qq.append(h); elems.append(h)
print("ball size:",len(kseen))
# index elements
KEYS=list(kseen.keys())
K2I={k:i for i,k in enumerate(KEYS)}
N=len(KEYS)
LEN=[len(kseen[k]) for k in KEYS]
# right descent sets: D_R(w) = {s: l(ws)<l(w)}; compute by multiplying and comparing BFS length
descR=[]
multR=[[None]*3 for _ in range(N)]
for i,k in enumerate(KEYS):
    g=elems[i]
    d=set()
    for s in range(3):
        h=compose(g,GENS[s]); kh=key(h)
        j=K2I.get(kh,None)
        multR[i][s]=j  # None if outside ball
        if j is not None and LEN[j]<LEN[i]: d.add(s)
    descR.append(d)

# all reduced words via braid closure (within ball words only for interval computation we need words of w up to len RMAX; braid moves preserve length so fine)
Mmat=[[1,2,3],[2,1,6],[3,6,1]]
def braid_closure(word):
    seen={tuple(word)}; stack=[list(word)]
    while stack:
        w=stack.pop()
        L=len(w)
        for a in range(L):
            for b in range(a+1,L+1):
                # try alternating braid at position a of length m
                for s in range(3):
                    for t in range(s+1,3):
                        m=Mmat[s][t]
                        if b-a==m and w[a:b]==([s,t]*(m//2+1))[:m]:
                            w2=w[:a]+([t,s]*(m//2+1))[:m]+w[b:]
                            if tuple(w2) not in seen:
                                seen.add(tuple(w2)); stack.append(w2)
                        if b-a==m and w[a:b]==([t,s]*(m//2+1))[:m]:
                            w2=w[:a]+([s,t]*(m//2+1))[:m]+w[b:]
                            if tuple(w2) not in seen:
                                seen.add(tuple(w2)); stack.append(w2)
        # also commutation m=2 covered above
    return seen

def subword_elements(wordset):
    """all group elements obtainable as subwords (as indices) of any word in set; return dict key->minlen? Use BFS lengths for len."""
    out={}
    for w in wordset:
        L=len(w)
        for mask in range(1<<L):
            sub=[w[i] for i in range(L) if mask>>i & 1]
            # evaluate group element
            g=e
            for s in sub: g=compose(g,GENS[s])
            k=key(g)
            # element's true length <= len(sub); record
            out[k]=sub
    return out

# Bruhat intervals: for each w (len<=6 to keep cost sane), interval = subword elements whose ... all subword elements are <= w automatically? Any subword of a reduced word is <= w. And ranging over all reduced words gives full interval. So interval[w] = keys from subword_elements(braid_closure(rw)).
from functools import lru_cache
INTERVAL={}
for i,k in enumerate(KEYS):
    if LEN[i]>6: continue
    rw=kseen[k]
    clo=braid_closure(rw)
    subs=subword_elements(clo)
    # keep only those in ball (all are, since shorter)
    INTERVAL[i]=set(K2I[kk] for kk in subs if kk in K2I)
print("intervals done for", len(INTERVAL))

# KL recursion with memo: P[(x,w)] for x<=w.
# order pairs by l(w).
def addp(p,q):
    r=dict(p)
    for k,v in q.items(): r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v!=0}
def mul_q_pow(p,e):
    return {k+e:v for k,v in p.items()}
P={}
def getP(x,w):
    if x==w: return {0:1}
    if x not in INTERVAL.get(w,set()): return {}
    return P[(x,w)]

# process w by increasing length
order=sorted(INTERVAL.keys(), key=lambda i:LEN[i])
import sys
for w in order:
    if LEN[w]==0: continue
    # choose descent s in descR[w] (right descent)
    s=min(descR[w]) if descR[w] else None
    if s is None: continue
    v=multR[w][s]  # ws, len-1
    for x in INTERVAL[w]:
        if x==w:
            P[(x,w)]={0:1}; continue
        if LEN[x]>LEN[w]: continue
        # xs = x*s
        xs=multR[x][s] if x in INTERVAL and True else None
        # classical recursion (see e.g. Soergel's formula): with v=ws:
        # P_{x,w} = P_{x,v} [if x<=v] + q P_{xs,v} [if xs<=v, xs<x... ] - sum mu(z,v) q^{(lw-lz)/2} P_{x,z}
        # sum over z in [x,v], z<=v, with lz<lw-... and zs<z (s in descR[z]).
        Pv_x = getP(x,v) if (v in INTERVAL and x in INTERVAL.get(v,set())) else {}
        # xs term: standard: q * P_{xs,v} if xs<x (i.e., s in descR[x]) else P_{xs,v}?? Different conventions (left vs right). We use right descent version:
        # If xs > x (s not in descR[x]) then term is q*P_{x... } hmm. Let's use the well-known recursion:
        # P_{x,w} = q P_{x,v}?? No.
        # Use Deodhar-style: choose s with ws<w. Then:
        #   if xs<x: P_{x,w} = P_{xs,v} + q P_{x,v} - sum mu...
        #   if xs>x or xs not comparable: P_{x,w} = q P_{x,v} + P_{... }? 
        # To avoid convention error, implement via Hecke algebra action directly: C'_v C'_s = ... and extract P. That's cleaner and self-verifying:
        pass
print("switching to Hecke-action recursion")
