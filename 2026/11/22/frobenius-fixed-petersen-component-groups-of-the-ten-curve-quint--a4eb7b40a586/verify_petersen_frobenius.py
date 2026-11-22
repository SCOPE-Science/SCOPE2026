"""Exact integer certificate for the Petersen critical-group Frobenius table.

Run with Python 3, no third-party packages.  Geometric vertices are the ten
2-subsets of a five-element label set; adjacency means disjointness.
"""
from itertools import combinations
from math import prod

V = list(combinations(range(5), 2))
N = len(V)
L = [[(3 if i == j else -int(set(V[i]).isdisjoint(V[j])))
      for j in range(N)] for i in range(N)]
R = [row[:-1] for row in L[:-1]]
I = [[int(i == j) for j in range(9)] for i in range(9)]

# Q = 10 R^{-1}. This small integral identity proves exponent(K) divides 10.
Q = [
 [6,2,3,3,2,3,3,4,4],
 [2,6,3,3,2,4,4,3,3],
 [3,3,8,4,4,4,5,4,5],
 [3,3,4,8,4,5,4,5,4],
 [2,2,4,4,6,3,3,3,3],
 [3,4,4,5,3,8,4,4,5],
 [3,4,5,4,3,4,8,5,4],
 [4,3,4,5,3,4,5,8,4],
 [4,3,5,4,3,5,4,4,8],
]
assert [[sum(R[i][k]*Q[k][j] for k in range(9)) for j in range(9)]
        for i in range(9)] == [[10*x for x in row] for row in I]


def determinant_integer(A):
    """Fraction-free Bareiss algorithm for an exact integral determinant."""
    B = [r[:] for r in A]
    n = len(B)
    sign = 1
    prev = 1
    for k in range(n-1):
        pivot = B[k][k]
        if pivot == 0:
            t = next((i for i in range(k+1,n) if B[i][k]), None)
            if t is None: return 0
            B[k], B[t] = B[t], B[k]
            sign *= -1
            pivot = B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z = B[i][j]*pivot - B[i][k]*B[k][j]
                assert z % prev == 0
                B[i][j] = z // prev
        for i in range(k+1,n): B[i][k] = 0
        prev = pivot
    return sign*B[n-1][n-1]


def rank_mod(A, prime):
    B = [[a % prime for a in row] for row in A]
    rows = len(B); cols = len(B[0]); rank = 0
    for j in range(cols):
        pivot = next((i for i in range(rank,rows) if B[i][j]), None)
        if pivot is None: continue
        B[rank], B[pivot] = B[pivot], B[rank]
        inv = pow(B[rank][j],-1,prime)
        B[rank] = [(u*inv) % prime for u in B[rank]]
        for i in range(rows):
            if i != rank and B[i][j]:
                c = B[i][j]
                B[i] = [(u-c*v) % prime for u,v in zip(B[i], B[rank])]
        rank += 1
        if rank == rows: break
    return rank


def perm_of_cycle_type(part):
    p=[]; start=0
    for a in part:
        p += list(range(start+1,start+a))+[start]
        start += a
    assert sorted(p)==list(range(5))
    return p


def on_degree_zero_lattice(part):
    p = perm_of_cycle_type(part)
    psi = [V.index(tuple(sorted((p[a],p[b])))) for a,b in V]
    # Basis e_{V[j]} - e_{V[9]}, 0 <= j < 9.
    return [[int(i == psi[j])-int(i == psi[9]) for j in range(9)]
            for i in range(9)]

TYPES = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),
         (3,2),(4,1),(5,)]
EXPECTED = [(4,3),(2,2),(2,1),(0,1),(0,0),(1,0),(0,1)]

assert len(V) == 10
assert sum(-L[i][j] for i in range(10) for j in range(i+1,10)) == 15
assert determinant_integer(R) == 2000
assert rank_mod(R,2) == 5 and rank_mod(R,5) == 6
for part,(d2,d5) in zip(TYPES,EXPECTED):
    T=on_degree_zero_lattice(part)
    # Check explicitly that T maps the column lattice R Z^9 into itself:
    # R^{-1} T R = (Q T R)/10 has integral entries.
    QTR = [[sum(Q[i][u]*T[u][v]*R[v][j]
                 for u in range(9) for v in range(9))
             for j in range(9)] for i in range(9)]
    assert all(x % 10 == 0 for row in QTR for x in row)
    augmented = [R[i]+[T[i][j]-I[i][j] for j in range(9)]
                 for i in range(9)]
    r2=9-rank_mod(augmented,2)
    r5=9-rank_mod(augmented,5)
    assert (r2,r5)==(d2,d5),(part,r2,r5)
    print(part, "2-rank",r2,"5-rank",r5,
          "fixed-order",2**r2*5**r5)
print("PETERSEN_FROBENIUS_COMPONENT_GROUPS_EXACT_OK")
