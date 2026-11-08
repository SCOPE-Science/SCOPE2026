#!/usr/bin/env python3
"""Finite diagnostics for antisquares in the Mephisto Waltz word.

Runs with the Python standard library. These checks complement, but do not
replace, the infinite structural and frequency proofs in RESULT.md.
"""


def word(depth):
    v = bytearray([0])
    for _ in range(depth):
        u = bytearray(3 * len(v))
        u[0::3] = v
        u[1::3] = v
        u[2::3] = bytearray(1 - a for a in v)
        v = u
    return v


def diff_at(w, q):
    return int(w[q] != w[q + 1])


def admissible(k):
    while k and k % 3 == 0:
        k //= 3
    return k in (1, 2)


def predicted(w, start, k):
    if not admissible(k):
        return False
    tscale = 1
    h = k
    while h % 3 == 0:
        h //= 3
        tscale *= 3
    q, r = divmod(start, tscale)
    if h == 1:
        return bool(diff_at(w, q) and (r == 0 or diff_at(w, q + 1)))
    if r:
        return q % 9 == 2
    a, m = divmod(q, 3)
    return bool((m == 0 and diff_at(w, a)) or
                (m == 2 and not diff_at(w, a)))


def verify():
    w = word(9)
    assert len(w) == 19683
    # Independently build its terms by digit parity.
    for n in range(len(w)):
        t = n
        parity = 0
        while t:
            parity ^= (t % 3 == 2)
            t //= 3
        assert w[n] == parity, ('word', n)
    comparisons = 0
    occurrence_matches = 0
    # Exhaust all starts through 4095 and half-lengths through 512.
    # The sliding sum counts noncomplementary paired symbols.
    for k in range(1, 513):
        stop = 4096
        mismatch = bytearray(int(w[j] == w[j + k]) for j in range(stop + k))
        nbad = sum(mismatch[:k])
        for i in range(stop):
            observed = (nbad == 0)
            claimed = predicted(w, i, k)
            assert observed == claimed, ('antisquare', i, k, observed, claimed)
            comparisons += 1
            occurrence_matches += observed
            nbad += mismatch[i + k] - mismatch[i]
    # Exact small-scale base-pattern frequency identities on complete ternary blocks.
    for a in range(3 ** 7):
        assert diff_at(w, 3*a) == 0
        assert diff_at(w, 3*a+1) == 1
        assert diff_at(w, 3*a+2) == 1-diff_at(w, a)
        for q in (3*a,3*a+1,3*a+2):
            assert ((diff_at(w,q)==0 and diff_at(w,q+1)==1) ==
                    (q%3==0)), ('adjacent01', q)
    assert ''.join(map(str, w[2:6])) == '1001'
    assert ''.join(map(str, w[1:3])) == '01'
    print('VERIFY_OK', 'length=',len(w), 'orders=1..512',
          'starts=0..4095', 'compared=',comparisons,
          'observed_antisquares=',occurrence_matches,
          'digit_parity_checks=',len(w), 'derivative_checks=',3**7)


if __name__ == '__main__':
    verify()
