"""Exact cyclotomic Fourier test for proper three-colourings of cycles.

Arithmetic uses pairs (a,b) for a+b*omega with omega**2+omega+1=0.
This independent full-domain transform does not use the closed theorem formula
until the final comparison.
"""
from math import factorial


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def omega(x):
    a, b = x
    return -b, a - b


def omega2(x):
    a, b = x
    return b - a, -a


def digits_ternary(k, n):
    out = []
    for _ in range(n):
        out.append(k % 3)
        k //= 3
    return out


def theorem_frequency(b):
    n = len(b)
    if sum(b) % 3:
        return (0, 0)
    suffix = 0
    z = [1, 0, 0]  # The terminal increment has coefficient zero.
    for i in range(n - 1, 0, -1):
        suffix = (suffix + b[i]) % 3
        z[suffix] += 1
    return ((-1) ** n * sum((-2) ** k for k in z), 0)


def theorem_internal_zero_count(n):
    if n % 3 != 1:
        return 0
    a = (n - 1) // 3
    return factorial(n) // (factorial(a) ** 2 * factorial(a + 1))


def exact_transform(n):
    N = 3 ** n
    coefficients = []
    for k in range(N):
        x = digits_ternary(k, n)
        valid = all(x[i] != x[(i + 1) % n] for i in range(n))
        coefficients.append((int(valid), 0))
    stride = 1
    for axis in range(n):
        for base in range(0, N, 3 * stride):
            for t in range(stride):
                i = base + t
                p0, p1, p2 = coefficients[i], coefficients[i + stride], coefficients[i + 2 * stride]
                coefficients[i] = add(add(p0, p1), p2)
                coefficients[i + stride] = add(add(p0, omega(p1)), omega2(p2))
                coefficients[i + 2 * stride] = add(add(p0, omega2(p1)), omega(p2))
        stride *= 3
    return coefficients


def main():
    total = 0
    for n in range(3, 11):
        obs = exact_transform(n)
        zeros_inside = 0
        nonzero = 0
        for k, value in enumerate(obs):
            b = digits_ternary(k, n)
            expected = theorem_frequency(b)
            assert value == expected, (n, k, value, expected)
            if sum(b) % 3 == 0:
                if value == (0, 0):
                    zeros_inside += 1
                else:
                    nonzero += 1
                    assert value[0] % 3 == 0
        assert zeros_inside == theorem_internal_zero_count(n)
        assert nonzero == 3 ** (n - 1) - theorem_internal_zero_count(n)
        total += len(obs)
        print(f"n={n} Fourier coefficients={len(obs)} internal_zeros={zeros_inside} rank={nonzero}")
    print(f"TERNARY_CYCLE_FULL_FOURIER_PASS total_coefficients={total}")


if __name__ == "__main__":
    main()
