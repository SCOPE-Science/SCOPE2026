#!/usr/bin/env python3
"""Independent GF(2)-matrix verification and bipartite spine-edit comparison."""


def rank(columns):
    pivots = {}
    for col in columns:
        while col:
            i = col.bit_length() - 1
            if i in pivots:
                col ^= pivots[i]
            else:
                pivots[i] = col
                break
    return len(pivots)


def transform(columns, other):
    result = []
    for y in other:
        z = 0
        while y:
            bit = y & -y
            z ^= columns[bit.bit_length() - 1]
            y ^= bit
        result.append(z)
    return result


def sweep_basis(k, t, spine):
    n = k + 2
    order = [0] + list(range(2, 2 + t)) + [1] + list(range(2 + t, n))
    leaves = sum(1 << i for i in range(2, n))
    adj = [leaves | (2 if spine else 0), leaves | (1 if spine else 0)] + [3] * k
    ans = []
    for j in range(n):
        x = 1 << j
        for v in order:
            x ^= ((x & adj[v]).bit_count() & 1) << v
        ans.append(x)
    return ans


def fixed_dimension(power, n):
    return n - rank([v ^ (1 << i) for i, v in enumerate(power)])


def expected_dimension(k, t, spine, d):
    if k % 2:
        return k if d % 2 else (k + 1 if d % 4 else k + 2)
    two_phase = (t % 2 != 0) if spine else (t % 2 == 0)
    return k + 2 if d % (2 if two_phase else 3) == 0 else k


def main():
    identities = 0
    rank_checks = 0
    comparisons = 0
    for k in range(1, 41):
        n = k + 2
        ident = [1 << j for j in range(n)]
        for t in range(k + 1):
            for spine in (False, True):
                mat = sweep_basis(k, t, spine)
                pwr = ident
                for d in range(1, 13):
                    pwr = transform(mat, pwr)
                    dim = fixed_dimension(pwr, n)
                    pred = expected_dimension(k, t, spine, d)
                    assert dim == pred, (k, t, spine, d, dim, pred)
                    identities += int(dim == n)
                    rank_checks += 1
            book_2 = sweep_basis(k, t, True)
            bip_2 = sweep_basis(k, t, False)
            for d in (1, 2, 3, 4, 6, 12):
                def dim_for(M):
                    P = ident
                    for _ in range(d):
                        P = transform(M, P)
                    return fixed_dimension(P, n)
                bb, bip = dim_for(book_2), dim_for(bip_2)
                expected_bip = expected_dimension(k, t, False, d)
                assert bip == expected_bip
                if k % 2:
                    assert bb == bip
                elif t % 2 == 0:
                    assert dim_for(book_2) == expected_dimension(k, t + 1, False, d)
                else:
                    assert dim_for(book_2) == expected_dimension(k, t - 1, False, d)
                comparisons += 1
    print(f'k=1..40, all cyclic gap classes t=0..k, both graphs: {rank_checks} fixed-space dimension comparisons PASS')
    print(f'{comparisons} cross-graph orbit-census comparison tests PASS; {identities} identity powers verified')


if __name__ == '__main__':
    main()
