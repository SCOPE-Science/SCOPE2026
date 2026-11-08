#!/usr/bin/env python3
"""Exact-rational sanity checks for the two-state Markov beta-map result.

Only finite algebraic/covariance comparisons are executed; the ergodic
and functional limit arguments are analytical, not computational claims.
"""
from fractions import Fraction as F
from itertools import product

CHECKS = 0

def eq(x, y):
    global CHECKS
    assert x == y, (x, y)
    CHECKS += 1

def multiplication_covariance(m):
    # Split [0,1) into the m monotone branches of x -> {mx}.
    # Use u={mx}; the terms constant in u integrate to zero.
    out = F(0)
    for j in range(m):
        c = F(j, m) - F(1, 2)
        # integral_0^1 (c+u/m)(u-1/2) du / m
        out += (c * (F(1, 2)-F(1, 2)) + (F(1, 3)-F(1, 4))/m) / m
    return out

def mat_mult(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def mat_powers_row_cov(a, b, t, n):
    d, e = F(1,a), F(1,b)
    P = [[t,1-t],[1-t,t]]
    D = [[d,F(0)],[F(0),e]]
    PD = mat_mult(P,D)
    r = [[F(1,2),F(1,2)]]
    for _ in range(n):
        r=mat_mult(r,PD)
    return (r[0][0]+r[0][1])/12

def enumerate_cov(a,b,t,n):
    # Initial E_0 uniform and its transition into E_1 is P.
    rates=(a,b)
    total=F(0)
    for indices in product((0,1),repeat=n+1):
        p=F(1,2)
        for k in range(1,n+1):
            p *= t if indices[k]==indices[k-1] else 1-t
        m=1
        for j in indices[1:]: m*=rates[j]
        total += p*F(1,12*m)
    return total

def closed_variance(a,b,t):
    d,e=F(1,a),F(1,b)
    denominator=1-t*(d+e)+(2*t-1)*d*e
    numerator=d+e+2*d*e-4*t*d*e
    return (1+numerator/denominator)/12

def finite_variance(a,b,t,N):
    return F(1,12)+2*sum((1-F(k,N))*mat_powers_row_cov(a,b,t,k)
                              for k in range(1,N))

def main():
    # Identity for each integer multiplication map.
    for m in range(2,70): eq(multiplication_covariance(m),F(1,12*m))
    cases=((2,3,F(1,3)),(2,3,F(1,2)),(2,5,F(3,5)),
           (3,7,F(4,5)),(4,4,F(1,4)),(6,9,F(2,7)))
    for a,b,t in cases:
        for n in range(1,8):
            eq(enumerate_cov(a,b,t,n),mat_powers_row_cov(a,b,t,n))
        d,e=F(1,a),F(1,b)
        H=1-t*(d+e)+(2*t-1)*d*e
        U=d+e+2*d*e-4*t*d*e
        # Derivative identity: (U' H - U H') = (d-e)^2.
        eq(-4*d*e*H+U*(d+e-2*d*e),(d-e)**2)
        eq(closed_variance(a,b,F(1)),
           ((1+d)/(1-d)+(1+e)/(1-e))/24)
        eq(closed_variance(a,b,F(1,2)),
           (1+2*((d+e)/2)/(1-(d+e)/2))/12)
        for N in (8,16,32,64):
            vN=finite_variance(a,b,t,N)
            v=closed_variance(a,b,t)
            assert vN<v and v-vN<F(4,N), (vN,v)
            global CHECKS
            CHECKS+=1
    # Explicit heterogeneous slope example.
    for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        eq(closed_variance(2,3,t),(12-7*t)/(12*(5-3*t)))
    eq(closed_variance(2,3,F(1,2)),F(17,84))
    eq(closed_variance(2,3,F(1)),F(5,24))
    print('PASS:',CHECKS,'exact rational finite checks')

if __name__=='__main__': main()
