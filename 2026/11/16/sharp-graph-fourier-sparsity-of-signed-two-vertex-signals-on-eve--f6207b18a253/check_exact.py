"""Exact congruence enumeration of binary two-site path Fourier sparsity.
No numerical trigonometric zero tests are used. Requires Python 3.9+.
"""
from math import gcd


def predicted(n):
    if n % 2 == 0:
        q = n
        while q % 2 == 0:
            q //= 2
        count = n if q == 1 else (n // q) // 2
        return (n - q + 1) // 2, count
    p = next(k for k in range(3, n + 1, 2) if n % k == 0)
    return (n - n // p) // 2, (p - 1) // 2


def exact_zeros(n, u, v, sign):
    a, b = u + v + 1, v - u
    if sign == 1:
        return sum(((a * k) % (2 * n) == n) or
                   ((b * k) % (2 * n) == n) for k in range(n))
    return sum(((a * k) % (2 * n) == 0) or
               ((b * k) % (2 * n) == 0) for k in range(n))


def predicted_optimizers(n):
    result = set()
    for u in range(n // 2):
        v = n - 1 - u
        b = v - u
        if n % 2:
            p = next(k for k in range(3, n + 1, 2) if n % k == 0)
            if gcd(b // 2, n) == n // p:
                result.add((u, v, -1))
        else:
            q = n
            while q % 2 == 0:
                q //= 2
            if gcd(b, n) == q:
                result.add((u, v, 1))
                if q == 1:
                    result.add((u, v, -1))
    return result


def main():
    total_cases = 0
    for n in range(2, 81):
        optimum, number = predicted(n)
        winners = set()
        for u in range(n):
            for v in range(u + 1, n):
                for sign in (-1, 1):
                    total_cases += 1
                    support = n - exact_zeros(n, u, v, sign)
                    assert support >= optimum, (n, u, v, sign, support, optimum)
                    if support == optimum:
                        winners.add((u, v, sign))
        assert winners == predicted_optimizers(n), (n, winners)
        assert len(winners) == number, (n, number, len(winners))
    print('PASS: all path sizes 2..80; every candidate/minimum/optimizer; cases=', total_cases)


if __name__ == '__main__':
    main()
