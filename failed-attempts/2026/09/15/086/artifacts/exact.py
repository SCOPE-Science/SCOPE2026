"""Exact linear algebra over Q(i): elements a+bi with Fractions. Exact principal-series matrices over Q(i,t1,t2) specialized at exact t values (roots of unity / small rationals). Then exact spinning/MeatAxe (no numerics)."""
from fractions import Fraction

class G:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a=a if isinstance(a,Fraction) else Fraction(a)
        self.b=b if isinstance(b,Fraction) else Fraction(b)
    def __add__(self,o):
        if not isinstance(o,G): o=G(o)
        return G(self.a+o.a,self.b+o.b)
    def __sub__(self,o):
        if not isinstance(o,G): o=G(o)
        return G(self.a-o.a,self.b-o.b)
    def __neg__(self): return G(-self.a,-self.b)
    def __mul__(self,o):
        if not isinstance(o,G): o=G(o)
        return G(self.a*o.a-self.b*o.b, self.a*o.b+self.b*o.a)
    def __truediv__(self,o):
        if not isinstance(o,G): o=G(o)
        d=o.a*o.a+o.b*o.b
        assert d!=0
        return G((self.a*o.a+self.b*o.b)/d,(self.b*o.a-self.a*o.b)/d)
    def __eq__(self,o):
        if not isinstance(o,G): o=G(o)
        return self.a==o.a and self.b==o.b
    def is0(self): return self.a==0 and self.b==0
    def __repr__(self): return f"({self.a}+{self.b}i)"
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        r=G(1)
        for _ in range(n): r=r*self
        return r
    def __hash__(self): return hash((self.a,self.b))
ZERO=G(0); ONE=G(1); II=G(0,1)

def mat_eye(n):
    return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def mat_mul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    C=[[ZERO]*m for _ in range(n)]
    for i in range(n):
        for l in range(k):
            if A[i][l].is0(): continue
            for j in range(m):
                C[i][j]=C[i][j]+A[i][l]*B[l][j]
    return C
def mat_vec(M,v):
    return [sum((M[i][j]*v[j] for j in range(len(v))),ZERO) for i in range(len(M))]

def rref(rows):
    """rows: list of row-vecs. Returns (basis, pivots). Exact."""
    M=[list(r) for r in rows]
    m=len(M); n=len(M[0]) if m else 0
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if not M[i][c].is0(): p=i; break
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        d=M[r][c]
        M[r]=[x/d for x in M[r]]
        for i in range(m):
            if i!=r and not M[i][c].is0():
                f=M[i][c]
                M[i]=[x-f*y for x,y in zip(M[i],M[r])]
        piv.append(c); r+=1
    return M[:r],piv

def row_space_basis(vecs):
    if not vecs: return []
    return rref(vecs)[0]

def in_span(basis_rows, v):
    # is v in row-span of basis? append and check rank increase
    r1=len(rref(basis_rows)[0]) if basis_rows else 0
    r2=len(rref(basis_rows+[v])[0])
    return r2==r1

def span_dim(vecs): return len(rref(vecs)[0]) if vecs else 0

def ker_basis(M):
    """nullspace of square M as list of vecs (right kernel): solve Mx=0 exact via RREF of M rows? Use augmented RREF on M as linear map: RREF rows of M, free cols."""
    n=len(M)
    R,piv=rref([list(r) for r in M])
    pivset=set(piv)
    free=[c for c in range(n) if c not in pivset]
    basis=[]
    # R has len(piv) rows; row j has pivot at piv[j]
    for f in free:
        v=[ZERO]*n; v[f]=ONE
        for j,p in enumerate(piv):
            v[p]=v[p]-R[j][f]
        basis.append(v)
    return basis

def spin_fix(gens, seeds):
    """row-space saturation: smallest subspace containing seeds stable under all g (rows: v -> v g? We use column convention: submodule spanned by cols stable under left mult. Implement with column vecs: represent subspace by row-basis of transposes.)"""
    # work with row vecs, action v -> v G (right action of transposed system = same submodule lattice as left for the opposite... careful: submodules under LEFT action Gv. Saturation: S <- S + G S. With row representation, use S^T... simplest: define action on row vecs by v -> v G^T? No: left submodule {Gv} corresponds to row space stable under right mult by G^T... Let me just implement columns directly with column-RREF via transpose trick.
    pass

# Column-space implementation: represent subspace by list of column vecs; RREF via rows of transpose.
def col_rref_dim(vecs):
    if not vecs: return 0
    rows=[list(v) for v in zip(*vecs)]  # transpose: rows are coords
    return len(rref(rows)[0])

def col_space_contains(basis_cols, v):
    if not basis_cols: return all(x.is0() for x in v)
    n=len(v)
    # solve basis*c = v
    B=[[basis_cols[j][i] for j in range(len(basis_cols))] for i in range(n)]  # n x k
    aug=[B[i]+[v[i]] for i in range(n)]
    R,piv=rref(aug)
    k=len(basis_cols)
    for row in R:
        if all(x.is0() for x in row[:k]) and not row[k].is0():
            return False
    return True

