#!/usr/bin/env python3
"""Independent finite checks for binary cyclic trigram-profile rigidity.

Requires only Python 3 standard library. Execute: python verify.py
"""
from collections import defaultdict, Counter
from itertools import product


def profile(word):
    n = len(word)
    counts = [0] * 8
    for i in range(n):
        counts[4*int(word[i]) + 2*int(word[(i+1) % n]) + int(word[(i+2) % n])] += 1
    return tuple(counts)


def least_rotation(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def run_vectors(word):
    if word.count('0') == 0 or word.count('1') == 0:
        return None
    n = len(word)
    first = next(i for i in range(n) if word[i-1] == '1' and word[i] == '0')
    lengths = []
    k = 0
    while k < n:
        symbol = word[(first+k) % n]
        m = 1
        while k + m < n and word[(first+k+m) % n] == symbol:
            m += 1
        lengths.append((symbol,m))
        k += m
    return tuple(v for c,v in lengths if c == '0'), tuple(v for c,v in lengths if c == '1')


def vector_type(v):
    r = len(v)
    if r == 1 or all(x == 1 for x in v) or all(x == 2 for x in v):
        return 'U'
    if sum(x >= 2 for x in v) == 1 and all(x == 1 or x >= 2 for x in v):
        return 'D'
    if r >= 3 and v.count(1) == 1 and all(x in (1,2) for x in v):
        return 'D'
    if v.count(3) == 1 and all(x in (2,3) for x in v):
        return 'D'
    return 'X'


def predicted_singleton(word):
    vectors = run_vectors(word)
    if vectors is None:
        return True
    u,v = vectors
    if len(u) == 1:
        return True
    a,b = vector_type(u),vector_type(v)
    return (a == 'U' and b in ('U','D')) or (b == 'U' and a == 'D')


def formula_counts(nmax):
    out = Counter()
    for n in range(1,nmax+1):
        out[n] += n+1 # two monochromatic and n-1 one-run-of-each profiles
    for r in range(2,nmax//2 + 1):
        U = Counter({r:1,2*r:1})
        D = Counter({2*r+1:1})
        for n in range(r+1,nmax+1):
            D[n] += 1
        if r >= 3:
            D[2*r-1] += 1
        for a,ca in U.items():
            for b,cb in U.items():
                if a+b <= nmax:
                    out[a+b] += ca*cb
            for b,cb in D.items():
                if a+b <= nmax:
                    out[a+b] += 2*ca*cb
    return out


def polynomial_identity():
    """Exact formal-polynomial identity, without truncated series testing."""
    def add(a,b):
        c = dict(a)
        for k,v in b.items():
            c[k] = c.get(k,0) + v
        return {k:v for k,v in c.items() if v}
    def multiply(a,b):
        c = {}
        for i,x in a.items():
            for j,y in b.items():
                c[i+j] = c.get(i+j,0) + x*y
        return {k:v for k,v in c.items() if v}
    def times(c,a):
        return {k:c*v for k,v in a.items() if c*v}
    one = {0:1}
    def z(n): return {n:1}
    def one_minus(n): return {0:1,n:-1}
    def R(num,den): return (num,den)
    def plus(A,B):
        return R(add(multiply(A[0],B[1]),multiply(B[0],A[1])),multiply(A[1],B[1]))
    def prod(A,B):
        return R(multiply(A[0],B[0]),multiply(A[1],B[1]))
    def term(c,k,den):
        return R(times(c,z(k)),den)
    vals = [
        term(2,1,one_minus(1)),term(1,2,multiply(one_minus(1),one_minus(1))),
        term(1,4,one_minus(2)),term(2,6,one_minus(3)),term(1,8,one_minus(4)),
        term(2,5,multiply(one_minus(1),one_minus(2))),
        term(2,7,multiply(one_minus(1),one_minus(3))),
        term(2,7,one_minus(3)),term(2,9,one_minus(4)),
        term(2,8,one_minus(3)),term(2,11,one_minus(4))
    ]
    lhs = R({},one)
    for value in vals:
        lhs = plus(lhs,value)
    P = {1:2,2:3,3:4,4:4,5:3,6:5,7:6,8:7,9:5,11:-1,12:-4,14:-2}
    rhs = R(P,multiply(one_minus(3),one_minus(4)))
    assert multiply(lhs[0],rhs[1]) == multiply(rhs[0],lhs[1])
    assert sum(P.values()) == 32
    return True


def verify():
    assert polynomial_identity()
    nmax = 19
    expected = formula_counts(120)
    total_words = 0
    total_necklaces = 0
    for n in range(1,nmax + 1):
        observed = defaultdict(list)
        for bits in product('01',repeat=n):
            w = ''.join(bits)
            total_words += 1
            if w != least_rotation(w):
                continue
            total_necklaces += 1
            observed[profile(w)].append(w)
        singletons = sum(len(fiber) == 1 for fiber in observed.values())
        if singletons != expected[n]:
            raise AssertionError(('count',n,singletons,expected[n]))
        for fiber in observed.values():
            for w in fiber:
                if predicted_singleton(w) != (len(fiber) == 1):
                    raise AssertionError(('classification', n, w, fiber))
        print('n=%2d  necklaces=%6d  spectra=%4d  singleton=%3d' %
              (n,sum(map(len,observed.values())),len(observed), singletons))
    # Exact rational-series identity through index 120, beyond the finite census.
    # P(z)=sum p_i z^i, S(z)=P(z)/((1-z^3)(1-z^4)).
    P = {1:2,2:3,3:4,4:4,5:3,6:5,7:6,8:7,9:5,11:-1,12:-4,14:-2}
    for n in range(1,121):
        lhs = expected[n]-expected[n-3]-expected[n-4]+expected[n-7]
        if lhs != P.get(n,0):
            raise AssertionError(('rational identity',n,lhs,P.get(n,0)))
    print('PASS: %d linear binary words examined, %d necklaces; n=1..%d classification and counts, 120 rational coefficients; exact formal rational identity.' % (total_words,total_necklaces,nmax))


if __name__ == '__main__':
    verify()
