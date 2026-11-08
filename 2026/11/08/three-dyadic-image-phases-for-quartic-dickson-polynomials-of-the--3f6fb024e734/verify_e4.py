"""Independent finite-level checks for the quartic Dickson value-image theorem.

Uses the standard library only. It verifies all target multiplicities for
odd parameters 1,3,...,31 and moduli 2**k, 5 <= k <= 13.
"""
from collections import Counter


def e4(x, a, modulus):
    return (x**4 - 3*a*x*x + a*a) % modulus


def square_image_size(m):
    return len({x*x % (1 << m) for x in range(1 << m)})


def run():
    tested = 0
    for k in range(5, 14):
        modulus = 1 << k
        m = k - 4
        square_mod = 1 << m
        square_roots = Counter(x*x % square_mod for x in range(square_mod))
        for a in range(1, 32, 2):
            counts = Counter(e4(x, a, modulus) for x in range(modulus))
            b = -3*a
            first = a*a - 3*a + 1
            second = a*a - 12*a + 16
            for y in range(modulus):
                expected = 4*int((y-first) % 8 == 0)
                expected += 8*int((y-second) % 32 == 0)
                if (y-a*a) % 16 == 0:
                    root_target = (((y-a*a)//16)*pow(b, -1, square_mod)) % square_mod
                    expected += 4*square_roots[root_target]
                assert counts[y] == expected, (a, k, y, counts[y], expected)
                tested += 1
            B = 1 << (k-5)
            C = square_image_size(k-4)
            image_size = ((1 << (k-3)) +
                          (B + C if a % 8 in (1, 5)
                           else B if a % 8 == 3 else C))
            assert len(counts) == image_size, (a, k, len(counts), image_size)
    print(f'VERIFY_OK targets={tested} k=5..13 odd_parameters=1..31')


if __name__ == '__main__':
    run()
