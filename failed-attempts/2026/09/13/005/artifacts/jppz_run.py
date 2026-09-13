"""Staged JPPZ integration. Stage 1: smooth graph (ne=0). Computes its exact contribution with full logging."""
from fractions import Fraction
from math import factorial as F
import itertools, sys
sys.path.insert(0, "output/artifacts")
from psi_engine import psi
from jppz_main import leg_series, kappa_series, expcoef, R, X, A, MU, DIM, Bp, defclc

def kappa_integral(g, nlegs, kvec, legpow_extra):
    """int_{Mbar_{g,nlegs}} prod_m kappa_m^{e_m} prod_{i} psi_i^{q_i}, kvec=(e1,..), legpow_extra tuple len nlegs.
    Reduce kappa products by adding one marking per kappa factor: kappa_{m} = pi_*(psi_{new}^{m+1})."""
    es=[]
    for m,e in enumerate(kvec):
        es+=[m]*e  # careful: kvec index m corresponds to kappa_m? our kappa_series keys are tuples over m=1..M
    return Fraction(0)

if __name__=="__main__":
    # Smooth graph: single vertex g=2, legs (3,2,1,1)<->a=(4,5,6,6).
    # Integrand: exp(sum CV kappa) * prod_legs exp(sum cl psi^m) * [denominator prod 1/(1-mu psi)]
    # Needed total degree DIM=7. Enumerate (q_legs from denom+legseries combined, kappa exps).
    LS={l: leg_series(A[l],DIM) for l in range(4)}
    # folded leg series: F_l[q] = sum_{p<=q} LS[l][p]*MU[l]^{q-p}
    FL={}
    for l in range(4):
        d={}
        for q in range(DIM+1):
            d[q]=sum(LS[l][p]*Fraction(MU[l]**(q-p)) for p in range(q+1))
        FL[l]=d
    KS=kappa_series(DIM)
    def kappas_to_psi_integral(g,nlegs,kkey,legq):
        # kkey tuple (e_1..e_M) over m=1..; legq tuple of total leg powers. Add K=sum e markings with powers m+1.
        new=list(legq)
        for m,e in enumerate(kkey):
            mm=m+1
            new+=[mm+1]*e
        return psi(g,tuple(new))
    tot=Fraction(0); log=open("output/artifacts/hodge_smooth.log","w")
    for q in itertools.product(range(DIM+1),repeat=4):
        if sum(q)>DIM: continue
        fc=Fraction(1)
        for l in range(4): fc*=FL[l][q[l]]
        for kkey,kc in KS.items():
            deg=sum((m+1)*e for m,e in enumerate(kkey))
            if sum(q)+deg!=DIM: continue
            v=kappas_to_psi_integral(2,4,kkey,q)
            tot+=Fraction(R**(2*2-1-0))*fc*kc*v
            if v!=0 and fc*kc!=0:
                log.write(f"q={q} k={[ (m+1,e) for m,e in enumerate(kkey) if e]} fc={fc} kc={kc} psi-int={v} -> {Fraction(R**3)*fc*kc*v}\n")
    log.write(f"SMOOTH TOTAL (incl r^3=343) = {tot}\n"); log.close()
    print("smooth total =",tot,float(tot))
