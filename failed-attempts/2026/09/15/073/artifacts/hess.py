from fractions import Fraction
import itertools
from collections import defaultdict
import sympy as sp

def mons(nvars,deg):
    return sorted([e for e in itertools.product(range(deg+1),repeat=nvars) if sum(e)==deg])
def diff_poly(F,a):
    G=dict(F)
    for vi,ee in enumerate(a):
        for _ in range(ee):
            NG=defaultdict(Fraction)
            for e,c in G.items():
                if e[vi]>0:
                    ne=list(e); ne[vi]-=1; ne=tuple(ne)
                    NG[ne]+=c*e[vi]
            G=dict(NG)
    return G
def rank_frac(M):
    if not M or not M[0]: return 0
    R=[row[:] for row in M]; m=len(R); n=len(R[0]); r=0
    for c in range(n):
        piv=None
        for i in range(r,m):
            if R[i][c]!=0: piv=i; break
        if piv is None: continue
        R[r],R[piv]=R[piv],R[r]
        inv=R[r][c]
        for i in range(m):
            if i!=r and R[i][c]!=0:
                f=R[i][c]/inv
                for j in range(c,n): R[i][j]-=f*R[r][j]
        r+=1
    return r
def cat_matrix(F,d,i):
    src=mons(4,i); tgt=mons(4,d-i)
    tindex={b:j for j,b in enumerate(tgt)}
    M=[]
    for a in src:
        G=diff_poly(F,a)
        row=[Fraction(0)]*len(tgt)
        for e,c in G.items():
            if sum(e)==d-i and e in tindex: row[tindex[e]]=c
        M.append(row)
    return src,tgt,M
def hvec(F,d):
    return [rank_frac(cat_matrix(F,d,i)[2]) for i in range(d+1)]
def mul_rank(F,d,i,L):
    if i+1>d: return 0
    src_i=mons(4,i); src_ip1=mons(4,i+1); tgt=mons(4,d-i-1)
    tindex={b:j for j,b in enumerate(tgt)}
    D={b:diff_poly(F,b) for b in src_ip1}
    Mcomp=[]
    for a in src_i:
        row=[Fraction(0)]*len(tgt)
        for j in range(4):
            na=list(a); na[j]+=1; na=tuple(na)
            G=D[na]
            for e,c in G.items():
                if sum(e)==d-i-1 and e in tindex:
                    row[tindex[e]]+=Fraction(L[j])*c
        Mcomp.append(row)
    return rank_frac(Mcomp)

X1,X2,X3,X4=sp.symbols('X1 X2 X3 X4')
vars=[X1,X2,X3,X4]
def to_sym(F):
    p=0
    for e,c in F.items():
        m=1
        for v,ee in zip(vars,e): m*=v**ee
        p+=sp.Rational(c.numerator,c.denominator)*m
    return sp.expand(p)

def hess_zero(F):
    P=to_sym(F)
    H=sp.hessian(P,vars)
    return sp.simplify(H.det())==0

def test(F,d,label):
    h=hvec(F,d)
    S=max(h); N=sum(1 for x in h if x==S)
    hz=hess_zero(F)
    print(f"{label}: h={h} S={S} N={N} hess0={hz}")
    for L in ([1,1,1,1],[1,2,3,5],[1,0,2,3]):
        mr=[mul_rank(F,d,i,L) for i in range(d)]
        need=[min(h[i],h[i+1]) for i in range(d)]
        wlp=all(a==b for a,b in zip(mr,need))
        print(f"   L={L} ranks={mr} need={need} WLP={wlp}")

# Perazzo-like candidates degree 5 in 4 vars
# F = X1^4*X2 + X1^3*X3^2? Let's try known vanishing-hessian family: F depending on fewer vars after change?
# Try F = X1^3*X2 + X1^2*X3^2 + X2^2*X3^2? hmm
cands={
 "P1": {(4,1,0,0):Fraction(1),(0,4,1,0):Fraction(1),(0,0,4,1):Fraction(1),(1,0,0,4):Fraction(1)},
 "P2": {(3,2,0,0):Fraction(1),(0,3,2,0):Fraction(1),(0,0,3,2):Fraction(1),(2,0,0,3):Fraction(1)},
 "P3": {(4,1,0,0):Fraction(1),(4,0,1,0):Fraction(1),(0,4,0,1):Fraction(1),(0,0,4,1):Fraction(1)},
 "P4": {(3,1,1,0):Fraction(1),(0,3,1,1):Fraction(1),(1,0,3,1):Fraction(1),(1,1,0,3):Fraction(1)},
}
for k,F in cands.items():
    test(F,5,k)
