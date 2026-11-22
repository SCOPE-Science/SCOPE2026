"""Standalone checks for an entropy capture theorem in a trophic Allee model.

Proof of the all-parameter statement is in RESULT.md; these calculations
independently check its algebra and one biologically feasible calibration.
"""
import math
import sympy as sp
from scipy.integrate import solve_ivp


def symbolic_checks():
    u, r, s, v, w = sp.symbols('u r s v w', positive=True)
    a, d, e, b, c = sp.symbols('a d e b c', positive=True)
    F = lambda x: (1-a*x)*(x-b)/(x+c)
    D = (b+c)*(1+a*c)
    assert sp.simplify(F(u)-F(s)-(u-s)*(-a+D/((u+c)*(s+c)))) == 0
    # Distinct roots F(r)=F(s) force D=a(r+c)(s+c).
    assert sp.simplify((F(r)-F(s))/(r-s) + a-D/((r+c)*(s+c))) == 0
    vstar = F(s)
    wstar = s-d
    # On the comparison equilibrium, the apex mortality is e*vstar.
    dH = ((u-s)*(F(u)-v)
          +(v-vstar)*(u-w-d)
          +(w-wstar)*(v-vstar))
    assert sp.simplify(dH-(u-s)*(F(u)-vstar)) == 0
    root_factorization = ((u-s)*(u-s)*
                          (-a + a*(r+c)/(u+c)))
    claimed = -a*(u-s)**2*(u-r)/(u+c)
    assert sp.simplify(root_factorization-claimed) == 0
    # The positive humps are always strictly concave.
    assert sp.simplify(sp.diff(F(u),u,2)+2*D/(u+c)**3) == 0
    return True


def example_checks():
    u=sp.symbols('u',positive=True)
    a=sp.Rational(1,10); d=sp.Rational(1,10)
    e=sp.Rational(1,4); g=sp.Rational(3,20)
    b=c=sp.Rational(1,5)
    F=sp.factor((1-a*u)*(u-b)/(u+c))
    roots=sp.solve(sp.Eq(F,g/e),u)
    assert roots == [sp.Integer(1),sp.Rational(16,5)],roots
    r,s=roots
    vstar=g/e; wstar=s-d
    assert (r,s,vstar,wstar)==(1,sp.Rational(16,5),sp.Rational(3,5),sp.Rational(31,10))
    assert sp.simplify((u-s)*(F-vstar) + a*(u-s)**2*(u-r)/(u+c)) == 0
    barrier=float(sp.N(r-s-s*sp.log(r/s),40))
    x0=(2.0, 0.6, 3.1)
    h=lambda x,z: x-z-z*math.log(x/z)
    def H(x):return h(x[0],float(s))+h(x[1],float(vstar))+(1/float(e))*h(x[2],float(wstar))
    assert 1.52208<barrier<1.52209
    assert 0.30401<H(x0)<0.30402
    assert H(x0)<barrier
    def rhs(t,x):
        uu,vv,ww=x
        ff=(1-float(a)*uu)*(uu-float(b))/(uu+float(c))
        return [uu*(ff-vv), vv*(uu-ww-float(d)),ww*(float(e)*vv-float(g))]
    sol=solve_ivp(rhs,(0,500),x0,rtol=1e-11,atol=1e-12,dense_output=False,
                  max_step=0.1)
    assert sol.success
    assert min(sol.y[0])>float(r)
    assert max(H(sol.y[:,i]) for i in range(sol.y.shape[1])) <barrier
    assert max(abs(sol.y[i,-1]-z) for i,z in enumerate([float(s),float(vstar),float(wstar)]))<1e-6
    return {'roots': [str(q) for q in roots], 'barrier':barrier,
            'witness_H':H(x0), 'terminal': [float(x) for x in sol.y[:,-1]],
            'num_trajectory_points':sol.y.shape[1]}


def test_jensen():
    # A nonconstant positive periodic trajectory (if one exists) must obey
    # <F(u)>=v*, and F concavity gives F(<u>)>v*.
    u=sp.symbols('u',positive=True)
    a=sp.Rational(1,10);b=c=sp.Rational(1,5)
    F=(1-a*u)*(u-b)/(u+c)
    assert sp.simplify(sp.diff(F,u,2) + sp.Rational(102,125)/(u+sp.Rational(1,5))**3) == 0
    return True


if __name__=='__main__':
    symbolic_checks()
    result=example_checks()
    test_jensen()
    print('PASS: exact cancellation, two-root factorization, strong concavity, numerical example')
    print(result)
