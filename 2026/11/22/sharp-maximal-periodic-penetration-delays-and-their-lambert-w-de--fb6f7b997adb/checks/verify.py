#!/usr/bin/env python3
"""Exact integer and independent finite-word checks for modular-gap periodic penetration.
The exhaustive tests establish only finite cases; the universal assertions use the proof.
No external packages are required.
"""
from decimal import Decimal, localcontext
from itertools import product


def valid_word(w, mod):
    ones = [i for i, a in enumerate(w) if a == '1']
    return all((b - a - 1) % mod == 0 for a, b in zip(ones, ones[1:]))


def cyclic_valid(v, mod):
    ones = [i for i, a in enumerate(v) if a == '1']
    if not ones:
        return True
    gaps = [b - a - 1 for a, b in zip(ones, ones[1:])]
    gaps.append(ones[0] + len(v) - ones[-1] - 1)
    return all(g % mod == 0 for g in gaps)


def penetration(w, mod):
    n = len(w)
    for p in range(1, n + mod):
        if p <= n:
            v = w[:p]
            if not all(w[i] == v[i % p] for i in range(n)):
                continue
            if cyclic_valid(v, mod):
                return p
        else:
            for bits in product('01', repeat=p - n):
                if cyclic_valid(w + ''.join(bits), mod):
                    return p
    raise AssertionError('missing guaranteed extension')


def unbordered(w):
    return all(w[:k] != w[-k:] for k in range(1, len(w)))


def coefficient_arrays(mod, limit):
    # A(z)=z^2/(1-z-z^mod), H(z)=z^(mod-1)/(1-z-z^mod).
    a, h, u = [0] * (limit + 1), [0] * (limit + 1), [0] * (limit + 1)
    a[2] = 1
    h[mod - 1] = 1
    for n in range(3, limit + 1):
        a[n] = a[n - 1] + (a[n - mod] if n >= mod else 0)
    for n in range(mod, limit + 1):
        h[n] = h[n - 1] + (h[n - mod] if n >= mod else 0)
    for n in range(2, limit + 1):
        u[n] = a[n] - sum(u[k] * h[n - 2 * k] for k in range(2, n // 2 + 1))
        assert u[n] > 0
    # Check all 300 exact coefficients of D(z)U(z)+z^(mod-1)U(z^2)=z^2.
    for n in range(limit + 1):
        lhs = u[n] - (u[n - 1] if n >= 1 else 0) - (u[n - mod] if n >= mod else 0)
        if n >= mod - 1 and (n - (mod - 1)) % 2 == 0:
            lhs += u[(n - mod + 1) // 2]
        assert lhs == (1 if n == 2 else 0), (mod, n, lhs)
    return a, h, u


def check_exhaustive():
    checks = 0
    for mod, max_n in [(2, 15), (3, 14), (4, 13), (5, 12), (6, 11)]:
        a, h, u = coefficient_arrays(mod, 300)
        for n in range(2, max_n + 1):
            admissible = (''.join(bits) for bits in product('01', repeat=n))
            words = [w for w in admissible if valid_word(w, mod)]
            selected = [w for w in words if penetration(w, mod) == n + mod - 1]
            oriented = [w for w in words if w.startswith('1') and w.endswith('0')
                        and (len(w) - len(w.rstrip('0'))) % mod == 1 and unbordered(w)]
            assert len(selected) == 2 * len(oriented) == 2 * u[n], (mod, n)
            assert all(unbordered(w) for w in selected), (mod, n)
            checks += len(words)
        print('modulus', mod, 'exhaustive through length', max_n,
              'example U[2..12]', u[2:13])
    print('admissible words whose minimum periods were exhaustively checked:', checks)


def U_at(z, mod):
    # With z<r^2, 40-bit-decimal convergence is very rapid under z->z^2.
    if z < Decimal('1e-35'):
        return z * z / (Decimal(1) - z - z ** mod)
    return (z*z - z ** (mod - 1) * U_at(z*z, mod)) / (Decimal(1)-z-z**mod)


def check_limits():
    with localcontext() as ctx:
        ctx.prec = 65
        for mod, expected in [(2, '0.1556298471279'), (3, '0.1070346578975'),
                              (4, '0.0801050893612'), (5, '0.0631438074423')]:
            low, high = Decimal(0), Decimal(1)
            for _ in range(270):
                r = (low + high) / 2
                if 1 - r - r ** mod > 0:
                    low = r
                else:
                    high = r
            r = (low + high) / 2
            delta = 1 - r
            p_direct = 2 * delta**2 * (1-r**(mod-3)*U_at(r*r,mod))
            p_reduced = delta**2 * (1 + delta**2 * U_at(r**4,mod)/r**6)
            assert abs(p_direct-p_reduced) < Decimal('1e-50'), (mod, p_direct, p_reduced)
            assert abs(p_direct-Decimal(expected))<Decimal('2e-13')
            assert delta**2 < p_direct < delta**2 * (1+delta**2*r*r/(1-r**4-r**(4*mod)))
            print('modulus', mod, 'limiting maximal-delay probability', str(+p_direct)[:28])


if __name__ == '__main__':
    check_exhaustive()
    check_limits()
    print('ALL CHECKS PASS')
