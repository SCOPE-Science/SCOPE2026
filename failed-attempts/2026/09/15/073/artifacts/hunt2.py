from fractions import Fraction
import itertools, random
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

def rand_dense(d,k,rng):
    M=mons(4,d)
    F=defaultdict(Fraction)
    for e in rng.sample(M,k):
        F[e]+=Fraction(rng.choice([1,-1,2,-2]))
    return dict(F)

def mult_matrix_L_sym(F,d,i,bc):
    src_i,tgt_i,Mi = bc[i]
    src_j,tgt_j,Mj = bc[i+1]
    def basis_rows(M):
        basis=[]; cur=[]
        for k,row in enumerate(M):
            t=cur+[row]
            if rank_frac(t)>rank_frac(cur):
                cur=t; basis.append(k)
        return basis
    bi=basis_rows(Mi); bj=basis_rows(Mj)
    ri=len(bi); rj=len(bj)
    Ms=sp.Matrix([[sp.Rational(Mj[r][c].numerator, Mj[r][c].denominator) for c in range(len(Mj[0]))] for r in range(len(Mj))])
    B=Ms.extract(bj, list(range(len(Mj[0]))))
    BT=B.T
    P=[]
    for k in range(len(src_j)):
        v=Ms.extract([k], list(range(len(Mj[0]))))
        aug=BT.row_join(v.T)
        rr,piv=aug.rref()
        x=[rr[t,-1] for t in range(rj)]
        P.append(x)
    l=sp.symbols('l0:4')
    idx_j={b:k for k,b in enumerate(src_j)}
    Mat=sp.zeros(ri,rj)
    for s,a in enumerate([src_i[k] for k in bi]):
        for j in range(4):
            na=list(a); na[j]+=1; na=tuple(na)
            k=idx_j[na]
            for t in range(rj):
                Mat[s,t]+=l[j]*P[k][t]
    return Mat,l,ri,rj

rng=random.Random(20260707)
Ls=([1,2,3,5],[1,0,2,3],[2,-1,1,4],[1,1,1,1])
hits=0; tested=0
for trial in range(400):
    d=6; k=rng.choice([6,8,10,12])
    F=rand_dense(d,k,rng)
    h=hvec(F,d)
    S=max(h); N=sum(1 for x in h if x==S)
    if N<3: continue
    tested+=1
    fails=[mul_rank(F,d,i,L)<min(h[i],h[i+1]) for L in Ls for i in range(d)]
    # count per L any failure
    perL=[any(mul_rank(F,d,i,L)<min(h[i],h[i+1]) for i in range(d)) for L in Ls]
    print(f"t{trial} k={k} h={h} N={N} perL-fail={perL} {sorted(F.items())}")
    if all(perL):
        print("  *** fails at all 4 test L's -> exact all-L check")
        bc={i:cat_matrix(F,d,i) for i in range(d+1)}
        for i in range(d):
            Mat,l,ri,rj=mult_matrix_L_sym(F,d,i,bc)
            r=min(ri,rj)
            from itertools import combinations
            allzero=True; wit=None
            for rs in combinations(range(ri),r):
                for cs in combinations(range(rj),r):
                    m=sp.expand(Mat.extract(list(rs),list(cs)).det())
                    if m!=0: allzero=False; wit=(rs,cs,m); break
                if not allzero: break
            print(f"    i={i} {ri}->{rj} allL-def={allzero} {str(wit)[:200]}")
        hits+=1
        break
print("tested-N3:",tested,"hits:",hits)