def col_basis(vecs):
    # greedy independent subset
    out=[]
    for v in vecs:
        if not col_space_contains(out,v):
            out.append(v)
    return out

def spin_submodule(gens, seeds):
    S=col_basis(seeds)
    changed=True
    while changed:
        changed=False
        for g in gens:
            for v in list(S):
                w=mat_vec(g,v)
                if not col_space_contains(S,w):
                    S.append(w); changed=True
        S=col_basis(S)
        if len(S)==len(gens[0]): return S
    return S

def restrict_mat(g, S):
    # find R with g S_j = sum_i S_i R[i,j]: solve each col
    k=len(S); n=len(g)
    B=[[S[j][i] for j in range(k)] for i in range(n)]
    R=[[ZERO]*k for _ in range(k)]
    for j in range(k):
        w=mat_vec(g,S[j])
        aug=[B[i]+[w[i]] for i in range(n)]
        Rr,piv=rref(aug)
        sol=[ZERO]*k
        for row in Rr:
            # find pivot col
            for c in range(k):
                if not row[c].is0():
                    sol[c]=row[k]; break
                    # assumes RREF single-pivot rows; ok since consistent
        R[j]=[sol[i] for i in range(k)]  # column j
    # convert to row-matrix (R as matrix with R[i][j])
    return [[R[j][i] for j in range(k)] for i in range(k)]

def charpoly_2x2_trace_det(M):
    pass

def eigenspace_seeds(gens):
    """widely applicable seeds: kernels of (g - lam) for eigenvalue lam of each generator restricted... eigenvalues unknown exactly. Instead: kernels of products (g-a)(g-b)? Without eigenvalues, use: minimal polynomial factors. Practical exact approach: take F = generic INTEGER combo f = c1 T1+c2 T2+c3 X1+c4 X2 (small ints); compute its characteristic polynomial exactly (Danilevsky/Faddeeva), factor over Q(i) by trial roots (eigenvalues are algebraic, often in Q(i,sqrt..)); kernels of (F - lam) need lam. If charpoly splits over Q(i), kernels exact. Else use rational kernels: ker p(F) for irreducible factors p (primary components) -> proper submodules (primary decomposition = submodule!). Great: primary components under ONE generic element that separates blocks give submodules. Implement: charpoly via Faddeeva (exact), factor into linears over Q(i) if splits else find irreducible factor kernel."""
    return None

def faddeeva_charpoly(M):
    n=len(M)
    # returns coeffs c_0..c_n with det(lam I - M) = lam^n + c_{n-1} lam^{n-1}+...+c_0, exact over Q(i)
    I=mat_eye(n)
    B=[[ZERO]*n for _ in range(n)]
    coeffs=[None]*n
    for k in range(1,n+1):
        if k==1:
            MB=M
        else:
            MB=mat_mul(M,B)
        # c_{n-k} = -tr(MB)/k
        tr=sum((MB[i][i] for i in range(n)),ZERO)
        coeffs[n-k]=ZERO-tr/G(k)
        # B = MB + c I
        B=[[MB[i][j]+(coeffs[n-k] if i==j else ZERO) for j in range(n)] for i in range(n)]
    return coeffs  # [c_0,...,c_{n-1}]

def mat_poly_eval(coeffs, M):
    """coeffs dict exp->G; evaluate at M + identity shifts."""
    n=len(M)
    R=[[ZERO]*n for _ in range(n)]
    for e,c in coeffs.items():
        if e==0:
            P=mat_eye(n)
        else:
            P=mat_eye(n)
            for _ in range(e): P=mat_mul(M,P) if False else mat_pow(M,e)
            P=mat_pow(M,e)
        for i in range(n):
            for j in range(n):
                R[i][j]=R[i][j]+c*P[i][j]
    return R

def mat_pow(M,e):
    n=len(M); R=mat_eye(n)
    for _ in range(e): R=mat_mul(R,M)
    return R

def mat_add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def mat_scale(A,c): return [[A[i][j]*c for j in range(len(A))] for i in range(len(A))]

def kernel_of_mat(K):
    return ker_basis(K)

def primary_seeds(F):
    """Return list of nonzero proper kernels ker p(F) for factors: try linear factors over Q(i) via rational-root-like search (eigenvalues in Q(i) common here: +-1, +-i, etc.), plus complement kernels."""
    n=len(F)
    cp=faddeeva_charpoly(F)  # c_0..c_{n-1}
    # evaluate trial roots lam in Q(i) grid
    grid=[G(a,b) for a in range(-3,4) for b in range(-3,4)]
    grid+=[G(Fraction(a,2),Fraction(b,2)) for a in range(-3,4) for b in range(-3,4)]
    found=[]
    for lam in grid:
        # evaluate charpoly at lam
        v=sum((cp[k]*lam**k if k>0 else cp[k] for k in range(n)),ZERO)+lam**n
        if v.is0():
            # eigenspace kernel
            K=[[F[i][j]-(lam if i==j else ZERO) for j in range(n)] for i in range(n)]
            kb=ker_basis(K)
            if kb: found.append((lam,kb))
    return found, cp
