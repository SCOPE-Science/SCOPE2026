"""Standalone reproducibility checks for a one-dimensional flow/branching threshold.
Only standard Python libraries are used. Numerical examples check, not replace, the analytic proof.
"""
from fractions import Fraction
from math import tanh, exp, isclose


def riccati(q, h, t):
    z=tanh(q*t)
    return (q*q*z+h*q)/(q+h*z)


def top_growth_for_atom(D,v,L,beta,a):
    assert all(z>0 for z in (D,v,L,beta)) and 0<a<L and beta>v
    h=v/(2*D)
    def f(q): return riccati(q,h,a)+riccati(q,h,L-a)-beta/D
    lo=h
    hi=max(2*h,beta/D+2*h)
    assert f(lo)<0 and f(hi)>0,(f(lo),f(hi))
    for _ in range(160):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    q=(lo+hi)/2
    return D*(q*q-h*h),q


def check():
    # Exact completion of squares at arbitrary rational coefficients.
    D=Fraction(7,5); v=Fraction(4,3); h=v/(2*D)
    for u0,ua,uL,aa,bb in [(Fraction(2),Fraction(3),Fraction(5),Fraction(1,7),Fraction(5,9)),
                              (Fraction(-2),Fraction(8,3),Fraction(1,3),Fraction(4,5),Fraction(1,4))]:
        # Construct a continuous piecewise-linear test u across (0,a,L):
        slope1=(ua-u0)/aa; slope2=(uL-ua)/bb
        # E= D int u'^2 +D h (u0^2+uL^2)+ D h^2 int u^2
        iu2=(aa*(u0*u0+u0*ua+ua*ua)+bb*(ua*ua+ua*uL+uL*uL))/3
        energy=D*(aa*slope1*slope1+bb*slope2*slope2)+D*h*(u0*u0+uL*uL)+D*h*h*iu2
        # completed square: D int_0^a (u'-hu)^2 + D int_a^L (u'+hu)^2
        left=D*(aa*slope1*slope1-h*(ua*ua-u0*u0)+h*h*aa*(u0*u0+u0*ua+ua*ua)/3)
        right=D*(bb*slope2*slope2+h*(uL*uL-ua*ua)+h*h*bb*(ua*ua+ua*uL+uL*uL)/3)
        assert energy-v*ua*ua==left+right
        assert left>=0 and right>=0
    # Boundary conditions and distributional jump at critical beta=v.
    for D,v,L,a in [(1.,1.,3.,.25),(.4,3.,2.,.8),(2.,.3,8.,4.)]:
        h=v/(2*D)
        phi_left=lambda x:1.
        phi_right=lambda x:exp(-2*h*(x-a))
        assert isclose(phi_left(a),phi_right(a))
        assert isclose(D*(-2*h)-0,-v,rel_tol=1e-14)
        assert isclose(D*(-2*h*phi_right(L))+v*phi_right(L),0,abs_tol=1e-13)
    # Exact threshold ratio and symmetric, strict position ordering for beta>v.
    for D,v,L,beta in [(1.,2.,3.,3.),(.1,1.,2.,1.8),(.5,.3,5.,3.)]:
        aa=[.04*L,.15*L,.35*L,.5*L]
        spec=[top_growth_for_atom(D,v,L,beta,a)[0] for a in aa]
        assert spec[0]>spec[1]>spec[2]>spec[3]>0,(D,v,L,beta,spec)
        for a,la in zip(aa,spec):
            assert isclose(la,top_growth_for_atom(D,v,L,beta,L-a)[0],rel_tol=2e-13)
    # At B=2, D=.01, v=L=1, uniform b=2 has lambda<=-23;
    # concentrated atom b=2 delta_(1/2) has lambda>0.
    assert 2.-1./(4*.01) < 0
    assert top_growth_for_atom(.01,1.,1.,2.,.5)[0]>0
    print('PASS: exact rational square identities, critical atom, three strict supercritical location orders, and dispersal-versus-concentration witness')

if __name__=='__main__': check()
