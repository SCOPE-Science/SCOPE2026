"""Phase 3g: iterate Smart reduction to convergence + finalize ord_p cap.
After first reduction B0: 1e21 -> B1=6012 (u=14). Re-run with B0=6012: threshold 4*6012^2
~1.4e8; shortest at small u already exceeds -> much smaller u fires -> B2 smaller.
Iterate until fixed point. Then FINAL step: Smart Lemma: ord_p bound from B_final:
  ord_p(x(1-x)) <= ... the reduced B bounds EXPONENTS; valuation cap needs one more turn:
  per Sage pipeline, reduced B0 => for each place, m0_Kv_new = (u+c9)/c5 style bound on
  ord_v (the 'K0' values become small). Actually in Sage, p_adic_LLL_bound returns new
  K0 (bound on ord valuations weighted) — the returned B2 IS the new valuation bound
  up to c5 scaling? Let's read Sage p_adic_LLL_bound wrapper + S_unit_equation loop to
  get exact final conversion. For K=Q at v=(p): returned value max(4,w,floor(B2)) with
  B2=(u+c9)/c5 — this is the new bound on ...K0_l (which bounds ord_v * e_v * ... ).
  K0_l relates to ord via c5: ord_v <= K0_l * e_v * log Nv / c3-ish. We'll read the code.
Meanwhile iterate LLL loop with decreasing B0 (need care: lattice depends on B0 only via
threshold; Bi same). Also must handle: SECOND iteration lattice u smaller; fine.
"""
import math
from fractions import Fraction
P=50069
c3_cert=0.027; c5=c3_cert/math.log(P); c9=1
def padic_log(a,p,prec):
    mod=p**prec; modj=mod*p
    A=pow(a,p-1,modj); t=(A-1)%modj; J=prec+2
    L=0; pw=1
    for j in range(1,J+1):
        pw=(pw*t)%modj
        inv=pow(j,-1,modj); term=pw*inv%modj
        L=(L+term)%modj if j%2==1 else (L-term)%modj
    return ((L%mod)*pow(p-1,-1,mod))%mod
def lll_rows(B):
    B=[list(map(Fraction,r)) for r in B]
    n=len(B); d=len(B[0])
    def gs(B):
        Bs=[]; mu=[[Fraction(0)]*n for _ in range(n)]; sq=[]
        for i in range(n):
            v=list(B[i])
            for j in range(i):
                num=sum(B[i][k]*Bs[j][k] for k in range(d))
                mu[i][j]=num/sq[j]
                v=[a-b*mu[i][j] for a,b in zip(v,Bs[j])]
            Bs.append(v); sq.append(sum(a*a for a in v))
        return Bs,mu,sq
    k=1
    while k<n:
        Bs,mu,sq=gs(B)
        for j in range(k-1,-1,-1):
            q=int(math.floor(float(mu[k][j])+0.5))
            if q: B[k]=[a-q*b for a,b in zip(B[k],B[j])]; Bs,mu,sq=gs(B)
        if sq[k-1]!=0 and sq[k] < (Fraction(3,4)-mu[k][k-1]**2)*sq[k-1]:
            B[k],B[k-1]=B[k-1],B[k]; k=max(k-1,1)
        else: k+=1
    return B
def shortest_lb_and_exact(B, thr):
    # returns (fires:bool, shortest_exact_or_None). Exact via brute force if box small.
    import itertools
    n=len(B); d=len(B[0])
    Bf=[[float(x) for x in row] for row in B]
    Bs=[]; mu=[[0.0]*n for _ in range(n)]; sq=[]
    for i in range(n):
        v=list(Bf[i])
        for j in range(i):
            mu[i][j]=sum(Bf[i][k]*Bs[j][k] for k in range(d))/sq[j]
            v=[a-b*mu[i][j] for a,b in zip(v,Bs[j])]
        Bs.append(v); sq.append(sum(a*a for a in v))
    best=min(sum(float(x*x) for x in row) for row in B)
    if best>thr: return True,best  # LLL vector already exceeds -> fires (rigorous!)
    R=int(math.ceil(math.sqrt(thr)/min(math.sqrt(s) for s in sq if s>0)))+1
    if R>40: return None,None  # box too big, undecided at this u (try bigger u)
    rng=range(-R,R+1)
    for co in itertools.product(rng,repeat=n):
        if all(c==0 for c in co): continue
        v=[Fraction(0)]*d
        for i,c in enumerate(co):
            if c: v=[a+c*b for a,b in zip(v,B[i])]
        s2=sum(a*a for a in v)
        if float(s2)<=thr: return False,s2  # found short vector -> does NOT fire
    return True,None  # enumerated all: everything > thr -> fires
prec=48
logs={a:padic_log(a,P,prec) for a in (2,3,7,11)}
Bi={a:(v//P) for a,v in logs.items()}
B0=1e21
for it in range(10):
    thr=4*B0*B0
    fired=None
    for u in range(1,30):
        mod=P**u
        Bu=[Bi[a]%mod for a in (2,3,7,11)]
        G=[[1,0,0,0,Bu[0]],[0,1,0,0,Bu[1]],[0,0,1,0,Bu[2]],[0,0,0,1,Bu[3]],[0,0,0,0,P**u]]
        red=lll_rows(G)
        r,_=shortest_lb_and_exact(red,thr)
        if r is None: continue
        if r:
            B2=(u+c9)/c5
            print(f"iter{it}: B0={B0:.4g} u={u} FIRES -> Bnew={B2:.4f}", flush=True)
            B0=B2; fired=True; break
        # else: short vector exists at this u; try next u (don't conclude)
    if not fired:
        print(f"iter{it}: no firing u<=29 with B0={B0:.4g} (STALLED)")
        break
print(f"FINAL B0={B0}")
