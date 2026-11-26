#!/usr/bin/env python3
"""Reproduce exact identities and compare the first-passage formula with independent finite-difference boundary-value calculations."""
import math
import random
from fractions import Fraction


def H(b, z):
    return 2*b*(2*b*b-1)*z/(z*z+b*b-1)-b/z-1


def Hprime(b, z):
    return b*((3-4*b*b)*z**4+4*b*b*(b*b-1)*z*z+(b*b-1)**2)/(z*z*(z*z+b*b-1)**2)


def solve_hit_transform(N, rho, target):
    # D = L = 1 and r = 4*rho; this solves D*u'' = r*u.
    r = 4*rho
    h2 = N*N
    lower = [0.]*(N+1)
    diag = [0.]*(N+1)
    upper = [0.]*(N+1)
    rhs = [0.]*(N+1)
    for i in range(N+1):
        if (target in ('left', 'either') and i == 0) or (target in ('right', 'either') and i == N):
            diag[i] = rhs[i] = 1.
        elif i == 0:
            diag[i], upper[i] = 2*h2+r, -2*h2
        elif i == N:
            lower[i], diag[i] = -2*h2, 2*h2+r
        else:
            lower[i], diag[i], upper[i] = -h2, 2*h2+r, -h2
    for i in range(1, N+1):
        factor = lower[i]/diag[i-1]
        diag[i] -= factor*upper[i-1]
        rhs[i] -= factor*rhs[i-1]
    u=[0.]*(N+1)
    u[-1]=rhs[-1]/diag[-1]
    for i in range(N-1, -1,-1):
        u[i]=(rhs[i]-upper[i]*u[i+1])/diag[i]
    return u


def check():
    tests=0
    rnd=random.Random(20260529)
    for b in [Fraction(21,20), Fraction(6,5),Fraction(5,4),Fraction(13,10),Fraction(2,1),Fraction(10,1)]:
        for i in range(1,13):
            z=Fraction(12-i,12)+Fraction(i,12)*b
            assert z >= 1 and z <= b
            assert H(b,1)==(b-1)*(3*b+2)/b
            assert H(b,b)==2*(b*b-1)
            assert H(b,1)-H(b,b)==-(b-1)*(2*b*b-b-2)/b
            assert Hprime(b,z)==2*b*(2*b*b-1)*(b*b-1-z*z)/(z*z+b*b-1)**2+b/(z*z)
            tests += 4
    bcritical=(1+math.sqrt(17))/4
    bspin=math.sqrt(1+1/math.sqrt(5))
    critical=math.acosh(bcritical)**2
    spin=math.acosh(bspin)**2
    assert 0<spin<critical and abs(critical-0.5370803732334924)<1e-13
    assert abs(spin-0.39296557427210493)<1e-13
    tests+=2
    for rho in [0.07, .25, spin*.999, (spin+critical)/2, critical*1.002, 1, 4]:
        b=math.cosh(math.sqrt(rho))
        costs=[H(b,math.cosh((2*i/3000-1)*math.sqrt(rho))) for i in range(3001)]
        loc=[i for i,v in enumerate(costs) if v <= min(costs)+1.e-12]
        if rho<critical:
            assert 0 in loc and 3000 in loc and 1500 not in loc
        else:
            assert 1500 in loc and 0 not in loc
        # The interior stationary point is never a strict minimum.
        assert all(costs[i] >= min(costs[0],costs[1500])-1.e-10 for i in range(3001))
        tests+=2
    for rho in [.1,.3,.48,.9,2.0]:
        n=800
        U={k:solve_hit_transform(n,rho,k) for k in ['left','right','either']}
        b=math.cosh(math.sqrt(rho))
        for i in (0,80,200,296,400,504,600,720,800):
            x=i/n
            numeric=(1/U['left'][i]-1)+(1/U['right'][i]-1)-(1/U['either'][i]-1)
            z=math.cosh((2*x-1)*math.sqrt(rho))
            expected=H(b,z)
            assert abs(numeric-expected)<3.1e-5,(rho,x,numeric,expected)
            tests+=1
    for j in range(1,400):
        b=1+rnd.random()*4
        z=1+(b-1)*rnd.random()
        t=1.e-6
        fd=(H(b,z+t)-H(b,z-t))/(2*t)
        assert abs(fd-Hprime(b,z))<1.5e-6, (b,z,fd,Hprime(b,z))
        tests+=1
    print(f'PASS: {tests} exact-algebra, phase-diagram, independent finite-difference, and derivative checks')
    print(f'spinodal rho={spin:.15f}; global transition rho={critical:.15f}')

if __name__=='__main__':
    check()
