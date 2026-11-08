#!/usr/bin/env python3
"""Independent arithmetic and numerical spot checks for a critical two-cycle map.
Requires Python 3 standard library only; finite tests do not replace the proof.
"""
from fractions import Fraction as F
from math import sqrt, isfinite


def formal_coefficients(b):
    b = F(b)
    kappa = (1-b)/(1+b)
    a = 4/kappa
    assert kappa > 0 and 0 <= b < 1
    # The two points form an exact two-cycle in (v,y) order.
    def phi(x): return x/(1+x*x)
    def T(v,y):
        v1 = b*v+(1-b)*y
        return v1, y-a*phi(v1)
    P = (F(1),-1/kappa)
    Q = (F(-1),1/kappa)
    assert T(*P) == Q and T(*Q) == P
    # Expansion of phi(1-u)=(1-u)/(2-2u+u^2):
    c = [F(0)]*5
    for j in range(5):
        rhs = F(1) if j == 0 else F(-1) if j == 1 else F(0)
        c[j] = (rhs + (2*c[j-1] if j > 0 else 0) - (c[j-2] if j > 1 else 0))/2
    assert c == [F(1,2),F(0),-F(1,4),-F(1,4),-F(1,8)]
    A = -1/(1-b)
    B = 3*(1+b)/(1-b)**2
    # On the center graph p=q+A*q^2+B*q^3+O(q^4),
    # the sign-reflected map has q'=-q+c2*q^2+c3*q^3+O(q^4).
    c2 = 1/kappa
    c3 = (1+2*b*A)/kappa
    assert -b*A == c2+A
    assert -b*B == c3-2*A*c2-B
    assert c2 == (1+b)/(1-b)
    assert c3 == (1+b)*(1-3*b)/(1-b)**2
    K = 2*(c3+c2*c2)
    assert K == 4*(1+b)/(1-b) and K > 0
    return kappa,a,A,B,K


def trajectory(b,n=120000):
    k = float((1-b)/(1+b))
    a = 4/k
    A = -1/(1-float(b))
    B = 3*(1+float(b))/(1-float(b))**2
    q = 0.01
    p = q+A*q*q+B*q*q*q
    v,y = 1+p,-1/k+q
    for _ in range(n):
        v = float(b)*v+(1-float(b))*y
        y = y-a*v/(1+v*v)
        v = float(b)*v+(1-float(b))*y
        y = y-a*v/(1+v*v)
    scale = sqrt(8*(1+float(b))/(1-float(b))*n)
    u = abs((y+1/k)*scale)
    w = abs((v-1)*scale)
    assert isfinite(u) and isfinite(w) and abs(u-1)<0.03 and abs(w-1)<0.03,(b,u,w)
    return (u,w)


def main():
    bs=(F(0),F(1,5),F(1,2),F(9,10))
    for b in bs:
        formal_coefficients(b)
        trajectory(b)
    print('VERIFY_OK exact_fraction_cases=4 critical_two_step_trajectories=4 each_120000_iterations')

if __name__ == '__main__':
    main()
