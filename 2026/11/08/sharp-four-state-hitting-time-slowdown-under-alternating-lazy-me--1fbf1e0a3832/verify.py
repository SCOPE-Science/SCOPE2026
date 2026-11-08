"""Exact, standalone certificate for the four-vertex alternating Metropolis walk theorem.

Run: python3 verify.py
Uses only the Python standard library. All numerical operations are rational.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement


def connected(n, edges):
    reached = {0}
    while True:
        nxt = reached | {v for u,v in edges if u in reached} | {u for u,v in edges if v in reached}
        if nxt == reached:
            return len(reached) == n
        reached = nxt


def matrices(n):
    edge_space = list(combinations(range(n), 2))
    result = []
    for mask in range(1 << len(edge_space)):
        edges = [e for k,e in enumerate(edge_space) if (mask >> k) & 1]
        if not connected(n, edges):
            continue
        degrees = [sum(u == i or v == i for u,v in edges) for i in range(n)]
        P = [[F(i == j) for j in range(n)] for i in range(n)]
        for u,v in edges:
            prob = F(1, 2*max(degrees[u], degrees[v]))
            P[u][u] -= prob
            P[v][v] -= prob
            P[u][v] += prob
            P[v][u] += prob
        assert all(sum(row) == 1 for row in P)
        assert all(P[u][v] == P[v][u] for u in range(n) for v in range(n))
        assert all(P[i][i] >= F(1,2) for i in range(n))
        result.append((mask, P))
    return result


def solve(A, b):
    """Gaussian elimination over Q, with checked exact residuals."""
    m = len(b)
    aa = [list(A[i]) + [b[i]] for i in range(m)]
    for j in range(m):
        pivot = next((i for i in range(j,m) if aa[i][j]), None)
        assert pivot is not None, 'absorption system singular'
        aa[j], aa[pivot] = aa[pivot], aa[j]
        factor = aa[j][j]
        aa[j] = [v/factor for v in aa[j]]
        for i in range(j+1,m):
            fac = aa[i][j]
            if fac:
                aa[i] = [v-fac*w for v,w in zip(aa[i], aa[j])]
    x = [F(0)]*m
    for i in range(m-1,-1,-1):
        x[i] = aa[i][-1] - sum(aa[i][j]*x[j] for j in range(i+1,m))
    assert all(sum(A[i][j]*x[j] for j in range(m)) == b[i] for i in range(m))
    return x


def killed(P, t):
    keep = [i for i in range(len(P)) if i != t]
    return [[P[i][j] for j in keep] for i in keep]


def hitting(P, Q, t):
    """Return first-phase and second-phase hitting vectors on non-target states."""
    A, B = killed(P,t), killed(Q,t)
    d = len(A)
    # h_A = 1 + A h_B, h_B = 1 + B h_A.
    M = [[F(i == j) - sum(A[i][k]*B[k][j] for k in range(d))
          for j in range(d)] for i in range(d)]
    b = [1 + sum(A[i][k] for k in range(d)) for i in range(d)]
    hA = solve(M,b)
    hB = [1 + sum(B[i][k]*hA[k] for k in range(d)) for i in range(d)]
    assert all(hA[i] == 1+sum(A[i][k]*hB[k] for k in range(d)) for i in range(d))
    assert all(hB[i] == 1+sum(B[i][k]*hA[k] for k in range(d)) for i in range(d))
    return hA,hB


def run():
    counts = []
    for n in (2,3,4):
        graphs = matrices(n)
        statics = {(bits,t): hitting(P,P,t)[0] for bits,P in graphs for t in range(n)}
        best = F(1)
        max_witnesses = []
        total = bad = 0
        for (b1,P),(b2,Q) in combinations_with_replacement(graphs,2):
            for t in range(n):
                a,b = hitting(P,Q,t)
                keep = [i for i in range(n) if i != t]
                for k,s in enumerate(keep):
                    denominator = max(statics[b1,t][k], statics[b2,t][k])
                    for phase,h in enumerate((a[k],b[k])):
                        total += 1
                        ratio = h/denominator
                        if ratio > 1:
                            bad += 1
                        if ratio > best:
                            best = ratio
                            max_witnesses = [(b1,b2,t,s,phase,h,denominator)]
                        elif ratio == best and ratio > 1:
                            max_witnesses.append((b1,b2,t,s,phase,h,denominator))
        counts.append((n,len(graphs),total,bad,best,len(max_witnesses)))
    assert counts == [(2,1,4,0,F(1),0),
                      (3,4,120,0,F(1),0),
                      (4,38,17784,168,F(646,607),24)], counts

    # Independent witness replay via the full, phase-augmented system.
    graphs = dict(matrices(4))
    P,Q = graphs[51],graphs[58]
    t = 3
    keep = [0,1,2]
    d = len(keep)
    A,B = killed(P,t),killed(Q,t)
    # Rebuild the augmented system without sharing the phase-reduction formula.
    mat = [[F(i == j) for j in range(2*d)] for i in range(2*d)]
    for i in range(d):
        for j in range(d):
            mat[i][d+j] -= A[i][j]
            mat[d+i][j] -= B[i][j]
    vals = solve(mat, [F(1)]*(2*d))
    assert vals[:d] == [F(5538,607), F(3876,607), F(4236,607)]
    assert vals[d:] == [F(5928,607), F(3574,607), F(4294,607)]
    assert hitting(P,P,t)[0] == [F(8),F(6),F(6)]
    assert hitting(Q,Q,t)[0] == [F(15),F(6),F(9)]
    print('VERIFY_OK', counts, 'witness=3876/607 > 6; ratio=646/607')


if __name__ == '__main__':
    run()
