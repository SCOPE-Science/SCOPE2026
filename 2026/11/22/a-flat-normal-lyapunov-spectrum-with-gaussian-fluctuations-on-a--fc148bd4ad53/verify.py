"""Standalone checks for the cubic Chebyshev boundary and normal log-cocycle.
Run: python3 verify.py. Symbolic checks use SymPy; other checks use only Python.
"""
import math
from fractions import Fraction


def symbolic_checks():
    import sympy as s
    z, f, P, m = s.symbols('z f P m', real=True)
    root2 = s.sqrt(2)
    N = s.Rational(1, 2) + z/root2
    h = 2*root2
    eps = root2/4
    prey = N + h/eps * N*(1-N)*(N-s.Rational(1,2))
    assert s.simplify(root2*(prey-s.Rational(1,2))-(3*z-4*z**3)) == 0
    ms = s.Rational(1,2) + 1/(2*root2)
    assert s.simplify(1+h*(N-ms)-2*z) == 0
    assert s.simplify((3*z-4*z**3)**2-1).subs(z,s.Rational(1,2)) == 0
    print('Exact conjugacy, normal multiplier, and branch endpoint checks: PASS')


def moment_checks():
    for n in range(1,121):
        c = lambda k: Fraction(1,12*3**k)
        from_cov = n*c(0)+2*sum((n-k)*c(k) for k in range(1,n))
        from_closed = Fraction(n,6)-Fraction(1,8)*(1-Fraction(1,3**n))
        assert from_cov == from_closed, n
    print('120 exact-rational finite-horizon variance identities: PASS')


def transfer_checks():
    for t in [0.101,0.213,0.329,0.785,1.411,2.67]:
        # 3-to-1 expanding map T(x)=3x+pi mod 2pi.
        pre=[(t-math.pi+2*math.pi*j)/3 for j in range(3)]
        v = sum(math.log(abs(2*math.cos(q))) for q in pre)/3
        target=math.log(abs(2*math.cos(t)))/3
        assert abs(v-target) < 1e-12, (t,v,target)
    print('Six transfer-operator values: PASS')


def finite_quadrature():
    # Midpoint quadrature of stationary correlations; an independent check
    # which is not used as a proof of the infinite-horizon identities.
    sample_count = 24000
    means=[]
    for lag in range(5):
        running=0.0; running2=0.0
        for i in range(sample_count):
            t = 2*math.pi*(i+0.43719)/sample_count
            a=math.log(abs(2*math.cos(t)))
            b=math.log(abs(2*math.cos(3**lag*t)))
            running+=a*b
            running2+=a
        approx=running/sample_count
        target=math.pi**2/(12*3**lag)
        assert abs(approx-target)<0.007, (lag,approx,target)
        means.append(running2/sample_count)
    assert max(abs(x) for x in means)<0.002
    print('Five stationary numerical covariance diagnostics: PASS')


if __name__=='__main__':
    symbolic_checks()
    moment_checks()
    transfer_checks()
    finite_quadrature()
    print('ALL CHECKS PASS')
