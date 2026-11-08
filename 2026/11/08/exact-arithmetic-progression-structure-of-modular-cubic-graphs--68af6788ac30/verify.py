"""Exact checks of four-term progressions in modular cubic graphs.
Run: python3 verify.py
"""
from math import gcd, prod


def factors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            k = 0
            while n % p == 0:
                n //= p
                k += 1
            out.append((p, k))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def ordinary_local(p, k):
    if k == 0:
        return 1
    r = (k + 1) // 2
    s = (k + 2) // 3
    return p ** (2 * k - r) + p ** (k + r - 1) - p ** (k + s - 1)


def local_count(p, k):
    return p * p * ordinary_local(p, k - 1) if p in (2, 3) else ordinary_local(p, k)


def predicted_count(n):
    return prod(local_count(p, k) for p, k in factors(n))


def predicted_max_order(n):
    return prod(p ** (k - max(0, (k - int(p in (2, 3)) + 2) // 3)) for p, k in factors(n))


def is_progression(x, h, n):
    # Second differences of the cubic coordinate at indices zero and one.
    return (6 * h * h * x) % n == 0 and (6 * h * h * h) % n == 0


def actual_points_are_AP(x, h, n, length):
    xvec = [((x+j*h) % n, pow(x+j*h, 3, n)) for j in range(length)]
    return all(((xvec[j][0]-2*xvec[j+1][0]+xvec[j+2][0]) % n == 0 and
                (xvec[j][1]-2*xvec[j+1][1]+xvec[j+2][1]) % n == 0)
               for j in range(length - 2))


number_of_checked_pairs = 0
number_of_checked_extensions = 0
for n in range(1, 91):
    good = 0
    max_order = 1
    for h in range(n):
        if (6*h*h*h) % n == 0:
            max_order = max(max_order, n // gcd(n, h))
        for x in range(n):
            valid = is_progression(x, h, n)
            good += valid
            assert valid == actual_points_are_AP(x, h, n, 4), (n, x, h)
            if valid and n <= 30:
                assert actual_points_are_AP(x, h, n, 9), (n, x, h)
                number_of_checked_extensions += 1
            number_of_checked_pairs += 1
    assert good == predicted_count(n), (n, good, predicted_count(n))
    assert max_order == predicted_max_order(n), (n, max_order, predicted_max_order(n))

for p in (2, 3, 5, 7, 11, 13):
    for k in range(1, 9):
        eps = int(p in (2, 3))
        lower = max(0, (k - eps + 2) // 3)
        direct = p**k
        for s in range(lower, k):
            direct += (p-1)*p**(k-s-1 + min(k, eps+2*s))
        assert direct == local_count(p, k), (p, k, direct, local_count(p, k))

print('VERIFY_OK exact_moduli=1..90')
print('full_pair_tests=' + str(number_of_checked_pairs))
print('length_9_extensions=' + str(number_of_checked_extensions))
print('symbolic_local_sum_cases=48')
