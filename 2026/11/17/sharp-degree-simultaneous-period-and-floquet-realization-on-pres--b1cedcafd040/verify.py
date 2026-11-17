"""Independent arithmetic and ODE checks for prescribed circular cycles.

Run: python3 verify.py. Requires NumPy, SciPy, and SymPy.
The analytic argument, not finite sampling, proves the general theorem.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import BarycentricInterpolator
import sympy as sp


def construct(radii, periods, log_multipliers):
    radii = np.asarray(radii, float)
    periods = np.asarray(periods, float)
    logarithms = np.asarray(log_multipliers, float)
    nodes = radii**2
    assert np.all(radii > 0) and np.all(np.diff(nodes) > 0)
    assert np.all(periods > 0) and np.all(logarithms != 0)
    deriv = np.array([np.prod(nodes[i]-np.delete(nodes, i)) for i in range(len(nodes))])
    bound = max(abs(logarithms/(2*deriv*radii*periods)))
    K = max(1.0, 3.0*bound)
    z = -logarithms/(2*K*deriv*radii*periods)
    assert np.all(np.abs(z) < 1)
    w = 2*math.pi/periods
    aval = w*(1+z*z)/(1-z*z)
    bval = 2*w*z/(radii*(1-z*z))
    A = (lambda xx: aval[0]) if len(nodes) == 1 else BarycentricInterpolator(nodes, aval)
    B = (lambda xx: bval[0]) if len(nodes) == 1 else BarycentricInterpolator(nodes, bval)
    return nodes, deriv, K, z, aval, bval, A, B


def check_case(radii, periods, logarithms):
    nodes, deriv, K, z, aval, bval, A, B = construct(radii, periods, logarithms)
    radii = np.asarray(radii, float)
    periods = np.asarray(periods, float)
    logarithms = np.asarray(logarithms, float)
    assert np.all(aval > np.abs(radii*bval))
    for i,r in enumerate(radii):
        a, b = float(A(nodes[i])), float(B(nodes[i]))
        assert abs(a-aval[i]) < 2e-11 and abs(b-bval[i]) < 2e-11
        C = lambda th: a+r*b*math.cos(th)
        tcalc = quad(lambda th: 1/C(th), 0, 2*math.pi, epsabs=2e-12)[0]
        ecalc = 2*K*r*deriv[i]*quad(lambda th: math.cos(th)/C(th), 0, 2*math.pi, epsabs=2e-12)[0]
        assert abs(tcalc-periods[i]) < 2e-10*(1+periods[i])
        assert abs(ecalc-logarithms[i]) < 2e-10*(1+abs(logarithms[i]))
        # Integrate physical flight time and normal cocycle along a full turn.
        fun = lambda th, y: [-1/C(th), -2*K*r*deriv[i]*math.cos(th)/C(th)]
        sol = solve_ivp(fun, [0,-2*math.pi], [0.,0.], method='DOP853',
                        rtol=3e-12, atol=3e-13)
        assert sol.success
        assert abs(sol.y[0,-1]-periods[i]) < 2e-9*(1+periods[i])
        assert abs(sol.y[1,-1]-logarithms[i]) < 2e-9*(1+abs(logarithms[i]))
    return len(radii)


def check_symbolic():
    x,y=sp.symbols('x y',real=True)
    s=x*x+y*y
    F=(s-1)*(s-4)
    A=sp.Rational(5,3)+(s-1)/sp.Integer(7)
    B=sp.Rational(1,5)-(s-1)/sp.Integer(11)
    K=sp.Rational(7,3)
    P=K*F + y*(A+x*B)
    Q=-x*(A+x*B)
    assert sp.expand(x*P+y*Q-K*x*F)==0
    assert sp.Poly(P,x,y).total_degree()==4
    assert sp.Poly(Q,x,y).total_degree()==4
    # At a root of F, the tangential speed is exactly -[A(s)+x B(s)].
    angular=sp.expand((x*Q-y*P)/s)
    assert sp.simplify(angular + (A+x*B) + K*y*F/s)==0


def main():
    check_symbolic()
    cases=[
        ([1.0], [2*math.pi], [-1.3]),
        ([1.,2.], [2*math.pi,math.pi], [math.log(2),math.log(5)]),
        ([1.,1.5,2.], [3.,5.,7.], [0.7,-0.3,1.2]),
        ([0.75,1.25,2.,3.], [2.2,3.7,4.9,6.2], [-1.1,0.4,-0.7,1.9])
    ]
    checks=sum(check_case(*c) for c in cases)
    print('PASS: exact symbolic radial/angular identities; total-degree witness')
    print(f'PASS: {checks} prescribed circles in four families, independent quadrature and ODE flight/normal exponents')
    print('PASS: same-sign multipliers on the two prescribed circles (no enforced alternation)')
    print('LIMIT: finite computations are supplementary to the theorem for arbitrary radii, periods, and multipliers')

if __name__ == '__main__':
    main()
