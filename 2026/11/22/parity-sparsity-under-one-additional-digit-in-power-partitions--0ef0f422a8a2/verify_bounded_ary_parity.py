#!/usr/bin/env python3
"""Recompute odd coefficient counts of base-b restricted power partitions.

The restricted-partition product is evaluated independently of the
finite-state parity transfer; no floating-point arithmetic is used.
"""
from fractions import Fraction


def product_coefficients(base, limit):
    a = [0] * limit
    a[0] = 1
    power = 1
    while power < limit:
        new = [0] * limit
        for n, v in enumerate(a):
            if v == 0:
                continue
            for j in range(base + 2):
                i = n + j * power
                if i >= limit:
                    break
                new[i] += v
        a = new
        power *= base
    return a


def parity_recursive(base, limit):
    out = [0] * limit
    out[0] = 1
    for n in range(1, limit):
        m, r = divmod(n, base)
        out[n] = (out[m] + (out[m-1] if m else 0)) % 2 if r <= 1 else out[m]
    return out


def matrix_counts(base, steps):
    x, y, z = 1, 0, 0
    result=[]
    for _ in range(steps+1):
        result.append(x+y)
        x, y, z = x+y, (base-1)*x+(base-3)*y+2*z, y+z
    return result


def gf_counts(base, steps):
    # (1+z-4z^2)/[(1-z)(1-(base-2)z-4z^2)]
    den = [1, -(base-1), base-6, 4]
    num = [1, 1, -4]
    terms=[]
    for i in range(steps+1):
        terms.append((num[i] if i < len(num) else 0)-sum(den[j]*terms[i-j] for j in range(1,min(i,len(den)-1)+1)))
    return terms


def main():
    checked=0
    for base in range(3,10):
        exponent = 4 if base >= 7 else 5
        limit=base**exponent
        coeff=product_coefficients(base,limit)
        par=parity_recursive(base,limit)
        assert all((c&1)==p for c,p in zip(coeff,par)), f'coefficient mismatch b={base}'
        matrix=matrix_counts(base,exponent)
        gf=gf_counts(base,exponent)
        assert matrix==gf, f'GF mismatch b={base}'
        for i in range(exponent+1):
            assert sum(par[:base**i])==matrix[i], f'level mismatch b={base} i={i}'
            checked += 1
        print(base, 'level_odd_counts',matrix)
    # The base-two endpoint is exactly b_{3,2}(n)=floor(n/2)+1.
    assert all(c == n//2 +1 for n,c in enumerate(product_coefficients(2,2048)))
    print('BOUNDED_POWER_PARITY_OK',checked)

if __name__ == '__main__':
    main()
