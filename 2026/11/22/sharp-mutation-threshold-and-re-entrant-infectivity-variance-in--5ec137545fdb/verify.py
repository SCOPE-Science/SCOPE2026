"""Independent symbolic identities and numerical checks for bimodal trait variance.

Dependencies: Python 3, sympy, scipy, numpy.
The analytic theorem and sign certificates are contained in RESULT.md;
numerical checks below are corroborative, not a proof over infinite time.
"""
from fractions import Fraction
from math import sqrt
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad


def symbolic_checks():
    x, m, v, k, S, diffusion, mu = sp.symbols(
        'x m v k S diffusion mu', positive=True, real=True
    )
    # Gaussian log derivative, using m'=k*S*v and v'=diffusion.
    dlog_phi = -diffusion / (2*v) + k*S*(x-m) + diffusion*(x-m)**2 / (2*v**2)
    d2_phi_over_phi = (x-m)**2/v**2 - 1/v
    dlog_mass = k*S*m-mu
    residual = sp.simplify(dlog_mass+dlog_phi - (k*S*x-mu) -diffusion*d2_phi_over_phi/2)
    assert residual == 0, 'Gaussian component PDE residual'
    p, gap, i = sp.symbols('p gap i', positive=True, real=True)
    pprime = k*S*gap*p*(1-p)
    variance_prime = sp.expand(diffusion+gap**2*(1-2*p)*pprime)
    assert sp.simplify(variance_prime-(diffusion-k*S*gap**3*p*(1-p)*(2*p-1))) == 0
    g=p*(1-p)*(2*p-1)
    root=(1+1/sp.sqrt(3))/2
    assert sp.simplify(sp.diff(g,p).subs(p,root)) == 0
    assert sp.simplify(g.subs(p,root)-1/(6*sp.sqrt(3))) == 0
    assert sp.simplify(g.subs(p,sp.Rational(3,5))-sp.Rational(6,125))==0
    assert sp.simplify(g.subs(p,sp.Rational(4,5))-sp.Rational(12,125))==0
    # p'(t), i'(t) and component mass derivatives are algebraically compatible.
    z=sp.symbols('z',real=True)
    abar=sp.symbols('abar',real=True)
    mass_hi_dot_over_i = (k*S*(abar+gap)-mu)*p
    mass_hi_from_ip = sp.expand(p*(k*S*(abar+gap*p)-mu)+pprime)
    assert sp.simplify(mass_hi_dot_over_i-mass_hi_from_ip)==0
    print('Symbolic Gaussian PDE, mixture ODE, variance, maximizer: PASS')


def explicit_certificate():
    k=Fraction(10); gap=Fraction(1,10); diffusion=Fraction(1,1600)
    p0=Fraction(3,5); s0=1-Fraction(1,1000000)
    g=lambda p:p*(1-p)*(2*p-1)
    assert diffusion-k*s0*gap**3*g(p0)>0
    assert diffusion-k*Fraction(9,10)*gap**3*g(Fraction(4,5))<0
    # For t in [0,2], z <= k*(2*v0 + 2*diffusion)=127/10000.
    zmax=k*(2*Fraction(1,100000)+2*diffusion)
    assert zmax==Fraction(127,10000)
    assert k*(Fraction(1,5)+zmax+gap)<4
    # e<3 implies e^8<3^8. Gronwall gives s(t)>1-i0*3^8>0.9.
    assert 1-Fraction(3**8,10**6)>Fraction(9,10)
    # At t=2 the logistic logit advances by >1.8 > log(8/3).
    assert Fraction(9,10)*2>1
    # And exp(1)>8/3 from its rational Taylor terms through 1/4!.
    assert sum(Fraction(1,sp.factorial(j)) for j in range(5))>Fraction(8,3)
    print('Rational sharp-threshold and two-reversal sign certificate: PASS')


def trajectory_and_moments():
    k=10.;mu=1.;gap=.1; diffusion=1/1600;v0=1/100000; a=.2
    i0=1e-6;p0=.6
    def rhs(t,y):
        infected,recovered,p,z=y
        susceptible=1-infected-recovered
        mean=a+z+gap*p
        return [infected*(k*susceptible*mean-mu), mu*infected,
                k*gap*susceptible*p*(1-p),k*susceptible*(v0+diffusion*t)]
    sol=solve_ivp(rhs,(0,6),[i0,0,p0,0],dense_output=True,
                  rtol=1e-11,atol=1e-14,max_step=.025)
    assert sol.success
    def stats(t):
        infected,recovered,p,z=sol.sol(t)
        susceptible=1-infected-recovered
        variance=v0+diffusion*t+gap*gap*p*(1-p)
        derivative=diffusion-k*gap**3*susceptible*p*(1-p)*(2*p-1)
        return infected,recovered,p,z,susceptible,variance,derivative
    assert stats(0)[-1]>0
    assert stats(.6)[-1]<0
    assert stats(3)[-1]>0
    assert stats(1)[4]>.9
    for t in (.1,.6,2.5):
        infected,recovered,p,z,susceptible,variance,derivative=stats(t)
        v=v0+diffusion*t
        m0=a+z;m1=m0+gap
        def phi(x,m): return np.exp(-((x-m)**2)/(2*v))/np.sqrt(2*np.pi*v)
        def distribution(x):return (1-p)*phi(x,m0)+p*phi(x,m1)
        mean=quad(lambda x:x*distribution(x),m0-12*np.sqrt(v),m1+12*np.sqrt(v),epsabs=1e-12)[0]
        var=quad(lambda x:(x-mean)**2*distribution(x),m0-12*np.sqrt(v),m1+12*np.sqrt(v),epsabs=1e-12)[0]
        assert abs(var-variance)<1e-10,(t,var,variance)
    print('Numerical ODE sign changes and independent mixture quadrature: PASS')
    print('Vprime(t=0,0.6,3):',*[f'{stats(t)[-1]:.12g}' for t in (0,.6,3)])
    print('Universal diffusion cutoff for witness: ',f'{k*(1-i0)*gap**3/(6*sqrt(3)):.12g}')


if __name__=='__main__':
    symbolic_checks()
    explicit_certificate()
    trajectory_and_moments()
    print('ALL CHECKS PASSED')
