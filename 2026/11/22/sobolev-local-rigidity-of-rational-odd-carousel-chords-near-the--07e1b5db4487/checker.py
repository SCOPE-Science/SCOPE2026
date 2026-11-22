#!/usr/bin/env python3
"""Independent finite tests of the analytic fixed-arclength chord calculation.

The infinite odd-denominator theorem is proved analytically, not by these tests.
Requires only Python 3 standard library.
"""
import cmath
import math

TAU = 2 * math.pi


def linear_symbol(p, q, m):
    d = math.pi * p / q
    return (8j * math.sin(d) * cmath.exp(1j*m*d) /
            (m*m-1) * (m*math.sin(d)*math.cos(m*d)
                         - math.cos(d)*math.sin(m*d)))


def complex_chord_integral(p, q, m, t, eps, subintervals=768):
    h = TAU*p/q
    total = 0j
    for j in range(subintervals):
        u = h * (j+0.5)/subintervals
        total += cmath.exp(1j*(u+eps*math.cos(m*(t+u))))
    return h*total/subintervals


def numerical_derivative_mode(p, q, m, nt=128, eps=0.00005):
    coeff = 0j
    for j in range(nt):
        t = TAU*j/nt
        a = complex_chord_integral(p,q,m,t,eps)
        b = complex_chord_integral(p,q,m,t,-eps)
        d = (abs(a)**2-abs(b)**2)/(2*eps)
        coeff += d*cmath.exp(-1j*m*t)
    return coeff/nt


def main():
    checked = 0
    for p,q,m in [(1,7,2),(2,7,3),(3,7,5),(2,9,11),
                  (4,11,7),(1,13,9),(3,17,23)]:
        computed = numerical_derivative_mode(p,q,m,nt=128)
        predicted = linear_symbol(p,q,m)/2  # input cos(mt) has coefficient 1/2
        err = abs(computed-predicted)
        assert err < 0.00009, (p,q,m,err,computed,predicted)
        checked += 1
    for q in range(7,66,2):
        for p in range(1,q):
            if math.gcd(p,q)!=1:
                continue
            for m in range(2,450):
                s = abs(linear_symbol(p,q,m))
                assert s > 1e-13, (p,q,m)
                checked += 1
    # Exact integer Galois-norm nonresonance test across numerous orders.
    def phi(n):
        return sum(math.gcd(k,n)==1 for k in range(1,n+1))
    def cyclo_at_one(n):
        # For n>1, Phi_n(1) is its base prime if prime-power, else 1.
        for prime in range(2,n+1):
            if n%prime==0:
                if any(prime%d==0 for d in range(2,math.isqrt(prime)+1)):
                    continue
                x=n
                while x%prime==0:x//=prime
                return prime if x==1 else 1
        raise ValueError(n)
    for q in range(7,76,2):
        for m in range(2,200):
            Q=q//math.gcd(q,m)
            if Q==1:
                continue
            a=phi(q)//phi(Q)
            assert m**phi(q)*cyclo_at_one(q) != cyclo_at_one(Q)**a
            checked+=1
    print(f"PASS: {checked} finite checks; derivative examples agree to 9e-5.")
    print("The infinite theorem and quantitative stability use the written proof.")

if __name__ == '__main__':
    main()
