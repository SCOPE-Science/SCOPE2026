"""Exact arithmetic over Q(i,sqrt2) = Q-basis {1,i,s,is}, s^2=2. Covers 8th roots: zeta8=(1+i)*s/2."""
from fractions import Fraction
BASIS_N=4
def _v(a0=0,a1=0,a2=0,a3=0):
    return [Fraction(a0),Fraction(a1),Fraction(a2),Fraction(a3)]
# mult table: i^2=-1, s^2=2, (is)^2=-2
MT=[[0]*4 for _ in range(4)]
# e0=1,e1=i,e2=s,e3=is
MT[0]=[((0,1),),((1,1),),((2,1),),((3,1),)]
MT[1]=[((1,1),),((0,-1),),((3,1),),((2,-1),)]
MT[2]=[((2,1),),((3,1),),((0,2),),((1,2),)]
MT[3]=[((3,1),),((2,-1),),((1,2),),((0,-2),)]
class F:
    __slots__=("c",)
    def __init__(self,c=None):
        if c is None: self.c=[Fraction(0)]*4
        elif isinstance(c,F): self.c=list(c.c)
        elif isinstance(c,int): self.c=[Fraction(c),Fraction(0),Fraction(0),Fraction(0)]
        elif isinstance(c,tuple) and len(c)==2: self.c=[Fraction(c[0]),Fraction(c[1]),Fraction(0),Fraction(0)]
        else: self.c=[Fraction(x) for x in c]
    def __add__(self,o):
        if not isinstance(o,F): o=F(o)
        return F([a+b for a,b in zip(self.c,o.c)])
    def __sub__(self,o):
        if not isinstance(o,F): o=F(o)
        return F([a-b for a,b in zip(self.c,o.c)])
    def __neg__(self): return F([-a for a in self.c])
    def __mul__(self,o):
        if not isinstance(o,F): o=F(o)
        r=[Fraction(0)]*4
        for i in range(4):
            if self.c[i]==0: continue
            for j in range(4):
                if o.c[j]==0: continue
                for (k,s) in MT[i][j]:
                    r[k]+=self.c[i]*o.c[j]*s
        return F(r)
    def __truediv__(self,o):
        if not isinstance(o,F): o=F(o)
        # solve M(o) x = self
        M=multmat(o)
        b=list(self.c)
        x=solve4(M,b)
        return F(x)
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        r=F(1)
        for _ in range(n): r=r*self
        return r
    def is0(self): return all(x==0 for x in self.c)
    def __eq__(self,o):
        if not isinstance(o,F): o=F(o)
        return self.c==o.c
    def __repr__(self): return f"F{self.c}"
    def __hash__(self): return hash(tuple(self.c))
ZERO=F(0); ONE=F(1); II=F((0,1)); SS=F([0,0,1,0])
def _inv2():
    return F([Fraction(1,2),Fraction(0),Fraction(0),Fraction(0)])
ZETA8=(ONE+II)*SS*_inv2()  # (1+i)s/2
def multmat(o):
    M=[[Fraction(0)]*4 for _ in range(4)]
    for j in range(4):
        e=[Fraction(0)]*4; e[j]=Fraction(1)
        w=(F(e)*o).c
        for i in range(4): M[i][j]=w[i]
    return M
def solve4(M,b):
    # exact solve 4x4
    A=[list(M[i])+[b[i]] for i in range(4)]
    for c in range(4):
        p=None
        for i in range(c,4):
            if A[i][c]!=0: p=i; break
        assert p is not None, "singular"
        A[c],A[p]=A[p],A[c]
        d=A[c][c]
        A[c]=[x/d for x in A[c]]
        for i in range(4):
            if i!=c and A[i][c]!=0:
                f=A[i][c]
                A[i]=[x-f*y for x,y in zip(A[i],A[c])]
    return [A[i][4] for i in range(4)]
def mat_eye(n): return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def mat_mul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    C=[[ZERO]*m for _ in range(n)]
    for i in range(n):
        for l in range(k):
            if A[i][l].is0(): continue
            for j in range(m): C[i][j]=C[i][j]+A[i][l]*B[l][j]
    return C
def mat_vec(M,v):
    return [sum((M[i][j]*v[j] for j in range(len(v))),ZERO) for i in range(len(M))]
def mat_pow(M,e):
    n=len(M); R=mat_eye(n)
    for _ in range(e): R=mat_mul(R,M)
    return R
