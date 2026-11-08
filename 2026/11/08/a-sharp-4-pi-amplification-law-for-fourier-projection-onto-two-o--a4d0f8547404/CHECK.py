"""Direct finite Fourier check of the two-opposite-parabola projection theorem.
Run: python CHECK.py. The all-prime theorem is proved analytically in RESULT.md.
"""
import cmath
import math


def check_prime(p):
    assert p >= 5 and all(p % d for d in range(2, math.isqrt(p) + 1))
    e = lambda n: cmath.exp(2j * math.pi * (n % p) / p)
    points = {(x, (x * x) % p) for x in range(p)} | {(x, (-x * x) % p) for x in range(p)}
    assert len(points) == 2 * p - 1
    vals = [sum(e(u * a + v * b) for (a, b) in points) for u in range(p) for v in range(p)]
    direct = sum(abs(z) for z in vals) / (p * p)
    legendre = lambda t: 1 if pow(t % p, (p - 1) // 2, p) == 1 else -1
    trig = math.cos if p % 4 == 1 else math.sin
    b0 = 2 * (p - 1) * math.sqrt(p) if p % 4 == 1 else (p - 1)
    explicit = (3 * p - 2 + b0 + (p - 1) * sum(
        abs(2 * math.sqrt(p) * legendre(t) * trig(2 * math.pi * t / p) - 1)
        for t in range(1, p)
    )) / (p * p)
    assert abs(direct - explicit) < 1e-9, (p, direct, explicit)
    single_pts = {(x, x * x % p) for x in range(p)}
    single_direct = sum(abs(sum(e(u * a + v * b) for a, b in single_pts))
                        for u in range(p) for v in range(p)) / (p * p)
    assert abs(single_direct - (1 + (p - 1) * math.sqrt(p)) / p) < 1e-9
    ratio_direct = (sum(abs(z) for z in vals) / p) / math.sqrt(2 * p - 1)
    assert abs(ratio_direct - p * explicit / math.sqrt(2 * p - 1)) < 1e-9
    return p * p


def main():
    primes = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    tests = sum(check_prime(p) for p in primes)
    print(f"CHECK_OK primes={len(primes)} target_coefficients={tests} exact_formula=True")


if __name__ == "__main__":
    main()
