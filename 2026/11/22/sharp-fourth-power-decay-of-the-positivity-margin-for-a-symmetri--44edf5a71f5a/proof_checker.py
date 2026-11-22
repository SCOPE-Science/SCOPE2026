#!/usr/bin/env python3
"""Exact symbolic corroboration of a positivity-margin proof.

Needs Python 3 and SymPy. These checks do not replace the analytic proof
of universal lower bounds on all real vectors.
"""
import sympy as S
from fractions import Fraction

n=S.symbols("n", positive=True, integer=True)

def power_sums(k, a, b):
    return {j:S.factor(k*a**j+(n-k)*b**j) for j in (1,2,3,4,6)}

def F(p):
    return S.factor(4*p[1]**2*(p[3]-4*p[1]**3)**2+
                    9*p[2]*(p[6]-8*p[1]**2*p[4]+16*p[1]**4*p[2])-
                    16*p[1]**8)

def must_equal(a,b):
    assert S.cancel(a-b)==0, (a,b)

# Identity for the original octic on the hyperplane p1=1/2.
q2,q3,q4,q6=S.symbols('q2 q3 q4 q6')
mapped={1:S.Rational(1,2),2:q2,3:q3,4:q4,6:q6}
must_equal(F(mapped),(q3-S.Rational(1,2))**2+
           9*q2*(q6-2*q4+q2)-S.Rational(1,16))

formulas=[
  (0,(4*n*n+1)/(4*n),(2544*n**6+2512*n**4+508*n**2+9)/(256*n**6)),
  (1,(4*n*n-3)/(4*n),(2544*n**6-3632*n**4+892*n**2+297)/(256*n**6)),
]
for parity, expected_q, expected_f in formulas:
    eps=1-2*parity
    k=(n+parity)/2
    plus=1+S.Rational(eps,2)/n
    minus=-1+S.Rational(eps,2)/n
    p=power_sums(k,plus,minus)
    must_equal(p[1],S.Rational(1,2))
    must_equal(p[2],expected_q)
    must_equal(F(p),expected_f)
    for N in range(2+parity,31,2):
        # Direct rational evaluations, independent of the closed formulas.
        signs=[Fraction(1,1)+Fraction(eps,2*N)]*((N+parity)//2)
        signs += [Fraction(-1,1)+Fraction(eps,2*N)]*((N-parity)//2)
        power={j:sum((x**j for x in signs),Fraction(0)) for j in (1,2,3,4,6)}
        computed=4*power[1]**2*(power[3]-4*power[1]**3)**2
        computed+=9*power[2]*(power[6]-8*power[1]**2*power[4]+16*power[1]**4*power[2])-16*power[1]**8
        assert S.Rational(computed.numerator,computed.denominator)==expected_f.subs(n,N)
        assert computed > 0
        assert Fraction(N**4)*computed / power[2]**4 < 16
print("PASS symbolic identities and finite diagnostics")
