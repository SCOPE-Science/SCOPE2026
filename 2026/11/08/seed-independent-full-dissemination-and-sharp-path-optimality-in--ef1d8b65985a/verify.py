"""Exact rational check of complete-reach probability in a stifling rumor model.

Run: python3 verify.py
No external packages or input files are needed.
The proof for arbitrarily large trees is in RESULT.md; finite checks corroborate it.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product


def prufer_tree(seq, n):
    degree = [1] * n
    for v in seq:
        degree[v] += 1
    edges = []
    for v in seq:
        u = next(j for j in range(n) if degree[j] == 1)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
    last = [j for j in range(n) if degree[j] == 1]
    edges.append(tuple(last))
    return edges


def from_generator(n):
    if n == 2:
        yield [(0,1)]
    elif n <= 5:
        for seq in product(range(n), repeat=n-2):
            yield prufer_tree(seq,n)
    else:
        for k in range(22):
            seq = tuple((k * k + 3 * k * j + 7 * j * j + 2 * j) % n
                        for j in range(n-2))
            yield prufer_tree(seq,n)


def full_reach_exact(n, edges, alpha, root, beta=None):
    # Direct 3-state CTMC transition recursion, without using the claimed formula.
    if beta is None:
        beta = [Fraction(1)]*n
    neighbor = [[] for _ in range(n)]
    for u,v in edges:
        neighbor[u].append(v)
        neighbor[v].append(u)
    @lru_cache(maxsize=None)
    def future(s):
        if 1 not in s:
            return Fraction(int(0 not in s))
        jumps = {}
        for v in range(n):
            if s[v] != 1:
                continue
            for w in neighbor[v]:
                t = list(s)
                if s[w] == 0:
                    t[w] = 1
                    rate = beta[v]
                else:
                    t[v] = 2
                    rate = beta[v] * alpha[v]
                t = tuple(t)
                jumps[t] = jumps.get(t, Fraction(0)) + rate
        total = sum(jumps.values(), Fraction(0))
        return sum((rate * future(t) / total for t, rate in jumps.items()),
                   Fraction(0))
    return future(tuple(1 if v==root else 0 for v in range(n)))


def product_prediction(n, edges, alpha):
    deg = [0] * n
    for u,v in edges:
        deg[u] += 1
        deg[v] += 1
    result = Fraction(1)
    for v,d in enumerate(deg):
        for j in range(1,d):
            result *= Fraction(d-j, 1) / (d-j+alpha[v]*j)
    return result


def check():
    tests = roots = 0
    for n in range(2,8):
        for edges in from_generator(n):
            # Two non-proportional vertex-dependent stifling profiles,
            # plus the homogeneous rate ratio of one.
            profiles = [
                [Fraction(1)] * n,
                [Fraction((3*v+1) % 7 + 1, (2*v+1) % 5 + 1) for v in range(n)],
                [Fraction((5*v+2) % 9 + 1, (3*v+1) % 7 + 1) for v in range(n)],
            ]
            for alpha in profiles:
                p = product_prediction(n, edges, alpha)
                beta = [Fraction((2*v+3) % 7+1,(v+1) % 5+1) for v in range(n)]
                for root in range(n):
                    got = full_reach_exact(n, edges, alpha, root, beta)
                    assert got == p, (n,edges,alpha,root,got,p)
                    roots += 1
                tests += 1
            # The path bound is a check on numerical cases, not its proof.
            rho = Fraction(2,3)
            homogeneous = product_prediction(n,edges,[rho]*n)
            ceiling = (1+rho)**(-(n-2))
            assert homogeneous <= ceiling
            if any(sum(v in e for e in edges)>2 for v in range(n)):
                assert homogeneous < ceiling
    print('PASS: %d distinct tree/profile tests and %d independent root exact CTMC comparisons' % (tests, roots))

if __name__=='__main__':
    check()
