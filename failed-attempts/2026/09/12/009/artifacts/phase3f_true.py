"""Phase 3f: TRUE Smart/Sage reduction semantics.
minimal_vector(A.T, y=0): y IS in lattice (0 vector) -> returns |b1*|^2/2^{n-1} where b1*
is SHORTEST GRAM-SCHMIDT vector of LLL-reduced basis (a LOWER bound for lambda1^2, since
lambda1^2 >= min GS norm... precisely |b1*|^2/c1 with c1=2^{n-1}).
So c10^2 = LB(lambda1^2), NOT exact SVP! Our exact SVP=1 gives LB possibly << 1.
Key: test c10^2 > n*B0^2 needs LB > 4e42 — needs shortest GS vector huge — the e_i rows
keep lattice short. UNLESS... wait: lattice = rows of A^T. Rows of A^T for our A:
A rows: e1..e4,(B,p^u). A^T rows = columns of A: (1,0,0,0,B1),(0,1,0,0,B2),...,(0,0,0,0,p^u).
LLL of THESE: short vectors exist (e.g. combos killing last coord?). The GS-shortest is
bounded by... the lattice contains vectors with first-4 coords small and last coord ~Bi.
Hmm, but actually the intended test per Smart Lemma VI.5: ell(L,y) with y NOT in L typically
(b0 != 0). Our y=0 IS in L -> second branch -> LB(shortest). With e_i-like vectors of
length ~1 present... wait are e_i=(1,0,0,0,0) IN the lattice? Lattice gens: c1=(1,0,0,0,B1),
c2=(0,1,0,0,B2), c3, c4, c5=(0,0,0,0,p^u). (1,0,0,0,0) = c1 - B1*c5/p^u — NOT integral combo
(unless p^u | B1). So e_i NOT in lattice; shortest vector could still be small though
(e.g. c1 itself has length sqrt(1+B1^2) ~ B1 ~ p^u huge for large u!). As u grows, ALL
nonzero vectors get long?? c1 length ~ p^u. Any combo z: first coords z1..z4 (integers),
last = sum ziBi + z5 p^u. For small z1..z4 (e.g. (1,0,0,0,z5)): last = B1+z5 p^u, min over
z5 = (B1 mod p^u) ~ up to p^u/2. So shortest ~ min over small combos — as u grows, the
residues Bi mod p^u are essentially random mod p^u, shortest grows like p^{u*(1 - 4/5)}?
By Minkowski: det = p^u (det A = p^u), dim 5 -> lambda1 ~ det^{1/5} = p^{u/5}.
Test needs lambda1^2 > 4 B0^2 = 4e42 -> p^{2u/5} > 4e42 -> u > 5*log_p(2e21) ~ 5*4.6 ~ 23.
So with u ~ 25-30 (prec ~32), reduction CAN fire! Our loop only went to u=8. And our exact
SVP enumeration with R cap 200 was also wrong-ish for large u (coeff range must scale).
Continue properly: exact SVP via smarter enumeration (LLL + Fincke-Pohst with correct radius
update), u up to ~40, prec 44. Each u: 5-dim SVP, cheap.
Also B0: use B0=1e21 (K0~7e20 dominated by place 2; Sage then takes B0 ~ K0 scale).
Actually Sage S_unit_equation: B0arch from archimedean + K0 = max; then loops reductions.
B0=1e21 safe overestimate (larger B0 only makes test harder; success at 1e21 implies
success at true smaller B0 — NO, wait: test c10^2 > nB0^2 with LARGER B0 is HARDER. Using
overestimate is CONSERVATIVE: if fires at 1e21, fires at true B0. Good.)
"""
import math
from fractions import Fraction
P=50069
c3_cert=0.027; c5=c3_cert/math.log(P); c9=1
B0=1e21
print(f"B0={B0:.0e} threshold 4B0^2={4*B0*B0:.2e} c5={c5:.6e}")
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
    from fractions import Fraction
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
def svp_exact(B):
    # Fincke-Pohst exact SVP on LLL basis B (rows), dim 5; returns shortest^2 (exact Fraction)
    import math
    from fractions import Fraction
    n=len(B); d=len(B[0])
    Bf=[[float(x) for x in row] for row in B]
    Bs=[]; mu=[[0.0]*n for _ in range(n)]; sq=[]
    for i in range(n):
        v=list(Bf[i])
        for j in range(i):
            mu[i][j]=sum(Bf[i][k]*Bs[j][k] for k in range(d))/sq[j]
            v=[a-b*mu[i][j] for a,b in zip(v,Bs[j])]
        Bs.append(v); sq.append(sum(a*a for a in v))
    best=sum(float(x*x) for x in B[0]); bestc=None
    for row in B[1:]:
        s=sum(float(x*x) for x in row)
        if s<best: best=s
    # coefficient bound per level
    def recurse(k, center_tail, r2, coeff):
        nonlocal best
        if k<0:
            v=[Fraction(0)]*d
            for i,c in enumerate(coeff):
                if c: v=[a+c*b for a,b in zip(v,B[i])]
            s2=sum(a*a for a in v)
            if s2>0 and float(s2)<best: best=float(s2); bestc=tuple(coeff)
            return
        # x_k range: (x_k + center)^2*sq[k] <= r2
        import math
        rad=math.sqrt(r2/sq[k]) if sq[k]>0 else 0
        lo=int(math.ceil(-center_tail-rad)); hi=int(math.floor(-center_tail+rad))
        for xk in range(lo,hi+1):
            coeff[k]=xk
            # update: new center for lower levels: center_j += mu[k][j]*(xk+center_tail)? standard FP:
            recurse(k-1, 0, r2-(xk+center_tail)**2*sq[k], coeff)
            # NOTE: simplified (ignores off-diagonal recentering) — valid only if mu small (LLL: |mu|<=.5)
            # To stay EXACT we instead do full brute force when ranges small; fallback below.
    # Simpler rigorous approach: brute force with radius-derived box (valid box, may over-enumerate)
    R=int(math.ceil(math.sqrt(best)/min(math.sqrt(s) for s in sq if s>0)))+1
    if R>60:
        print(f"    [u-level] R={R} too big for brute force; using LLL-LB only"); return None
    import itertools
    rng=range(-R,R+1)
    bestF=None
    for co in itertools.product(rng,repeat=n):
        if all(c==0 for c in co): continue
        v=[Fraction(0)]*d
        for i,c in enumerate(co):
            if c: v=[a+c*b for a,b in zip(v,B[i])]
        s2=sum(a*a for a in v)
        if float(s2)<best and s2>0: best=float(s2); bestF=s2
    return best
prec=48
logs={a:padic_log(a,P,prec) for a in (2,3,7,11)}
Bi={a:(v//P) for a,v in logs.items()}
for u in (10,12,14,16,18,20,24,28,32,36,40):
    mod=P**u
    Bu=[Bi[a]%mod for a in (2,3,7,11)]
    # lattice gens = COLUMNS of Sage A = rows of A^T:
    G=[[1,0,0,0,Bu[0]],[0,1,0,0,Bu[1]],[0,0,1,0,Bu[2]],[0,0,0,1,Bu[3]],[0,0,0,0,P**u]]
    red=lll_rows(G)
    s2=svp_exact(red)
    print(f"u={u}: shortest^2={('%.4e'%float(s2)) if s2 else 'SKIP'} vs 4B0^2=4.00e42", flush=True)
    if s2 is not None and float(s2)>4*B0*B0:
        B2=(u+c9)/c5
        print(f"  FIRES: B2=({u}+1)/{c5:.6e}={B2:.2f}")
        break
