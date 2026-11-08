"""Independent finite checks for weighted-spanning-tree fairness on wheel graphs.

Run: python3 verify.py. Standard library only.
"""
from itertools import combinations
from fractions import Fraction
from math import comb, cos, pi, sqrt

CHECKS = 0

def ck(assertion, message):
    global CHECKS
    CHECKS += 1
    assert assertion, message

def bareiss_det(M):
    """Fraction-free exact determinant, nonzero principal minors."""
    A = [r[:] for r in M]
    n = len(A)
    d = 1
    for k in range(n-1):
        q = A[k][k]
        ck(q != 0, ('pivot', k, A))
        for i in range(k+1,n):
            for j in range(k+1,n):
                a = A[i][j]*q - A[i][k]*A[k][j]
                ck(a % d == 0, ('division', i,j,k))
                A[i][j] = a // d
        for i in range(k+1,n): A[i][k]=0
        d = q
    return A[-1][-1]

def rim_cofactor(m, w):
    L = [[(w+2 if i==j else 0) for j in range(m)] for i in range(m)]
    for i in range(m):
        L[i][(i+1)%m] -= 1
        L[i][(i-1)%m] -= 1
    return bareiss_det(L)

def graph_edges(m):
    return [(i,(i+1)%m) for i in range(m)]+[(m,i) for i in range(m)]

def poly_brute(m):
    E = graph_edges(m)
    C=[0]*(m+1)
    edge_counts=[0]*(2*m)
    for S in combinations(range(2*m),m):
        parent=list(range(m+1))
        def find(v):
            while parent[v]!=v:
                v=parent[v]
            return v
        good=True
        for eid in S:
            u,v=E[eid]
            u,v=find(u),find(v)
            if u==v:
                good=False; break
            parent[u]=v
        if not good: continue
        C[sum(eid>=m for eid in S)]+=1
        for eid in S: edge_counts[eid]+=1
    return C,edge_counts

def poly_value(C,w):
    return sum(c*w**k for k,c in enumerate(C))

def sp_probability(m,w):
    return sum(w/(w+2-2*cos(2*pi*j/m)) for j in range(m))/m

def root(m):
    lo,hi=1.0, 4/3
    for _ in range(90):
        mid=(hi+lo)/2
        if sp_probability(m,mid)<.5:lo=mid
        else:hi=mid
    return (hi+lo)/2

for m in range(3,9):
    C,E=poly_brute(m)
    ck(C[0]==0,('zero spokes',m))
    ck(C[m]==1,('all spokes',m))
    for w in range(1,5):
        ck(poly_value(C,w)==rim_cofactor(m,w),('Kirchhoff',m,w))
    total=sum(C)
    sp=sum(k*C[k] for k in range(m+1))
    for q in E[m:]:
        ck(q*m == sp, ('spoke symmetry',m,q,sp))
    for q in E[:m]:
        ck(q*m == m*total-sp,('rim symmetry',m,q,total,sp))
    a = Fraction(sp, m*total)
    actual_overlap = sum(Fraction(q, total)**2 for q in E)
    exact_overlap_formula = Fraction(m,2) + 2*m*(a-Fraction(1,2))**2
    ck(actual_overlap == exact_overlap_formula, ('uniform overlap',m))
    ck((actual_overlap > Fraction(m,2)) == (m>=4), ('strict gap',m))
    w=root(m)
    ck(abs(sp_probability(m,w)-.5)<1e-12,('marginal',m,w))
    x=(w+2-sqrt(w*w+4*w))/2
    ck(abs(1-3*x+3*x**m-x**(m+1))<1e-11,('root polynomial',m))
    if m==3: ck(abs(w-1)<1e-12,('K4',m))
    else: ck(1<w<4/3,('bounds',m,w))
for m in range(3,25):
    w=root(m)
    ck(1-1e-11 <=w<4/3,('all bounded',m))
    if m>3: ck(root(m-1)<w,('monotone',m))
for m in [15,20,25]:
    w=root(m)
    # double precision cancellation limits the precision for larger m
    ck(abs(w-4/3)<1e-6,('limit',m,w))
print('VERIFY_OK',CHECKS, 'exact and numerical assertions')
