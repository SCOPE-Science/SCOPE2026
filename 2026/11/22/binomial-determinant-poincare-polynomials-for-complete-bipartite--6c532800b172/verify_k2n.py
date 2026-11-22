"""Exact integer determinant and finite-field exterior-differential checks."""
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def predicted(n):
    out = [0] * (3 * n + 3)
    for a in range(n + 1):
        for b in range(a + 1):
            for c in range(b + 1):
                v = [a, b, c]
                mult = det3([[choose(n, v[i] - i + j)
                              for j in range(3)] for i in range(3)])
                assert mult >= 0
                for j, coefficient in enumerate((b - c + 1,
                                                  a - c + 2,
                                                  a - b + 1)):
                    out[a + b + c + j] += mult * coefficient
    assert out == out[::-1]
    assert out[0] == 1 and out[-1] == 1
    return out


def sorted_sign(seq):
    if len(set(seq)) < len(seq):
        return 0
    return -1 if sum(seq[i] > seq[j]
                     for i in range(len(seq))
                     for j in range(i + 1, len(seq))) % 2 else 1


def direct_betti(n, prime):
    # Basis a,b,x[0:n],z[0:n],w[0:n]; d(z_i)=a*x_i,
    # d(w_i)=b*x_i. All signs are computed from actual wedge permutations.
    dim = 3 * n + 2
    groups = [[sum(1 << i for i in subset)
               for subset in combinations(range(dim), k)]
              for k in range(dim + 1)]
    ranks = []
    for k in range(dim):
        targets = {mask: j for j, mask in enumerate(groups[k + 1])}
        pivots = {}
        for mask in groups[k]:
            original = [j for j in range(dim) if mask >> j & 1]
            column = {}
            for pos, j in enumerate(original):
                if j < n + 2:
                    continue
                edge = j - (n + 2)
                substitute = ([0, 2 + edge] if edge < n
                              else [1, 2 + edge - n])
                sign = ((-1) ** pos) * sorted_sign(
                    substitute + original[:pos] + original[pos + 1:])
                if sign:
                    new_mask = (mask ^ (1 << j))
                    for r in substitute:
                        new_mask |= 1 << r
                    row = targets[new_mask]
                    column[row] = (column.get(row, 0) + sign) % prime
            column = {j: v for j, v in column.items() if v}
            while column:
                j = min(column)
                if j not in pivots:
                    inverse = pow(column[j], -1, prime)
                    pivots[j] = {a: (b * inverse) % prime
                                 for a, b in column.items()}
                    break
                factor = column[j]
                for a, b in pivots[j].items():
                    column[a] = (column.get(a, 0) - factor * b) % prime
                    if column[a] == 0:
                        del column[a]
        ranks.append(len(pivots))
    return [len(groups[i]) - (ranks[i - 1] if i else 0) -
            (ranks[i] if i < dim else 0) for i in range(dim + 1)]


def main():
    expected_totals = [20, 116, 728, 4792, 32568, 226480,
                       1602392, 11491016, 83299112]
    for n, expected in enumerate(expected_totals, 1):
        b = predicted(n)
        assert sum(b) == expected
        print(f"formula n={n}: total={sum(b)}, betti={b}")
    for n in (1, 2, 3):
        for p in (3, 101):
            b = direct_betti(n, p)
            assert b == predicted(n), (n, p, b, predicted(n))
            print(f"direct CE n={n}, characteristic={p}: MATCH")
    print("ALL CHECKS PASSED")


if __name__ == '__main__':
    main()
