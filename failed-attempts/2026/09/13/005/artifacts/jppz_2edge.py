"""2-edge stage. Enumerate canonical 2-edge graphs, integrate. General vertex integrator for nv<=3."""
from fractions import Fraction
from math import factorial as F
import itertools, sys
sys.path.insert(0, "output/artifacts")
from psi_engine import psi
from jppz_main import leg_series, kappa_series, edge_series, R, X, A, MU, DIM, aut_order

LS={l: leg_series(A[l],DIM) for l in range(4)}
FL={l: {q: sum(LS[l][p]*Fraction(MU[l]**(q-p)) for p in range(q+1)) for q in range(DIM+1)} for l in range(4)}
KS=kappa_series(DIM)
ESw={w: edge_series(w,DIM) for w in range(R)}

def graphs_2edge():
    out=[]
    for nv in (1,2,3):
        for assign in itertools.product(range(nv), repeat=4):
            for gv in itertools.product(range(3), repeat=nv):
                pairs=[(i,j) for i in range(nv) for j in range(i,nv)]
                for edges in itertools.combinations_with_replacement(pairs, 2):
                    if sum(gv)+2-nv+1!=2: continue
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

def run():
    U=graphs_2edge()
    log=open("output/artifacts/hodge_2edge.log","w")
    log.write(f"2-edge graphs: {len(U)}\n")
    total=Fraction(0)
    for (gv,assign,edges) in U:
        nv=len(gv); ne=2
        aut=aut_order(gv,assign,edges)
        h1=ne-nv+1
        pref=Fraction(R**(3-h1))/Fraction(aut)
        need=DIM-ne
        br_v=[[] for _ in range(nv)]
        for q,(i,j) in enumerate(edges):
            br_v[i].append((q,0)); br_v[j].append((q,1))
        contrib=Fraction(0); nw=0
        for wv in itertools.product(range(R), repeat=ne):
            ok=True
            for v in range(nv):
                s=sum(A[l] for l in range(4) if assign[l]==v)
                for q,(i,j) in enumerate(edges):
                    if i==v: s+=wv[q]
                    if j==v: s-=wv[q]
                if s%R!=0: ok=False; break
            if not ok: continue
            nw+=1
            ES=[ESw[w] for w in wv]
            # enumerate allocations
            for q in itertools.product(range(need+1),repeat=4):
                if sum(q)>need: continue
                fc=Fraction(1)
                for l in range(4): fc*=FL[l][q[l]]
                if fc==0: continue
                # kappa per vertex
                for kkeys in itertools.product(list(KS.items()), repeat=nv):
                    dk=sum(sum((m+1)*e for m,e in enumerate(k)) for k,v in kkeys)
                    if sum(q)+dk>need: continue
                    for ees in itertools.product(*[list(ES[q2].items()) for q2 in range(ne)]):
                        if sum(q)+dk+sum(i+j for (i,j),v in ees)!=need: continue
                        ec=Fraction(1)
                        for (k2,v) in ees: ec*=v
                        if ec==0: continue
                        # per-vertex integrals
                        val=Fraction(1)
                        for v in range(nv):
                            lq=tuple(q[l] for l in range(4) if assign[l]==v)
                            bq=tuple(ee[0][0] if side==0 else ee[0][1] for (qq,side) in br_v[v] for ee in [ees[qq]])
                            new=list(lq)+list(bq)
                            for m,e in enumerate(kkeys[v][0]): new+=[m+2]*e
                            val*=psi(gv[v],tuple(new))
                            if val==0: break
                        contrib+=pref*fc*Fraction(kkeys[0][1])*Fraction(kkeys[1][1] if nv>1 else 1)*Fraction(kkeys[2][1] if nv>2 else 1)*ec*val
        log.write(f"{gv} {assign} {edges} aut={aut} h1={h1} #W={nw} contrib={contrib}\n")
        total+=contrib
    log.write(f"TWO-EDGE TOTAL = {total}\n"); log.close()
    print("two-edge total =",total,float(total))
    return total

if __name__=="__main__":
    run()
