"""Exact stationary energy-covariance calculations for a telegraph-driven inertial harmonic particle.

Run: python verify.py
Requires: sympy.
All mathematical assertions are exact; sample cases do not replace the global proof.
"""
import sympy as S

G, R = S.symbols('g rho', positive=True)
P = (48*R**4 + 192*G*R**3 + (288*G**2+104)*R**2
     + (138*G**3+136*G)*R + 3*(6*G**2-1)*(G**2+3))
H = (G*(3*G**2+4)*(2*G*R+4*R**2+1)**2
     *(6*G*R+4*R**2+9)*(2*G**2+6*G*R+4*R**2+1))
CLOSED = -4*R*P/H


def stationarity_moments(g, rho):
    """Solve successive homogeneous-degree generator equations independently."""
    ordinary = {(0, 0): S.Integer(1)}
    signed = {(0, 0): S.Integer(0)}
    for degree in range(1, 5):
        target = signed if degree % 2 else ordinary
        other = ordinary if degree % 2 else signed
        unknowns = [S.Symbol('u%d_%d' % (degree, k)) for k in range(degree + 1)]
        unknown = {(i, degree-i): unknowns[i] for i in range(degree + 1)}
        identities = []
        for (i,j), z in unknown.items():
            eq = i*unknown.get((i-1,j+1), 0) - j*unknown.get((i+1,j-1), 0) - g*j*z
            eq += j*other.get((i,j-1), 0)
            if degree % 2:
                eq -= 2*rho*z
            identities.append(eq)
        mat, rhs = S.linear_eq_to_matrix(identities, unknowns)
        sol = mat.inv()*rhs
        for idx, (ij,_) in enumerate(unknown.items()):
            target[ij] = S.factor(sol[idx])
    return ordinary, signed


def check_all():
    assert S.expand(P - (18*G**4+138*G**3*R+288*G**2*R**2+51*G**2
                         +192*G*R**3+136*G*R+48*R**4+104*R**2-9)) == 0
    ordinary, signed = stationarity_moments(G,R)
    A = 2*G*R+4*R**2+1
    assert S.factor(ordinary[(2,0)] - (G+2*R)/(G*A)) == 0
    assert S.factor(ordinary[(0,2)] - 2*R/(G*A)) == 0
    assert ordinary[(1,1)] == 0
    assert S.factor(ordinary[(2,2)] - ordinary[(2,0)]*ordinary[(0,2)] - CLOSED) == 0
    # Independently verify all stationary generator equations, without trusting algebraic displays.
    count=4
    for degree in range(1,5):
        targ = signed if degree%2 else ordinary
        other = ordinary if degree%2 else signed
        for i in range(degree+1):
            j=degree-i
            lhs=i*targ.get((i-1,j+1),0)-j*targ.get((i+1,j-1),0)-G*j*targ[(i,j)]
            lhs+=j*other.get((i,j-1),0)
            if degree%2:lhs-=2*R*targ[(i,j)]
            assert S.cancel(lhs)==0,(degree,i)
            count+=1
    # The sign classification is global because every denominator factor is positive,
    # the switching-rate derivative of P is positive, and P(g,0) has a unique positive zero.
    assert S.expand(P.subs(R,0)-3*(6*G**2-1)*(G**2+3))==0
    for derivative in (S.diff(P,R),S.diff(P,G)):
        poly=S.Poly(derivative,G,R)
        assert all(c>=0 for c in poly.coeffs())
        assert any(c>0 for c in poly.coeffs())
        count+=2
    assert S.simplify(P.subs(G,0).subs(R,S.sqrt(3)/6))==0
    assert S.expand(S.diff(P,R).subs(R,0) - (138*G**3+136*G))==0
    count+=2
    gs=[S.Rational(k,l) for k,l in [(1,10),(1,5),(1,4),(1,3),(2,5),(1,2),(1,1),(2,1),(3,1)]]
    rs=[S.Rational(k,l) for k,l in [(1,50),(1,10),(1,5),(1,2),(1,1),(3,1)]]
    for g in gs:
        for rho in rs:
            mm,_=stationarity_moments(g,rho)
            exact=S.factor(mm[(2,2)]-mm[(2,0)]*mm[(0,2)])
            assert S.factor(exact-CLOSED.subs({G:g,R:rho}))==0,(g,rho)
            assert S.sign(exact)==-S.sign(P.subs({G:g,R:rho}))
            count+=2
    assert CLOSED.subs({G:S.Rational(1,5),R:S.Rational(1,100)})>0
    assert CLOSED.subs({G:S.Rational(1,5),R:S.Rational(1,2)})<0
    assert CLOSED.subs({G:S.Rational(1,2),R:S.Rational(1,100)})<0
    count+=3
    print('PASS: %d exact identities, independent rational solves, and sign assertions'%count)
    print('Example g=1/5, rho=1/100: energy covariance > 0')
    print('Example g=1/5, rho=1/2: energy covariance < 0')
    print('Endpoint g=0: rho*=sqrt(3)/6; endpoint rho=0: g*=1/sqrt(6)')

if __name__=='__main__':
    check_all()
