#!/usr/bin/env python3
"""Independent finite checks for the dyadic Baum--Sweet abelian-complexity theorem.
The proof in RESULT.md, not this finite computation, establishes all exponents.
"""

def digit_rule(n):
    if n == 0:
        return 1
    bits = bin(n)[2:]
    return int(all(len(run) % 2 == 0 for run in bits.split('1')))


def morphic_prefix(exp):
    trans = {'A': 'AB', 'B': 'CB', 'C': 'BD', 'D': 'DD'}
    word = 'A'
    for _ in range(exp):
        word = ''.join(trans[c] for c in word)
    return [int(c in 'AB') for c in word]


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    M = 17
    w = morphic_prefix(M)
    assert len(w) == 2 ** M
    assert w == [digit_rule(i) for i in range(len(w))], 'independent generators disagree'
    ps = [0]
    for bit in w:
        ps.append(ps[-1] + bit)
    for m in range(12):
        N = 1 << m
        expected = fib(m + 2)
        assert ps[N] == expected
        # Full factor scan within the generated prefix, not a proof about infinity.
        maximum = max(ps[i+N] - ps[i] for i in range(len(w)-N+1))
        minimum = min(ps[i+N] - ps[i] for i in range(len(w)-N+1))
        assert (maximum, minimum) == (expected, 0), (m, maximum, minimum)
        # Also verify a finite sample of the stronger pointwise block domination.
        for q in range(min(32, len(w)//N)):
            for r in range(N):
                assert w[q*N+r] <= w[r], (m,q,r)
        print(f'm={m:2d} N={N:4d} max={maximum:3d} min={minimum} classes={expected+1}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
