"""Exact direct enumeration of proper ternary cycle colourings and Fourier coefficients."""
from itertools import product
from math import factorial


def predicted(n, frequency):
    if sum(frequency) % 3:
        return (0, 0)
    suffix = 0
    b = [0] * n
    for i in range(n - 1, -1, -1):
        b[i] = suffix
        suffix = (suffix + frequency[i]) % 3
    counts = [b.count(t) for t in range(3)]
    v = (-1) ** n * sum((-2) ** c for c in counts)
    return (v, 0)


def exact_direct(n, frequency, colourings):
    # In the Eisenstein ring: 1=(1,0), omega=(0,1), omega^2=(-1,-1).
    values = ((1, 0), (0, 1), (-1, -1))
    x = y = 0
    for colouring in colourings:
        exponent = sum(a * b for a, b in zip(colouring, frequency)) % 3
        dx, dy = values[exponent]
        x += dx
        y += dy
    return (x, y)


def resonance_count(n):
    if n % 3 != 1:
        return 0
    a = (n - 1) // 3
    return factorial(n) // (factorial(a + 1) * factorial(a) ** 2)


def main():
    for n in range(3, 8):
        colours = [x for x in product(range(3), repeat=n)
                   if all(x[i] != x[(i + 1) % n] for i in range(n))]
        assert len(colours) == 2 ** n + 2 * (-1) ** n
        nonzero = zeros_balance = 0
        for k in product(range(3), repeat=n):
            direct = exact_direct(n, k, colours)
            formula = predicted(n, k)
            assert direct == formula, (n, k, direct, formula)
            nonzero += (direct != (0, 0))
            zeros_balance += (sum(k) % 3 == 0 and direct == (0, 0))
        assert zeros_balance == resonance_count(n), (n, zeros_balance)
        assert nonzero == 3 ** (n - 1) - resonance_count(n)
        print(f'n={n} proper={len(colours)} extra_zeros={zeros_balance} rank={nonzero} OK')


if __name__ == '__main__':
    main()
