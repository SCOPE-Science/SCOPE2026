"""Exact rational checks for the weighted triangular-book two-leader theorem.

Run with Python 3: python verify.py. This checks representative finite
instances; the all-parameter statement follows from the proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations


def laplacian(m, a, b, c):
    n = m + 2
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    edges = [(0, 1, c)]
    for i in range(2, n):
        edges.extend(((0, i, a), (1, i, b)))
    for u, v, w in edges:
        L[u][u] += w
        L[v][v] += w
        L[u][v] -= w
        L[v][u] -= w
    return L


def trace_inverse(A):
    n = len(A)
    M = [list(A[i]) + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if M[i][j]), None)
        assert pivot is not None
        M[j], M[pivot] = M[pivot], M[j]
        d = M[j][j]
        M[j] = [x / d for x in M[j]]
        for i in range(n):
            if i != j:
                coeff = M[i][j]
                if coeff:
                    M[i] = [M[i][k] - coeff * M[j][k] for k in range(2 * n)]
    return sum((M[i][n+i] for i in range(n)), F(0))


def grounded_cost(L, S):
    n = len(L)
    follower = [i for i in range(n) if i not in S]
    return trace_inverse([[L[i][j] for j in follower] for i in follower])


def closed_forms(m, a, b, c):
    s = a + b
    uv = m / s
    ul = (m - 1) / s + (s*s + (m - 1)*b*b) / (s * (m*a*b+b*b+c*s))
    vl = (m - 1) / s + (s*s + (m - 1)*a*a) / (s * (m*a*b+a*a+c*s))
    ll = (2*(a*a+b*b) + a*b*m*(3*m-4) + c*s*(3*m-4)) / (2*s*(m*a*b+c*s))
    return uv, ul, vl, ll


def predicted_sets(m, a, b, c):
    s = a + b
    out = set()
    assert a >= b
    c_star = (a*a-(m-2)*a*b+(m-1)*b*b)/s
    if c <= c_star:
        out.add((0, 1))
    if c >= c_star:
        out |= {(0, i) for i in range(2, m+2)}
        if a == b:
            out |= {(1, i) for i in range(2, m+2)}
    return out


def run():
    configurations = []
    for m in range(4, 11):
        for a, b in [(F(1),F(1)), (F(2),F(1)), (F(5,2),F(1)), (F(7),F(2))]:
            crit = (a*a-(m-2)*a*b+(m-1)*b*b)/(a+b)
            for c in [F(1,20), F(1,2), F(1), F(3), F(10), crit]:
                if c > 0:
                    configurations.append((m,a,b,c))
    n_cases = n_sets = n_formula = n_region = n_gap = 0
    for m, a, b, c in configurations:
        L=laplacian(m,a,b,c)
        types=closed_forms(m,a,b,c)
        costs={}
        for pair in combinations(range(m+2),2):
            cost=grounded_cost(L,pair)
            costs[pair]=cost
            if pair == (0,1): expected=types[0]
            elif pair[0]==0: expected=types[1]
            elif pair[0]==1: expected=types[2]
            else: expected=types[3]
            assert cost==expected, (m,a,b,c,pair,cost,expected)
            n_sets+=1
            n_formula+=1
        best=min(costs.values())
        actual={p for p,v in costs.items() if v==best}
        predicted=predicted_sets(m,a,b,c)
        assert actual==predicted, (m,a,b,c,actual,predicted)
        n_region+=1
        uv,ul,vl,ll=types
        assert ll>uv
        n_gap+=1
        n_cases+=1
    assert F(5,2)**2-5*F(5,2)+6<0  # the m=7 always-leaf regime
    print('VERIFY_OK configurations=',n_cases,' exact_pair_matrices=',n_sets,
          ' class_formula_checks=',n_formula,' optimizer_checks=',n_region,
          ' leaf_exclusion_checks=',n_gap)

if __name__=='__main__':
    run()
