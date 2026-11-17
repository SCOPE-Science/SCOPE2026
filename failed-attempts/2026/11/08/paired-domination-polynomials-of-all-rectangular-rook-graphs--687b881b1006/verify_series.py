"""Independent exact binomial-polynomial recurrence for a formal square root.

E(u,v,z)^2=F(u,v,z)F(u,v,-z), F=sum (1+z)^(ab)u^a v^b/(a!b!).
Paired-domination coefficients follow by formal inclusion-exclusion.
Uses only the Python standard library.
"""
from collections import defaultdict
from math import comb
import json


def add(a, b, k=1):
    out = a.copy()
    for exp, value in b.items():
        out[exp] = out.get(exp, 0) + k * value
    return {i: v for i, v in out.items() if v}


def mul(a, b):
    c = defaultdict(int)
    for i, x in a.items():
        for j, y in b.items():
            c[i+j] += x*y
    return dict(c)


def signed_binom(p, sign):
    return {k: comb(p, k)*sign**k for k in range(p+1)}


def calculate(M, N):
    E = {(0, 0): {0: 1}}
    for t in range(1, M+N+1):
        for m in range(max(0, t-N), min(M, t)+1):
            n = t-m
            rhs = {}
            for i in range(m+1):
                for j in range(n+1):
                    part = mul(signed_binom(i*j, 1),
                               signed_binom((m-i)*(n-j), -1))
                    rhs = add(rhs, part, comb(m, i)*comb(n, j))
            for i in range(m+1):
                for j in range(n+1):
                    if (i, j) in ((0, 0), (m, n)):
                        continue
                    rhs = add(rhs, mul(E[i, j], E[m-i, n-j]),
                              -comb(m, i)*comb(n, j))
            assert all(value % 2 == 0 for value in rhs.values())
            E[m, n] = {k: v//2 for k, v in rhs.items() if v}
    P = {}
    for m in range(1, M+1):
        for n in range(1, N+1):
            out = {}
            for i in range(m+1):
                out = add(out, E[i, n], (-1)**(m-i)*comb(m, i))
            for j in range(n+1):
                out = add(out, E[m, j], (-1)**(n-j)*comb(n, j))
            for i in range(m+1):
                for j in range(n+1):
                    out = add(out, E[i, j],
                              -(-1)**(m+n-i-j)*comb(m, i)*comb(n, j))
            assert all(v >= 0 for v in out.values())
            P[m, n] = dict(sorted(out.items()))
    return P


if __name__ == '__main__':
    P = calculate(5, 6)
    expected = {
        (2, 2): {2: 4, 4: 1},
        (2, 3): {2: 3, 4: 15, 6: 1},
        (2, 4): {2: 4, 4: 62, 6: 28, 8: 1},
        (3, 3): {4: 81, 6: 84, 8: 9},
        (3, 4): {4: 129, 6: 840, 8: 495, 10: 66, 12: 1},
        (3, 5): {4: 210, 6: 3655, 8: 6300, 10: 3003, 12: 455, 14: 15},
        (4, 4): {4: 80, 6: 4464, 8: 12150, 10: 7992, 12: 1820,
                 14: 120, 16: 1},
    }
    for key, value in expected.items():
        assert P[key] == value, (key, P[key])
        print(json.dumps({'board': list(key), 'coefficients': P[key],
                          'formal_series': 'PASS'}, sort_keys=True))
    for key in ((5, 5), (5, 6)):
        leading = min(P[key])
        print(json.dumps({'board': list(key), 'minimum_size': leading,
                          'minimum_count': P[key][leading],
                          'formal_series': 'PASS'}, sort_keys=True))
    assert (min(P[5, 5]), P[5, 5][6]) == (6, 10900)
    assert (min(P[5, 6]), P[5, 6][6]) == (6, 12605)
    print('SERIES_PASS: formal identity agrees with all test cases.')
