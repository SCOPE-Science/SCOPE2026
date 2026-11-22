"""Independent finite-rate quadrature checks for a fast stochastic-return Laplace law.

Run: python CHECKER.py (requires NumPy and SciPy).
All coordinates are dimensionless: generator d^2/dx^2 in search,
return generator d^2/dx^2 - 2*x*d/dx, starting from 0, target at 1.
The renewal values use an exact killed Brownian Green kernel.
These checks do not prove the arbitrary-clock asymptotic theorem.
"""
import math
from scipy.special import pbdv
from scipy.integrate import quad

KAPPA = 2.0
COUNTS = 0


def verify(cond, message):
    global COUNTS
    assert cond, message
    COUNTS += 1


def OU_fundamental(s, x, sign):
    nu = -s/KAPPA
    z = sign*math.sqrt(KAPPA)*x
    v, dv = pbdv(nu, z)
    factor = math.exp(KAPPA*x*x/4)
    return (factor*v,
            factor*(KAPPA*x*v/2 + sign*math.sqrt(KAPPA)*dv))


def return_functions(s):
    u1, _ = OU_fundamental(s, 1.0, -1)
    u0, du0 = OU_fundamental(s, 0.0, -1)
    v1, _ = OU_fundamental(s, 1.0, +1)
    v0, dv0 = OU_fundamental(s, 0.0, +1)
    det = v0*u1 - u0*v1
    def phi(x):
        return OU_fundamental(s, x, -1)[0]/u1
    def phi_prime(x):
        return OU_fundamental(s, x, -1)[1]/u1
    def q(x):
        if x <= 0:
            return OU_fundamental(s, x, -1)[0]/u0
        u = OU_fundamental(s, x, -1)[0]
        v = OU_fundamental(s, x, +1)[0]
        return (v*u1-u*v1)/det
    qp_left = du0/u0
    qp_right = (dv0*u1-du0*v1)/det
    C = qp_left-qp_right
    return phi, phi_prime, q, C


def killed_brownian_resolvent(r, s, x):
    w = math.sqrt(r+s)
    return (math.exp(-w*abs(x)) - math.exp(-w*(2-x)))/(2*w)


def poisson_exact(s, r, k1=0.0):
    # The resolvent below applies only to k1=0; the return stiffness is KAPPA.
    assert k1 == 0.0
    phi, phip, q, C = return_functions(s)
    G = lambda x: killed_brownian_resolvent(r,s,x)
    Iq = quad(lambda x: G(x)*q(x), -6, 0, epsabs=2e-13)[0]
    Iq += quad(lambda x: G(x)*q(x), 0, 1, epsabs=2e-13)[0]
    If = quad(lambda x: G(x)*x*phip(x), -6, 0, epsabs=2e-13)[0]
    If += quad(lambda x: G(x)*x*phip(x), 0, 1, epsabs=2e-13)[0]
    d = 1-r*Iq
    phi0=phi(0)
    via_potential=phi0+KAPPA*If/d
    # Independent direct renewal numerator: search absorption before the alarm,
    # plus discounted absorption on a return stage before returning to home.
    h=lambda x:phi(x)-phi0*q(x)
    Ih=quad(lambda x:G(x)*h(x), -6, 0, epsabs=2e-13)[0]
    Ih+=quad(lambda x:G(x)*h(x), 0, 1, epsabs=2e-13)[0]
    via_renewal=(math.exp(-math.sqrt(r+s))+r*Ih)/d
    return via_potential, via_renewal, d, C, phi0


def killed_brownian_density(t, x):
    return (math.exp(-x*x/(4*t))-math.exp(-(2-x)**2/(4*t))) / math.sqrt(4*math.pi*t)


