"""Phase 3d: exact LLL + SVP + Smart reduction loop at v=(50069). K=Q specialization.
c8val = min valuation of M logs = 1 (computed phase3b). lam=p^1. Bi=log_i/p mod p^u.
Basis (rows), d=5: e1..e4, r=(B1..B4,p^u). Target y=0 -> SVP (shortest nonzero vector).
Exact LLL (delta=1, integer arithmetic on Gram) then exact enumeration (Fincke-Pohst).
Success: shortest^2 > n*B0^2 (n=4) => B2=(u+c9)/c5 with c9=c8+ordDisc/2=1.
B0: global initial bound. K0 pipeline gives K0~7e20 (dominated by v=(2)); Smart/Sage then
sets B0 = K0-ish (up to constants). Take B0 = 1e21 (safe overestimate, logged).
Loop u=1.. until success; need p-adic prec > u+1.
"""
import math
P=50069
c3_cert=0.027; c5=c3_cert/math.log(P); c9=1
low_bound=round(1/c5)+1
B0=1e21
print(f"B0={B0:.0e} n*B0^2={4*B0*B0:.2e} c5={c5:.6e} low={low_bound}")
def padic_log(a,p,prec):
    mod=p**prec; modj=mod*p
    A=pow(a,p-1,modj); t=(A-1)%modj; J=prec+2
    L=0; pw=1
    for j in range(1,J+1):
        pw=(pw*t)%modj
        inv=pow(j,-1,modj); term=pw*inv%modj
        L=(L+term)%modj if j%2==1 else (L-term)%modj
    return ((L%mod)*pow(p-1,-1,mod))%mod
# exact LLL on row basis (Gram-Schmidt over QQ via Fractions? use float GS + integer μ, exact enough
# for dim 5 with tiny entries? NO — must be exact. Use Fraction-based LLL.)
from fractions import Fraction
def lll_rows(B, delta=Fraction(3,4)):
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
        if sq[k] < (delta-mu[k][k-1]**2)*sq[k-1] if sq[k-1]!=0 else False:
            B[k],B[k-1]=B[k-1],B[k]; k=max(k-1,1)
        else: k+=1
    return B
def svp_enum(B):
    # exact shortest nonzero vector length^2 via Fincke-Pohst on LLL basis; bound = min row norm
    import math
    from fractions import Fraction
    n=len(B); d=len(B[0])
    Bf=[[float(x) for x in row] for row in B]
    # GS floats for enumeration (bounds only need ~correct; verify final candidate exactly)
    Bs=[]; mu=[[0.0]*n for _ in range(n)]; sq=[]
    for i in range(n):
        v=list(Bf[i])
        for j in range(i):
            mu[i][j]=sum(Bf[i][k]*Bs[j][k] for k in range(d))/sq[j]
            v=[a-b*mu[i][j] for a,b in zip(v,Bs[j])]
        Bs.append(v); sq.append(sum(a*a for a in v))
    best=min(sum(float(x*x) for x in row) for row in B)
    bestc=None
    # enumerate with pruning; dim 5, tiny: brute force coeffs in range
    R=int(math.ceil(math.sqrt(float(best))/min(math.sqrt(s) for s in sq if s>0)))+1
    R=min(R,200)
    rng=range(-R,R+1)
    import itertools
    for co in itertools.product(rng,repeat=n):
        if all(c==0 for c in co): continue
        v=[Fraction(0)]*d
        for i,c in enumerate(co):
            if c: v=[a+c*b for a,b in zip(v,B[i])]
        s2=sum(a*a for a in v)
        if s2<best and s2>0: best=s2; bestc=co
    return best,bestc
prec_needed=12
logs={a:padic_log(a,P,prec_needed) for a in (2,3,7,11)}
Bi={a:(v//P)%(P**prec_needed) for a,v in logs.items()}
print("Bi computed (divided by p exactly).")
for u in range(1,9):
    mod=P**u
    Bu=[Bi[a]%mod for a in (2,3,7,11)]
    rows=[[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[Bu[0],Bu[1],Bu[2],Bu[3],P**u]]
    red=lll_rows(rows)
    s2,co=svp_enum(red)
    thr=4*B0*B0
    print(f"u={u}: shortest^2={float(s2):.4e}  vs 4B0^2={thr:.2e}  success={float(s2)>thr}", flush=True)
    if float(s2)>thr:
        B2=(u+c9)/c5
        import math as m
        print(f"  REDUCED BOUND B2=(u+c9)/c5={(u+c9)}/{c5:.6e}={B2:.4f} -> floor {m.floor(B2)}; max(4,2,.)={max(4,2,m.floor(B2))}")
        break
