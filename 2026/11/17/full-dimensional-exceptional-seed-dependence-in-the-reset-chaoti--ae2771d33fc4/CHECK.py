#!/usr/bin/env python3
"""Independent finite consistency checks for the logistic-map reset identity.
The infinite-time and Hausdorff-dimension arguments are proved in RESULT.md.
Uses only the Python standard library.
"""
from fractions import Fraction
from math import sin, pi, log, sqrt, isclose


def seed_with_prescribed_blocks(blocks, N=156):
    assert N > max(k+L+3 for k,L in blocks)
    b = [None] * N
    b[:3] = list('001')
    for k,L in blocks:
        assert k > 3
        for p in range(k+1,k+L+1):
            assert b[p-1] in (None,'0')
            b[p-1] = '0'
        for i,z in enumerate('010'):
            p = k+L+1+i
            assert b[p-1] in (None,z)
            b[p-1] = z
    for i in range(N):
        if b[i] is None:
            b[i] = '0' if i%2 else '1'
    # Periodic tail 010101... is exactly 1/3 after digit N, avoiding dyadic seeds.
    return Fraction(3*int(''.join(b),2)+1,3*(1<<N))


def phase_frac(t,m):
    return (t*(1<<m)) % 1


def bn(t,m):
    frac=phase_frac(t,m)
    z=min(frac,1-frac)  # exact reduction avoids loss near the sine zeros
    return abs(sin(2*pi*float(z)))


def reset_suscept(t,r,n):
    q=1-r
    R=2*q
    c=bn(t,0)
    return (r*sum(R**m*bn(t,m) for m in range(n)) + R**n*bn(t,n))/c


def verify():
    tested=0
    # Logistic/doubling conjugacy and exact derivatives (finite floating checks).
    for t in [Fraction(11,97),Fraction(29,101),Fraction(17,91)]:
        x=sin(pi*float(t))**2
        der=1.
        for m in range(0,10):
            expected=2**m*bn(t,m)/bn(t,0)
            assert isclose(abs(der),expected,rel_tol=2e-7,abs_tol=1e-7), (m,der,expected)
            der*=4*(1-2*x)
            x=4*x*(1-x)
            tested+=1
    # All 2^n reset histories for n<=8 (no stochastic approximations).
    t=Fraction(11,97)
    for n in range(1,9):
        r=.21; q=1-r; total=0.
        for mask in range(1<<n):
            last=0; prob=1.
            for j in range(n):
                if (mask>>j)&1:
                    prob*=r; last=j+1
                else:
                    prob*=q
            m=n-last
            total+=prob*2**m*bn(t,m)/bn(t,0)
        assert isclose(total,reset_suscept(t,r,n),rel_tol=2e-12)
        tested+=1
    # Exact rational arithmetic certifies every finite zero-block digit bound.
    t=seed_with_prescribed_blocks([(16,16),(80,40)])
    assert Fraction(1,8)<t<Fraction(1,4)
    for k,L in [(16,16),(80,40)]:
        for m in range(k,k+L//2+1):
            assert phase_frac(t,m)<=Fraction(1,1<< (k+L-m))
            assert bn(t,m)<=2*pi*2**(m-k-L)*(1+1e-12)
            tested+=1
        f=phase_frac(t,k+L)
        assert Fraction(1,4)<=f<=Fraction(3,8)
        assert bn(t,k+L)>=sqrt(2)/2-1e-12
        tested+=1
    r=.2
    for k,L in [(16,16),(80,40)]:
        mid=k+L//2
        end=k+L
        assert log(reset_suscept(t,r,mid))/mid < log(reset_suscept(t,r,end))/end
        tested+=1
    print('OK',tested,'analytic-identity, enumerated-history and finite-block checks')

if __name__=='__main__':
    verify()
