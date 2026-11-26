"""Exact three-site current and optimization checks in occupation moments.

Requires SymPy. Run with Python 3, with no optimization flag (-O).
"""
from sympy import Matrix, Rational, cancel, diff, expand, factor, limit, simplify, sqrt, symbols, zeros
from sympy.polys.matrices import DomainMatrix


rho, delta, t = symbols('rho delta t', real=True)
half = Rational(1, 2)
left, right = rho + half*delta, rho - half*delta
sites = (1, 2, 4)  # Bit masks for left, centre and right.


def transitions(state):
    """Yield new state and rate multiplied by the common factor 4*t."""
    for mask, density in ((1, left), (4, right)):
        yield state ^ mask, 2*t*(1-density if state & mask else density)
    for p, q in ((1,2), (2,1), (2,4), (4,2)):
        if state & p and not state & q:
            yield state ^ (p | q), 2 if p == 2 else 2*t


def generator_on_moment(mask, state):
    return sum(rate*(int(target & mask == mask) - int(state & mask == mask))
               for target, rate in transitions(state))


def moment_system():
    # For each nonempty set S of sites, L prod_{i in S} eta_i is a
    # multilinear polynomial in occupation variables. Recover its coefficients
    # by successive Boolean differences, then take stationary expectations.
    coeff = zeros(7, 8)
    for moment in range(1, 8):
        row = [generator_on_moment(moment, x) for x in range(8)]
        for bit in sites:
            for mask in range(8):
                if mask & bit:
                    row[mask] -= row[mask ^ bit]
        coeff[moment-1, :] = Matrix([[expand(v) for v in row]])
    return coeff[:, 1:], -coeff[:, 0]


def currents(m):
    return ((m[1]-m[3])/2 - (m[2]-m[3])/(2*t),
            (m[2]-m[6])/(2*t) - (m[4]-m[6])/2,
            (left-m[1])/2)


def main():
    A, b = moment_system()
    Ad, bd = (z.to_dense() for z in DomainMatrix.unify(
        DomainMatrix.from_Matrix(A), DomainMatrix.from_Matrix(b)))
    num, den = Ad.solve_den(bd, method='rref')
    sol = num.to_Matrix() / Ad.domain.to_sympy(den)
    m = [1] + [cancel(v) for v in sol]
    assert all(cancel(v) == 0 for v in A*Matrix(m[1:])-b)

    B = t*(t-1)**2*delta**2 + 8*(t+1)*(2*t+1)*(1+rho*(t-1))
    J = delta*(2*t+1)*(t+1+rho*(t-1))/B
    for v in currents(m):
        assert cancel(v-J) == 0
    P = (2*(1+rho)*(delta**2+16*rho)*t**4
         +2*(3-rho)*(delta**2+16*rho)*t**3
         +(8*rho*(5-3*rho)-(3*rho+5)*delta**2)*t**2
         -4*(1-rho)*(delta**2+4*rho)*t+(1-rho)*(delta**2-8*rho))
    assert cancel(diff(J,t)+delta*P/B**2) == 0
    assert expand(P.subs(t,1)-144*rho) == 0
    assert cancel(J-delta/8+delta*t*(t-1)*(delta**2*(t-1)+8*rho*(2*t+1))/(8*B)) == 0
    assert cancel(J.subs(t,1)-delta/8) == 0
    assert cancel(limit(J,t,0,dir='+')-delta/8) == 0 and limit(J,t,'+oo') == 0
    case = {rho:half, delta:1}
    assert factor(P.subs(case)) == Rational(3,2)*(3*t+1)**2*(2*t**2+2*t-1)
    assert simplify(J.subs(case).subs(t,(sqrt(3)-1)/2)-(3*sqrt(3)-2)/23) == 0

    # Independently solve configuration-balance equations at admissible
    # rational points instead of substituting into the moment solution.
    samples = 0
    for density in (Rational(1,4), half, Rational(3,4)):
        for contrast in (Rational(1,4), half, 1):
            if contrast > 2*min(density, 1-density):
                continue
            for dwell in (Rational(1,5), Rational(1,3), 1, 2, 7):
                at = {rho:density, delta:contrast, t:dwell}
                Q = zeros(8)
                for x in range(8):
                    for y, rate in transitions(x):
                        rate = expand(rate).subs(at)
                        Q[y,x] += rate
                        Q[x,x] -= rate
                M = Q.copy()
                M[0,:] = Matrix([[1]*8])
                pi = M.inv()[:,0]
                assert all(v >= 0 for v in pi) and sum(pi) == 1 and Q*pi == zeros(8,1)
                moments = [sum(pi[x] for x in range(8) if x & mask == mask)
                           for mask in range(8)]
                assert all(cancel(v.subs(at)-J.subs(at)) == 0 for v in currents(moments))
                samples += 1
    assert samples == 35
    print('PASS: exact moment system, three currents, derivative, limits, factorization;',
          samples, 'rational configuration-balance checks.')


if __name__ == '__main__':
    main()
