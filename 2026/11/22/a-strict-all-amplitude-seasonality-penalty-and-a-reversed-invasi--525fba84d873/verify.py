#!/usr/bin/env python3
"""Reproduce exact sign inequalities and corroboratory Floquet values.

This is a standalone mathematical checker. The universal theorem itself is proved
in RESULT.md; finite numerical integration does not replace that proof.
"""
import math
from fractions import Fraction as F


def certificate():
    mean = F(1001, 1000)
    amp = F(1, 4)
    assert mean - amp > 0
    # For all t, V'+V >= mean - amp*sqrt(2) > 0.
    assert mean**2 > 2*amp**2
    assert F(9, 8)**2 > mean + amp
    # sqrt(mean) is between 1 and mean; the latter bound is strict.
    assert mean > 1
    delta = F(250, 169*1001)
    upper_lambda = F(1, 2000) - delta
    assert upper_lambda == -F(330831, 338338000)
    assert upper_lambda < -F(9, 10000)
    assert F(1, 2000) > 0
    return float(upper_lambda)


def floquet(a, d, b, c, vector, period=2*math.pi, steps=12000):
    """Return largest real Floquet exponent using numerical RK4 period map."""
    h = period/steps
    # Columns of the fundamental solution matrix.
    y = [1.0, 0.0, 0.0, 1.0]
    def rhs(t, y):
        v = vector(t)
        return [-a*y[0]+b*y[2], -a*y[1]+b*y[3],
                c*v*y[0]-d*y[2], c*v*y[1]-d*y[3]]
    for j in range(steps):
        t = j*h
        k1 = rhs(t, y)
        k2 = rhs(t+h/2, [z+h*dz/2 for z, dz in zip(y,k1)])
        k3 = rhs(t+h/2, [z+h*dz/2 for z, dz in zip(y,k2)])
        k4 = rhs(t+h, [z+h*dz for z, dz in zip(y,k3)])
        y = [z+h*(a1+2*a2+2*a3+a4)/6 for z,a1,a2,a3,a4 in zip(y,k1,k2,k3,k4)]
    # column-major ordering: (phi11,phi12,phi21,phi22).
    trace = y[0]+y[3]
    disc = math.sqrt((y[0]-y[3])**2 + 4*y[1]*y[2])
    rho = (trace+disc)/2
    return math.log(rho)/period


def main():
    upper = certificate()
    mean = 1001/1000
    true_exp = floquet(1,1,1,1,lambda t:mean+math.sin(t)/4)
    constant = math.sqrt(mean)-1
    print('rigorous rational upper bound:', upper)
    print('corroboratory periodic exponent:', true_exp)
    print('constant-mean exponent:', constant)
    assert constant > 0 and true_exp < upper
    # Additional nonconstant waveform and loss-rate checks; numerical only.
    for a,d,b,c,vm,alpha in [(1.0,2.0,2.0,1.0,2.5,0.2),
                              (0.3,1.7,1.4,0.8,1.4,0.3),
                              (0.7,0.5,0.8,2.0,1.1,0.35)]:
        v=lambda t: vm+alpha*(math.sin(t)+0.2*math.cos(2*t))
        lam=floquet(a,d,b,c,v)
        avg=-(a+d)/2+math.sqrt((a-d)**2/4+b*c*vm)
        print('nonconstant comparison:',lam,avg)
        assert lam < avg - 1e-6
    print('All exact witness and corroboratory tests passed.')

if __name__=='__main__':
    main()
