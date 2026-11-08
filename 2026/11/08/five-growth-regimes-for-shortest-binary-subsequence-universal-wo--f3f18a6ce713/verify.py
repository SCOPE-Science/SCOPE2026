#!/usr/bin/env python3
"""Finite checks of shortest binary universality under one length-four forbidden factor."""
from itertools import product, permutations

BLOCKS = ('01', '10')
REP = ('0000', '0001', '0010', '0011', '0101', '0110')
# Coefficients in ascending order; F_p(z) = N_p(z) / D_p(z).
RATIONAL = {
    '0000': ((0, 2), (1, -2)),
    '0001': ((0, 2), (1, -2)),
    '0010': ((0, 2, 0, -1), (1, -2, 0, 1)),
    '0011': ((0, 2, 0, 1), (1, -2, 1, -1)),
    '0101': ((0, 2, 3, 2), (1, 0, -1, -1)),
    '0110': ((0, 2, -1), (1, -2, 1)),
}

def complement(s):
    return s.translate(str.maketrans('01', '10'))

def orbit(p):
    return {p, p[::-1], complement(p), complement(p[::-1])}

def matrix(p):
    states = tuple(product(BLOCKS, repeat=2))
    init = [int(p not in x+y) for x, y in states]
    M = [[0] * 4 for _ in range(4)]
    for i, (x, y) in enumerate(states):
        for a in BLOCKS:
            if p not in (x+y+a)[1:]:
                M[i][states.index((y, a))] += 1
    return init, M

def dp(p, bound):
    v, M = matrix(p)
    out = [0, 2]
    curr = v
    for k in range(2, bound+1):
        if k>2:
            curr = [sum(curr[i] * M[i][j] for i in range(4)) for j in range(4)]
        out.append(sum(curr))
    return out

def rational_coeff(p, bound):
    num, den = RATIONAL[p]
    out = [0] * (bound+1)
    for n in range(bound+1):
        out[n] = (num[n] if n<len(num) else 0) - sum(den[j]*out[n-j] for j in range(1, min(n, len(den)-1)+1))
    return out

def poly_add(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out

def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out

def poly_scale(a, n):
    return [n*x for x in a]

def matrix_exact_rational(p):
    # det(I-zM) by the 4! signed terms, entirely in integer polynomials.
    v, M = matrix(p)
    den = [0]
    for perm in permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
        term = [1]
        for i, j in enumerate(perm):
            term = poly_mul(term, [int(i==j), -M[i][j]])
        den = poly_add(den, poly_scale(term, (-1)**inversions))
    assert den[0] == 1
    b = []
    row = v[:]
    for t in range(4):
        b.append(sum(row))
        row = [sum(row[i]*M[i][j] for i in range(4)) for j in range(4)]
    # Cayley-Hamilton gives numerator degree at most 3 for S=v(I-zM)^(-1)1.
    numer_s = [sum(den[j]*b[t-j] for j in range(min(t,len(den)-1)+1)) for t in range(4)]
    numer_f = poly_add(poly_mul([0,2], den),poly_mul([0,0,1],numer_s))
    return numer_f, den

def is_subsequence(needle, word):
    i = 0
    for c in word:
        if i<len(needle) and needle[i]==c:
            i += 1
    return i==len(needle)

def universal(word, k):
    return all(is_subsequence(''.join(t), word) for t in product('01', repeat=k))

def main():
    observed = {}
    for p in map(''.join, product('01', repeat=4)):
        rep = next(r for r in REP if p in orbit(r))
        v = dp(p, 32)
        assert v == dp(rep, 32), (p, rep, 'orbit')
        assert v == rational_coeff(rep, 32), (p, rep, 'rational')
        nf, df = matrix_exact_rational(p)
        n0, d0 = RATIONAL[rep]
        assert poly_mul(nf, d0) == poly_mul(df, n0), (p, rep, 'exact symbolic rational identity')
        for k in range(1, 11):
            brute = sum(p not in ''.join(blocks) for blocks in product(BLOCKS, repeat=k))
            assert v[k] == brute, (p, k, 'brute', v[k], brute)
        observed[p] = v
    direct = 0
    for k in range(1, 6):
        for b in product('01', repeat=2*k):
            w = ''.join(b)
            u = universal(w, k)
            assert u == all(w[2*i]!=w[2*i+1] for i in range(k)), (w, k)
            direct += 1
    assert len({next(r for r in REP if p in orbit(r)) for p in observed}) == 6
    assert len(set(REP[0:2])) == 2
    print('VERIFY_OK patterns=16 orbits=6 rational_terms=32 symbolic_identities=16 direct_minimal_lengths=1..5 tested_words=%d pattern_cases=%d' % (direct, 16*sum(2**k for k in range(1,11))))
    for r in REP:
        print(r, observed[r][1:10])

if __name__ == '__main__': main()
