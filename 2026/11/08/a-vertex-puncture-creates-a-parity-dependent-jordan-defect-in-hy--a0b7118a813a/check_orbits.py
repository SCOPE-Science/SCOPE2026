"""Independent full state enumeration for punctured-cube parity dynamics.

Finite experiments only: they are not used to prove the all-dimension theorem.
"""
from collections import Counter

def edges(d):
    return [[(i ^ (1 << k)) - 1 for k in range(d) if i ^ (1 << k)]
            for i in range(1, 1 << d)]


def update(x, adjacent, q):
    digits = []
    z = x
    for _ in adjacent:
        digits.append(z % q)
        z //= q
    new = 0
    power = 1
    for nbrs in adjacent:
        val = 0
        for u in nbrs:
            val ^= digits[u]  # XOR is GF(2^f) addition for a polynomial basis
        new += val * power
        power *= q
    return new


def exhaustive(d, q):
    adj = edges(d)
    n = len(adj)
    N = 1 << d
    bins = Counter()
    cycles = Counter()
    for x in range(q ** n):
        x1 = update(x, adj, q)
        x2 = update(x1, adj, q)
        x3 = update(x2, adj, q)
        if d % 2 == 0:
            assert x3 == 0
            t = next(k for k, val in enumerate((x, x1, x2, x3)) if val == 0)
            bins[t] += 1
        else:
            assert x3 == x1
            t = 0 if x2 == x else 1
            bins[t] += 1
            if not t:
                p = 1 if x1 == x else 2
                cycles[p] += 1
    if d % 2 == 0:
        assert [bins[t] for t in range(4)] == [1, q**(N//2-1)-1, q**(N-2)-q**(N//2-1), q**(N-1)-q**(N-2)]
        print('d=%d, q=%d, states=%d, exact first-zero counts=%s' % (d,q,q**n,[bins[t] for t in range(4)]))
    else:
        assert [bins[t] for t in range(2)] == [q**(N-2),(q-1)*q**(N-2)]
        assert [cycles[p] for p in (1,2)] == [q**(N//2-1),q**(N-2)-q**(N//2-1)]
        print('d=%d, q=%d, states=%d, entry counts=%s, periodic period counts=%s' % (d,q,q**n,[bins[t] for t in (0,1)],[cycles[p] for p in (1,2)]))


def main():
    for d,q in [(2,2),(3,2),(4,2),(2,4),(3,4)]:
        exhaustive(d,q)
    print('PASS: complete labelled-state checks in the five listed cases')

if __name__ == '__main__':
    main()
