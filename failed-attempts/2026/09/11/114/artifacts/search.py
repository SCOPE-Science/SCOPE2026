"""Randomized local search over integer 10-configs in a box, minimizing the
count of strict-uniform small pairs (fast orientation predicate)."""
import itertools, random, time
P = None
def det3(M):
    (a,b,c),(d,e,f),(g,h,k) = M
    return a*(e*k-f*h)-b*(d*k-f*g)+c*(d*h-e*g)
def ori(a,b,c,d):
    pa,pb,pc,pd = P[a],P[b],P[c],P[d]
    return det3([[pb[j]-pa[j] for j in range(3)],[pc[j]-pa[j] for j in range(3)],[pd[j]-pa[j] for j in range(3)]])
def pierce(p,q,a,b,c):
    s1=ori(p,a,b,c); s2=ori(q,a,b,c)
    if s1==0 or s2==0 or (s1>0)==(s2>0): return False
    t1=ori(p,q,a,b); t2=ori(p,q,b,c); t3=ori(p,q,c,a)
    if t1==0 or t2==0 or t3==0: return False
    return (t1>0)==(t2>0)==(t3>0)
def inset(x,a,b,c,d):
    o=ori(a,b,c,d)
    if o==0: return False
    return ori(x,b,c,d)*o>0 and ori(x,a,c,d)*ori(b,a,c,d)>0 and ori(x,a,b,d)*ori(c,a,b,d)>0 and ori(x,a,b,c)*ori(d,a,b,c)>0
def meet(A,B):
    A=list(A);B=list(B)
    if len(B)>=4:
        for x in A:
            for q in itertools.combinations(B,4):
                if inset(x,*q): return True
    if len(A)>=4:
        for x in B:
            for q in itertools.combinations(A,4):
                if inset(x,*q): return True
    if len(B)>=3:
        for e in itertools.combinations(A,2):
            for t in itertools.combinations(B,3):
                if pierce(e[0],e[1],*t): return True
    if len(A)>=3:
        for e in itertools.combinations(B,2):
            for t in itertools.combinations(A,3):
                if pierce(e[0],e[1],*t): return True
    return False
verts=list(range(10))
PAIRS=[]
seen=set()
for r1 in (2,3,4):
    for s in itertools.combinations(verts,r1):
        S=frozenset(s); rest=[v for v in verts if v not in S]
        for r2 in (2,3,4):
            if r2>len(rest): continue
            for t in itertools.combinations(rest,r2):
                T=frozenset(t)
                a,b=(S,T) if str(sorted(S))<=str(sorted(T)) else (T,S)
                if (a,b) in seen: continue
                seen.add((a,b)); PAIRS.append((sorted(a),sorted(b)))
print("pairs:",len(PAIRS))
def score(cfg):
    global P; P=cfg
    n=0
    for (A,B) in PAIRS:
        if not meet(A,B): continue
        if all(meet([x for x in A if x!=v],[x for x in B if x!=v]) for v in range(10)):
            n+=1
    return n
rng=random.Random(11)
t0=time.time()
best=None
for tr in range(12):
    cfg=[(rng.randint(0,6),rng.randint(0,6),rng.randint(0,6)) for _ in range(10)]
    if len(set(cfg))<10: continue
    s=score(cfg)
    print(f"trial {tr}: uniform={s} t={round(time.time()-t0,1)}", flush=True)
    if best is None or s<best[0]: best=(s,cfg)
    if time.time()-t0>48: break
print("BEST:",best[0],best[1])
