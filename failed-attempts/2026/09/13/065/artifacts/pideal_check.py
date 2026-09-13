"""Finite-truncation check of the P-ideal diagonal lemma for the density-zero
ideal Z0 (see output/DRAFT.md, Lemma 2).

Lemma: every countable family in Z0 has a pseudo-union in Z0. Reducing to an
increasing sequence A_0 ⊆ A_1 ⊆ ... of density-zero sets, the construction is:
thresholds t_j with |A_j ∩ n|/n <= 2^-j for all n >= t_j; then inductively
  m_0 = max(t_0,1),
  m_j = max(t_j, m_{j-1}+1, 2^j * S_{j-1}),  S_{j-1} = |A ∩ m_{j-1}|,
and A = union_j (A_j ∩ [m_j, m_{j+1})), last block running to the truncation N.

The analysis gives A_j \\ A ⊆ m_j (finite) and, on each window
[m_j, m_{j+1}), density ratio |A ∩ n|/n <= 2^(-j+2) -> 0.

This script implements EXACTLY that construction on {0,...,N-1} with nested
sparse test families and asserts both conclusions on the window. Finite
combinatorial sanity check only; the real proof is analytic (DRAFT.md).
"""

def build_and_check(families, N, label):
    J = len(families)
    # nestedness
    for j in range(J - 1):
        assert families[j] <= families[j + 1], f"{label}: not nested at {j}"

    def threshold(j):
        eps = 2.0 ** (-j)
        for M in range(N + 1):
            if all(
                len([a for a in families[j] if a < n]) / n <= eps
                for n in range(max(M, 1), N + 1)
            ):
                return M
        raise AssertionError(f"{label}: no threshold for j={j}")

    m = [None] * J
    A = set()
    for j in range(J):
        t = threshold(j)
        if j == 0:
            m[0] = max(t, 1)
        else:
            S_prev = len([a for a in A if a < m[j - 1]])
            m[j] = max(t, m[j - 1] + 1, (2 ** j) * S_prev)
            assert m[j] < N, f"{label}: threshold exceeds window at j={j}"
            A |= {a for a in families[j - 1] if m[j - 1] <= a < m[j]}
    A |= {a for a in families[J - 1] if m[J - 1] <= a < N}

    # (a) almost-containment: A_j \\ A ⊆ m_j
    for j in range(J):
        excess = [a for a in families[j] if a not in A and a >= m[j]]
        assert not excess, f"{label}: A_{j} not almost-contained: {excess[:5]}"

    # (b) windowed density bound 2^(-j+2)
    for j in range(J):
        hi = m[j + 1] if j + 1 < J else N
        bound = 2.0 ** (-j + 2)
        for n in range(m[j], hi):
            ratio = len([a for a in A if a < n]) / n
            assert ratio <= bound + 1e-12, (
                f"{label}: density bound fails j={j} n={n} ratio={ratio} bound={bound}"
            )
    tail = len([a for a in A if a < N]) / N
    print(f"{label}: OK  m={m}  final-window density={tail:.5f}")


def sparse_chain(N):
    p2 = {2 ** k for k in range(N) if 2 ** k < N}
    cubes = {k ** 3 for k in range(N) if k ** 3 < N}
    squares = {k * k for k in range(N) if k * k < N}
    facts = set()
    f, k = 1, 1
    while f < N:
        facts.add(f)
        k += 1
        f *= k
    pow3 = {3 ** k for k in range(N) if 3 ** k < N}
    shifted = {k * k + k + 1 for k in range(N) if k * k + k + 1 < N}
    chain, acc = [], set()
    for fam in (p2, cubes, squares, facts, pow3, shifted):
        acc = acc | fam
        chain.append(set(acc))
    return chain


if __name__ == "__main__":
    N = 20000
    build_and_check(sparse_chain(N), N, "nested-sparse-chain/J=6")
    print("All finite-truncation checks passed.")
