"""Exact finite checks for a proposed all-dimensional pellytope face formula.

Independent face counts use chord compatibility, not the fan-subdivision
recurrence. All computations are integral and require only Python 3.
"""
from math import comb


def add(a, b):
    return [(a[i] if i < len(a) else 0) +
            (b[i] if i < len(b) else 0) for i in range(max(len(a), len(b)))]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def polynomial(n):
    result = [0] * (n+1)
    for j in range(n//2+1):
        term = [0]*j + [comb(n-j, j)]
        for _ in range(j):
            term = mul(term, [1, 1])
        for _ in range(n-2*j):
            term = mul(term, [1, 2])
        result = add(result, term)
    return result


def crosses(x, y):
    a, b = x
    c, d = y
    return a < c < b < d or c < a < d < b


def chords(n):
    q = n+3
    return ([('A', i, (i+1, q)) for i in range(1, n+1)] +
            [('B', i, (1, i+2)) for i in range(1, n+1)] +
            [('C', i, (i+1, i+3)) for i in range(1, n)])


def incompatible(x, y):
    if not crosses(x[2], y[2]):
        return False
    if {x[0], y[0]} == {'A', 'B'}:
        a = x if x[0] == 'A' else y
        b = y if x[0] == 'A' else x
        if b[1] - a[1] >= 2:
            return False
    return True


def face_counts_via_chords(n):
    v = chords(n)
    m = len(v)
    bad = [0]*m
    for i in range(m):
        for j in range(i):
            if incompatible(v[i], v[j]):
                bad[i] |= 1 << j
                bad[j] |= 1 << i
    counts = [0]*(n+1)
    for mask in range(1 << m):
        r = mask.bit_count()
        if r > n:
            continue
        if any((mask >> i) & 1 and (bad[i] & mask) for i in range(m)):
            continue
        counts[r] += 1
    return counts


def h_from_faces(f):
    n = len(f)-1
    out = [0]*(n+1)
    for r, coeff in enumerate(f):
        term = [0]*r+[coeff]
        for _ in range(n-r):
            term = mul(term, [1, -1])
        out = add(out, term)
    return out


def h_from_gamma(n):
    out = [0]*(n+1)
    for j in range(n//2+1):
        term = [0]*j+[comb(n-j, j)]
        for _ in range(n-2*j):
            term = mul(term, [1, 1])
        out = add(out, term)
    return out


def matching_count(n, j):
    # Independent edge-subsets in the path on n vertices.
    return sum(mask.bit_count() == j and not (mask & (mask << 1))
               for mask in range(1 << max(0,n-1)))


def main():
    tests = 0
    for n in range(1, 8):
        f = polynomial(n)
        assert f == face_counts_via_chords(n), (n, f, face_counts_via_chords(n)); tests += 1
        assert f[1] == 3*n-1; tests += 1
        assert f[-1] == sum(comb(n-j,j)*2**(n-2*j) for j in range(n//2+1)); tests += 1
        assert h_from_faces(f) == h_from_gamma(n); tests += 1
        assert h_from_faces(f) == h_from_faces(f)[::-1]; tests += 1
        for j in range(n//2+1):
            assert matching_count(n, j) == comb(n-j, j); tests += 1
        print('dimension',n,'f by codimension',f,'h',h_from_faces(f))
    prior = [1]
    current = [1,2]
    for n in range(2, 51):
        next_f = add(mul([1,2], current), mul([0,1,1], prior))
        assert next_f == polynomial(n); tests += 1
        assert h_from_faces(next_f) == h_from_gamma(n); tests += 1
        assert h_from_faces(next_f) == h_from_faces(next_f)[::-1]; tests += 1
        prior,current = current,next_f
    print('PASS:',tests,'exact assertions.')


if __name__ == '__main__':
    main()
