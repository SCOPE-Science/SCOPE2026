"""Fast staged JPPZ integrator: per-vertex dimension-filtered enumeration.
Usage: python3 jppz_fast.py <ne>  -> hodge_ne<ne>.log, prints stage total."""
from fractions import Fraction
from math import factorial as F
import itertools, sys, time
sys.path.insert(0, "output/artifacts")
from psi_engine import psi
from jppz_main import leg_series, kappa_series, edge_series, R, X, A, MU, DIM, aut_order

LS={l: leg_series(A[l],DIM) for l in range(4)}
FL={l: {q: sum(LS[l][p]*Fraction(MU[l]**(q-p)) for p in range(q+1)) for q in range(DIM+1)} for l in range(4)}
KS=list(kappa_series(DIM).items())
ESw={w: list(edge_series(w,DIM).items()) for w in range(R)}

def graphs_ne(ne):
    out=[]
    for nv in range(1, ne+2):
        if nv>4: continue
        for assign in itertools.product(range(nv), repeat=4):
            for gv in itertools.product(range(3), repeat=nv):
                pairs=[(i,j) for i in range(nv) for j in range(i,nv)]
                for edges in itertools.combinations_with_replacement(pairs, ne):
                    if sum(gv)+ne-nv+1!=2: continue
                    parent=list(range(nv))
                    def find(x):
                        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
                        return x
                    for (i,j) in edges: parent[find(i)]=find(j)
                    if len(set(find(i) for i in range(nv)))!=1: continue
                    ok=True
                    for v in range(nv):
                        nl=sum(1 for l in range(4) if assign[l]==v)
                        nh=sum(1 for (i,j) in edges for x in (i,j) if x==v)
                        if 2*gv[v]-2+nl+nh<=0: ok=False
                    if not ok: continue
                    out.append((tuple(gv),tuple(assign),tuple(edges)))
    seen=set(); uniq=[]
    for (gv,assign,edges) in out:
        best=None
        for perm in itertools.permutations(range(len(gv))):
            g2=tuple(gv[perm[i]] for i in range(len(gv)))
            a2=tuple(perm[assign[l]] for l in range(4))
            e2=tuple(sorted(tuple(sorted((perm[i],perm[j]))) for (i,j) in edges))
            key=(g2,a2,e2)
            if best is None or key<best: best=key
        if best in seen: continue
        seen.add(best); uniq.append(best)
    return uniq

def aut_order_full(gv,assign,edges):
    from math import factorial as _F
    nv=len(gv)
    # vertex perms preserving genera+leg-sets+edge multiset
    cnt=0
    for perm in itertools.permutations(range(nv)):
        if tuple(gv[perm[i]] for i in range(nv))!=tuple(gv): continue
        if tuple(perm[assign[l]] for l in range(4))!=tuple(assign): continue
        if tuple(sorted(tuple(sorted((perm[i],perm[j]))) for (i,j) in edges))!=tuple(sorted(edges)): continue
        cnt+=1
    # half-edge swaps: 2 per loop; 2 per... plus k! for k parallel same-endpoint edges
    from collections import Counter
    c=Counter()
    for (i,j) in edges: c[(min(i,j),max(i,j))]+=1
    h=1
    for (i,j) in edges:
        if i==j: h*=2
    for key,m in c.items():
        h*=int(_F(m))
    return cnt*h

def vertex_options(gv_v, legs_v, nbr_v, tgt):
    """All (coeff, legq tuple, kkey, branch-power-tuple placeholder) with leg+kappa degree<=tgt.
    Returns list of (coeff, legq, kkey, lkdeg). Branch powers handled by caller."""
    res=[]
    nl=len(legs_v)
    for q in itertools.product(range(tgt+1), repeat=nl) if nl else [()]:
        dq=sum(q)
        if dq>tgt: continue
        fc=Fraction(1)
        for qq,l in zip(q,legs_v): fc*=FL[l][qq]
        if fc==0: continue
        for kkey,kc in KS:
            dk=sum((m+1)*e for m,e in enumerate(kkey))
            if dq+dk>tgt: continue
            res.append((fc*kc, q, kkey, dq+dk))
    return res

def run(ne):
    t0=time.time()
    U=graphs_ne(ne)
    log=open(f"output/artifacts/hodge_ne{ne}.log","w")
    log.write(f"{ne}-edge graphs: {len(U)}\n"); log.flush()
    total=Fraction(0)
    for gi,(gv,assign,edges) in enumerate(U):
        nv=len(gv)
        aut=aut_order_full(gv,assign,edges)
        h1=ne-nv+1
        pref=Fraction(R**(3-h1))/Fraction(aut)
        need=DIM-ne
        legs_v=[[l for l in range(4) if assign[l]==v] for v in range(nv)]
        br_v=[[] for _ in range(nv)]
        for q,(i,j) in enumerate(edges):
            br_v[i].append((q,0)); br_v[j].append((q,1))
        dv=[3*gv[v]-3+len(legs_v[v])+len(br_v[v]) for v in range(nv)]
        vopts=[vertex_options(gv[v],legs_v[v],len(br_v[v]),dv[v]) for v in range(nv)]
        contrib=Fraction(0); nw=0
        for wv in itertools.product(range(R), repeat=ne):
            ok=True
            for v in range(nv):
                s=sum(A[l] for l in legs_v[v])
                for q,(i,j) in enumerate(edges):
                    if i==v: s+=wv[q]
                    if j==v: s-=wv[q]
                if s%R!=0: ok=False; break
            if not ok: continue
            nw+=1
            EL=[ESw[w] for w in wv]
            for ees in itertools.product(*EL):
                de=sum(i+j for (i,j),c in ees)
                if de>need: continue
                ec=Fraction(1)
                for (k2,c) in ees: ec*=c
                if ec==0: continue
                # per-vertex branch sums
                bs=[0]*nv
                bpow=[None]*nv
                for v in range(nv):
                    bp=tuple(ees[q][0][0] if side==0 else ees[q][0][1] for (q,side) in br_v[v])
                    bpow[v]=bp; bs[v]=sum(bp)
                # per-vertex completion to local dim
                def rec(v, acc):
                    nonlocal contrib
                    if v==nv:
                        contrib+=pref*ec*acc
                        return
                    for (coeff,qq,kkey,lkd) in vopts[v]:
                        if lkd+bs[v]!=dv[v]: continue
                        new=list(qq)+list(bpow[v])
                        for m,e in enumerate(kkey): new+=[m+2]*e
                        val=psi(gv[v],tuple(new))
                        if val==0: continue
                        rec(v+1, acc*coeff*val)
                rec(0, Fraction(1))
        log.write(f"{gv} {assign} {edges} aut={aut} h1={h1} #W={nw} contrib={contrib}\n"); log.flush()
        total+=contrib
        if gi%20==0: print(f"  graph {gi}/{len(U)} t={time.time()-t0:.0f}s run={float(total):.3f}", flush=True)
    log.write(f"STAGE ne={ne} TOTAL = {total}\n"); log.close()
    print(f"STAGE ne={ne} TOTAL = {total} = {float(total)}  ({time.time()-t0:.0f}s)")
    return total

if __name__=="__main__":
    run(int(sys.argv[1]))
