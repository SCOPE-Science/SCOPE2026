"""Standalone numerical cross-checks for a two-state active particle in a piecewise-linear bistable trap.

The analytic stationary law and singular-limit theorem are established separately;
these finite tests serve only as reproducibility cross-checks.
"""
from math import exp, expm1, isclose
from scipy.integrate import quad


def rates(v, b, r_plus, r_minus):
    e = v - b
    assert e > 0 and b > 0 and r_plus > 0 and r_minus > 0
    left = r_minus / e - r_plus / (v + b)
    right = r_plus / e - r_minus / (v + b)
    assert left > 0 and right > 0
    return left, right


def stationary(v, b, a, r_plus, r_minus):
    L, R = rates(v, b, r_plus, r_minus)
    invC = exp(R*a) / L + expm1(R*a) / R + expm1(L*a) / L + exp(L*a) / R
    C = 1 / invC

    def density(x):
        if x < -a:
            return C * exp(R*a + L*(x+a))
        if x < 0:
            return C * exp(-R*x)
        if x < a:
            return C * exp(L*x)
        return C * exp(L*a - R*(x-a))

    right_mass = C * (expm1(L*a)/L + exp(L*a)/R)
    return density, right_mass, (L, R)


def run():
    tests = 0
    for b, a, v, rp, rm in [(1,2,2,.7,1.2), (1,1.2,1.3,1,1.1),
                             (2,.3,2.6,1.5,1.7),(.7,3,1.6,2.1,1.3),
                             (.9,.7,2.5,1,1)]:
        p, mass, (L, R) = stationary(v,b,a,rp,rm)
        segments = [(-float('inf'),-a),(-a,0),(0,a),(a,float('inf'))]
        vals = [quad(p,l,u,epsabs=1e-12)[0] for l,u in segments]
        assert isclose(sum(vals),1,abs_tol=1e-11)
        assert isclose(vals[2]+vals[3],mass,abs_tol=1e-11)
        tests += 2
        for x in [-a-1,-a/2,a/2,a+1]:
            f = b if (x < -a or 0 < x < a) else -b
            p_plus = p(x)*(v-f)/(2*v)
            p_minus = p(x)*(v+f)/(2*v)
            assert isclose((v+f)*p_plus,(v-f)*p_minus,rel_tol=1e-12)
            slope = L if f == b else -R
            # Steady plus-component transport equation.
            lhs = slope * (v+f)*p_plus
            rhs = -rp*p_plus+rm*p_minus
            assert isclose(lhs,rhs,rel_tol=1e-11,abs_tol=1e-13)
            tests += 2
    from scipy.special import expit
    for theta in [-3,-1,0,0.8,2.5]:
        for eps in [.2,.1,.05,.025,.0125]:
            b,a,r=1,1.4,1.1
            rp = r-theta*eps/(2*a)
            rm = r+theta*eps/(2*a)
            p,m,(L,R)=stationary(b+eps,b,a,rp,rm)
            assert abs(m-expit(theta)) < .2
            # Test local exponent limits (both sides of either well).
            assert abs(eps*L-r)<2*eps and abs(eps*R-r)<2*eps
            tests+=3
    print(f"Passed {tests} independent numerical identities and crossover checks")

if __name__=='__main__': run()
