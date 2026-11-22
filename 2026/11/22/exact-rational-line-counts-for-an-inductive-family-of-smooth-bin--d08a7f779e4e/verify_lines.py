#!/usr/bin/env python3
"""Independent GF(2) polynomial restriction and five-state line-count checks.

Run: python3 verify_lines.py
No third-party packages required.
"""
from itertools import product

V = range(4)

def det(u, v):
    return ((u & 1) & ((v >> 1) & 1)) ^ (((u >> 1) & 1) & (v & 1))

def add(a, b):
    assert len(a) == len(b)
    return tuple(x ^ y for x, y in zip(a, b))

def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i + j] ^= c & d
    return tuple(out)

def lin(u):
    return (u & 1, (u >> 1) & 1)

def phi(u, v):
    a, b = lin(u), lin(v)
    return add(mul(mul(a, a), b), mul(a, mul(b, b)))

FIRST = {(u, v): mul(lin(v), phi(u, v)) for u, v in product(V, repeat=2)}
SECOND = {(u, v): mul(add(lin(u), lin(v)), phi(u, v))
          for u, v in product(V, repeat=2)}

def restrict_quartic(word):
    # H(X0,X1,X2,X3) = F(X0,X1,X2+X3,X2).
    a, b, cc, dd = word[:4]
    c, d = cc ^ dd, cc
    out = (0, 0, 0, 0, 0)
    for u, v in ((a, b), (b, c), (c, d)):
        out = add(out, FIRST[u, v])
    out = add(out, SECOND[d, a])
    for u, v in zip(word[3:-1], word[4:]):
        out = add(out, SECOND[u, v])
    return out

def full_rank(word):
    return any(det(u, v) for u, v in product(word, repeat=2))

def direct_lines(n):
    count = 0
    for word in product(V, repeat=n + 1):
        if full_rank(word) and restrict_quartic(word) == (0,) * 5:
            count += 1
    assert count % 6 == 0
    return count // 6

def correction(u, v):
    return (u ^ v) if det(u, v) else 0

def initial(a, b, c, d):
    return ((b if det(a, b) else 0)
            ^ (c if det(b, c) else 0)
            ^ (d if det(c, d) else 0)
            ^ ((d ^ a) if det(d, a) else 0))

def state(d, z):
    if d == 0:
        return 0 if z == 0 else 1
    if z == 0:
        return 2
    if z == d:
        return 3
    return 4

M = ((1, 0, 3, 0, 0),
     (0, 1, 0, 1, 2),
     (1, 0, 1, 0, 2),
     (0, 1, 0, 3, 0),
     (0, 1, 1, 0, 2))

def matrix_step(v):
    return tuple(sum(M[i][j] * v[j] for j in range(5)) for i in range(5))

def matrix_lines(n):
    v = (22, 14, 18, 18, 14)
    for _ in range(n - 3):
        v = matrix_step(v)
    good = v[0] + 3 * v[2]
    bad = 3 * 2 ** (n + 1) - 2
    assert (good - bad) % 6 == 0
    return (good - bad) // 6

def check_transition():
    for orbit in range(5):
        vals = {(d,z): int(state(d,z) == orbit) for d,z in product(V,repeat=2)}
        new = {(e,w): sum(vals[(d, w ^ correction(d, e))] for d in V)
               for e,w in product(V,repeat=2)}
        for target in range(5):
            c = {new[(e,w)] for e,w in product(V,repeat=2) if state(e,w)==target}
            assert c == {M[target][orbit]}, (orbit,target,c,M[target][orbit])

def main():
    by_state = {i: [] for i in range(5)}
    base = {(d,z):0 for d,z in product(V,repeat=2)}
    for a,b,c,d in product(V,repeat=4):
        base[(d, initial(a,b,c ^ d,c))] += 1
    expected = (22, 14, 18, 18, 14)
    for d,z in product(V,repeat=2):
        assert base[(d,z)] == expected[state(d,z)]
    check_transition()
    known = (5,31,147,635,2635)
    for n,k in enumerate(known,start=3):
        observed = direct_lines(n)
        predicted = matrix_lines(n)
        assert observed == predicted == k, (n,observed,predicted,k)
        print('P^%d F2-lines: %d (direct homogeneous restriction and transfer agree)'%(n,k))
    for n in range(8,18):
        assert matrix_lines(n)>0
    # Recurrence induced by the reduced rational generating function.
    from functools import reduce
    def poly_product(a,b):
        z=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): z[i+j]+=x*y
        return z
    d = reduce(poly_product, ((1,-1),(1,-2),(1,-4)), [1])
    numerator=[5,-4]
    vals=[matrix_lines(n) for n in range(3,35)]
    for k in range(len(vals)):
        lhs=sum(d[j]*vals[k-j] for j in range(min(k,len(d)-1)+1))
        rhs=numerator[k] if k<len(numerator) else 0
        assert lhs==rhs,(k,lhs,rhs)
    for n in range(3,35):
        assert 12 * matrix_lines(n) == 2 * 4 ** n - 9 * 2 ** n + 4
    print('Five-state transition, closed formula and 32 generating coefficients verified.')

if __name__ == '__main__': main()
