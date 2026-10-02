from fractions import Fraction
from itertools import product
from functools import lru_cache

# Exact rational linear algebra for a finite-dimensional sanity check of
# the finite-signature lemma used in the arbitrary-field extension.

def rref(rows):
    A = [[Fraction(x) for x in row] for row in rows]
    if not A:
        return [], []
    m, n = len(A), len(A[0])
    pivots = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        z = A[r][c]
        A[r] = [x / z for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                z = A[i][c]
                A[i] = [A[i][j] - z*A[r][j] for j in range(n)]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return A, pivots

def basis(vectors, D=4):
    if not vectors:
        return tuple()
    R, piv = rref(vectors)
    rows = []
    for row in R:
        if any(row):
            rows.append(tuple(row))
    return tuple(rows)

def rank(vectors, D=4):
    return len(basis(vectors, D))

def add(U, V, D=4):
    return basis(list(U)+list(V), D)

def nullspace(M):
    if not M:
        return []
    R, piv = rref(M)
    n = len(R[0])
    free = [j for j in range(n) if j not in piv]
    out=[]
    for f in free:
        x=[Fraction(0) for _ in range(n)]
        x[f]=1
        for i,p in enumerate(piv):
            x[p] = -R[i][f]
        out.append(x)
    return out

@lru_cache(maxsize=None)
def intersect(U, V, D=4):
    if not U or not V:
        return tuple()
    # Convert row bases to column matrices; solve U^T a = V^T b.
    ru, rv = len(U), len(V)
    M=[]
    for d in range(D):
        M.append([U[i][d] for i in range(ru)] + [-V[j][d] for j in range(rv)])
    ns = nullspace(M)
    vecs=[]
    for x in ns:
        a=x[:ru]
        v=[sum(a[i]*U[i][d] for i in range(ru)) for d in range(D)]
        if any(v):
            vecs.append(v)
    return basis(vecs,D)

@lru_cache(maxsize=None)
def dimcap(U,V,D=4):
    return len(intersect(U,V,D))

D=4
Y=[
    (1,0,0,0),
    (0,1,0,0),
    (1,1,1,0),
    (0,1,1,1),
]
# All states span(Z), Z subseteq Y.
states=[]
for mask in range(1<<len(Y)):
    W=basis([Y[i] for i in range(len(Y)) if mask>>i & 1],D)
    if W not in states:
        states.append(W)

# A finite sample of rational subspaces, including the states and many
# additional lines/planes that are not spans of subsets of Y.
raw=[v for v in product([0,1], repeat=D) if any(v)]
lines=[]
for v in raw:
    L=basis([v],D)
    if L not in lines:
        lines.append(L)
subspaces=list(states)
for L in lines:
    if L not in subspaces:
        subspaces.append(L)
for i in range(min(8,len(lines))):
    for j in range(i+1,min(8,len(lines))):
        P=add(lines[i],lines[j],D)
        if P not in subspaces:
            subspaces.append(P)

# Signature as in the proof: dim L plus dim(W cap L) for every reachable state W.
def signature(L):
    return (len(L),) + tuple(dimcap(W,L,D) for W in states)

# Any affine invariant constraint assembled from these dimensions is constant
# on signatures. Check this for several exact rational coefficient vectors.
coeff_sets=[
    [Fraction((7*j+3)%11-5, 13) for j in range(len(states))],
    [Fraction((5*j+1)%9-4, 17) for j in range(len(states))],
    [Fraction((3*j+2)%7-3, 19) for j in range(len(states))],
]

def score(L, coeff):
    return -Fraction(5,3)*len(L) + sum(c*dimcap(W,L,D) for c,W in zip(coeff,states))

by_sig={}
for L in subspaces:
    s=signature(L)
    vals=tuple(score(L,c) for c in coeff_sets)
    if s in by_sig:
        assert by_sig[s] == vals
    else:
        by_sig[s]=vals

# Supermodularity check for L -> dim(Z cap L), hence for nonnegative mixtures
# minus a modular rank term.
weights=[Fraction(j+1, sum(range(1,len(states)+1))) for j in range(len(states))]
def g(L):
    return -Fraction(2,1)*len(L) + Fraction(7,1)*sum(a*dimcap(Z,L,D) for a,Z in zip(weights,states))

checks=0
for L in subspaces:
    for H in subspaces:
        lhs=g(L)+g(H)
        rhs=g(intersect(L,H,D))+g(add(L,H,D))
        assert lhs <= rhs
        checks += 1

print("PASS")
print(f"states={len(states)}")
print(f"sampled_subspaces={len(subspaces)}")
print(f"distinct_signatures={len(by_sig)}")
print(f"supermodularity_checks={checks}")
