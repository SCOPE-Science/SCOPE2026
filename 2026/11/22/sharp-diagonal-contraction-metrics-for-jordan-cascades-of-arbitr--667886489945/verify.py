"""Numerical diagnostics for a sharp diagonal Hilbert metric on a cascade.
The universal theorem is proved analytically in RESULT.md; this code is not a proof.
"""
from math import sqrt
from random import Random


def power_root(edges, steps=30000, tol=5e-13):
    # Use I+T to avoid the period-two oscillation of a path adjacency matrix.
    n = len(edges) + 1
    v = [1.0 / sqrt(n)] * n
    old = 0.0
    for _ in range(steps):
        w = [v[i] + (edges[i - 1] * v[i - 1] if i else 0.0) +
             (edges[i] * v[i + 1] if i < n-1 else 0.0)
             for i in range(n)]
        norm = sqrt(sum(a*a for a in w))
        v = [a / norm for a in w]
        val = sum(v[i] * edges[i] * v[i+1] for i in range(n-1))*2
        if abs(val-old) < tol:
            break
        old = val
    return val


def candidate(n, k):
    q = (4*k)**(-1/(2*(n-1)))
    p = [1.] + [1/(2*q**(2*i)) for i in range(1,n-1)] + [k]
    return p, q


def edges_of(p):
    return [sqrt(p[i]/p[i+1]) for i in range(len(p)-1)]


def run():
    rng=Random(2177)
    tests=0
    for n in [5,6,7,8,11]:
        for multiplier in [1,1.01,2,5,80]:
            k=(2**(n-3))*multiplier
            p,q=candidate(n,k)
            assert abs(min(p)-1)<1e-12
            assert abs(max(p)-k)<1e-8*max(1,k)
            edges=edges_of(p)
            assert abs(edges[0]-sqrt(2)*q)<1e-10
            assert abs(edges[-1]-sqrt(2)*q)<1e-10
            for x in edges[1:-1]:
                assert abs(x-q)<1e-10
            assert abs(power_root(edges)-2*q)<2e-9
            tests+=5+len(edges)
            for _ in range(120):
                p_alt=[1.0] + [k**rng.random() for _ in range(n-2)] + [k]
                ep=edges_of(p_alt)
                assert power_root(ep) >= 2*q - 2e-8
                tests+=1
    # Exact critical certificate on five sites: (1,2,8,32,64), a=1, c=2
    p,q=candidate(5,64)
    assert p==[1.,2.,8.,32.,64.]
    assert q==.5
    assert abs(-1 + power_root(edges_of(p))) < 1e-10
    tests+=3
    print(f'CASCADE_DIAGONAL_METRIC_DIAGNOSTIC_OK {tests}')

if __name__=='__main__':
    run()
