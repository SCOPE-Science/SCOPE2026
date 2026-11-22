"""Numerical and exact consistency tests for planar dual-curvature rectangle inverse law.

No external dependencies. Run: python3 verify.py
Finite testing corroborates, but does not replace, the analytic proof.
"""
from math import atan, cos, asinh, isclose, log, sqrt
from fractions import Fraction


def simpson(f, lo, hi, n=2048):
    assert n % 2 == 0
    h = (hi - lo) / n
    acc = f(lo) + f(hi)
    for k in range(1, n):
        acc += (4 if k % 2 else 2) * f(lo + k * h)
    return acc * h / 3


def atom_mass_cone(a, b, q):
    p = (q - 2) / 2
    return a * b * simpson(lambda t: (a*a + b*b*t*t)**p, 0, 1)


def atom_mass_angular(a, b, q):
    # Independent spherical definition: (1/2) integral on angular normal preimage.
    theta = atan(b / a)
    return a**q * simpson(lambda u: cos(u)**(-q), 0, theta, 16384)


def general_rectangle_masses(am, ap, bm, bp, q):
    p=(q-2)/2
    return (ap/2*simpson(lambda y:(ap*ap+y*y)**p,-bm,bp),
            am/2*simpson(lambda y:(am*am+y*y)**p,-bm,bp),
            bp/2*simpson(lambda x:(bp*bp+x*x)**p,-am,ap),
            bm/2*simpson(lambda x:(bm*bm+x*x)**p,-am,ap))


def opposite_pair_mass(s, q):
    p = (q-2)/2
    return s*simpson(lambda y:(s*s+y*y)**p,0,1,4096)


def asymmetric_witness(q):
    assert 0<q<1
    left=.05
    target=opposite_pair_mass(left,q)
    peak_right = {0.25:0.2, 0.5:0.4, 0.75:1.0}[q]
    assert opposite_pair_mass(peak_right,q)>target
    lo,hi=peak_right,1000.0
    assert opposite_pair_mass(hi,q)<target
    for _ in range(64):
        mid=(lo+hi)/2
        if opposite_pair_mass(mid,q)>target:
            lo=mid
        else:
            hi=mid
    return left,(lo+hi)/2


def ratio(r, q):
    return atom_mass_cone(r, 1, q) / atom_mass_cone(1, r, q)


def invert_ratio(rho, q):
    assert q != 2
    decreasing = q < 2
    lo, hi = -10.0, 10.0
    from math import exp
    for _ in range(130):
        mid = (lo + hi) / 2
        m = ratio(exp(mid), q)
        if (m > rho) == decreasing:
            lo = mid
        else:
            hi = mid
    return exp((lo+hi)/2)


def attainable(rho, q):
    if q == 2:
        return rho == 1
    if q <= 1:
        return rho > 0
    lower, upper = sorted((q-1, 1/(q-1)))
    return lower < rho < upper


def test():
    cases = 0
    for q in (0.3, 0.75, 1.0, 1.5, 1.95, 2.0, 2.2, 3.0, 4.0, 6.0):
        for a, b in ((1,1), (1,2), (2,1), (0.25,3), (7,0.4)):
            for x,y in ((a,b),(b,a)):
                lhs = atom_mass_cone(x,y,q)
                rhs = atom_mass_angular(x,y,q)
                assert abs(lhs-rhs) < 8e-9 * max(lhs,rhs,1), (q,x,y,lhs,rhs)
                cases += 1
    for a,b in ((1,1),(2,3),(7,11),(Fraction(3,7),Fraction(19,4))):
        a,b = Fraction(a),Fraction(b)
        # q=4 cone mass is an exact degree-four polynomial in side lengths.
        m = a*b*(a*a+b*b/Fraction(3))
        assert m == a*b*(3*a*a+b*b)/3
        assert isclose(float(m),atom_mass_cone(float(a),float(b),4),rel_tol=2e-12)
        assert isclose(atom_mass_cone(float(a),float(b),2),float(a*b),rel_tol=2e-12)
        cases += 2
    for q in (0.5, 1, 1.5, 1.95, 2.2, 3, 4, 6):
        vals = [ratio(r,q) for r in (0.08,0.15,0.4,1,2,4,15)]
        assert all((u>v if q<2 else u<v) for u,v in zip(vals,vals[1:])), (q,vals)
        for r in (0.2,0.5,1,2,6):
            assert isclose(ratio(r,q)*ratio(1/r,q),1,rel_tol=2e-12)
            r2 = invert_ratio(ratio(r,q),q)
            assert abs(log(r2/r)) < 1e-9, (q,r,r2)
            cases += 2
    assert isclose(ratio(sqrt(5),4),2,rel_tol=2e-12)
    assert isclose(ratio(4,1),4*asinh(.25)/asinh(4),rel_tol=2e-12)
    assert all(ratio(7,2)==1 for _ in range(2))
    for q,rho in ((1.5,0.49),(1.5,0.5),(1.5,0.75),(1.5,1.5),(1.5,2.0),(1.5,2.1),(4,0.3),(4,1/3),(4,2),(4,3),(4,3.1)):
        if attainable(rho,q):
            z=invert_ratio(rho,q)
            assert isclose(ratio(z,q),rho,rel_tol=1e-10)
        cases+=1
    for q in (0.25,0.5,0.75):
        left,right=asymmetric_witness(q)
        axp,axm,ayp,aym=general_rectangle_masses(left,right,1,1,q)
        assert right!=left and abs(axp-axm)<1e-9
        assert isclose(ayp,aym,rel_tol=1e-12)
        rho=axp/ayp
        r=invert_ratio(rho,q)
        b=(ayp/(r*simpson(lambda t:(1+r*r*t*t)**((q-2)/2),0,1)))**(1/q)
        ac,bc=r*b,b
        xm,xn,ym,yn=general_rectangle_masses(ac,ac,bc,bc,q)
        assert isclose(xm,axp,rel_tol=1e-8) and isclose(ym,ayp,rel_tol=1e-8)
        cases+=3
    for q in (1,1.5,2,3,4):
        p=(q-2)/2
        for s in (.2,.6,1.5,4):
            derivative=simpson(lambda y:(s*s+y*y)**(p-1)*((q-1)*s*s+y*y),-1,1)
            assert derivative>0
            cases+=1
    print(f'PASS {cases} cone/angular/exact/monotonic/inverse/symmetry checks')


if __name__ == '__main__':
    test()
