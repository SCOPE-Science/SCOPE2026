"""Exact stationary-current coefficient certificates for open site-departure exclusion.

Requirements: Python 3 and SymPy. Run: python verify.py
"""
from itertools import product
from sympy import Matrix, Rational, symbols, factor, simplify, nroots


def matrices(rates):
    """Column generator Q(delta)=Q0+delta Q1, mean bath density 1/2."""
    n = len(rates)
    states = list(product((0, 1), repeat=n))
    where = {state: i for i, state in enumerate(states)}
    delta = symbols("delta")
    left = Rational(1, 2) + delta / 2
    right = Rational(1, 2) - delta / 2
    Q = Matrix.zeros(2**n)

    for j, state in enumerate(states):
        def transition(new, rate):
            k = where[tuple(new)]
            Q[k, j] += rate
            Q[j, j] -= rate

        for site, bath in ((0, left), (n - 1, right)):
            new = list(state)
            new[site] = 1 - new[site]
            rate = bath if state[site] == 0 else rates[site] * (1 - bath)
            transition(new, rate)
        for site in range(n - 1):
            if state[site] != state[site + 1]:
                new = list(state)
                new[site], new[site + 1] = new[site + 1], new[site]
                rate = rates[site] if state[site] == 1 else rates[site + 1]
                transition(new, rate)

    J = Matrix([rates[0] if x[:2] == (1, 0) else
                -rates[1] if x[:2] == (0, 1) else 0 for x in states])
    return Q.subs(delta, 0), Q.diff(delta), J, states


def coefficient(rates):
    Q0, Q1, J, states = matrices(rates)
    n = len(rates)
    equilibrium = Matrix([
        __import__('sympy').prod(1 / rates[k] if x[k] else 1 for k in range(n))
        for x in states
    ])
    equilibrium /= sum(equilibrium)
    A = Q0.copy()
    A[-1, :] = Matrix.ones(1, 2**n)

    def zero_sum_rhs(v):
        rhs = v.copy()
        rhs[-1] = 0
        return rhs

    p1 = A.inv() * zero_sum_rhs(-Q1 * equilibrium)
    p2 = A.inv() * zero_sum_rhs(-Q1 * p1)
    return factor((J.T * p2)[0])


def main():
    t = symbols('t', positive=True)
    p = (5148*t**8 - 61284*t**7 - 275777*t**6 - 414618*t**5
         - 292561*t**4 - 103752*t**3 - 19176*t**2 - 2304*t - 144)
    d = (t+1)**2 * (2*t+1)**2 * (324*t**3+987*t**2+700*t+108)**2
    expected = 4*t*p/d
    observed = coefficient((t, 1, 2*t))
    assert simplify(observed - expected) == 0
    print('Exact three-site quadratic coefficient verified.')
    assert p.subs(t, 15) < 0 < p.subs(t, 16)
    # Descending coefficient sequence has exactly one sign change.
    coeffs = __import__('sympy').Poly(p,t).all_coeffs()
    assert coeffs[0] > 0 and all(c < 0 for c in coeffs[1:])
    root = [z for z in nroots(p, maxsteps=250) if abs(float(__import__('sympy').im(z))) < 1e-12 and float(__import__('sympy').re(z)) > 0]
    assert len(root) == 1
    print('Unique positive threshold:', root[0])

    a,c = symbols('a c',positive=True)
    two_expected = (8*a*c*(a-c)*(a*a+6*a*c+4*a+c*c+4*c)
                    / ((a+1)**2*(c+1)**2*(5*a+5*c+2)**2))
    two_observed = coefficient((a,c))
    assert simplify(two_observed-two_expected) == 0
    print('Exact two-site no-reversal comparator verified.')
    print('PASS')


if __name__ == '__main__':
    main()
