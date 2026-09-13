"""Boundary stages: 1-edge graphs (18 sep + 1 nonsep loop), exact integration with logging."""
from fractions import Fraction
from math import factorial as F
import itertools, sys
sys.path.insert(0, "output/artifacts")
from psi_engine import psi
from jppz_main import leg_series, kappa_series, edge_series, expcoef, R, X, A, MU, DIM

FL={}
LS={l: leg_series(A[l],DIM) for l in range(4)}
for l in range(4):
    FL[l]={q: sum(LS[l][p]*Fraction(MU[l]**(q-p)) for p in range(q+1)) for q in range(DIM+1)}
KS=kappa_series(DIM)

def vp_integral(g, leg_exps, br_exps, kkey):
    """int over Mbar_{g,n} (n=len(leg_exps)+len(br_exps)) of prod psi_leg^q prod psi_br^b with kappas->extra markings."""
    new=list(leg_exps)+list(br_exps)
    for m,e in enumerate(kkey):
        new+=[(m+1)+1]*e
    return psi(g,tuple(new))

def run_one_edge():
    log=open("output/artifacts/hodge_1edge.log","w")
    total=Fraction(0)
    # --- separating graphs: splits of legs with leg0 on side A ---
    splits=[]
    for mask in range(1,(1<<4)-1):
        I1=tuple(i for i in range(4) if mask>>i & 1); I2=tuple(i for i in range(4) if not mask>>i & 1)
        if 0 not in I1: continue
        for g1 in range(3):
            g2=2-g1
            if 2*g1-2+len(I1)+1<=0 or 2*g2-2+len(I2)+1<=0: continue
            splits.append((I1,I2,g1,g2))
    log.write(f"sep graphs: {len(splits)}\n")
    for (I1,I2,g1,g2) in splits:
        # weighting: w at side A determined: sum_A a + w = 0; w = -sum_A
        w=(R-sum(A[l] for l in I1)%R)%R
        assert (sum(A[l] for l in I2)-w)%R==0 or True
        # check side B: sum_B - w = 0 mod R (total sum 0)
        assert (sum(A[l] for l in I2)-w)%R==0, (I1,I2,w)
        ES=edge_series(w,DIM)
        h1=0; pref=Fraction(R**(3-h1))
        need=DIM-1
        contrib=Fraction(0)
        # enumerate leg powers, kappa per side, edge (i,j)
        for q in itertools.product(range(need+1),repeat=4):
            if sum(q)>need: continue
            fc=Fraction(1)
            for l in range(4): fc*=FL[l][q[l]]
            if fc==0: continue
            for kA,kcA in KS.items():
                dA=sum((m+1)*e for m,e in enumerate(kA))
                for kB,kcB in KS.items():
                    dB=sum((m+1)*e for m,e in enumerate(kB))
                    if sum(q)+dA+dB>need: continue
                    for (i,j),ec in ES.items():
                        if sum(q)+dA+dB+i+j!=need: continue
                        qA=tuple(q[l] for l in I1); qB=tuple(q[l] for l in I2)
                        vA=vp_integral(g1,qA,(i,),kA); vB=vp_integral(g2,qB,(j,),kB)
                        contrib+=pref*fc*kcA*kcB*ec*vA*vB
        log.write(f"sep I1={I1} I2={I2} g=({g1},{g2}) w={w} contrib={contrib}\n")
        total+=contrib
    # --- nonseparating loop: vertex g=1, 4 legs, 7 weightings, aut=2 ---
    ESw={w: edge_series(w,DIM) for w in range(R)}
    need=DIM-1
    for w in range(R):
        ES=ESw[w]; pref=Fraction(R**(3-1),1)/Fraction(2)
        contrib=Fraction(0)
        for q in itertools.product(range(need+1),repeat=4):
            if sum(q)>need: continue
            fc=Fraction(1)
            for l in range(4): fc*=FL[l][q[l]]
            if fc==0: continue
            for kkey,kc in KS.items():
                dk=sum((m+1)*e for m,e in enumerate(kkey))
                if sum(q)+dk>need: continue
                for (i,j),ec in ES.items():
                    if sum(q)+dk+i+j!=need: continue
                    v=vp_integral(1,q,(i,j),kkey)
                    contrib+=pref*fc*kc*ec*v
        log.write(f"nonsep w={w} contrib={contrib}\n")
        total+=contrib
    log.write(f"ONE-EDGE TOTAL = {total}\n"); log.close()
    print("one-edge total =",total,float(total))
    return total

if __name__=="__main__":
    run_one_edge()
