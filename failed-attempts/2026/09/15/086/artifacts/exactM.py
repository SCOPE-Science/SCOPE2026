"""Exact M(t) over Q(i) at exact t: rebuild engine with G arithmetic; theta recursion polys evaluated directly at t (exact), avoiding symbolic polys."""
import sys
sys.path.insert(0,'output/artifacts')
from exact import G,ZERO,ONE,II,mat_eye,mat_mul,mat_vec,mat_pow,mat_add,mat_scale,rref,ker_basis,col_basis,col_space_contains,spin_submodule,restrict_mat,faddeeva_charpoly,primary_seeds
from engine import WORDS, LENS, mat_of_word, MAT2IDX, descend, act_s, Qpoly
sys.path.insert(0,'output/artifacts')

QQ=II  # q=i as G
def left_mult_by_s_exact(s,widx):
    from engine import left_mult_by_s
    terms=left_mult_by_s(s,widx)
    out=[]
    for c,u in terms:
        # c in {1, q-1, q}: convert complex to G
        if abs(c-1)<1e-9: out.append((ONE,u))
        elif abs(c-1j)<1e-9: out.append((II,u))
        elif abs(complex(c-(1j-1)))<1e-9: out.append((II-ONE,u))
        else: raise AssertionError(c)
    return out

def gpow(g,k):
    from exact import ONE as _O
    if k==0: return _O
    r=_O
    for _ in range(abs(k)): r=r*g
    return r if k>0 else _O/r
def th_tw_exact(x, widx, t):
    """ rec[T_w](x) evaluated at t: returns list of 12 G-values b_u (coeff of T_u in theta_x T_w)."""
    from functools import lru_cache
    n=12
    if widx==0:
        r=[ZERO]*n
        r[0]=gpow(t[0],x[0])*gpow(t[1],x[1])
        return r
    s,vidx=descend(widx)
    sx=act_s(s,x)
    rec=th_tw_exact(sx,vidx,t)
    out=[ZERO]*n
    for u,bu in enumerate(rec):
        if bu.is0(): continue
        for (c,z) in left_mult_by_s_exact(s,u):
            out[z]=out[z]+bu*c
    Qp=Qpoly(x,s)
    if Qp:
        qm1=II-ONE
        for y,cy in Qp.items():
            cyG=G(int(round(cy.real)),int(round(cy.imag)))
            rec2=th_tw_exact(y,vidx,t)
            for u,bu in enumerate(rec2):
                if bu.is0(): continue
                out[u]=out[u]+bu*cyG*qm1
    return out

def M_exact(t):
    n=12
    T1=[[ZERO]*n for _ in range(n)]; T2=[[ZERO]*n for _ in range(n)]
    for w in range(n):
        for c,u in left_mult_by_s_exact(1,w): T1[u][w]=T1[u][w]+c
        for c,u in left_mult_by_s_exact(2,w): T2[u][w]=T2[u][w]+c
    X1=[[ZERO]*n for _ in range(n)]; X2=[[ZERO]*n for _ in range(n)]
    for w in range(n):
        r1=th_tw_exact((1,0),w,t); r2=th_tw_exact((0,1),w,t)
        for u in range(n): X1[u][w]=r1[u]; X2[u][w]=r2[u]
    return {"T1":T1,"T2":T2,"X1":X1,"X2":X2}

def lin(g1,g2):
    return g1+g2
def mat_lincomb(coefs, mats):
    n=len(mats[0]); R=[[ZERO]*n for _ in range(n)]
    for c,M in zip(coefs,mats):
        for i in range(n):
            for j in range(n):
                R[i][j]=R[i][j]+c*M[i][j]
    return R

