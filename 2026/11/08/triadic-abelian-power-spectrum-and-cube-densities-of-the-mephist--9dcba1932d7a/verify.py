"""Finite diagnostics for triadic Abelian powers of the Mephisto Waltz word.

The all-length theorem is established mathematically in RESULT.md; these checks
are independent finite tests of its local identities and explicit recurrence.
Runs with Python 3.9+ and no third-party dependencies.
"""
from collections import defaultdict


def signs(n):
    a = [1] * n
    for j in range(1, n):
        a[j] = a[j // 3] * (-1 if j % 3 == 2 else 1)
    return a


def prefix(a):
    out = [0]
    for v in a:
        out.append(out[-1] + v)
    return out


def recurrence_counts(kmax):
    state = {(0, 1): 1}
    out = []
    for k in range(kmax + 1):
        l = 3**k
        assert sum(state.values()) == l
        total = sum(v for (p, eps), v in state.items() if p in (0, 1))
        out.append(total)
        nxt = defaultdict(int)
        for (p, eps), count in state.items():
            nxt[p, eps] += count
            nxt[p + eps, eps] += count
            nxt[p + 2 * eps, -eps] += count
        state = dict(nxt)
    return out


def main():
    checks = 0
    bound = 50 * 3**8 + 4 * 3**8 + 10
    a = signs(bound)
    p = prefix(a)
    # Check the digit-parity definition against the finite substitution iterate.
    w = '0'
    for k in range(9):
        assert len(w) == 3**k
        assert all((0 if a[j] == 1 else 1) == int(w[j]) for j in range(len(w)))
        checks += len(w)
        w = ''.join('001' if ch == '0' else '110' for ch in w)

    # Direct compare aligned-block sum identity, cube classification, and avoidance.
    for k in range(9):
        L = 3**k
        for q in range(50):
            for r in range(L):
                i = q * L + r
                P = p[r]
                for j in range(4):
                    block_sum = p[i + (j+1)*L] - p[i+j*L]
                    expected = (1-P)*a[q+j] + P*a[q+j+1]
                    assert block_sum == expected
                    checks += 1
                cube = (p[i+L] - p[i] == p[i+2*L] - p[i+L]
                        == p[i+3*L] - p[i+2*L])
                pred = (P == 0 and a[q] == a[q+1] == a[q+2]) or (
                    P == 1 and a[q+1] == a[q+2] == a[q+3])
                assert cube == pred
                four = (p[i+L] - p[i] == p[i+2*L] - p[i+L]
                        == p[i+3*L] - p[i+2*L]
                        == p[i+4*L] - p[i+3*L])
                assert not four
                checks += 2
    # Exact recurrence for prefix sums and density numerators.
    counts = recurrence_counts(8)
    assert counts == [1, 2, 5, 13, 35, 96, 267, 750, 2123]
    for k in range(9):
        L = 3**k
        cnt = sum(1 for r in range(L) if p[r] in (0, 1))
        assert cnt == counts[k]
        checks += L
    # The transition recursion and the precise start-of-triple-run rule.
    def trans(i):
        return int(a[i] != a[i+1])
    for n in range(50000):
        assert trans(3*n) + trans(3*n+1) + trans(3*n+2) == 2 - trans(n)
        assert (a[3*n+2] == a[3*n+3] == a[3*n+4]) == bool(trans(n))
        assert not (a[n] == a[n+1] == a[n+2] == a[n+3])
        checks += 3
    # An explicitly checked, nontriadic Abelian fourth power.
    witness = ['0100111', '0110110', '0011101', '1000111']
    assert [''.join('0' if x == 1 else '1' for x in a[37+7*j:44+7*j])
            for j in range(4)] == witness
    assert [sum(a[37+7*j:44+7*j]) for j in range(4)] == [-1]*4
    print('VERIFY_OK checks=', checks, 'density_numerators=', counts,
          'nontriadic_witness=(start=37,length=7,blocks=4)')


if __name__ == '__main__':
    main()
