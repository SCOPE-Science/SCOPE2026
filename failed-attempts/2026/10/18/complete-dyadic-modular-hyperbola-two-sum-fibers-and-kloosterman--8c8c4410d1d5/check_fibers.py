"""Exact integer checks for two-sum fibers of modular inverse graphs."""
from collections import Counter
from cmath import exp
from math import pi


def square_root_count(m, d):
    modulus = 1 << m
    d %= modulus
    if d == 0:
        return 1 << (m // 2)
    val = (d & -d).bit_length() - 1
    if val & 1:
        return 0
    j = val // 2
    ell = m - 2 * j
    unit = d >> (2 * j)
    if ell == 1:
        odd_roots = 1
    elif ell == 2:
        odd_roots = 2 if unit % 4 == 1 else 0
    else:
        odd_roots = 4 if unit % 8 == 1 else 0
    return (1 << j) * odd_roots


def predicted(k, s, z):
    modulus = 1 << k
    s %= modulus
    z %= modulus
    if s == 0:
        return (1 << (k - 1)) if z == 0 else 0
    if s & 1 or z == 0:
        return 0
    a = (s & -s).bit_length() - 1
    if (z & -z).bit_length() - 1 != a:
        return 0
    m = k - a
    t = s // 2
    u = s >> a
    v = z >> a
    d = (t * t - u * pow(v, -1, 1 << m)) % (1 << m)
    return (1 << a) * square_root_count(m, d)


def expected_energy(k):
    if k == 2:
        return 8
    if k == 3:
        return 64
    return 6 * (k - 3) * (1 << (2 * k - 2))


def check(k):
    modulus = 1 << k
    units = range(1, modulus, 2)
    inverse = {u: pow(u, -1, modulus) for u in units}
    actual = Counter(((x+y) % modulus,
                      (inverse[x]+inverse[y]) % modulus)
                     for x in units for y in units)
    assert sum(actual.values()) == (modulus//2)**2
    for s in range(modulus):
        for z in range(modulus):
            assert predicted(k, s, z) == actual.get((s,z), 0), (k,s,z)
    energy = sum(v*v for v in actual.values())
    assert energy == expected_energy(k), (k, energy)
    if k >= 4:
        assert modulus**2 * energy // (modulus//2)**4 == 24 * (k-3)
    return len(actual), energy, dict(sorted(Counter(actual.values()).items()))


if __name__ == '__main__':
    count = 0
    for k in range(2, 11):
        support, energy, histogram = check(k)
        print(f'k={k} support={support} energy={energy} fibers={histogram}')
        count += (1 << k)**2
    # Direct complex Fourier fourth moments for the two smallest nontrivial levels.
    for k in (2, 3, 4, 5):
        modulus = 1 << k
        units = list(range(1, modulus, 2))
        ks = [[sum(exp(2j*pi*(u*x + v*pow(x,-1,modulus))/modulus)
                   for x in units) for v in range(modulus)]
              for u in range(modulus)]
        fourth = sum(abs(w)**4 for row in ks for w in row)
        target = modulus*modulus*expected_energy(k)
        assert abs(fourth-target) < 1.e-7 * max(1., target)
    print(f'VERIFY_OK exact_fiber_positions={count} exponents=2..10 direct_complex_fourth_moments=4')
