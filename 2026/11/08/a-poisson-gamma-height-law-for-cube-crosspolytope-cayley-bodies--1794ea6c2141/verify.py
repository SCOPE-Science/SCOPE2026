#!/usr/bin/env python3
"""Standalone exact-rational checks for the Cayley height beta-mixture."""
from fractions import Fraction as F
from math import factorial, comb

def test(d, rho):
    h=sum((rho**k)/factorial(k) for k in range(d+1))
    # Every section-polynomial term integrates to its stated beta-mixture mass.
    masses=[F(comb(d,k)*factorial(k)*factorial(d-k),(factorial(d+1)*factorial(k)))*rho**k*(d+1) for k in range(d+1)]
    assert sum(masses)==h
    weights=[rho**k/F(factorial(k),1)/h for k in range(d+1)]
    assert sum(weights)==1
    m=sum(weights[k]*F(k+1,d+2) for k in range(d+1))
    sq=sum(weights[k]*F((k+1)*(k+2),(d+2)*(d+3)) for k in range(d+1))
    assert sq>=m*m
    return float(d*m),float(d*d*(sq-m*m))

def main():
    cases=0
    for rho in [F(1,5),F(1,2),F(1),F(2),F(3),F(5)]:
        for d in range(2,61):
            test(d,rho);cases+=1
        m,v=test(300,rho)
        assert abs(m-(1+float(rho))) < .1
        assert abs(v-(1+2*float(rho))) < .5
    print('CAYLEY_POISSON_GAMMA_CHECKS_PASSED profiles=',cases,' large_dimension_checks=6')
if __name__=='__main__':main()
