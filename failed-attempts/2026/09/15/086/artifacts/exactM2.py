"""Exact M(t) over Q(i,s) with t entries in F; full exact decomposition incl. generalized kernels + Burnside cert."""
import sys
sys.path.insert(0,'output/artifacts')
from exact2 import F,ZERO,ONE,II,SS,ZETA8,mat_eye,mat_mul,mat_vec,mat_pow,mat_add,mat_scale,rref,ker_basis,col_contains,col_basis,spin,gen_kernel,charpoly,eval_poly_at,factor_roots,TRIALS
from engine import WORDS, LENS, descend, act_s, Qpoly
from exact2 import burnside_dim
QQ=II
def gpow(g,k):
    if k==0: return ONE
    r=ONE
    for _ in range(abs(k)): r=r*g
    if k>0: return r
    # inverse via division
    return ONE/r
def left_terms(s,widx):
    from engine import left_mult_by_s
    out=[]
    for c,u in left_mult_by_s(s,widx):
        if abs(c-1)<1e-9: out.append((ONE,u))
        elif abs(c-1j)<1e-9: out.append((II,u))
        elif abs(complex(c-(1j-1)))<1e-9: out.append((II-ONE,u))
        else: raise AssertionError(c)
    return out
def th_tw(x,widx,t):
    n=12
    if widx==0:
        r=[ZERO]*n; r[0]=gpow(t[0],x[0])*gpow(t[1],x[1]); return r
    s,vidx=descend(widx)
    sx=act_s(s,x)
    rec=th_tw(sx,vidx,t)
    out=[ZERO]*n
    for u,bu in enumerate(rec):
        if bu.is0(): continue
        for (c,z) in left_terms(s,u): out[z]=out[z]+bu*c
    Qp=Qpoly(x,s)
    if Qp:
        qm1=II-ONE
        for y,cy in Qp.items():
            cyF=F((int(round(cy.real)),int(round(cy.imag))))
            rec2=th_tw(y,vidx,t)
            for u,bu in enumerate(rec2):
                if bu.is0(): continue
                out[u]=out[u]+bu*cyF*qm1
    return out
def M_of(t):
    n=12
    T1=[[ZERO]*n for _ in range(n)]; T2=[[ZERO]*n for _ in range(n)]
    for w in range(n):
        for c,u in left_terms(1,w): T1[u][w]=T1[u][w]+c
        for c,u in left_terms(2,w): T2[u][w]=T2[u][w]+c
    X1=[[ZERO]*n for _ in range(n)]; X2=[[ZERO]*n for _ in range(n)]
    for w in range(n):
        r1=th_tw((1,0),w,t); r2=th_tw((0,1),w,t)
        for u in range(n): X1[u][w]=r1[u]; X2[u][w]=r2[u]
    return [T1,T2,X1,X2]
def lincomb(cf,gens):
    n=len(gens[0]); R=[[ZERO]*n for _ in range(n)]
    for c,M in zip(cf,gens):
        for i in range(n):
            for j in range(n): R[i][j]=R[i][j]+c*M[i][j]
    return R
def decomp(gens, combos, depth=0):
    n=len(gens[0])
    if n<=1: return [n]
    for cf in combos:
        Fm=lincomb(cf,gens)
        cp=charpoly(Fm)
        roots=factor_roots(cp)
        for lam in roots:
            for pw in (1,2,3):
                K=gen_kernel(Fm,lam,pw)
                if not K: break
                S=spin(gens,K)
                d=len(S)
                if 0<d<n:
                    sub=[restrict(g,S) for g in gens]
                    C=complement(S,n)
                    quo=[quotient(g,S,C) for g in gens]
                    return decomp(sub,combos,depth+1)+decomp(quo,combos,depth+1)
                if len(K)==len(gen_kernel(Fm,lam,pw+1)): break
    return [n]
def restrict(g,S):
    k=len(S); n=len(g)
    B=[[S[j][i] for j in range(k)] for i in range(n)]
    Rcols=[]
    for j in range(k):
        w=mat_vec(g,S[j])
        a=solve_cols(B,w)
        Rcols.append(a)
    return [[Rcols[j][i] for j in range(k)] for i in range(k)]
def complement(S,n):
    B=col_basis(list(S))
    std=[[ONE if i==k else ZERO for i in range(n)] for k in range(n)]
    for v in std:
        if not col_contains(B,v): B.append(v)
    return B[len(S):]
def quotient(g,S,C):
    n=len(g); k=len(S); m=len(C)
    Bcols=S+C
    B=[[Bcols[j][i] for j in range(len(Bcols))] for i in range(n)]
    R=[[ZERO]*m for _ in range(m)]
    for j in range(m):
        w=mat_vec(g,C[j])
        a=solve_cols(B,w)
        for i in range(m): R[i][j]=a[k+i]
    return R
def solve_cols(B,w):
    n=len(w); k=len(B[0])
    aug=[list(B[i])+[w[i]] for i in range(n)]
    Rr,piv=rref(aug)
    sol=[ZERO]*k
    for row in Rr:
        lead=None
        for c in range(k):
            if not row[c].is0(): lead=c; break
        if lead is not None: sol[lead]=row[k]
    return sol
COMBOS=[(F(1),F(2),F(1),F(0)),(F(0),F(1),F(3),F(1)),(F(2),F(-1),F(0),F(1)),(F(1),F(1),F(1),F(1)),(F(1),F(0),F(2),F(-1)),(F(0),F(0),F(1),F(2)),(F(5),F(1),F(0),F(3)),(F(1),F(3),F(-2),F(1))]
if __name__=="__main__":
    G_=lambda a,b: F((a,b))
    Z=ZETA8
    tests={"t11":(ONE,ONE),"t1m1":(ONE,F(-1)),"tm11":(F(-1),ONE),"tm1m1":(F(-1),F(-1)),
      "ti1":(II,ONE),"t1i":(ONE,II),"tii":(II,II),"tmi1":(F(-1),II),
      "tz1":(Z,ONE),"t1z":(ONE,Z),"tzz":(Z,Z),"tgen":(F(2),F(3))}
    import json
    res={}
    for name,t in tests.items():
        gens=M_of(t)
        try:
            bd=burnside_dim(gens)
        except Exception as e: bd=f"ERR {e}"
        try:
            d=sorted(decomp(gens,COMBOS))
        except Exception as e: d=f"ERR {e}"
        print(name,"decomp=",d,"sum=",sum(d) if isinstance(d,list) else "?","burnside=",bd,flush=True)
        res[name]=str(d)
