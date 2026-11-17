#!/usr/bin/env python3
"""Exact arithmetic checks for mixed enzyme-total flux response in HMM transformation cycles."""
from fractions import Fraction as Q
from math import isclose


def flux_data(j, enzymes, beta, sigma, alpha, total):
    u = [e-s*j for e, s in zip(enzymes, sigma)]
    assert all(x>0 for x in u)
    f = alpha*j + sum(b*j/v for b, v in zip(beta, u))-total
    h = alpha+sum(b*e/v**2 for b,e,v in zip(beta,enzymes,u))
    h2 = sum(2*b*s*e/v**3 for b,s,e,v in zip(beta,sigma,enzymes,u))
    d=[b*j/(v*v*h) for b,v in zip(beta,u)]
    m=(enzymes[0]+sigma[0]*j)/(j*u[0])+(enzymes[1]+sigma[1]*j)/(j*u[1])-h2/h
    return f, h, h2, d[0]*d[1]*m


def test_three():
    E=[Q(3),Q(3),Q(11,10)]
    beta=[Q(1),Q(1),Q(1,50)]
    sigma=[Q(1)]*3
    alpha=Q(3)
    expected=[(Q(1,2),Q(23,12),Q(71805312,33856161185)),
              (Q(1),Q(21,5),Q(-4675,1203052))]
    for j,T,derivative in expected:
        f,h,h2,cross=flux_data(j,E,beta,sigma,alpha,T)
        assert f==0,(j,T,f)
        assert cross==derivative,(j,cross,derivative)
        x=[beta[i]*j/(E[i]-j) for i in range(3)]
        c=[j]*3
        efree=[E[i]-j for i in range(3)]
        kon=[Q(2),Q(2),Q(100)]
        koff=[Q(1)]*3
        kcat=[Q(1)]*3
        for i in range(3):
            assert kon[i]*efree[i]*x[i]-koff[i]*c[i]==kcat[i]*c[i]==j
        assert sum(x)+sum(c)==T
    print('Two exact equilibria, every mass-action balance, and both mixed responses: PASS')


def polynomial_checks():
    # P(j) is the numerator giving the sign of minus the cross-response.
    P=[Q(7500),Q(-47250),Q(33975),Q(378862),Q(-1033626),Q(991782),Q(-331056)]
    # ascending coefficients of the sign-equivalent transformed P(11t/[10(1+t)])
    transformed=[Q(-5472000),Q(-14799600),Q(-12590520),Q(-3471116),Q(35967),Q(31407),Q(6859)]
    from math import comb
    # Multiply P(j(t)) by [10(1+t)]^6, compare coefficientwise.
    obtained=[Q(0) for _ in range(7)]
    for idx,a in enumerate(P):
        power=6-idx
        # coefficient a*j^power: a*11^power*10^(6-power)*t^power*(1+t)^(6-power)
        for ell in range(6-power+1):
            obtained[power+ell]+=a*(11**power)*(10**(6-power))*comb(6-power,ell)
    assert obtained==[60500*z for z in transformed],(obtained,transformed)
    # Exactly one variation of sign from high-degree to constant => exactly one positive root,
    # since sign at 0 is negative and leading coefficient is positive.
    assert transformed[0]<0 and transformed[-1]>0
    print('Exact degree-six transformed polynomial identity and one-sign-change certificate: PASS')


def test_two_pools():
    # Samples are supplementary checks; the general strict inequality is proved in RESULT.md.
    for E, b, s, a, j in [
      ([Q(3),Q(4)],[Q(2),Q(5)],[Q(1),Q(2)],Q(3),Q(1)),
      ([Q(20),Q(7)],[Q(1,5),Q(4,3)],[Q(4),Q(1,2)],Q(5),Q(1)),
    ]:
        T=a*j+sum(bi*j/(ei-si*j) for ei,si,bi in zip(E,s,b))
        f,h,h2,c=flux_data(j,E,b,s,a,T)
        assert f==0 and c>0
    print('Two independent positive two-pool checks: PASS (not a general proof)')


if __name__=='__main__':
    test_three()
    polynomial_checks()
    test_two_pools()
