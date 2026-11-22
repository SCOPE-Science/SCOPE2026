"""Finite reproducibility checks for polynomial Volterra operators on power-Fock spaces.

These tests validate coefficients and examples; the analytical theorem is in RESULT.md.
"""
from fractions import Fraction
from math import exp, lgamma, log, isclose


def weight(n, j, d):
    x = (2 * n + 2) / d
    return exp(log(j) - log(n+j) - j / d * log(2)
               + (lgamma(x + 2*j/d) - lgamma(x)) / 2)


def weight_d_sq(n,d):
    return Fraction((n+1)*(2*n+d+2), 2*(n+d)**2)


def poch(a, k):
    ans=Fraction(1)
    for j in range(k):
        ans*=a+j
    return ans


def column(n, coefficients, d):
    return {n+j: a*weight(n,j,d) for j,a in coefficients.items() if a}


def witness_norm2(n, coefficients, d, q):
    ell=d-q
    u=column(n,coefficients,d)
    v=column(n+ell,coefficients,d)
    cross=sum(w.conjugate()*v.get(i,0) for i,w in u.items())
    return (sum(abs(w)**2 for w in u.values())+
            sum(abs(w)**2 for w in v.values()))/2+abs(cross)


def run():
    checks=0
    for d in range(3,9):
        for r in range(d):
            A=Fraction(r+1,d)
            B=A+Fraction(1,2)
            C=Fraction(r+d,d)
            assert C>A and C>B
            for k in range(1,6):
                moment=poch(A,k)*poch(B,k)/poch(C,k)**2
                product=Fraction(1)
                for h in range(k):
                    product*=weight_d_sq(r+h*d,d)
                assert moment==product
                checks+=1
        for n in (100,1000,5000):
            assert weight_d_sq(n,d)<1
            assert weight_d_sq(n+1,d)>weight_d_sq(n,d)
            assert isclose(weight(n,d,d)**2,float(weight_d_sq(n,d)),rel_tol=2e-10)
            checks+=3
        for q in range(1,d):
            coefficients={d:1.0,q:-0.7}
            exponent=q/d-1
            predicted=0.7*q*d**(-q/d)
            for n in (10000,30000):
                cross=0.7*weight(n,d,d)*weight(n+d-q,q,d)
                assert isclose(cross/n**exponent,predicted,rel_tol=0.005)
                checks+=1
            if q>=d-2:
                assert witness_norm2(200000,coefficients,d,q)>1
                checks+=1
    print(f"PASS: {checks} exact moment and numerical witness diagnostics")


if __name__ == '__main__':
    run()
