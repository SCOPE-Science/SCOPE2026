#!/usr/bin/env python3
"""Exact transfer-polynomial checks for a finite Ising ring with two defect bonds.

Uses Python 3 standard library only. Checks finite test instances; the universal
root-count classification is established by the separate analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def add(a, b):
    return [((a[i] if i < len(a) else F(0)) +
             (b[i] if i < len(b) else F(0)))
            for i in range(max(len(a), len(b)))]


def scale(a, v):
    return [v * x for x in a]


def shift(a):
    return [F(0)] + a


def recurrences(n, determinant):
    # L_m(v) = tr(T^m), R_m(v) = det(T)^((m)/2) U_m(v/sqrt(det(T))).
    l = [[F(2)], [F(0), F(2)]]
    r = [[F(1)], [F(0), F(2)]]
    for j in range(2, n + 1):
        l.append(add(scale(shift(l[-1]), F(2)), scale(l[-2], -determinant)))
        r.append(add(scale(shift(r[-1]), F(2)), scale(r[-2], -determinant)))
    return l, r


def impurity_polynomial(n, a, g):
    # a = exp(K)>1 and g = exp(K_i)>0, each chosen rational for checking.
    b = 1 / a
    det = a*a - b*b
    c = g/a
    d = 1/g - g/(a*a)
    l, r = recurrences(n, det)
    return add(add(scale(l[n], c*c), scale(l[n-2], d*d)),
               scale(r[n-2], F(4)*c*d*b))


def evaluate(coeff, v):
    z = F(0)
    for k in reversed(coeff):
        z = z*v + k
    return z


def transfer_trace(n, a, g, w):
    t = ((a*w, 1/a), (1/a, a/w))
    ti = ((g*w, 1/g), (1/g, g/w))
    def mult(x, y):
        return tuple(tuple(sum(x[i][k]*y[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))
    m = mult(ti, ti)
    for _ in range(n-2):
        m = mult(m, t)
    return m[0][0]+m[1][1]


def spin_sum(n, a, g, w):
    total = F(0)
    for s in product((-1, 1), repeat=n):
        w_bulk = sum(s[j]*s[j+1] for j in range(1, n-1))
        w_defect = s[0]*(s[1]+s[-1])
        total += (a**w_bulk) * (g**w_defect) * (w**sum(s))
    return total


def cheb_coeffs(n):
    t = [[F(1)], [F(0), F(1)]]
    u = [[F(1)], [F(0), F(2)]]
    for _ in range(2, n+1):
        t.append(add(scale(shift(t[-1]), F(2)), scale(t[-2], F(-1))))
        u.append(add(scale(shift(u[-1]), F(2)), scale(u[-2], F(-1))))
    return t, u


def main():
    checks=0
    for a in (F(2), F(3,2)):
        for g in (F(1,2), F(4,5), F(1), F(5,4)):
            for n in range(3,11):
                coefficients = impurity_polynomial(n,a,g)
                assert len(coefficients) == n+1
                assert all(coefficients[j] == 0 for j in range(n+1) if (n-j)%2)
                for w in (F(2), F(3,2)):
                    v=a*(w+1/w)/2
                    assert evaluate(coefficients,v) == transfer_trace(n,a,g,w)
                    assert evaluate(coefficients,v) == spin_sum(n,a,g,w)
                    checks += 2
                # At v=0, exact even-N coefficient, and at v=0 odd-N slope.
                q = a**(-2)
                u = g*g
                det = a*a - a**(-2)
                if n%2 == 0:
                    # Z(0)=2*D^((n-2)/2) *(-1)^(n/2)*(u-1/u)
                    wanted=F(2)*(det**((n-2)//2))*((-1)**(n//2))*(u-1/u)
                    assert coefficients[0] == wanted
                else:
                    # dZ/dv =2 D^((n-3)/2)*(-1)^((n-1)/2) [N u-(N-2)/u-2q]
                    wanted=F(2)*(det**((n-3)//2))*((-1)**((n-1)//2))*(n*u-(n-2)/u-2*q)
                    assert coefficients[1] == wanted
                checks+=1
    # Exact critical odd threshold: with a=2, q=1/4, N=3, u_c=2/3.
    assert F(3)*F(2,3)**2 - F(2)*F(1,4)*F(2,3)-F(1)==0
    checks+=1
    print(f"PASS: {checks} exact rational transfer, enumeration, and local-coefficient identities")
    print("Limits: finite checks do not establish the theorem; see the analytic proof.")

if __name__ == '__main__':
    main()
