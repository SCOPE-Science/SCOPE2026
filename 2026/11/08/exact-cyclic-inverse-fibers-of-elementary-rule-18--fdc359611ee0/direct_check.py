"""Direct finite enumeration of one-step preimages for elementary Rule 18."""
from collections import Counter


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


def predicted(y, n):
    sites = [i for i in range(n) if (y >> i) & 1]
    if not sites:
        return lucas(n) + 1
    if len(sites) % 2:
        return 0
    gaps = [(sites[(i + 1) % len(sites)] - sites[i] - 1) % n
            for i in range(len(sites))]
    result = 0
    for parity in (0, 1):
        product = 1
        for j in range(parity, len(gaps), 2):
            product *= fibonacci(gaps[j])
        result += product
    return result


def update(x, n):
    mask = (1 << n) - 1
    left = ((x << 1) | (x >> (n - 1))) & mask
    right = (x >> 1) | ((x & 1) << (n - 1))
    return (left ^ right) & (~x) & mask


def main():
    for n in range(1, 19):
        cnt = Counter(update(x, n) for x in range(1 << n))
        for y in range(1 << n):
            assert predicted(y, n) == cnt.get(y, 0), (n, y)
        assert cnt[0] == max(cnt.values()), n
        assert sum(c == cnt[0] for c in cnt.values()) == 1, n
    print('DIRECT_OK: all indexed inputs and all output labels for n=1..18')


if __name__ == '__main__':
    main()
