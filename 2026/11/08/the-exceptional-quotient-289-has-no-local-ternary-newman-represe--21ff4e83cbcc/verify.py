#!/usr/bin/env python3
"""Exact finite-state certificate for the polynomial quotient at multiplier 289.

Run with Python >= 3.8. Uses no third-party packages. The proof that this
finite certificate controls all lengths is stated in RESULT.md.
"""
from collections import deque
from itertools import product

M = 289
WEIGHTS = (96, 32, 11, 4, 1)
R = (1, 0, -1, -1, 1, 1)
LIVE = frozenset((0, 1, 4, 11, 12, 32, 33, 37, 44, 48, 96, 100,
                  107, 111, 112, 132, 133, 140, 143, 144))
DEAD = frozenset((5, 14, 15, 16, 43, 46, 98, 101, 128, 129, 130, 139))
UNIVERSE = LIVE | DEAD


def transitions(c):
    """All digit pairs (p, q) that induce a bounded integral carry."""
    out = []
    for q in (0, 1):
        for p in (0, 1):
            num = c + M * q - p
            if num % 3 == 0:
                d = num // 3
                if 0 <= d <= M // 2:
                    out.append((d, p, q))
    return out


def check_certificate():
    assert len(LIVE) == 20 and len(DEAD) == 12
    assert not (LIVE & DEAD) and 0 in LIVE
    assert R[0] + sum(R[k] * (3 ** k) for k in range(1, 6)) == M
    assert tuple(sum(R[k] * (3 ** (k - j)) for k in range(j, 6))
                 for j in range(1, 6)) == WEIGHTS
    for c in UNIVERSE:
        edges = transitions(c)
        assert edges and all(d in UNIVERSE for d, p, q in edges), c
        if c in DEAD:
            assert all(d in DEAD for d, p, q in edges), c
    # Strictly separated weights yield an injective 5-bit carry encoding.
    assert all(WEIGHTS[j] > sum(WEIGHTS[j + 1:]) for j in range(4))
    decode = {sum(a * b for a, b in zip(bits, WEIGHTS)): bits
              for bits in product((0, 1), repeat=5)}
    assert len(decode) == 32 and LIVE <= decode.keys()
    verified_live_edges = 0
    for c in LIVE:
        h = decode[c]  # bits q_{i-1}, ..., q_{i-5}, newest to oldest
        for d, p, q in transitions(c):
            if d in DEAD:
                continue
            assert d in LIVE
            assert decode[d] == (q,) + h[:4], (c, d, h, q)
            convolution_digit = q - h[1] - h[2] + h[3] + h[4]
            assert convolution_digit == p, (c, d, p, q, convolution_digit)
            verified_live_edges += 1
    assert verified_live_edges == 26, verified_live_edges

    # Independently rediscover the reachable and returnable carry states.
    visited, pending = {0}, deque([0])
    while pending:
        c = pending.popleft()
        for d, _, _ in transitions(c):
            if d not in visited:
                visited.add(d)
                pending.append(d)
    assert visited == UNIVERSE
    reversed_edges = {c: set() for c in visited}
    for c in visited:
        for d, _, _ in transitions(c):
            reversed_edges[d].add(c)
    returnable, pending = {0}, deque([0])
    while pending:
        d = pending.popleft()
        for c in reversed_edges[d]:
            if c not in returnable:
                returnable.add(c)
                pending.append(c)
    assert returnable == LIVE

    return verified_live_edges


def coeffs_match(pdigits, qdigits):
    max_degree = len(qdigits) + len(R) - 2
    for j in range(max(max_degree + 1, len(pdigits))):
        coeff = sum(R[k] * qdigits[j - k]
                    for k in range(len(R)) if 0 <= j - k < len(qdigits))
        actual = pdigits[j] if j < len(pdigits) else 0
        if coeff != actual:
            return False
    return True


def finite_crosscheck(max_length=38):
    """Extra, non-probative finite path experiment; not the infinite proof."""
    pdigits, qdigits = [], []
    count = 0
    def explore(c, length):
        nonlocal count
        if c == 0 and length:
            # Ignore common trailing zeros when translating back to polynomials.
            assert sum(a * (3 ** i) for i, a in enumerate(pdigits)) == M * sum(
                b * (3 ** i) for i, b in enumerate(qdigits))
            assert coeffs_match(pdigits, qdigits)
            count += 1
            return
        if length == max_length:
            return
        for d, p, q in transitions(c):
            pdigits.append(p)
            qdigits.append(q)
            explore(d, length + 1)
            pdigits.pop()
            qdigits.pop()
    # The first nonzero digits must be 1 and 1; leading zero shifts are irrelevant.
    pdigits.append(1)
    qdigits.append(1)
    explore((M - 1) // 3, 1)
    assert count > 900
    return count


def known_example_and_control():
    Q = (1, 0, 1, 1, 0, 1)
    P = (1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1)
    assert coeffs_match(P, Q)
    assert sum(a * 3 ** i for i, a in enumerate(P)) == 80920
    assert sum(a * 3 ** i for i, a in enumerate(Q)) == 280
    # Positive control: 22 has a known *local* quotient (not polynomial division).
    q22 = (1, 0, 1, 1)
    p22 = (1, 1, 0, 0, 1, 0, 1)
    assert sum(a * 3 ** i for i, a in enumerate(p22)) == 22 * sum(
        a * 3 ** i for i, a in enumerate(q22))
    # Polynomial long division, with monic leading coefficient.
    rem = list(p22)
    for i in range(len(rem) - 1, len(q22) - 2, -1):
        factor = rem[i]
        for j in range(len(q22)):
            rem[i - len(q22) + 1 + j] -= factor * q22[j]
    assert any(rem[:len(q22) - 1])


if __name__ == '__main__':
    edges = check_certificate()
    known_example_and_control()
    paths = finite_crosscheck()
    print('VERIFY_OK live_states=20 dead_states=12 live_edges=' + str(edges)
          + ' returning_paths_through_length_38=' + str(paths)
          + ' identity_for_all_lengths=finite_state_proof')
