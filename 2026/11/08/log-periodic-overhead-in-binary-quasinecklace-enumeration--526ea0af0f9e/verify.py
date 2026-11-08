"""Reproducible finite checks for binary quasinecklace counting and its asymptotic phase."""
from itertools import product
from math import log2, exp


def direct_quasinecklace(w):
    if len(set(w)) == 1:
        return True
    if w[-1] != '1':
        return False
    max_run = 0
    current = 0
    for c in w:
        current = current + 1 if c == '0' else 0
        max_run = max(max_run, current)
    return w.startswith('0' * max_run)


def count_compositions(total, largest_part):
    ways = [0] * (total + 1)
    ways[0] = 1
    rolling_sum = 1
    for t in range(1, total + 1):
        ways[t] = rolling_sum
        rolling_sum += ways[t]
        if t >= largest_part:
            rolling_sum -= ways[t - largest_part]
    return ways[-1]


def count_by_compositions(n):
    return 2 + sum(count_compositions(n - ell - 1, ell + 1)
                   for ell in range(1, n)) if n >= 1 else 0


def count_by_zero_run_automata(n):
    total = 2
    for ell in range(1, n):
        trailing = [0] * (ell + 1)
        trailing[0] = 1
        t = n - ell - 1
        for _ in range(t):
            nxt = [0] * (ell + 1)
            nxt[0] = sum(trailing)
            for k in range(ell):
                nxt[k + 1] = trailing[k]
            trailing = nxt
        total += trailing[0] if t else 1
    return total


def phase(theta):
    return sum((2.0 ** (theta - j - 2)) * exp(-2.0 ** (theta - j - 2))
               for j in range(-50, 60))


def main():
    for n in range(1, 17):
        direct = sum(direct_quasinecklace(''.join(bits))
                     for bits in product('01', repeat=n))
        via_comp = count_by_compositions(n)
        via_automata = count_by_zero_run_automata(n)
        assert direct == via_comp == via_automata, (n, direct, via_comp, via_automata)
    print('direct_membership_and_independent_automata: lengths 1..16 OK')
    for n in (32, 64, 128, 256, 512, 1024):
        q = count_by_compositions(n)
        ratio = n * q / 2**n
        predicted = phase(log2(n) % 1)
        assert abs(ratio - predicted) < 1.0/n, (n, ratio, predicted)
        print(f'n={n}: n*Q/2^n={ratio:.12f}, phase={predicted:.12f}')
    for theta in (0.0, 0.25, 0.5, 0.75):
        assert 1.4426 < phase(theta) < 1.4428
    print('BINARY_QUASINECKLACE_ASYMPTOTIC_VERIFY_OK')


if __name__ == '__main__':
    main()
