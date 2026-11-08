"""Finite standard-library checks of block identities for polynomial-weighted Rhaly matrices.

The infinite trace-class theorem requires the mathematical proof in RESULT.md.
Run: python3 verify.py
"""
from math import isclose, sqrt, log


def blocks(n):
    output = [[0]]
    k = 1
    while 2 ** (k - 1) < n:
        output.append(list(range(2 ** (k - 1), min(2 ** k, n))))
        k += 1
    return output


def close(a, b):
    return isclose(a, b, rel_tol=1e-11, abs_tol=1e-11)


count = 0
n = 64
partition = blocks(n)
assert sorted(v for block in partition for v in block) == list(range(n))
count += 1
for case in range(3):
    eta = [complex(((i * 7 + 3) % 11 - 5) / (i + 1) ** 1.6,
                   ((i * 5 + 1) % 7 - 3) / (i + 1) ** 1.75) for i in range(n)]
    if case == 1:
        eta = [x if i in {0, 1, 2, 7, 15, 31, 63} else 0j for i, x in enumerate(eta)]
    elif case == 2:
        eta = [complex((-1) ** i / (i + 1) ** 1.7, 0) for i in range(n)]
    for a in (-3.0, -1.0, 0.0, 0.5, 0.99):
        f = [[eta[i] * ((i + 1) / (j + 1)) ** (a / 2) if j <= i else 0j
              for j in range(n)] for i in range(n)]
        for k, rows in enumerate(partition):
            # The diagonal block is a diagonal similarity of the unweighted block.
            for i in rows:
                for j in rows:
                    expected = eta[i] * ((i + 1) / (j + 1)) ** (a / 2) if j <= i else 0j
                    assert close(abs(f[i][j] - expected), 0)
                    count += 1
            if not k:
                continue
            earlier = [j for B in partition[:k] for j in B]
            # Every strictly preceding row block is a single rank-one rectangle.
            for i in rows:
                for j in earlier:
                    assert close(abs(f[i][j] - eta[i] * (i + 1) ** (a / 2)
                                     * (j + 1) ** (-a / 2)), 0)
                    count += 1
            adjacent = partition[k - 1]
            row_energy = sum(abs(eta[i]) ** 2 * (i + 1) ** a for i in rows)
            col_energy = sum((j + 1) ** (-a) for j in adjacent)
            adjacent_hs = sqrt(sum(abs(f[i][j]) ** 2 for i in rows for j in adjacent))
            assert close(adjacent_hs, sqrt(row_energy * col_energy))
            count += 1
            previous_energy = sum((j + 1) ** (-a) for j in earlier)
            all_prev_hs = sqrt(sum(abs(f[i][j]) ** 2 for i in rows for j in earlier))
            assert close(all_prev_hs, sqrt(row_energy * previous_energy))
            count += 1
            # Finite check that the full preceding column energy dominates the adjacent one.
            assert previous_energy >= col_energy - 1e-12
            count += 1
# In the sparse endpoint witness, individual Hardy rank-one trace costs are h^{-5/4}
# while weighted Dirichlet Hilbert-Schmidt squares are h^{-5/2}H_{2^{h^2}+1}.
for h in range(1, 7):
    nh = 2 ** (h * h)
    eta_h = (nh + 1) ** (-0.5) * h ** (-1.25)
    assert close(eta_h * sqrt(nh + 1), h ** (-1.25))
    assert h ** (-2.5) * log(nh + 2) >= log(2) * h ** (-0.5)
    count += 2
print(f'POLYNOMIAL_RHALY_BLOCK_CHECK_OK {count} finite assertions')
