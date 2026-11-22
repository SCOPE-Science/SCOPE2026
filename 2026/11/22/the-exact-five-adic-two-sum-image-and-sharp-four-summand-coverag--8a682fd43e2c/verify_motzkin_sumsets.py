#!/usr/bin/env python3
"""Reproduce exact finite tests for the stated Motzkin-zero index sumset.

Only the Python standard library is used. The infinite equalities are proved
in RESULT.md; bounded tests are diagnostics, not substitute proofs.
"""

def valuation_and_unit(t):
    if t == 0:
        return None
    v = 0
    while t % 5 == 0:
        t //= 5
        v += 1
    return v, t % 5


def in_x_integer(t):
    if t == 0:
        return True
    z = valuation_and_unit(t)
    v, unit = z
    return v >= 1 and unit == (2 if v % 2 else 4)


def in_z_integer(n):
    return in_x_integer(n+1) or in_x_integer(-n-2)


def x_residues(k):
    q = 5**k
    ans = {0}
    for t in range(5, q, 5):
        if in_x_integer(t):
            ans.add(t)
    return ans


def p_membership(t, k):
    q = 5**k
    t %= q
    if k <= 1:
        return t % 5 == 0
    if k == 2:
        return t % 25 in (0, 10, 20)
    if t % 25 in (10, 20):
        return True
    if t % 125 in (75, 100):
        return True
    return t % 25 == 0 and p_membership(t//25, k-2)


def d_membership(t, k):
    if k == 1:
        return t % 5 == 0
    return t % 25 in (0, 10, 15)


def sum_membership(t, k):
    q = 5**k
    if t % 5 == 3:
        return p_membership(t+2, k)
    if t % 5 == 2:
        return d_membership(t+3, k)
    if t % 5 == 1:
        return p_membership(-t-4, k)
    return False


def motzkin_values(upto):
    arr = [1, 1]
    for n in range(2, upto+1):
        numerator = (2*n+1)*arr[-1] + 3*(n-1)*arr[-2]
        assert numerator % (n+2) == 0
        arr.append(numerator//(n+2))
    return arr[:upto+1]


def run():
    checks = 0
    # Direct integer recurrence is independent of the quoted zero-index criterion.
    for n, m in enumerate(motzkin_values(1600)):
        assert (m % 5 == 0) == in_z_integer(n), (n, m % 5)
        checks += 1

    for k in range(1, 7):
        q = 5**k
        X = x_residues(k)
        Z = {(-1+x) % q for x in X} | {(-2-x) % q for x in X}
        assert len(Z) == (2 * len(X))
        # Direct modular sum enumeration, not invoking the claimed branch recursion.
        actual = {(a+b)%q for a in Z for b in Z}
        predicted = {t for t in range(q) if sum_membership(t, k)}
        assert actual == predicted, (k, actual ^ predicted)
        assert len(actual) == (3 if k == 1 else 8*5**(k-2)+1)
        # Fourfold coverage obtained from independently enumerated twofold sums.
        fourfold = {(a+b)%q for a in actual for b in actual}
        assert len(fourfold) == q, ('fourfold', k)
        assert len({(a+b+c)%5 for a in (3,4) for b in (3,4) for c in (3,4)}) == 4
        if k >= 2:
            P = {(a+b) % q for a in X for b in X}
            D = {(a-b) % q for a in X for b in X}
            assert len(P) == (5**(k-1)+1)//2
            assert len(D) == 3*5**(k-2)
            assert all(p_membership(x,k) for x in P)
            assert all(d_membership(x,k) for x in D)
            assert len(actual) == 2*len(P)+len(D)
        print(f'k={k}: X={len(X)}, Z={len(Z)}, sums={len(actual)}, modulus={q}')
        checks += len(Z)**2 + q

    # Finite certificate of all four signed digit-lift cases in the proof.
    from itertools import product
    digit_options = (0, 10, 35, 60, 85, 110, 100)
    for r in range(5):
        residues = {(sum(qs[:r])-sum(qs[r:])) % 125
                    for qs in product(digit_options, repeat=4) if any(qs)}
        assert all(x in residues for x in range(5, 125, 5)), r
        checks += len(residues)
    # No exceptional boundary mistakes: equality checked through 5^6.
    print(f'VERIFY_OK checks={checks}')


if __name__ == '__main__':
    run()
