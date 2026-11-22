"""Exact certificate for the intersection-graph critical group of the Fermat quintic."""
from collections import Counter, deque
from itertools import permutations
from math import prod

D = 5
VERTICES = [(f, a, b) for f in range(3) for a in range(D) for b in range(D)]
N = len(VERTICES)
assert N == 75


def incident(u, v):
    f, a, b = u
    g, c, e = v
    if f == g:
        return u != v and (a == c or b == e)
    if f > g:
        return incident(v, u)
    if (f, g) == (0, 1):
        return (a + e - b - c) % 5 == 0
    if (f, g) == (0, 2):
        return (a + b + e - c) % 5 == 0
    assert (f, g) == (1, 2)
    return (a + b - c - e) % 5 == 0


A = [[int(i != j and incident(VERTICES[i], VERTICES[j]))
      for j in range(N)] for i in range(N)]
assert all(sum(row) == 18 for row in A)
assert sum(map(sum, A)) == 1350

# Independent projective-line rank check over F_11. As 3^5=1 (mod 11),
# the coefficients -3^a run through the five roots of t^5=-1.
P = 11
root = [(-pow(3, a, P)) % P for a in range(5)]
assert len(set(root)) == 5 and all(pow(t, 5, P) == P-1 for t in root)


def span(u):
    f, a, b = u
    x, y = root[a], root[b]
    if f == 0:
        return ((x, 1, 0, 0), (0, 0, y, 1))
    if f == 1:
        return ((x, 0, 1, 0), (0, y, 0, 1))
    return ((0, y, 1, 0), (x, 0, 0, 1))


def det4(cols):
    mat = [[cols[j][i] for j in range(4)] for i in range(4)]
    total = 0
    for perm in permutations(range(4)):
        inv = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1,4))
        t = prod(mat[i][perm[i]] for i in range(4))
        total += -t if inv % 2 else t
    return total % P


for i in range(N):
    for j in range(i):
        actual = det4(span(VERTICES[i]) + span(VERTICES[j])) == 0
        assert actual == bool(A[i][j]), (i, j)

seen = {0}; queue = deque([0])
while queue:
    i = queue.popleft()
    for j, e in enumerate(A[i]):
        if e and j not in seen:
            seen.add(j); queue.append(j)
assert len(seen) == N


def matmul(B, C):
    n = len(B); m = len(C[0]); k = len(C)
    Z = [[0]*m for _ in range(n)]
    for i in range(n):
        for h in range(k):
            if B[i][h]:
                coef = B[i][h]
                for j in range(m):
                    Z[i][j] += coef*C[h][j]
    return Z


# Exact, integer polynomial certificate for the adjacency spectrum:
# (A-18I)(A-3I)(A+2I)(A+7I)=0.
def shifted(base, diagonal):
    return [[base[i][j] + (diagonal if i==j else 0)
             for j in range(len(base))] for i in range(len(base))]

B = matmul(shifted(A, -18), shifted(A, -3))
C = matmul(shifted(A, 2), shifted(A, 7))
assert all(v == 0 for row in matmul(B, C) for v in row)
A2 = matmul(A, A)
A3 = matmul(A2, A)
# These traces uniquely fix the multiplicities among distinct roots.
mult = {18:1,3:38,-2:24,-7:12}
for n, mat in [(0,None),(1,A),(2,A2),(3,A3)]:
    trace = N if n == 0 else sum(mat[i][i] for i in range(N))
    assert trace == sum(k**n*v for k,v in mult.items()), (n, trace)

# The matrix-tree theorem and the above spectrum give the exact order.
TREE = 2**48 * 3**37 * 5**84
assert 15**38 * 20**24 * 25**12 == 75 * TREE


def valuation(x, p, cap):
    if not x:
        return cap
    ans = 0
    while ans < cap and x % p == 0:
        x //= p
        ans += 1
    return ans


def local_smith(sink, p, K):
    """Unimodular row/column reduction over Z/(p^K).

    A minimum-valuation pivot generates the largest ideal of the remaining
    matrix. Dividing its entries by p^v makes an invertible unit. Row and
    column operations clear the pivot, leaving an equivalent smaller block.
    K exceeds the total p-adic determinant valuation, so no invariant
    factor can vanish modulo p^K.
    """
    L = [[(18 if i==j else 0)-A[i][j] for j in range(N) if j != sink]
         for i in range(N) if i != sink]
    n = N - 1
    mod = p**K
    T = [[e % mod for e in row] for row in L]
    ans = []
    for k in range(n):
        best = K
        pos = None
        for i in range(k, n):
            for j in range(k, n):
                if T[i][j]:
                    v = valuation(T[i][j], p, best)
                    if v < best:
                        best, pos = v, (i,j)
                    if best == 0:
                        break
            if best == 0:
                break
        assert pos is not None, (p, sink, k)
        i, j = pos
        T[k], T[i] = T[i], T[k]
        for h in range(n):
            T[h][k], T[h][j] = T[h][j], T[h][k]
        pv = p**best
        smallmod = p**(K-best)
        unit = T[k][k]//pv
        assert unit % p != 0
        inv = pow(unit, -1, smallmod)
        # Every below-pivot entry is divisible by p^best.
        for i in range(k+1, n):
            if T[i][k]:
                assert T[i][k] % pv == 0
                factor = (T[i][k]//pv * inv) % smallmod
                for j in range(k, n):
                    T[i][j] = (T[i][j]-factor*T[k][j]) % mod
                assert T[i][k] == 0
        # The newly cleared column permits independent column elimination.
        for j in range(k+1, n):
            if T[k][j]:
                assert T[k][j] % pv == 0
                factor = (T[k][j]//pv * inv) % smallmod
                for i in range(k, n):
                    T[i][j] = (T[i][j]-factor*T[i][k]) % mod
                assert T[k][j] == 0
        ans.append(best)
    assert len(ans) == n
    return Counter(ans)


EXPECTED = {
    2:Counter({0:50,2:24}),
    3:Counter({0:37,1:37}),
    5:Counter({0:26,1:25,2:12,3:9,4:2}),
}
for p, total_val in [(2,48),(3,37),(5,84)]:
    for sink in [0,26,50]:
        found = local_smith(sink,p,total_val+1)
        assert found == EXPECTED[p], (p,sink,found)
    assert sum(v*n for v,n in EXPECTED[p].items()) == total_val

# Align the sorted primary exponents to recover the invariant factors.
exps = {p:sorted(e for e,n in data.items() for _ in range(n))
        for p,data in EXPECTED.items()}
invariants = [prod(p**exps[p][i] for p in [2,3,5]) for i in range(N-1)]
assert all(b%a==0 for a,b in zip(invariants, invariants[1:]))
assert prod(invariants) == TREE
assert Counter(invariants) == Counter({1:26,5:11,15:13,60:1,
                                     300:12,1500:9,7500:2})
print('FERMAT_QUINTIC_75_LINE_CRITICAL_GROUP_OK')
print('Smith invariants:', sorted(Counter(invariants).items()))
print('Tree order:', TREE)
