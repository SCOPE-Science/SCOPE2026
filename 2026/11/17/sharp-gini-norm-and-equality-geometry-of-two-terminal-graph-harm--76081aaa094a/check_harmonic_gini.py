"""Exact-rational checks for two-terminal harmonic interpolation and pairwise dispersion.

Run with: python3 check_harmonic_gini.py
The checker is finite evidence; the accompanying proof establishes the theorem for all graphs.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def solve(matrix, rhs):
    n = len(rhs)
    a = [[F(v) for v in row] + [F(rhs[i])] for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        assert pivot is not None
        a[k], a[pivot] = a[pivot], a[k]
        d = a[k][k]
        a[k] = [x / d for x in a[k]]
        for i in range(n):
            if i != k:
                z = a[i][k]
                a[i] = [x - z*y for x, y in zip(a[i], a[k])]
    return [r[-1] for r in a]


def potential(weights):
    n = len(weights)
    if n == 2: return [F(0), F(1)]
    a, b = [], []
    for i in range(2, n):
        a.append([sum(weights[i]) if i == j else -weights[i][j]
                  for j in range(2, n)])
        b.append(weights[i][1])
    return [F(0), F(1)] + solve(a, b)


def gini(values):
    return sum((abs(values[i]-values[j])
                for i in range(len(values)) for j in range(i+1, len(values))), F(0))


def connected(weights):
    n = len(weights)
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in range(n):
            if weights[v][w] > 0 and w not in seen:
                seen.add(w); stack.append(w)
    return len(seen) == n


def test(weights):
    n = len(weights)
    h = potential(weights)
    assert h[0] == 0 and h[1] == 1
    assert all(0 <= x <= 1 for x in h)
    for i in range(2, n):
        assert sum(weights[i][j]*(h[i]-h[j]) for j in range(n)) == 0
    formula = F(1) + gini(h[2:]) / (n-1)
    assert gini(h) / (n-1) == formula
    # Every nonconstant binary signal is tested: coarea then handles real signals.
    max_ratio = F(0)
    for mask in range(1, (1 << n) - 1):
        x = [F((mask >> i) & 1) for i in range(n)]
        y = [x[0] + (x[1]-x[0])*v for v in h]
        r = gini(y)/gini(x)
        max_ratio = max(max_ratio, r)
        assert r <= formula
    assert max_ratio == formula
    stable = len(set(h[2:])) <= 1
    assert (formula == 1) == stable
    criteria = any(all(t*weights[i][0] == (1-t)*weights[i][1]
                       for i in range(2, n))
                   for t in ([F(0)] if n==2 else [h[2]]))
    assert stable == criteria
    if n >= 4:
        v=sorted(h[2:])
        m=n-2
        peak=max(k*(m-k) for k in range(1,m))
        upper=F(peak)
        assert gini(v)<=upper
        rigid=(v[0]==0 and v[-1]==1 and
               all(v[k]==v[k-1] or k*(m-k)==peak for k in range(1,m)))
        assert (gini(v)==upper)==rigid
    return formula


def build(n, edges, conductances=None):
    weights = [[F(0) for _ in range(n)] for _ in range(n)]
    for k, (i,j) in enumerate(edges):
        w = F(1) if conductances is None else F(conductances[k])
        weights[i][j]=weights[j][i]=w
    return weights


def main():
    checked=0
    for n in range(2,6):
        edges=list(combinations(range(n),2))
        for mask in range(1,1 << len(edges)):
            chosen=[e for i,e in enumerate(edges) if (mask>>i)&1]
            w=build(n, chosen)
            if not connected(w):continue
            test(w); checked+=1
    print('EXHAUSTIVE_CONNECTED_SIMPLE_GRAPHS_N2_TO_N5_PASSED',checked)
    rng=Random(27721)
    weighted_count=0
    for n in range(2,8):
        edges=list(combinations(range(n),2))
        for _ in range(65):
            chosen=[(i,i+1) for i in range(n-1)]
            for e in edges:
                if e not in chosen and rng.randrange(3)==0: chosen.append(e)
            conductances=[rng.randrange(1,7) for _ in chosen]
            test(build(n,chosen,conductances))
            weighted_count+=1
    print('EXACT_RATIONAL_WEIGHTED_NETWORKS_PASSED',weighted_count)
    for n in range(2,30):
        m=n-2
        k=m//2
        edges=[(0,1)]+[(0,i) for i in range(2,2+k)] + [(1,i) for i in range(2+k,n)]
        h=potential(build(n,edges))
        formula=F(1)+gini(h[2:])/(n-1)
        assert formula == 1+F((m*m)//4,n-1)
    print('SHARP_GLOBAL_ENVELOPE_DOUBLE_STAR_WITNESSES_PASSED_N2_TO_N29')
    for n in range(2,50):
        edges=[(i,i+1) for i in range(n-1)]
        w=build(n,edges)
        # Reindex so graph endpoints 0 and 1 rather than 0 and n-1.
        labels = [0,n-1]+list(range(1,n-1))
        wn=[[w[labels[i]][labels[j]] for j in range(n)] for i in range(n)]
        h=potential(wn)
        assert gini(h)/F(n-1) == F(n*(n+1),6*(n-1))
    print('EXACT_UNIFORM_PATH_CONSTANTS_PASSED_N2_TO_N49')
    print('ALL_TWO_TERMINAL_HARMONIC_GINI_CHECKS_PASSED')

if __name__=='__main__':main()
