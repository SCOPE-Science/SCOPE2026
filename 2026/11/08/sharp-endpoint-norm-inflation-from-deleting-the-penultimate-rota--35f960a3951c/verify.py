#!/usr/bin/env python3
"""Numerical and symbolic checks for the SO(3) penultimate-block deletion theorem.

Requires Python 3, mpmath and sympy. Finite checks corroborate the analytic proof.
"""
import math
import mpmath as mp
import sympy as sp


def weighted_kernel_direct(L, theta, missing=False):
    indices=range(L+1)
    return mp.sin(theta)*sum((2*j+1)*mp.sin((2*j+1)*theta) for j in indices if not missing or j != L-1)


def weighted_kernel_closed(L, theta, missing=False):
    N=L+1
    phi=2*N*theta
    base=-N*mp.cos(phi)+mp.mpf('0.5')*mp.cot(theta)*mp.sin(phi)
    if missing:
        base-=(2*L-1)*mp.sin((2*L-1)*theta)*mp.sin(theta)
    return base


def weighted_kernel_asymptotic(L, theta, missing=False):
    N=L+1
    phi=2*N*theta
    if missing:
        main=-N*(2*mp.cos(2*theta)-1)*mp.cos(2*L*theta)
        error=mp.mpf('0.5')*mp.cot(theta)*mp.sin(phi)+3*mp.sin(theta)*mp.sin((2*L-1)*theta)
    else:
        main=-N*mp.cos(phi)
        error=mp.mpf('0.5')*mp.cot(theta)*mp.sin(phi)
    return main, error


def numeric_norm(L, missing):
    # Integrate over every oscillation cell to control cancellation near edges.
    cells = 8 * (L+1)
    return (2/mp.pi)*sum(mp.quad(lambda th: abs(weighted_kernel_closed(L,th,missing)),
                                [mp.pi*j/cells, mp.pi*(j+1)/cells]) for j in range(cells))


def main():
    mp.mp.dps=30
    t=sp.symbols('t',real=True)
    # The nontrivial exact cancellation behind the new leading profile.
    u=sp.symbols('u',real=True)
    identity=sp.cos(t)+2*sp.sin(u)*sp.sin(t-3*u)-(2*sp.cos(2*u)-1)*sp.cos(t-2*u)
    assert sp.trigsimp(identity,method='fu') == 0
    checks=0
    for L in (2,3,5,11,27):
        for j in range(1,11):
            th=mp.pi*(j+mp.mpf('.31'))/17
            for missing in (False,True):
                left=weighted_kernel_direct(L,th,missing)
                right=weighted_kernel_closed(L,th,missing)
                main,error=weighted_kernel_asymptotic(L,th,missing)
                assert abs(left-right)<mp.mpf('1e-26')
                assert abs(left-main-error)<mp.mpf('1e-26')
                checks+=1
    # Exact leading constant from the signed six intervals.
    w_integral=mp.quad(lambda th:abs(2*mp.cos(2*th)-1),[0,mp.pi/6,5*mp.pi/6,mp.pi])
    assert abs(w_integral-(mp.pi/3+2*mp.sqrt(3)))<mp.mpf('1e-27')
    a=4/mp.pi
    b=4/(3*mp.pi)+8*mp.sqrt(3)/mp.pi**2
    assert b>a
    norms=[]
    for L in (6,16,40):
        original=numeric_norm(L,False)
        punctured=numeric_norm(L,True)
        assert punctured>original
        norms.append((L,float(original/(L+1)),float(punctured/(L+1))))
    assert abs(norms[-1][1]-float(a))<0.03
    assert abs(norms[-1][2]-float(b))<0.09
    print('SO3_PENULTIMATE_PASS exact_kernel_checks=%d quad_orders=%d integral=%s baseline=%s punctured=%s' % (checks,len(norms),mp.nstr(w_integral,14),mp.nstr(a,12),mp.nstr(b,12)))
    for x in norms: print('L=%d baseline_per_band=%.9f punctured_per_band=%.9f'%x)

if __name__=='__main__':main()
