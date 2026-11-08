"""Independent finite replay of a two-agent S5 believed-announcement cascade.

The program uses set-valued relations and computes the announcement's Boolean
truth set directly. The general all-size theorem is proved separately.
"""


def block_equivalence(n, start):
    blocks = []
    j = 0
    if start == 1:
        blocks.append([0]); j = 1
    while j + 1 < n:
        blocks.append([j, j + 1]); j += 2
    if j < n:
        blocks.append([j])
    return {(u, v) for B in blocks for u in B for v in B}


def equivalence(R, n):
    W = range(n)
    return (all((i, i) in R for i in W)
            and all((j, i) in R for i, j in R)
            and all(not ((i, j) in R and (j, k) in R) or (i, k) in R
                    for i in W for j in W for k in W))


def truth_set(n, p, Ra, Rb):
    # (p and diamond_a not-p) or (not-p and diamond_b p)
    return {j for j in range(n)
            if ((j in p and any((j, v) in Ra and v not in p for v in range(n)))
                or (j not in p and any((j, v) in Rb and v in p for v in range(n))))}


def active_targets(rels):
    return {v for R in rels for _, v in R}


def verify_two_agents(n):
    p = set(range(0, n, 2))
    Ra = block_equivalence(n, 0)
    Rb = block_equivalence(n, 1)
    assert equivalence(Ra, n) and equivalence(Rb, n)
    for k in range(n + 1):
        active = active_targets([Ra, Rb])
        assert active == set(range(n - k)), (n, k, sorted(active))
        if k == n:
            assert not Ra and not Rb
            assert not truth_set(n, p, Ra, Rb)
            break
        accepted = truth_set(n, p, Ra, Rb)
        assert accepted & active == set(range(n - k - 1)), (n, k, accepted)
        A1 = {(u, v) for (u, v) in Ra if v in accepted}
        B1 = {(u, v) for (u, v) in Rb if v in accepted}
        assert (A1, B1) != (Ra, Rb)
        Ra, Rb = A1, B1


def verify_one_agent(n, r):
    k = min(n, 2**r)
    # k distinct truth types encoded as bit vectors; duplicate type 0 if needed.
    types = list(range(k)) + [0] * (n - k)
    R = {(u, v) for u in range(n) for v in range(n)}
    # psi = OR_{i=0}^{k-2} (q_i AND diamond q_{i+1})
    for j in range(k + 1):
        T = {v for _, v in R}
        expected = {v for v in range(n) if types[v] < k - j}
        assert T == expected, (n, r, j, T, expected)
        phi = {u for u in range(n) if any(types[u] == i and
               any((u, v) in R and types[v] == i + 1 for v in range(n))
               for i in range(k - 1))}
        R2 = {(u, v) for (u, v) in R if v in phi}
        if j < k:
            assert R2 != R
        else:
            assert R2 == R
        R = R2


def main():
    for n in range(1, 101):
        verify_two_agents(n)
    for r in range(0, 5):
        for n in range(1, 31):
            verify_one_agent(n, r)
    print('PASS: n=1..100 alternating-pair two-agent S5 construction')
    print('PASS: n=1..30 and r=0..4 single-agent bit-type lower witnesses')

if __name__ == '__main__':
    main()
