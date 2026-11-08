"""Exact independent checks for cyclic graphical EFX orientations.
Run using Python 3 standard library: python verify.py
"""
from fractions import Fraction
from itertools import product


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def correction(n):
    return (1, 1, 0, -1, -1, 0)[n % 6]


def expected(n, special):
    if special == 1:
        return lucas(n) + (2, 1, -1, -2, -1, 1)[n % 6]
    return fibonacci(n + 1) + correction(n)


def efx_direct(n, bits, weights):
    """Inspect every ordered agent pair and every removal, not a local EFX lemma."""
    owned = [[] for _ in range(n)]
    for i, forward in enumerate(bits):
        head = (i + 1) % n if forward else i
        owned[head].append(i)

    def utility(agent, edges):
        return sum((weights[e] for e in edges
                    if e == agent or (e + 1) % n == agent), Fraction(0))

    for i in range(n):
        own = utility(i, owned[i])
        for j in range(n):
            for removed in owned[j]:
                if own < utility(i, (e for e in owned[j] if e != removed)):
                    return False
    return True


def efx_local(n, bits, weights):
    """Independent edge-tail/head criterion used to check the derived lemma."""
    indegree = [0] * n
    own = [Fraction(0)] * n
    ends = []
    for i, forward in enumerate(bits):
        tail, head = (i, (i + 1) % n) if forward else ((i + 1) % n, i)
        ends.append((tail, head))
        indegree[head] += 1
        own[head] += weights[i]
    return all(indegree[head] < 2 or own[tail] >= weights[i]
               for i, (tail, head) in enumerate(ends))


def no_singletons(bits):
    n = len(bits)
    return all(not (bits[(i - 1) % n] == bits[(i + 1) % n]
                    and bits[i] != bits[(i - 1) % n])
               for i in range(n))


def defect_predicate(bits, special):
    n = len(bits)
    if not no_singletons(bits):
        return False
    if special == 1:
        return True
    if special > 1:
        return (not bits[0] or bits[1]) and (bits[0] or not bits[-1])
    return not (bits[1] and not bits[2]) and not (bits[-2] and not bits[-1])


def transfer_counts(n):
    states = ((0,0),(0,1),(1,0),(1,1))
    T = [[0]*4 for _ in range(4)]
    for i,(a,b) in enumerate(states):
        for c in (0,1):
            if not (a == c and a != b):
                T[i][states.index((b,c))] = 1
    P = [[int(i==j) for j in range(4)] for i in range(4)]
    for _ in range(n):
        P = [[sum(P[i][k]*T[k][j] for k in range(4))
              for j in range(4)] for i in range(4)]
    return sum(P[i][i] for i in range(4)), 2*P[3][3]


def main():
    orientations_checked = 0
    for n in range(3, 14):
        for special in (Fraction(1,2), Fraction(3,4),
                        Fraction(1), Fraction(5,4), Fraction(2)):
            weights = [special] + [Fraction(1)]*(n-1)
            actual = 0
            for bits in product((0,1), repeat=n):
                direct = efx_direct(n,bits,weights)
                local = efx_local(n,bits,weights)
                patterns = defect_predicate(bits,special)
                assert direct == local == patterns, (n,special,bits,direct,local,patterns)
                actual += direct
                orientations_checked += 1
            assert actual == expected(n,special), (n,special,actual,expected(n,special))
        homog, defect = transfer_counts(n)
        assert homog == expected(n,1)
        assert defect == expected(n,Fraction(2))
        print(f'n={n}: uniform={homog}; nonunit={defect}')
    for n in range(3, 101):
        homog, defect = transfer_counts(n)
        assert homog == expected(n,1) and defect == expected(n,Fraction(2))
    print(f'VERIFY_OK direct_efx_orientations={orientations_checked} counts_cases={11*5} matrix_cases=98')

if __name__ == '__main__':
    main()
