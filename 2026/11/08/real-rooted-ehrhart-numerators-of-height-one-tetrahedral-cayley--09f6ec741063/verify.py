#!/usr/bin/env python3
"""Exact, standard-library check of the tetrahedral-frustum Ehrhart-root certificate.

Run: python3 verify.py
Requires certificate.json in the same directory.
"""
import json
import math
from pathlib import Path

# Integer bivariate polynomials in X=a-1 and Y=b-1.
def const(c):
    return {} if not c else {(0, 0): int(c)}

def variable(which):
    return {(1, 0): 1} if which == 0 else {(0, 1): 1}

def add(*args):
    out = {}
    for p in args:
        for key, val in p.items():
            out[key] = out.get(key, 0) + val
    return {k: v for k, v in out.items() if v}

def neg(p):
    return {k: -v for k, v in p.items()}

def mul(p, q):
    out = {}
    for (i, j), v in p.items():
        for (k, l), w in q.items():
            ij = (i + k, j + l)
            out[ij] = out.get(ij, 0) + v * w
    return {k: v for k, v in out.items() if v}

def sc(c, p):
    return {k: c * v for k, v in p.items()} if c else {}

def power(p, n):
    out = const(1)
    for _ in range(n):
        out = mul(out, p)
    return out

def evaluate(p, x, y):
    return sum(v * x**i * y**j for (i, j), v in p.items())

def numerator_polynomials():
    a = add(const(1), variable(0))
    b = add(const(1), variable(1))
    n1 = add(power(a, 3), sc(6, power(a, 2)), sc(11, a),
             power(b, 3), sc(6, power(b, 2)), sc(11, b), const(-18))
    n2 = add(sc(4, power(a, 3)), sc(3, mul(power(a, 2), b)),
             sc(3, mul(a, power(b, 2))), sc(12, mul(a, b)),
             sc(-22, a), sc(4, power(b, 3)), sc(-22, b), const(18))
    s = add(a, b)
    n3 = mul(mul(add(s, const(-3)), add(s, const(-2))),
             add(s, const(-1)))
    return n1, n2, n3

def discriminator(n1, n2, n3):
    # 1296 times the discriminant of
    # z^3*n3/6 + z^2*n2/6 + z*n1/6 + 1.
    triple = add(mul(power(n2, 2), power(n1, 2)),
                 sc(-4, mul(n3, power(n1, 3))),
                 sc(-24, power(n2, 3)),
                 sc(-972, power(n3, 2)),
                 sc(108, mul(mul(n3, n2), n1)))
    assert all(v % 3 == 0 for v in triple.values())
    return {k: v // 3 for k, v in triple.items()}

def ehrhart(k, a, b):
    return sum(math.comb(a * (k-j) + b*j + 3, 3) for j in range(k+1))

def check():
    n1, n2, n3 = numerator_polynomials()
    d = discriminator(n1, n2, n3)
    stored = json.loads(Path(__file__).with_name('certificate.json').read_text('utf-8'))
    assert stored['definition'] == '432_times_discriminant_in_X=a_minus_1_Y=b_minus_1'
    expected = {(i, j): c for i, j, c in stored['coefficients']}
    assert len(expected) == len(stored['coefficients'])
    assert d == expected, 'discriminant coefficient certificate mismatch'
    assert len(d) == 90 and (0, 0) not in d
    assert all(isinstance(c, int) and c > 0 for c in d.values())
    assert d[(1, 0)] == d[(0, 1)] == 7776
    assert d[(12, 0)] == d[(0, 12)] == 4
    assert d == {(j, i): c for (i, j), c in d.items()}
    for a in range(1, 14):
        for b in range(1, 14):
            x, y = a-1, b-1
            h = [1] + [evaluate(n, x, y) // 6 for n in [n1, n2, n3]] + [0]
            assert all(evaluate(n, x, y) % 6 == 0 for n in [n1, n2, n3])
            for k in range(5):
                h_from_count = sum((-1)**(k-j)*math.comb(5, k-j)
                                   *ehrhart(j,a,b) for j in range(k+1))
                assert h[k] == h_from_count, (a,b,k,h[k],h_from_count)
            if a+b >= 4:
                assert min(h[1:4]) > 0 and evaluate(d,x,y)>0
    assert [evaluate(n,0,0)//6 for n in (n1,n2,n3)] == [3,0,0]
    assert [evaluate(n,0,1)//6 for n in (n1,n2,n3)] == [9,5,0]
    assert 9*9-4*5 == 61
    print('CERTIFICATE_OK: 90 strictly positive integral discriminant coefficients; 169 by 5 independent exact lattice-count checks; boundary cases verified.')

if __name__ == '__main__':
    check()
