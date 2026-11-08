"""Exact finite-state replay for three-state excitation on two matched cliques.

Run: python3 verify_dynamics.py
All state arrays use the labelled order (top 0,...,n-1; bottom 0,...,n-1).
"""
from itertools import product


def step(x, n):
    y = [0] * (2 * n)
    for row in (0, 1):
        start = row * n
        other = (1 - row) * n
        any_excited = sum(x[start + i] == 1 for i in range(n))
        for i in range(n):
            c = x[start + i]
            if c == 0:
                y[start + i] = int(any_excited > 0 or x[other + i] == 1)
            elif c == 1:
                y[start + i] = 2
            else:
                y[start + i] = 0
    return tuple(y)


def predicted(n):
    return 9**n - 6 * 6**n + 15 * 4**n - 12 * 3**n + 3


def successor_valid(x, n):
    for row in (0, 1):
        sl = x[row * n:(row + 1) * n]
        other = x[(1 - row) * n:(2 - row) * n]
        for i, c in enumerate(sl):
            successor = (c + 1) % 3
            if successor not in sl and other[i] != successor:
                return False
    return True


def main():
    checked = 0
    for n in range(2, 7):
        count = 0
        for x in product(range(3), repeat=2 * n):
            y = step(x, n)
            z = step(y, n)
            w = step(z, n)
            period_three = w == x and y != x
            local = successor_valid(x, n)
            assert period_three == local, (n, x, y, z, w, local)
            count += period_three
            checked += 1
        assert count == predicted(n), (n, count, predicted(n))
        print(f"n={n} states={3**(2*n)} primitive_three={count} predicted={predicted(n)}")
    print(f"PASS dynamics and local criterion: {checked} states")


if __name__ == '__main__':
    main()
