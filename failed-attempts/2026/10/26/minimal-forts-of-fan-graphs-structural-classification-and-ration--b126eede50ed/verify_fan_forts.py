#!/usr/bin/env python3
"""Exact subset tests for minimal forts of cone-over-path graphs.

All graph-neighborhood tests below use the original definition of a fort.
The predicted family uses an independent path-word/dominating-set description.
Only the finite instances explicitly reported here are exhaustively tested.
"""
from __future__ import annotations


def adjacencies(n):
    # Vertex 0 is the cone; vertices 1,...,n form a path.
    return [((1 << n) - 1) << 1] + [
        1 | ((1 << (i - 1)) if i > 1 else 0)
          | ((1 << (i + 1)) if i < n else 0)
        for i in range(1, n + 1)
    ]


def actual_minimal_forts(n):
    adj = adjacencies(n)
    all_forts = []
    for subset in range(1, 1 << (n + 1)):
        if all(((subset >> i) & 1) or ((adj[i] & subset).bit_count() != 1)
               for i in range(n + 1)):
            all_forts.append(subset)
    minimal = []
    for subset in sorted(all_forts, key=int.bit_count):
        if not any((subset & previous) == previous for previous in minimal):
            minimal.append(subset)
    return set(minimal)


def path_dominates(mask, n):
    for i in range(n):
        if (mask >> i) & 1:
            continue
        left = i > 0 and ((mask >> (i - 1)) & 1)
        right = i + 1 < n and ((mask >> (i + 1)) & 1)
        if not (left or right):
            return False
    return True


def predicted_minimal_forts(n):
    predicted = set()
    minimal_dominating = []
    min_path_forts = []
    alternating = sum(1 << i for i in range(0, n, 2))
    for mask in range(1, 1 << n):
        word = ''.join(str((mask >> i) & 1) for i in range(n))
        if word[0] == word[-1] == '1' and '00' not in word and '111' not in word:
            min_path_forts.append(mask)
            predicted.add(mask << 1)
        if path_dominates(mask, n) and all(
            not path_dominates(mask ^ (1 << i), n)
            for i in range(n) if (mask >> i) & 1
        ):
            minimal_dominating.append(mask)
            if not (n % 2 == 1 and mask == alternating):
                predicted.add(1 | (mask << 1))
    return predicted, len(min_path_forts), len(minimal_dominating)


def gf_sequences(up_to):
    # [z^n] (1+z+z^2-z^5)/(1-z^2-z^3-z^4+z^6)
    d = [0] * (up_to + 1)
    f = [0] * (up_to + 1)
    for n in range(up_to + 1):
        numerator_d = {0: 1, 1: 1, 2: 1, 5: -1}.get(n, 0)
        d[n] = numerator_d
        for k, sign in ((2, 1), (3, 1), (4, 1), (6, -1)):
            if n >= k:
                d[n] += sign * d[n - k]
        f[n] = int(n in (1, 2))
        for k in (2, 3):
            if n >= k:
                f[n] += f[n - k]
    return d, f


def main():
    d, f = gf_sequences(100)
    total_examined = 0
    for n in range(2, 17):
        actual = actual_minimal_forts(n)
        prediction, f_count, d_count = predicted_minimal_forts(n)
        total_examined += (1 << (n + 1)) - 1
        assert actual == prediction, (n, actual ^ prediction)
        assert f[n] == f_count, ('path fort coefficient', n, f[n], f_count)
        assert d[n] == d_count, ('minimal dominating coefficient', n, d[n], d_count)
        assert len(actual) == d[n] + f[n] - (n % 2)
        print(f'n={n:2d} forts={len(actual):3d} path_forts={f[n]:2d} minimal_dominating={d[n]:3d}')
    assert d[:16] == [1, 1, 2, 2, 4, 4, 7, 9, 13, 18, 25, 36, 49, 70, 97, 137]
    assert f[:9] == [0, 1, 1, 1, 2, 2, 3, 4, 5]
    assert all(d[n] + f[n] - (n % 2) > 0 for n in range(2, 101))
    print(f'EXHAUSTIVE_OK n=2..16 candidate_subsets={total_examined} exact_family_match=true')
    print('GENERATING_FUNCTION_OK coefficients=0..100')
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
