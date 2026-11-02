"""Exact finite verification of hypercube Rips translation characters.

Run: python3 vr_cube_translation_check.py
Only Python's standard library is required.
"""
from itertools import combinations, permutations
from math import comb


def beta(n):
    return sum(2 ** (j - 3) * comb(j, 3) for j in range(3, n + 1))


def predicted_trace(n, t):
    if t == 0:
        return beta(n)
    if t.bit_count() <= 2:
        return 1 + (n - 3) * 2 ** (n - 2)
    return 1


def predicted_mult(n, k):
    if k == 0:
        return comb(n, 3)
    return (n - 3) * (3*k*k - 3*k*n - 3*k + n*n + 2)//6


def maximal_candidates(n):
    vert = range(1 << n)
    out = set()
    for base in vert:
        out.add(tuple(sorted((base,) + tuple(base ^ (1 << i) for i in range(n)))))
    for idx in combinations(range(n), 3):
        mask = sum(1 << i for i in idx)
        for base in vert:
            if base & mask:
                continue
            for parity in (0, 1):
                out.add(tuple(sorted(base ^ sum(1 << idx[j] for j in sel)
                                     for z in range(4) for sel in combinations(range(3), z)
                                     if z % 2 == parity)))
    for idx in combinations(range(n), 2):
        mask = sum(1 << i for i in idx)
        for base in vert:
            if base & mask:
                continue
            out.add(tuple(sorted(base ^ sum(1 << j for j in sel)
                                 for z in range(3) for sel in combinations(idx, z))))
    return out


def all_faces(n):
    out = set()
    for fac in maximal_candidates(n):
        for z in range(1, len(fac) + 1):
            out.update(combinations(fac, z))
    return out


def signed_lefschetz(faces, f):
    total = 0
    for face in faces:
        im = tuple(f(x) for x in face)
        if sorted(im) != list(face):
            continue
        inversions = sum(im[i] > im[j] for i in range(len(im))
                         for j in range(i + 1, len(im)))
        total += (-1)**(len(face) - 1 + inversions)
    return total


def permute(x, perm):
    return sum(((x >> i) & 1) << perm[i] for i in range(len(perm)))


def sign_of_permutation(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p))
                       for j in range(i + 1, len(p)))


def run():
    assertions = 0
    for n in range(3, 7):
        faces = all_faces(n)
        # Verify each proposed maximal generating simplex is a legitimate clique.
        assert all(all((u ^ v).bit_count() <= 2 for u, v in combinations(s, 2))
                   for s in maximal_candidates(n))
        assert all(all((u ^ v).bit_count() <= 2 for u, v in combinations(s, 2))
                   for s in faces)
        assertions += 2
        euler = sum((-1)**(len(f) - 1) for f in faces)
        assert euler == 1 - beta(n), (n, euler, beta(n))
        assertions += 1
        for t in range(1 << n):
            # Lefschetz number = 1 - trace in degree three.
            actual = 1 - signed_lefschetz(faces, lambda x, t=t: x ^ t)
            expected = predicted_trace(n, t)
            assert actual == expected, (n, t, actual, expected)
            assertions += 1
        for k in range(n + 1):
            a = (1 << k) - 1
            wsum = sum((-1)**((a & t).bit_count()) * predicted_trace(n, t)
                       for t in range(1 << n))
            assert wsum % (1 << n) == 0
            assert wsum // (1 << n) == predicted_mult(n, k)
            assert predicted_mult(n, k) >= 0
            assertions += 3
        assert sum(comb(n, k) * predicted_mult(n, k) for k in range(n + 1)) == beta(n)
        assertions += 1
        print('n=', n, 'faces=', len(faces), 'rank_H3=', beta(n),
              'invariant_rank=', comb(n, 3), 'translations=', 1 << n)
    faces3 = all_faces(3)
    for perm in permutations(range(3)):
        for t in range(8):
            sign = sign_of_permutation(perm)
            actual = 1 - signed_lefschetz(faces3,
                        lambda x, perm=perm, t=t: permute(x, perm) ^ t)
            assert actual == sign, (perm, t, actual, sign)
            assertions += 1
    # Independently average full semidirect-product Lefschetz traces to
    # recover the coordinate-permutation character of translation invariants.
    for n in (4, 5):
        fs = all_faces(n)
        if n == 4:
            tests = list(permutations(range(n)))
        else:
            # Representatives of every S_5 conjugacy class.
            tests = [tuple(x) for x in (
                (0, 1, 2, 3, 4), (1, 0, 2, 3, 4),
                (1, 0, 3, 2, 4), (1, 2, 0, 3, 4),
                (1, 2, 0, 4, 3), (1, 2, 3, 0, 4),
                (1, 2, 3, 4, 0))]
        for perm in tests:
            sum_traces = sum(
                1 - signed_lefschetz(fs,
                     lambda x, perm=perm, t=t: permute(x, perm) ^ t)
                for t in range(1 << n))
            expected = 0
            for ix in combinations(range(n), 3):
                mapped = tuple(perm[i] for i in ix)
                if sorted(mapped) == list(ix):
                    expected += (-1)**sum(mapped[i] > mapped[j]
                                         for i in range(3) for j in range(i+1,3))
            assert sum_traces == (1 << n) * expected, (n, perm, sum_traces, expected)
            assertions += 1
        print('n=', n, 'coordinate-permutation tests=', len(tests),
              'invariant S_n module exterior cube verified')
    print('RIPS_QN_TRANSLATION_CHARACTER_CHECKS_OK', assertions)


if __name__ == '__main__':
    run()
