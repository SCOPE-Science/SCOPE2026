#!/usr/bin/env python3
"""Independent compatible-split enumeration and modular rank check."""
from itertools import combinations
from hashlib import sha256
from json import load
from pathlib import Path

P = 1000033
N = 6
U = frozenset(range(N))


def all_nontrivial_splits():
    a = []
    for k in range(2, N - 1):
        for seq in combinations(range(N), k):
            S = frozenset(seq)
            R = U - S
            if len(R) >= 2 and (len(S), tuple(sorted(S))) <= (len(R), tuple(sorted(R))):
                a.append(S)
    return a


def compatible(A, B):
    return any(not part_a.intersection(part_b)
               for part_a in (A, U - A) for part_b in (B, U - B))


def full_split_systems():
    raw = all_nontrivial_splits()
    assert len(raw) == 25
    for triple in combinations(raw, 3):
        if all(compatible(A, B) for A, B in combinations(triple, 2)):
            yield triple


def displays(A, B, C, D, system):
    return int(any(((A in S and B in S and C not in S and D not in S) or
                    (A not in S and B not in S and C in S and D in S)) for S in system))


def signature(system):
    bits = []
    for a, b, c, d in combinations(range(N), 4):
        bits.extend((displays(a, b, c, d, system),
                     displays(a, c, b, d, system),
                     displays(a, d, b, c, system)))
    assert all(sum(bits[i:i + 3]) == 1 for i in range(0, 45, 3))
    return tuple(bits)


def col_rank(columns):
    basis = {}
    count = 0
    for v in columns:
        vec = {i: x % P for i, x in enumerate(v) if x % P}
        while vec:
            i = min(vec)
            u = vec[i]
            if i not in basis:
                inv = pow(u, P - 2, P)
                basis[i] = {k: z * inv % P for k, z in vec.items()}
                count += 1
                break
            for k, z in basis[i].items():
                new = (vec.get(k, 0) - u * z) % P
                if new:
                    vec[k] = new
                else:
                    vec.pop(k, None)
    return count


def main():
    cert = load(open(Path(__file__).with_name('CERTIFICATE.json'), encoding='utf-8'))
    sig = sorted(signature(t) for t in full_split_systems())
    assert len(sig) == len(set(sig)) == 105
    assert sha256(bytes(x for s in sig for x in s)).hexdigest() == cert['signature_sha256']
    f = [[1] * 105] + [[row[i] for row in sig] for i in range(45)]
    assert col_rank(f) == 31
    f += [[row[i] * row[j] for row in sig] for i, j in combinations(range(45), 2)]
    assert col_rank(f) == 105
    # Boolean Fourier characters of degree <=2 span the same space as
    # degree <=2 products of the 0/1 incidence indicators.
    print('PASS: 105 compatible full split systems; rank 31 and rank 105 modulo', P)


if __name__ == '__main__':
    main()
