"""Independent finite checks for the reset-Brownian-driven harmonic particle.

Python 3 standard library only. The accompanying proof establishes the universal
claims; this script tests exact polynomial identities and finite-time dynamics.
"""
from fractions import Fraction as F
from math import exp, expm1, isclose


def stationary_moments(q):
    """Generator recurrence, solved degree by degree in rational arithmetic."""
    m = {(0, 0): F(1)}
    for n in (2, 4):
        for a in range(n + 1):
            b = n - a
            rhs = F(0)
            if a:
                rhs += a * q * m[a - 1, b + 1]
            if b >= 2:
                rhs += b * (b - 1) * m[a, b - 2]
            m[a, b] = rhs / (a + (q if b else 0))
    return m


def closed_moments(q):
    m20 = 2 * q / (q + 1)
    m11 = 2 / (q + 1)
    m02 = 2 / q
    poly = q * q + 19 * q + 12
    m40 = 12 * q**2 * poly / ((q + 1)**2 * (q + 2) * (q + 3))
    m31 = 12 * q * poly / ((q + 1)**2 * (q + 2) * (q + 3))
    m22 = 4 * poly / ((q + 1)**2 * (q + 2))
    A = 8 * q**2 * (q*q + 26*q + 15) / ((q+1)**2*(q+2)*(q+3))
    B = 8 * q * (q*q + 26*q + 15) / ((q+1)**2*(q+2)*(q+3))
    C = 8 * (8*q + 5) / ((q+1)**2*(q+2))
    return (m20, m11, m02, m40, m31, m22), (A, B, C)


def phi(rate, s):
    delta = rate - 2.0
    if abs(delta) <= 1e-13:
        return s * exp(-2*s)
    return exp(-2*s) * (-expm1(-delta*s)) / delta


def exact_covariance(beta, s):
    _, (A, B, C) = closed_moments(float(beta))
    return (A*exp(-2*s) + 2*beta*B*phi(beta+1, s)
            + 2*beta*beta*C*(phi(beta, s)-phi(beta+1, s)))


def integrate_covariance(beta, s, steps):
    """Independent RK4 evolution of the three covariance equations."""
    _, triple = closed_moments(float(beta))
    h = s/steps
    y = list(triple)
    def f(y):
        H, G, F0 = y
        return [-2*H+2*beta*G, -(1+beta)*G+beta*F0, -beta*F0]
    for _ in range(steps):
        k1 = f(y)
        k2 = f([y[i]+h*k1[i]/2 for i in range(3)])
        k3 = f([y[i]+h*k2[i]/2 for i in range(3)])
        k4 = f([y[i]+h*k3[i] for i in range(3)])
        y = [y[i]+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(3)]
    return y[0]


def asymptotic_amplitude(beta):
    _, (A, B, C) = closed_moments(float(beta))
    if beta < 2:
        return 2*beta*beta*C/(2-beta)
    if beta > 2:
        return A+2*beta*B/(beta-1)+2*beta*beta*C/((beta-2)*(beta-1))
    return 112/3


def test():
    count = 0
    for q in [F(1,10), F(1,3), F(1), F(3,2), F(2), F(5,2), F(3), F(7), F(29,3)]:
        m = stationary_moments(q)
        vals, (A, B, C) = closed_moments(q)
        for key, value in zip([(2,0),(1,1),(0,2),(4,0),(3,1),(2,2)], vals):
            assert m[key] == value, (q, key, m[key], value)
            count += 1
        assert A == m[4,0]-m[2,0]**2
        assert B == m[3,1]-m[2,0]*m[1,1]
        assert C == m[2,2]-m[2,0]*m[0,2]
        assert A>0 and B>0 and C>0
        count += 6
    for beta in [0.15,0.5,0.99,1.,1.3,1.9,2.,2.3,4.,10.]:
        for s in [0.,0.1,0.5,1.,2.,4.,6.]:
            expected=exact_covariance(beta,s)
            computed=integrate_covariance(beta,s,max(50,int(1200*s)))
            assert isclose(expected,computed,rel_tol=3e-9,abs_tol=1e-10), (beta,s,expected,computed)
            assert expected>0
            count+=2
    for beta in [0.5,1.,1.5,1.9,2.1,3.,5.]:
        s = 170.
        amp = asymptotic_amplitude(beta)
        observed = exact_covariance(beta,s)*exp(min(beta,2)*s)
        # Near-critical gap 0.1 requires enough time; at 170 error is tiny.
        assert isclose(observed, amp, rel_tol=1e-5,abs_tol=1e-8), (beta, observed, amp)
        count+=1
    beta=2
    for s in [0.,0.1,1.,4.,20.]:
        exact = exact_covariance(beta,s)
        critical=exp(-2*s)*(F(112,3)*s+F(8,15))+F(544,45)*exp(-3*s)
        assert isclose(exact,float(critical),rel_tol=1e-12,abs_tol=1e-12)
        count+=1
    for z in [-3.,-1.,0.,1.,3.]:
        s=200.
        beta=2+z/s
        lhs=exact_covariance(beta,s)*exp(2*s)/s
        limit=112/3 * (-expm1(-z)/z if z else 1.)
        assert isclose(lhs, limit, rel_tol=0.03), (z,lhs,limit)
        count+=1
    print(f"PASS: {count} exact and finite checks; independent moment recurrence and ODE integration")

if __name__ == '__main__':
    test()
