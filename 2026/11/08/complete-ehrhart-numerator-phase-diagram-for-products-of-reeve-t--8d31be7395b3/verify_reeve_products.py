#!/usr/bin/env python3
"""Independent exact-arithmetic checks for the Ehrhart numerator of two Reeve tetrahedra.

No external dependencies; analytic necessity and sufficiency of phase boundaries
are established in RESULT.md, not by this finite script.
"""
from math import comb
from fractions import Fraction


def direct_reeve_points(m, n):
    # Barycentric inequalities of t*conv(0,e1,e2,(1,1,m)), multiplied by m.
    total = 0
    for z in range(m*n + 1):
        for x in range(n + 1):
            if m*x < z:
                continue
            for y in range(n + 1):
                if m*y >= z and m*(x+y) <= m*n+z:
                    total += 1
    return total


def reeve_ehrhart(m, n):
    return Fraction(m*n**3 + 6*n**2 + (12-m)*n + 6, 6)


def predicted_h(m, r):
    a,b=m-1,r-1
    v=a*b; w=10*(a+b)
    return [1,9,v+w+9,9*v+w+1,9*v,v,0]


def from_ehrhart_product(m,r):
    return [sum((-1)**j*comb(7,j)*reeve_ehrhart(m,k-j)*reeve_ehrhart(r,k-j)
                for j in range(k+1)) for k in range(7)]


def is_unimodal(a):
    a=list(a)
    return any(all(a[i]<=a[i+1] for i in range(k)) and
               all(a[i]>=a[i+1] for i in range(k,len(a)-1)) for k in range(len(a)))


def is_log_concave(a):
    end=max(i for i,v in enumerate(a) if v)
    return all(a[i] > 0 for i in range(end+1)) and \
           all(a[i]*a[i]>=a[i-1]*a[i+1] for i in range(1,end))


def run():
    direct_checks = numerator_checks = phase_checks = 0
    for m in range(1,10):
        for n in range(0,9):
            assert direct_reeve_points(m,n)==reeve_ehrhart(m,n), (m,n)
            direct_checks+=1
    for m in range(1,25):
        for r in range(1,25):
            coeff=from_ehrhart_product(m,r)
            assert coeff==predicted_h(m,r), (m,r,coeff)
            numerator_checks+=1
            assert is_unimodal(coeff)
            assert is_log_concave(coeff)==((m-1)*(r-1)+10*(m+r-2)<=72)
            # Real-rootedness is proved analytically in RESULT.md;
            # this assertion checks the necessary boundary formula only for integer pairs.
            phase_checks+=2
    print('PASS: direct_reconstruction=%d, numerator_coefficients=%d, '
          'unimodality_and_log_concavity=%d' %
          (direct_checks,numerator_checks,phase_checks))

if __name__=='__main__':
    run()