def comp_dims_exact(t, combos=((1,2,1,0),(0,1,3,1),(2,-1,0,1),(1,1,1,1),(3,1,-2,0))):
    M=M_exact(t)
    gens=[M["T1"],M["T2"],M["X1"],M["X2"]]
    # gather seeds from primary kernels of several integer combos
    seeds=[]
    for cf in combos:
        F=mat_lincomb([G(c) for c in cf],gens)
        found,cp=primary_seeds(F)
        for lam,kb in found:
            S=spin_submodule(gens,kb)
            if 0<len(S)<12:
                seeds.append(S)
    # recursive split using seeds
    def split(gens, seeds):
        n=len(gens[0])
        if n<=1: return [n]
        for S in seeds:
            # S vecs length n? seeds computed for full 12-dim; for restrictions need recompute. Only use at top level; recurse with fresh seeds.
            if len(S[0])!=n: continue
            d=len(S)
            if 0<d<n:
                sub=[restrict_mat(g,S) for g in gens]
                # quotient: complement basis
                # build complement: extend S rows? S cols independent; quotient action on Cokernel: compute via matrices on quotient = dual of restricted transpose... simpler: compute quotient matrices via exact complement:
                C=complement(S,n)
                quo=[quotient_mat(g,S,C) for g in gens]
                return split(sub, fresh_seeds(sub))+split(quo, fresh_seeds(quo))
        return [n]
    return split(gens,seeds)

def complement(S,n):
    # find basis of quotient: rows complement: take standard basis vecs not in span... compute projection: use rref of S^T to find complement cols
    cols=list(S)
    # extend to basis of G^n
    std=[[ONE if i==k else ZERO for i in range(n)] for k in range(n)]
    B=col_basis(cols)
    for v in std:
        if not col_space_contains(B,v):
            B.append(v)
    k=len(S)
    return B[k:]  # complement cols

def quotient_mat(g,S,C):
    # [g] on V/S: for c in C: g c = s-part + sum C R: solve least squares exactly: [S C] coeff then take C part
    n=len(g); k=len(S); m=len(C)
    Bcols=S+C
    # for each c: solve Bcols * a = g c
    R=[[ZERO]*m for _ in range(m)]
    for j in range(m):
        w=mat_vec(g,C[j])
        a=solve_cols(Bcols,w)
        for i in range(m):
            R[i][j]=a[k+i]
    return R

def solve_cols(Bcols,w):
    n=len(w); k=len(Bcols)
    B=[[Bcols[j][i] for j in range(k)] for i in range(n)]
    aug=[B[i]+[w[i]] for i in range(n)]
    Rr,piv=rref(aug)
    sol=[ZERO]*k
    # RREF: each pivot col c has exactly one row with leading 1? With possible free vars; particular solution: set free=0
    for row in Rr:
        lead=None
        for c in range(k):
            if not row[c].is0(): lead=c; break
        if lead is not None:
            sol[lead]=row[k]
    return sol

def fresh_seeds(gens):
    n=len(gens[0])
    seeds=[]
    for cf in [(1,2,1,0),(0,1,3,1),(2,-1,0,1),(1,1,1,1),(1,0,2,-1),(0,0,1,2),(5,1,0,3)]:
        F=mat_lincomb([G(c) for c in cf],gens)
        found,cp=primary_seeds(F)
        for lam,kb in found:
            S=spin_submodule(gens,kb)
            if 0<len(S)<n:
                seeds.append(S)
    return seeds

if __name__=="__main__":
    ONE_=ONE
    tests={
      "t11":((ONE_,ONE_)),
      "t1m1":((ONE_,G(-1))),
      "tm11":((G(-1),ONE_)),
      "tm1m1":((G(-1),G(-1))),
      "ti1":((II,ONE_)),
      "t1i":((ONE_,II)),
      "tii":((II,II)),
      "tgen":((G(2),G(3))),
    }
    for name,t in tests.items():
        try:
            d=comp_dims_exact(t)
            print(name,sorted(d),"sum=",sum(d))
        except Exception as ex:
            import traceback; traceback.print_exc()
            print(name,"ERR",ex)