def mat_add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def mat_scale(A,c): return [[A[i][j]*c for j in range(len(A))] for i in range(len(A))]
def rref(rows):
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
def ker_basis(M):
    n=len(M)
    R,piv=rref([list(r) for r in M])
    pivset=set(piv)
    free=[c for c in range(n) if c not in pivset]
    basis=[]
    for f in free:
        v=[ZERO]*n; v[f]=ONE
        for j,p in enumerate(piv): v[p]=v[p]-R[j][f]
        basis.append(v)
    return basis
def col_contains(cols,v):
    if not cols: return all(x.is0() for x in v)
    n=len(v); k=len(cols)
    B=[[cols[j][i] for j in range(k)] for i in range(n)]
    aug=[B[i]+[v[i]] for i in range(n)]
    R,piv=rref(aug)
    for row in R:
        if all(x.is0() for x in row[:k]) and not row[k].is0(): return False
    return True
def col_basis(vecs):
    out=[]
    for v in vecs:
        if not col_contains(out,v): out.append(v)
    return out
def spin(gens,seeds):
    S=col_basis(seeds)
    while True:
        grew=False
        for g in gens:
            for v in list(S):
                w=mat_vec(g,v)
                if not col_contains(S,w): S.append(w); grew=True
        S=col_basis(S)
        if not grew or len(S)==len(gens[0]): return S
def gen_kernel(F,lam,power):
    n=len(F)
    G_=[[F[i][j]-(lam if i==j else ZERO) for j in range(n)] for i in range(n)]
    P=mat_pow(G_,power)
    return ker_basis(P)
def charpoly(M):
    n=len(M)
    B=[[ZERO]*n for _ in range(n)]
    coeffs=[None]*n
    for k in range(1,n+1):
        MB=M if k==1 else mat_mul(M,B)
        tr=sum((MB[i][i] for i in range(n)),ZERO)
        coeffs[n-k]=ZERO-tr/F(k)
        B=mat_add(MB,mat_scale(mat_eye(n),coeffs[n-k]))
    return coeffs
def eval_poly_at(coeffs,lam,n):
    # coeffs c_0..c_{n-1} of lam^n+c_{n-1}lam^{n-1}+...+c_0
    v=lam**n
    for k in range(n): v=v+coeffs[k]*(lam**k)
    return v
def trial_roots():
    vals=[]
    for a in range(-4,5):
        for b in range(-4,5):
            vals.append(F((a,b)))
            vals.append(F([Fraction(a,2),Fraction(b,2),Fraction(0),Fraction(0)]))
    # 8th roots multiples
    z=ZETA8
    for k in range(8): vals.append(z**k)
    for k in range(8):
        for c in [F(1),F(2),F((1,0))]:
            vals.append((z**k)*c)
    # dedupe
    out=[]
    for v in vals:
        if not any(v==w for w in out): out.append(v)
    return out
TRIALS=trial_roots()
def factor_roots(cp):
    n=len(cp)
    roots=[]
    for lam in TRIALS:
        if eval_poly_at(cp,lam,n).is0(): roots.append(lam)
    return roots
def burnside_dim(gens, cap_mults=40):
    """dim of span of words in gens (= dim image of H). Simple cert if == n^2."""
    n=len(gens[0])
    def flat(M): return tuple(M[i][j] for i in range(n) for j in range(n))
    basis=[mat_eye(n)]+list(gens)
    # row-reduce flats to basis
    def indep(mats):
        rows=[list(flat(M)) for M in mats]
        R,piv=rref(rows)
        return len(piv),R
    cur=col_basis_irrelevant=None
    # greedy span
    span=list(basis)
    # reduce: keep independent set
    def span_basis(mats):
        rows=[list(flat(M)) for M in mats]
        R,piv=rref(rows)
        # reconstruct basis mats from R rows? Instead greedy:
        out=[]
        for M in mats:
            # check if flat(M) in span of flats(out)
            f=list(flat(M))
            if not out: out.append(M); continue
            B=[list(flat(X)) for X in out]
            aug=[B[i]+[f[i]] for i in range(len(f))]
            # solve: is f in row span of B? row-space membership: rank test
            r1=len(rref([list(r) for r in B])[0])
            r2=len(rref([list(r) for r in B]+[f])[0])
            if r2>r1: out.append(M)
        return out
    S=span_basis(span)
    changed=True; rounds=0
    while changed and rounds<cap_mults:
        changed=False; rounds+=1
        new=[]
        for g in gens:
            for X in list(S):
                Y=mat_mul(g,X)
                f=list(flat(Y))
                B=[list(flat(Z)) for Z in S+new]
                r1=len(rref([list(r) for r in B])[0])
                r2=len(rref([list(r) for r in B]+[f])[0])
                if r2>r1: new.append(Y)
        if new: S=list(S+span_basis(S+new)[len(S):]); changed=True
    return len(S)
