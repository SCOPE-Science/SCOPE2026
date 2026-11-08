"""Independent exhaustive check of fixed-dinucleotide achiral-necklace formulas."""
from collections import defaultdict
from itertools import product
from math import comb, gcd


def c(n, k):
    return comb(n, k) if 0 <= k <= n and n >= 0 else 0


def phi(n):
    return sum(1 for j in range(1, n + 1) if gcd(j, n) == 1)


def f0(m, b):
    p = b // 2
    return c(m // 2 - 1, p - 1) if m % 2 == 0 else 0


def f2(m, b):
    p = b // 2
    if p == 1:
        return max(0, m - 1)
    return sum(c(j - 1, p - 2) * (m - 2*j - 1)
               for j in range(p - 1, (m - 2)//2 + 1))


def achiral(a, d, b):
    if b < 1 or min(a, d) < b:
        return 0
    if b % 2:
        p = (b - 1)//2
        return c((a-1)//2, p)*c((d-1)//2, p)
    q = f0(a, b)*f2(d, b) + f2(a, b)*f0(d, b)
    assert q % 2 == 0
    return q//2


def necklaces(a, d, b):
    h = gcd(gcd(a, d), b)
    return sum(phi(e)*c(a//e-1, b//e-1)*c(d//e-1, b//e-1)
               for e in range(1, h+1) if h%e == 0)//b


def canonical(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def check(max_length=17):
    comparisons = 0
    for n in range(2, max_length+1):
        seen = defaultdict(int)
        symmetric = defaultdict(int)
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            if w != canonical(w) or len(set(w)) < 2:
                continue
            a = w.count('0'); d = n-a
            b = sum(w[i] == '0' and w[(i+1)%n] == '1' for i in range(n))
            key = (a,d,b)
            seen[key] += 1
            symmetric[key] += int(canonical(w[::-1]) == w)
        for a in range(1, n):
            d=n-a
            for b in range(1, min(a,d)+1):
                key=(a,d,b)
                assert seen[key] == necklaces(a,d,b), ('necklaces', key)
                assert symmetric[key] == achiral(a,d,b), ('achiral', key)
                assert 0 <= symmetric[key] <= seen[key]
                assert (seen[key] - symmetric[key]) % 2 == 0
                if b % 2 == 0:
                    assert (symmetric[key] == 0) == (a % 2 == 1 and d % 2 == 1)
                else:
                    assert symmetric[key] > 0
                comparisons+=1
    return comparisons

if __name__ == '__main__':
    print(f'VERIFY_OK lengths=2..17 profiles={check()}')
