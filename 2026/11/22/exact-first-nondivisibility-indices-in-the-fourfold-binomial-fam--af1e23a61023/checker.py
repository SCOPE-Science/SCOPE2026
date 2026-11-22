"""Exact finite-state certificate and independent finite tests for a binomial divisibility threshold.
Python 3, standard library only; run: python checker.py
"""
from math import comb

START = (-1, 1, -1, 0, 0, 0, 0)


def transition(state, digit):
    """One least-significant-first binary digit of a positive odd index.

    State (R,M,S,old1,old2,C,T) carries arithmetic for 4n-1,
    1-3n, 3n-1, delayed input, addition carry and capped carry count.
    """
    R, M, S, old1, old2, C, T = state
    z = old2 + R
    rb, Rnew = z % 2, z // 2
    z = M - 3 * digit
    mb, Mnew = z % 2, z // 2
    Snew = (S + 3 * digit) // 2
    Cnew = (rb + mb + C) // 2
    Tnew = min(2, T + Cnew)
    return (Rnew, Mnew, Snew, digit, old1, Cnew, Tnew)


def next_set(states):
    return {transition(state, digit) for state in states for digit in (0, 1)}


def encode(states):
    return tuple(sorted(states))


EXPECTED_R3 = (
    (0, -3, 2, 1, 1, 0, 0),
    (0, -2, 1, 1, 0, 0, 1),
    (0, -1, 0, 0, 0, 1, 2),
    (0, -1, 1, 0, 1, 0, 0),
)
EXPECTED_R5 = (
    (0, -3, 2, 1, 0, 1, 2),
    (0, -3, 2, 1, 1, 0, 0),
    (0, -3, 2, 1, 1, 0, 1),
    (0, -3, 2, 1, 1, 0, 2),
    (0, -2, 1, 0, 1, 1, 1),
    (0, -2, 1, 0, 1, 1, 2),
    (0, -2, 1, 1, 0, 0, 1),
    (0, -2, 1, 1, 0, 0, 2),
    (0, -1, 0, 0, 0, 1, 2),
    (0, -1, 0, 0, 1, 0, 2),
    (0, -1, 1, 0, 1, 0, 0),
)


def main():
    checks = 0
    # Initialize with the forced odd least-significant bit.
    R1 = {transition(START, 1)}
    R3 = next_set(next_set(R1))
    assert encode(R3) == EXPECTED_R3
    checks += 1
    R5 = next_set(next_set(R3))
    assert encode(R5) == EXPECTED_R5
    checks += 1
    assert next_set(next_set(R5)) == R5
    checks += 1
    # S==0 means that the entire positive integer 3n-1 is below 2^h.
    # T<2 means fewer than two binary carries in the lowest h places.
    for states in (R3, R5):
        assert all(S != 0 or T == 2 for _, _, S, _, _, _, T in states)
        checks += 1
    # Cross-check the state convention with literal low-bit additions.
    for h in range(3, 13, 2):
        for n in range(1, min(2**h, 3000), 2):
            state = START
            for bit_idx in range(h):
                state = transition(state, (n >> bit_idx) & 1)
            R, M, S, d1, d2, c, T = state
            lowa = (4*n-1) % (2**h)
            lowb = (1-3*n) % (2**h)
            actual = lowa.bit_count()+lowb.bit_count()-(lowa+lowb).bit_count()
            assert T == min(2, actual)
            assert S == (3*n-1) // (2**h)
            checks += 2
    # Independently test exact failure using Kummer's digit-sum formula.
    def fails(b,n):
        M=(b+4)*n
        vp = (4*n-1).bit_count()+(b*n+1).bit_count()-M.bit_count()
        return n%2 == 1 and vp < 2
    for b in range(1, 2002, 2):
        k=((b+3)&-(b+3)).bit_length()-1
        h=k if k%2 else k-1
        predicted=(2**h+1)//3
        assert fails(b,predicted)
        checks += 1
        for n in range(1,predicted,2):
            assert not fails(b,n)
            checks += 1
    # Direct integer binomial divisibility tests; independent of v2 criterion.
    for b in range(1, 76):
        for n in range(1, 28):
            direct = comb((b+4)*n,4*n) % (b*n+1) != 0
            assert direct == fails(b,n)
            checks += 1
    print('PASS:', checks, 'exact assertions; 11-state recurrent certificate; no sampled basis for the infinite claim')


if __name__ == '__main__':
    main()
