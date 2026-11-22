"""Numerical consistency tests for a conditional Robin reaction-time theorem.
Run with Python 3, NumPy and SciPy: python check.py
"""
import math
import numpy as np
from scipy.optimize import brentq


def joint_transform(s, x, L, D, k):
    q = math.sqrt(s / D)
    value = k * math.sinh(q * (L-x)) / (D*q*math.cosh(q*L) + k*math.sinh(q*L))
    success = k * (L-x) / (D+k*L)
    return value / success


def separated_transform(s, x, L, D, k):
    q=math.sqrt(s / D)
    hit = math.sinh(q*(L-x))/math.sinh(q*L) / ((L-x)/L)
    exponent = D*q / math.tanh(q*L) - D/L
    return hit * (k+D/L)/(k+D/L+exponent)


def bernoulli_product(s, x, L, D, k, N):
    q = math.sqrt(s/D)
    hit = math.sinh(q*(L-x))/math.sinh(q*L) / ((L-x)/L)
    eta = k*L/D
    correction=0.0
    for n in range(1, N+1):
        z=brentq(lambda z: z/math.tan(z)+eta,
                 (n-0.5)*math.pi+1.e-12, n*math.pi-1.e-12)
        nu=D*(n*math.pi/L)**2
        rho=D*(z/L)**2
        correction += math.log1p(s/nu) - math.log1p(s/rho)
    return hit * math.exp(correction)


def moments(x,L,D,k):
    eta=k*L/D
    mean=(x*(2*L-x)/6 + L**2/(3*(1+eta)))/D
    variance=(L**4-(L-x)**4)/(90*D**2) + L**4/D**2 * (
        2/(45*(1+eta)) + 1/(9*(1+eta)**2))
    return mean,variance


if __name__ == '__main__':
    count=0
    for L,D,k,x in [(1,.8,.3,.33),(1.2,2,3,.2),(2,1.3,10,1.7)]:
        for s in (.002,.2,1.7,5):
            exact=joint_transform(s,x,L,D,k)
            sub=separated_transform(s,x,L,D,k)
            product=bernoulli_product(s,x,L,D,k,2400)
            assert abs(exact-sub) < 2.e-12
            assert abs(exact-product) < 2.e-4
            count+=2
        mean,var=moments(x,L,D,k)
        points=np.array([1.e-4,2.e-4,3.e-4,4.e-4,5.e-4])
        values=np.array([math.log(joint_transform(float(s),x,L,D,k)) for s in points])
        coefficients=np.polynomial.polynomial.polyfit(points,values,4)
        assert abs(-coefficients[1]-mean) < 1.e-4
        assert abs(2*coefficients[2]-var) < 2.e-3
        count+=2
    print('PASS:',count,'transform, spectral-product and moment consistency checks')
