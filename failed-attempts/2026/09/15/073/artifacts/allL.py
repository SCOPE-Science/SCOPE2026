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

def bases_and_cats(F,d):
    # returns dict i -> (src, tgt, M_frac)
    out={}
    for i in range(d+1):
        src=mons(4,i); tgt=mons(4,d-i)
        tindex={b:j for j,b in enumerate(tgt)}
        M=[]
        for a in src:
            G=diff_poly(F,a)
            row=[Fraction(0)]*len(tgt)
            for e,c in G.items():
                if sum(e)==d-i and e in tindex: row[tindex[e]]=c
            M.append(row)
        out[i]=(src,tgt,M)
    return out

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

def hvec(F,d):
    return [rank_frac(bases_and_cats(F,d)[i][2]) for i in range(d+1)]

def ann_rows(M):
    # row-reduce to get pivot cols; return pivot col list and reduced matrix for quotient basis
    return None

def mult_matrix_L(F,d,i,bc):
    # Build matrix of mult-by-L map A_i -> A_{i+1} in quotient coordinates:
    # A_i = R_i/Ann_i; represent as row-space: pick pivot columns of cat_i (tgt side) as basis functionals.
    # Simpler robust approach: full presentation. Let r_i = dim A_i, r_{i+1} = dim A_{i+1}.
    # Choose basis of A_i: subset of monomials x^a whose cat rows are independent; similarly for A_{i+1}.
    # Then for each basis monomial a of A_i: x^a * L = sum_j l_j x^{a+e_j}; express x^{a+e_j} in basis of A_{i+1} modulo Ann_{i+1}.
    # Expressing mod Ann: use the cat matrix M_{i+1} (rows=monomials, cols=tgt): two exponent vectors u,v represent same class iff rows equal? No: class determined by row vector (functionals). Write row(u) as combination of basis rows: solve.
    import copy
    src_i,tgt_i,Mi = bc[i]
    src_j,tgt_j,Mj = bc[i+1]
    # find basis row indices for i and j via greedy independence
    def basis_rows(M):
        basis=[]; cur=[]
        for k,row in enumerate(M):
            t=cur+[row]
            if rank_frac(t)>rank_frac(cur):
                cur=t; basis.append(k)
        return basis
    bi=basis_rows(Mi); bj=basis_rows(Mj)
    ri=len(bi); rj=len(bj)
    # For expressing: for any monomial index k in src_j, find coeffs c over basis bj with Mj[k] = sum c_t Mj[bj[t]].
    # Solve small linear systems over rationals with symbolic l? Instead precompute projection matrix P (len(src_j) x rj) rational.
    # Build via elimination on Mj restricted... solve for each k: least squares via normal equations over Fractions (exact solve using sympy rational).
    Ms=sp.Matrix([[sp.Rational(Mj[r][c].numerator, Mj[r].__len__() and Mj[r][c].denominator) for c in range(len(Mj[0]))] for r in range(len(Mj))])
    # Actually simpler: use sympy to get row-space coordinates via pinv-like: P = Mj * pinv(Mj[bj,:])? Use exact: for each k solve Mb^T? Let's do: B = Mj[bj] (rj x n). For row vector v (1 x n), solve c B = v.
    B=Ms.extract(bj, list(range(len(Mj[0]))))
    # Use B.rref? Solve per k with B.T? cB=v -> B^T c^T = v^T.
    BT=B.T
    P=[]
    for k in range(len(src_j)):
        v=Ms.extract([k], list(range(len(Mj[0]))).copy() if False else list(range(len(Mj[0]))))
        # solve BT x = v^T
        aug=BT.row_join(v.T)
        # check consistency via rref
        rr, piv = aug.rref()
        # solution: first rj entries of last col if consistent
        x=[rr[t, -1] for t in range(rj)]
        # verify
        if (BT*sp.Matrix(x) - v.T).norm() != 0:
            # inconsistent should not happen since row space contains all rows
            raise RuntimeError("inconsistent projection")
        P.append(x)
    # Now mult matrix: ri x rj with entries linear in l
    l=sp.symbols('l0:4')
    idx_j={b:k for k,b in enumerate(src_j)}
    Mat=sp.zeros(ri, rj)
    for s,a in enumerate([src_i[k] for k in bi]):
        for j in range(4):
            na=list(a); na[j]+=1; na=tuple(na)
            k=idx_j[na]
            for t in range(rj):
                Mat[s,t]+=l[j]*P[k][t]
    return Mat, l, ri, rj

def allL_rank_deficient(F,d,i,bc):
    # check whether mult map A_i->A_{i+1} drops rank for ALL L (identically vanishing maximal minors)
    Mat,l,ri,rj=mult_matrix_L(F,d,i,bc)
    r=min(ri,rj)
    if r==0: return True, "zero map"
    # enumerate maximal minors; if all are zero polynomials -> deficient for all L
    from itertools import combinations
    nzero=0; total=0; example=None
    for rs in combinations(range(ri),r):
        for cs in combinations(range(rj),r):
            total+=1
            m=Mat.extract(list(rs),list(cs)).det()
            m=sp.expand(m)
            if m!=0:
                return False, f"minor(rs={rs},cs={cs}) = {m}"
    return True, f"all {total} maximal minors vanish identically"

def rand_sparse(d,k,rng):
    M=mons(4,d)
    F=defaultdict(Fraction)
    for e in rng.sample(M,k):
        F[e]+=Fraction(rng.choice([1,-1,2,-2,3]))
    return dict(F)

rng=random.Random(999)
for trial in range(60):
    d=5; k=rng.choice([4,5,6,7,8])
    F=rand_sparse(d,k,rng)
    bc=bases_and_cats(F,d)
    h=[rank_frac(bc[i][2]) for i in range(d+1)]
    S=max(h); N=sum(1 for x in h if x==S)
    if N<3: continue
    print(f"trial {trial} k={k} h={h} N={N}")
    for i in range(d):
        defi,info=allL_rank_deficient(F,d,i,bc)
        need=min(h[i],h[i+1])
        print(f"  i={i} dims {h[i]}->{h[i+1]} allL-deficient={defi} :: {str(info)[:160]}")
    print("  F=",sorted(F.items()))
