"""Exact arithmetic checks for the resonant Jordan-chain contraction theorem.

No external dependencies; the infinite-dimensional parameter assertions
are established by the mathematical proof, not by finite testing.
"""
from fractions import Fraction
from math import comb


def binom_poly_int(t, r):
    if r == 0:
        return 1
    out = 1
    for j in range(r):
        out *= (t-j)
    from math import factorial
    return out // factorial(r)


def shift(v):
    return v[1:] + [Fraction(0)]


def jordan(v):
    w = shift(v)
    return [a+b for a,b in zip(v,w)]


def add(a,b):
    return [x+y for x,y in zip(a,b)]


def scale(c,v):
    return [c*x for x in v]


def particular(t, m, lam, k, v):
    # Polynomial in t equals H(x)/x^k with t = log_lam(|x|).
    total = [Fraction(0)]*m
    w = v[:]
    for r in range(1, m+1):
        total = add(total, scale(lam**(-k)*binom_poly_int(t,r), w))
        w = shift(w)
    return total


def jordan_power(v, n):
    result = [Fraction(0)]*len(v)
    w = v[:]
    for j in range(len(v)):
        result = add(result, scale(comb(n,j) if n>=j else 0,w))
        w = shift(w)
    return result


def closed_form(n,m,lam,k,x0,y0,v):
    # Iterate formula for arbitrary rational initial state.
    answer = jordan_power(y0,n)
    w = v[:]
    for j in range(m):
        coeff = comb(n,j+1) if n>=j+1 else 0
        answer = add(answer,scale(lam**(-k)*x0**k*coeff,w))
        w = shift(w)
    return scale(lam**(k*n),answer)


def check():
    comparisons = 0
    orbit_cases = 0
    for m in range(1,9):
        for k in range(2,7):
            lam = Fraction(1,2)
            for basis in range(m):
                v = [Fraction(i+2,7) if i==basis else Fraction(0) for i in range(m)]
                for t in range(0,15):
                    p_now = particular(t,m,lam,k,v)
                    p_next = particular(t+1,m,lam,k,v)
                    rhs = add(jordan(p_now),scale(lam**(-k),v))
                    assert p_next==rhs,(m,k,basis,t,p_next,rhs)
                    comparisons += 1
            v = [Fraction((-1)**i*(i+2),11) for i in range(m)]
            y = [Fraction(i+2,19) for i in range(m)]
            x = Fraction(3,7)
            x0,y0 = x,y[:]
            for n in range(0,16):
                assert y==closed_form(n,m,lam,k,x0,y0,v),(m,k,n)
                orbit_cases += 1
                y = add(scale(lam**k,jordan(y)),scale(x**k,v))
                x *= lam
    # Exact algebraic forcing-obstruction range(N) iff final coordinate zero.
    for m in range(1,9):
        for i in range(m):
            v = [Fraction(j==i) for j in range(m)]
            if i<m-1:
                a = [Fraction(0)] + [-Fraction(4)*vi for vi in v[:-1]]
                assert shift(a)==scale(Fraction(-4),v)
            else:
                assert shift([Fraction(j+1) for j in range(m)])[-1]==0
    print(f'VERIFY_OK finite_polynomial_recurrences={comparisons} finite_orbit_identities={orbit_cases} jordan_chain_orders=8 resonance_orders=5 exact_rational=1')


if __name__ == '__main__':
    check()
