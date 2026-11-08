"""Independent part-count implementation and binomial-tail census. Python 3 stdlib."""
from math import comb, asin, pi, sqrt


def part_step(state, sizes):
    total = sum(state)
    N = sum(sizes)
    return tuple(0 if 2 * (total - x) < N - sz else
                 sz if 2 * (total - x) > N - sz else x
                 for x, sz in zip(state, sizes))


def closed_count(n):
    m = n + 1
    pref = [0]
    for j in range(m + 1):
        pref.append(pref[-1] + comb(m, j))
    def tail(lo, hi):
        return pref[hi + 1] - pref[lo] if lo <= hi else 0
    result = 0
    for a in range(n + 1):
        for b in range(n + 1):
            w = comb(n, a) * comb(n, b)
            if a + b < n:
                result += 2 * w * tail(n + 1 - min(a, b), m)
            elif a + b == n:
                result += w * tail(min(a, b) + 1, max(a, b))
    return result


def direct_count(n):
    sizes = (n, n, n + 1)
    basin = 0
    already_two = 0
    for a in range(n + 1):
        for b in range(n + 1):
            for c in range(n + 2):
                x = (a, b, c)
                y = part_step(x, sizes)
                z = part_step(y, sizes)
                w = part_step(z, sizes)
                assert part_step(w, sizes) == z, (n, x, y, z, w)
                weight = comb(n, a)*comb(n, b)*comb(n+1, c)
                if z != w:
                    basin += weight
                if x != y and part_step(y, sizes) == x:
                    already_two += weight
    return basin, already_two


def phi(lam):
    return .25 + (asin(lam / (1 + lam)) - 2 * asin(1 / sqrt(2 * (1 + lam)))) / (2 * pi)


def run():
    for n in range(1, 21):
        ans, periodic = direct_count(n)
        closed = closed_count(n)
        assert ans == closed
        assert periodic == (1 << (n + 2)) - 2
        print(f'n={n}: total={1<<(3*n+1)}, basin={ans}, periodic={periodic}, identity=OK')
    for n in (30, 50, 100, 200):
        ans = closed_count(n)
        print(f'n={n}: probability={ans / 2**(3*n+1):.12f}')
    print(f'Phi(1)={phi(1):.12f}, Phi(2)={phi(2):.12f}, Phi(10)={phi(10):.12f}')
    assert abs(phi(1) - 1 / 6) < 1e-14


if __name__ == '__main__':
    run()
