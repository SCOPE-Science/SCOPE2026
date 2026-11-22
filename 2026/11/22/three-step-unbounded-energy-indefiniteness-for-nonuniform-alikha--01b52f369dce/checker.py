#!/usr/bin/env python3
"""Arithmetic checks of a three-step Alikhanov energy obstruction.

Only the Python standard library is required. Decimal square roots integrate the
alpha=1/2 kernel exactly over each polynomial interpolation panel.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
import math


def half_order_matrix(eps):
    # Returns the coefficients without the common positive 1/Gamma(1/2).
    D = Decimal
    tau = [D(1), D(eps), D(1)]
    knots = [D(0)]
    for h in tau:
        knots.append(knots[-1] + h)
    sigma = D(3) / 4
    M = [[D(0) for _ in range(3)] for _ in range(3)]
    for k in range(1, 4):
        s = knots[k-1] + sigma*tau[k-1]
        for j in range(1, k):
            L, U, d, e = knots[j-1], knots[j], tau[j-1], tau[j]
            x, y = s-L, s-U
            J0 = 2*(x.sqrt() - y.sqrt())
            J1 = (2*x-d)*J0 - D(4)/3*(x*x.sqrt()-y*y.sqrt())
            M[k-1][j-1] += J0/d - J1/(d*(d+e))
            M[k-1][j] += J1/(e*(d+e))
        M[k-1][k-1] += 2*(sigma*tau[k-1]).sqrt()/tau[k-1]
    return M


def quadratic(M, increments):
    return sum(increments[i]*M[i][j]*increments[j]
               for i in range(3) for j in range(3))


def main():
    with localcontext() as ctx:
        ctx.prec = 65
        D = Decimal
        A = D(2)/3
        B = D(4)*D(7).sqrt()/3 - D(2)*D(3).sqrt()
        assert B > 0
        witness = [D(0), D(-1), D(16)]
        M = half_order_matrix('0.0001')
        value = quadratic(M, witness)
        print('alpha=1/2; steps=(1,1/10000,1); increments=(0,-1,16)')
        print('Gamma(1/2) times the three-step bilinear energy:', value)
        assert value < D(-3075) and value > D(-3076)
        print('positive A:', A, '; positive B:', B)
        theoretical = -B*B/(4*A)
        print('limiting epsilon*Gamma(1/2)*energy for optimal increments:', theoretical)
        for e in ['0.00001','0.000001','0.0000001']:
            eps=D(e)
            opt=[D(0),-B/(2*A),D(1)]
            z=eps*quadratic(half_order_matrix(e),opt)
            print('epsilon=',e,'scaled energy=',z)
            assert abs(z-theoretical)<D(30)*eps.sqrt()
        print('CHECKS PASSED')

if __name__ == '__main__':
    main()
