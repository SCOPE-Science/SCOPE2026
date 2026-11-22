"""Independent brute-force check of finite cyclic majority preimage multiplicities."""
from collections import Counter

def image(bits):
    n = len(bits)
    return tuple(int(bits[(i-1) % n]+bits[i]+bits[(i+1) % n] >= 2)
                 for i in range(n))

def brute_singletons(n):
    fibers = Counter()
    for num in range(1 << n):
        input_bits = tuple((num >> i) & 1 for i in range(n))
        fibers[image(input_bits)] += 1
    return sum(value == 1 for value in fibers.values())

def main():
    expected = [2, 4, 0, 6, 20, 26, 28, 38, 108, 182, 242, 330,
                572, 1108, 1910, 2934]
    for n, count in enumerate(expected, 1):
        actual = brute_singletons(n)
        assert actual == count, (n, actual, count)
    print('PASS: independent cyclic input enumeration n=1..16')
    print('Counts:', expected)

if __name__ == '__main__':
    main()
