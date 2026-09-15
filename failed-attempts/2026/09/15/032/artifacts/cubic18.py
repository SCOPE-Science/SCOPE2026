"""Derive q=2 closed form for Eq.(17) from scratch and compare.
Eq17 q=2: 2*sqrt(1-J/r) = J, J=a(1-r). => 4(1-J/r)=J^2 => J^2 + 4J/r - 4 = 0.
Sub r=1-J/a: J^2 + 4J/(1-J/a) - 4 = 0 => multiply (1-J/a): J^2(1-J/a)+4J-4(1-J/a)=0
=> -J^3/a + J^2 + 4J - 4 + 4J/a = 0 => J^3 - a*J^2 - 4(a+1)J + 4a = 0... cubic (A)
Solve numerically and compare to bisect. Also test whether Eq.(18) as TYPESSET
(with cos((pi+theta)/3)) solves (A); scan sign variants cos((pi±theta)/3), cosh, etc.
"""
import numpy as np, math

def cubic_roots(a):
    # J^3 - a J^2 -4(a+1) J + 4a = 0
    c = np.poly1d([1, -a, -4*(a+1), 4*a])
    return np.roots(c)

def explicit18(alpha, sign=+1):
    th_denom = 36-18*alpha-alpha**2
    th_num = 6*math.sqrt(6*alpha**4+18*alpha**3+20*alpha**2+24*alpha+8)
    theta = math.atan2(th_num, alpha*th_denom)
    return (2/3)*(1 - math.sqrt(alpha**2+12*alpha+12)/(2*alpha)*math.cos((math.pi+sign*theta)/3))

def resid(a, r):
    J = a*(1-r)
    return 2*math.sqrt(max(0, 1-J/r)) - J

for a in [0.2, 0.5, 0.7, 1.0]:
    print(f"a={a} cubicroots={np.sort(cubic_roots(a))}")
    for s in [+1, -1]:
        re = explicit18(a, s)
        print(f"   sign {s:+d}: rho0={re:.6f} resid={resid(a,re):.4f}")