def periodic_exact(s, r):
    phi, phip, q, C = return_functions(s)
    t=1/r
    Pt=lambda x:killed_brownian_density(t,x)
    iq=quad(lambda x:Pt(x)*q(x), -2, 0, epsabs=1e-12)[0]
    iq+=quad(lambda x:Pt(x)*q(x), 0, 1, epsabs=1e-12)[0]
    d=1-math.exp(-s*t)*iq
    def integrand(v):
        G=lambda x:killed_brownian_density(v,x)
        f=quad(lambda x:G(x)*x*phip(x), -2, 0, epsabs=1e-12)[0]
        f+=quad(lambda x:G(x)*x*phip(x), 0, 1, epsabs=1e-12)[0]
        return math.exp(-s*v)*f
    A=quad(integrand,0,t,epsabs=1e-11)[0]
    via_potential=phi(0)+KAPPA*A/d
    # Direct renewal computation for the finite-duration deterministic clock.
    h=lambda x:phi(x)-phi(0)*q(x)
    Ih=quad(lambda x:Pt(x)*h(x), -2, 0, epsabs=1e-12)[0]
    Ih+=quad(lambda x:Pt(x)*h(x), 0, 1, epsabs=1e-12)[0]
    direct=quad(lambda v:math.exp(-s*v-1/(4*v))/(math.sqrt(4*math.pi)*v**1.5), 0,t,epsabs=1e-12)[0]
    via_renewal=(direct+math.exp(-s*t)*Ih)/d
    return via_potential, via_renewal, d, C, phi(0)


def main():
    for s in (0.25,0.75,1.5):
        phi, phip, q, C = return_functions(s)
        verify(0<phi(0)<1, 'nontrivial pure-return transform')
        verify(C>0, 'positive return deficit cusp')
        verify(abs(phi(1)-1)<1e-13, 'absorbing boundary')
        verify(abs(q(0)-1)<1e-13 and abs(q(1))<1e-13, 'home/target boundary')
        for j in range(1,25):
            x=-2+3*j/25
            verify(0<phi(x)<1 and 0<q(x)<1, 'return boundary transform bounds')
            dx=1e-4
            d2=(phi(x+dx)-2*phi(x)+phi(x-dx))/(dx*dx)
            verify(abs(d2-KAPPA*x*phip(x)-s*phi(x))<3e-7, 'return ODE')
        prev_error=1e100
        for r in (100,400,1600,6400):
            F1,F2,d,_,phi0=poisson_exact(s,r)
            verify(0<d<1 and 0<F1<1, 'physical renewal transform')
            verify(abs(F1-F2)<2e-11, 'independent renewal/potential identity')
            assert F1>phi0
            exact=(F1-phi0)*r**1.5
            predicted=4*KAPPA*s*phi0/C
            verify(abs(exact-predicted)/predicted<0.13, 'Poisson sharp coefficient')
            verify(abs(exact-predicted)<prev_error, 'Poisson convergence')
            prev_error=abs(exact-predicted)
    s=0.75
    _,_,_,C=return_functions(s)
    phi0=return_functions(s)[0](0)
    predicted=KAPPA*s*phi0*math.sqrt(math.pi)/C
    previous=1e100
    for r in (25,100,400):
        F1,F2,d,_,pp=periodic_exact(s,r)
        verify(abs(F1-F2)<2e-9, 'periodic renewal/potential identity')
        verify(0<d<1, 'positive cycle success deficit')
        scaled=(F1-pp)*r**1.5
        verify(abs(scaled-predicted)/predicted<0.085, 'periodic clock asymptotic')
        verify(abs(scaled-predicted)<previous, 'periodic approach to limit')
        previous=abs(scaled-predicted)
    verify(abs((4*KAPPA*s*phi0/C)/predicted - 4/math.sqrt(math.pi))<1e-12,
           'universal Poisson-to-periodic prefactor ratio')
    print('PASS:', COUNTS, 'deterministic analytical/quadrature assertions')
    print('Poisson s=0.75 coefficient:', 4*KAPPA*s*phi0/C)
    print('Periodic s=0.75 coefficient:', predicted)
    print('Clock ratio:', 4/math.sqrt(math.pi))

if __name__=='__main__':
    main()
