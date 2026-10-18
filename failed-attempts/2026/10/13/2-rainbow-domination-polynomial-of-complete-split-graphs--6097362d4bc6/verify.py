#!/usr/bin/env python3
from itertools import product

# Labels are encoded as 0=empty, 1={1}, 2={2}, 3={1,2}.

def conv(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def add(p, q, qscale=1):
    m = max(len(p), len(q))
    out = [0] * m
    for i in range(m):
        out[i] = (p[i] if i < len(p) else 0) + qscale * (q[i] if i < len(q) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def ppow(p, n):
    out = [1]
    for _ in range(n):
        out = conv(out, p)
    return out


def formula(r, n):
    # A=(1+x)^2, B=2x+x^2.
    A = [1, 2, 1]
    B = [0, 2, 1]
    onepx = [1, 1]
    x = [0, 1]

    out = conv(ppow(A, r), ppow(B, n))

    correction = add(ppow(onepx, r), ppow(x, r), qscale=-1)
    correction = [0] * n + [-2 * c for c in correction]
    out = add(out, correction)

    both_on_clique = add(add(ppow(A, r), ppow(onepx, r), qscale=-2), [1])
    empty_on_independent = add(ppow(A, n), ppow(B, n), qscale=-1)
    out = add(out, conv(both_on_clique, empty_on_independent))
    return out


def literal_coefficients(r, n):
    N = r + n
    coeff = [0] * (2 * N + 1)
    for labels in product(range(4), repeat=N):
        ok = True
        for v, label in enumerate(labels):
            if label != 0:
                continue
            colors = 0
            if v < r:  # Empty clique vertex sees every other vertex.
                for u in range(N):
                    if u != v:
                        colors |= labels[u]
            else:      # Empty independent vertex sees exactly the clique.
                for u in range(r):
                    colors |= labels[u]
            if colors != 3:
                ok = False
                break
        if ok:
            weight = sum(2 if label == 3 else 1 if label in (1, 2) else 0 for label in labels)
            coeff[weight] += 1
    while len(coeff) > 1 and coeff[-1] == 0:
        coeff.pop()
    return coeff


def expected_total(r, n):
    return (4**r) * (3**n) - 2 * (2**r - 1) + (4**r - 2**(r + 1) + 1) * (4**n - 3**n)


def expected_min_count(r, n):
    return r * r + (2 if n == 2 else 0)


def main():
    labelings = 0
    coefficient_checks = 0
    minimum_checks = 0
    total_checks = 0
    for r in range(2, 5):
        for n in range(2, 5):
            brute = literal_coefficients(r, n)
            closed = formula(r, n)
            labelings += 4 ** (r + n)
            coefficient_checks += max(len(brute), len(closed))
            if brute != closed:
                raise AssertionError(("coefficient mismatch", r, n, brute, closed))
            min_weight = next(i for i, c in enumerate(brute) if c)
            if min_weight != 2 or brute[2] != expected_min_count(r, n):
                raise AssertionError(("minimum mismatch", r, n, min_weight, brute[2]))
            minimum_checks += 1
            if sum(brute) != expected_total(r, n):
                raise AssertionError(("total mismatch", r, n, sum(brute), expected_total(r, n)))
            total_checks += 1
    print(
        "VERIFY_OK r_range=2..4 n_range=2..4 "
        f"labelings={labelings} coefficient_checks={coefficient_checks} "
        f"minimum_checks={minimum_checks} total_checks={total_checks} max_order=8"
    )


if __name__ == "__main__":
    main()
