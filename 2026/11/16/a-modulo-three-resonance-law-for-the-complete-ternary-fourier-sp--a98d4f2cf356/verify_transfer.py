"""Independent integer transfer-matrix check of cycle-colouring Fourier spectra."""
from itertools import product
from math import factorial


def add(u, v):
    return (u[0] + v[0], u[1] + v[1], u[2] + v[2])


def shift(u, j):
    out = [0, 0, 0]
    for i, c in enumerate(u):
        out[(i + j) % 3] += c
    return tuple(out)


def transfer(n, k):
    # Accumulate counts in the exponent residue ring Z[t]/(t^3-1).
    total = (0, 0, 0)
    for start in range(3):
        state = [(0, 0, 0)] * 3
        state[start] = (1, 0, 0)
        for i in range(n):
            follow = [(0, 0, 0)] * 3
            for x in range(3):
                if not any(state[x]):
                    continue
                for y in range(3):
                    if x != y:
                        follow[y] = add(follow[y], shift(state[x], k[i] * x))
            state = follow
        total = add(total, state[start])
    # (c0,c1,c2) encodes c0+c1*omega+c2*omega^2.
    return total[0] - total[2], total[1] - total[2]


def target(n, k):
    if sum(k) % 3:
        return (0, 0)
    cumulative = 0
    hist = [0] * 3
    for ki in reversed(k):
        hist[cumulative] += 1
        cumulative = (cumulative + ki) % 3
    return (-1) ** n * sum((-2) ** h for h in hist), 0


def main():
    for n in range(3, 8):
        zeros = 0
        for k in product(range(3), repeat=n):
            t = transfer(n, k)
            f = target(n, k)
            assert t == f, (n, k, t, f)
            if t == (0, 0) and sum(k) % 3 == 0:
                zeros += 1
        a = (n - 1) // 3
        expected = factorial(n) // (factorial(a + 1) * factorial(a)**2) if n % 3 == 1 else 0
        assert zeros == expected
        print(f'n={n} transfer agree; exceptional balanced zeros={zeros} OK')


if __name__ == '__main__':
    main()
