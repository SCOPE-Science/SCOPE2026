#!/usr/bin/env python3
"""Independent finite checks for radial Cantor localization.

Checks exact rational interval-occupancy inequalities for finite stages;
compares Poisson-Gamma integral eigenvalues to the proposed sharp norm.
The general theorem is proved analytically in RESULT.md, not by this script.
Requires Python 3.10+ standard library only.
"""
from decimal import Decimal, localcontext


def cantor_digits(n):
    L = 3 ** n
    bits = []
    for i in range(L):
        j = i
        good = True
        for _ in range(n):
            if j % 3 == 1:
                good = False
                break
            j //= 3
        bits.append(int(good))
    return bits


def intervals(n, x):
    bits = cantor_digits(n)
    length = x / Decimal(3**n)
    return [(Decimal(i) * length, Decimal(i + 1) * length)
            for i, b in enumerate(bits) if b]


def poisson_cdf_mass(k, t):
    # gamma(k+1,1) integrated from 0 to t
    total = Decimal(1)
    a = Decimal(1)
    for j in range(1, k+1):
        a *= t / Decimal(j)
        total += a
    return Decimal(1) - (-t).exp() * total


def eigenvalue(k, ints):
    return sum((poisson_cdf_mass(k, b)-poisson_cdf_mass(k, a)
                for a,b in ints), Decimal(0))


def vacuum_product(n, x):
    result = Decimal(1) - (-x / Decimal(3**n)).exp()
    for j in range(1, n+1):
        result *= Decimal(1) + (-Decimal(2)*x/Decimal(3**j)).exp()
    return result


def main():
    occupancy = 0
    for n in range(0,7):
        bits = cantor_digits(n)
        prefix=[0]
        for b in bits:
            prefix.append(prefix[-1]+b)
        L=len(bits)
        for i in range(L+1):
            for j in range(L+1):
                assert prefix[i]+prefix[j]>=prefix[min(i+j,L)], (n,i,j)
                occupancy+=1
    eigen_checks=0
    product_checks=0
    gap_checks=0
    with localcontext() as ctx:
        ctx.prec=75
        tol=Decimal('1e-48')
        for n in range(0,7):
            for x_str in ('0.3','1','3.7','15'):
                x=Decimal(x_str)
                ints=intervals(n,x)
                lam0=eigenvalue(0,ints)
                p=vacuum_product(n,x)
                assert abs(lam0-p)<tol,(n,x,'product',lam0,p)
                product_checks+=1
                for k in range(1,33):
                    lk=eigenvalue(k,ints)
                    assert lk < lam0, (n,x,k,'strict',lk,lam0)
                    eigen_checks+=1
                    # Explicit quantitative gap, derived from the Gamma(k,1) tail.
                    tail=(-x).exp()*sum((x**j/Decimal(__import__('math').factorial(j)) for j in range(k)),Decimal(0))
                    assert lam0-lk+tol>=lam0*tail,(n,x,k,'gap')
                    gap_checks+=1
    print('PASS',f'occupancy_exact={occupancy}',f'product={product_checks}',
          f'strict_spectrum={eigen_checks}',f'quantitative_gap={gap_checks}')

if __name__=='__main__':
    main()
