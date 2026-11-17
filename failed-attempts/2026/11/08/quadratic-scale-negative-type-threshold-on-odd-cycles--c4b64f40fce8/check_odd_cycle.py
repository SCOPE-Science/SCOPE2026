#!/usr/bin/env python3
"""Independent finite-frequency checks of the odd-cycle asymptotic theorem.
Uses only the Python standard library. Numerical checks are not used as proof.
"""
import math


def eigen(n, j, p):
    m = (n - 1) // 2
    return 2 * math.fsum((r ** p) * math.cos(2 * math.pi * j * r / n) for r in range(1, m + 1))


def exact_base(n, j):
    x = math.pi * j / (2*n)
    return -1 / (4*(math.cos(x)**2 if j % 2 == 0 else math.sin(x)**2))


def root(n, j):
    lo, hi = 1., 1.6
    if eigen(n,j,hi) <= 0:
        return float('inf')
    for _ in range(55):
        mid=(lo+hi)/2
        if eigen(n,j,mid)>0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def roundness_root(n):
    # Horak--LaRose--Moore--Rooney--Rosenthal's known four-point formula.
    k=(n-1)//4 if n % 4 == 1 else (n+1)//4
    lhs=2*k if n%4==1 else 2*k-1
    other=k+1 if n%4==1 else k-1
    def diff(p):
        return 2*(lhs/k)**p - 3 - (other/k)**p
    lo,hi=1.,2.
    for _ in range(60):
        mid=(lo+hi)/2
        if diff(mid)>0: hi=mid
        else:lo=mid
    return (lo+hi)/2


def integral_simpson(f, a, b, steps=100000):
    assert steps % 2 == 0
    h=(b-a)/steps
    v=f(a)+f(b)
    v+=4*sum(f(a+i*h) for i in range(1,steps,2))
    v+=2*sum(f(a+i*h) for i in range(2,steps,2))
    return v*h/3


def main():
    I2=2*integral_simpson(lambda x: x*math.log(x)*math.cos(4*math.pi*x) if x else 0.,0.,.5)
    c=.25/I2
    assert abs(c-8.0976273569)<1e-7
    print('asymptotic_constant=%.11f'%c)
    for n in [5,7,9,11,21,51,101,201]:
        m=(n-1)//2
        baseerr=max(abs(eigen(n,j,1)-exact_base(n,j)) for j in range(1,m+1))
        assert baseerr<4e-9, (n,baseerr)
        roots=[(root(n,j),j) for j in range(1,m+1)]
        crit,j=min(roots)
        assert j==2, (n,crit,j)
        rho=roundness_root(n)
        assert rho>crit
        print('N=%d first_mode=%d critical_p=%.12f scaled_gap=%.8f fourpoint_p=%.10f base_error=%.2g'%(n,j,crit,n*n*(crit-1),rho,baseerr))
    print('ODD_CYCLE_NEGATIVE_TYPE_FINITE_CHECKS_OK')

if __name__=='__main__': main()
