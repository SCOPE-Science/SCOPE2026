"""Reproducible checks for exact odd-budget scalar minimax differentiation.

No network, nonstandard data, or environmental state is required. Symbolic
checks support the exact proof, not a substitute for its universal inequalities.
"""
from fractions import Fraction
import math
import random
import sympy as sp
import numpy as np


def k(n):
    assert n >= 2
    return Fraction(1, n) if n % 2 == 0 else Fraction(n, n*n-1)


def scalar_check():
    a, b, K, h = sp.symbols('a b K h', positive=True)
    risk = a*a*h**4/36 + b*K/h**2
    hstar = (18*b*K/(a*a)) ** sp.Rational(1, 6)
    target = (3*a*a*b*b/16) ** sp.Rational(1, 3)*K**sp.Rational(2, 3)
    assert sp.simplify(sp.diff(risk, h).subs(h, hstar)) == 0
    assert sp.simplify(risk.subs(h, hstar) / target) == 1
    assert sp.simplify(sp.diff(risk, h, 2) - (a*a*h*h/3 + 6*b*K/h**4)) == 0
    print('symbolic stationary point, exact optimum, strict convexity: PASS')


def direct_check():
    for n in range(2, 20):
        p, q = n//2, (n+1)//2
        kn = float(k(n))
        assert Fraction(1, 4)*(Fraction(1,p)+Fraction(1,q)) == k(n)
        h=(18*kn)**(1/6)
        sites=np.array([h]*p + [-h]*q)
        weights=np.array([1/(2*p*h)]*p + [-1/(2*q*h)]*q)
        assert abs(weights.sum()) < 1e-13
        assert abs(weights@sites-1) < 1e-13
        assert abs(weights@(sites**2)) < 1e-13
        C=np.sum(abs(weights)*abs(sites)**3)
        V=sum(weights**2)
        observed=C*C/36+V
        target=(3/16)**(1/3)*kn**(2/3)
        assert math.isclose(observed,target,rel_tol=1e-12,abs_tol=1e-12)
        assert math.isclose(V,kn/(h*h),rel_tol=1e-12)
    # Exact rational demonstration of the sign partition penalty for n=3.
    assert k(3) == Fraction(3,8)
    assert k(2) == Fraction(1,2)
    assert k(5) == Fraction(5,24)
    print('all exactness constraints and integer sign allocations: PASS')


def arbitrary_feasible_stencils():
    gen=np.random.default_rng(20261117)
    count=0
    for n in (3, 4, 5, 6, 7, 8, 11, 15):
        lower=(3/16)**(1/3)*float(k(n))**(2/3)
        for _ in range(1500):
            nodes=gen.uniform(-4,4,size=n)
            A=np.vstack([np.ones(n),nodes,nodes**2])
            try:
                w=A.T @ np.linalg.solve(A@A.T,np.array([0,1,0]))
            except np.linalg.LinAlgError:
                continue
            if n>3:
                arbitrary=gen.normal(size=n)
                w=w+(np.eye(n)-A.T@np.linalg.solve(A@A.T,A))@arbitrary
            if max(abs(A@w-np.array([0,1,0])))>1e-7:
                continue
            C=np.sum(abs(w)*abs(nodes)**3)
            V=np.dot(w,w)
            # Rescale all nodes by c and all weights by 1/c, optimizing scale.
            # risk(c) = C^2*c^4/36 + V/c^2.
            c=(18*V/(C*C))**(1/6)
            achieved=C*C*c**4/36+V/c**2
            assert achieved+1e-8 >= lower,(n,achieved,lower)
            count+=1
    assert count>=9000
    print(f'{count} feasible full-domain inequality spot checks: PASS')


def main():
    scalar_check()
    direct_check()
    arbitrary_feasible_stencils()
    print('VERIFICATION PASSED; finite tests are supplementary to the proof.')

if __name__ == '__main__':
    main()
