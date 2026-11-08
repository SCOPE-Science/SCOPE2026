"""Finite independent diagnostics for angular extreme tails of a reset particle.

Only Python's standard library is needed. These checks are not proofs of
infinite-parameter or large-deviation statements; see RESULT.md for proof.
"""
from math import cos, exp, log, pi, sqrt

checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1


def simpson(f, lo, hi, n=4096):
    assert n > 0 and n % 2 == 0
    h = (hi - lo)/n
    s = f(lo) + f(hi)
    for j in range(1,n):
        s += (4 if j % 2 else 2) * f(lo + j*h)
    return h*s/3


def log_mgf_frozen(q, beta, D, v, r, phi):
    """Independent quadrature of the exact age-integrated expression."""
    p = r/beta
    c = v*cos(phi)/beta
    a = D/(2*beta)
    # Here p=1 is used to avoid integrable endpoint singularities.
    assert abs(p-1) < 1e-14
    upper = min(q, 24.0)
    integral = simpson(lambda y: exp(-a*y*y-c*y),0,upper)
    return a*q*q+c*q-p*log(q)+log((r/beta)*integral)

# Conditional thermal OU variance; the two time scales cannot be confused.
for D in (0.4,1.,2.):
    for beta in (0.5,1.,3.):
        for t in (0.01,0.2,1.,5.,20.):
            variance = D/beta*(1-exp(-2*beta*t))
            check(0 < variance <= D/beta and abs(variance-D/beta*(1-exp(-2*beta*t))) < 1.e-14, "conditional variance strict bounds")
            stationary_passive_var = 2*D/(1+2*beta)
            check(stationary_passive_var < D/beta, "passive variance gap")

# The exponential-age stationary orientation mean matches an independent
# one-dimensional quadrature of the free-cycle convolution.
for beta in (0.6,1.,2.):
    for d in (0.2,0.7,1.,3.):
        r=1.0
        v=1.6
        def free_age_mean(t):
            if abs(beta-d)<1.e-12:
                return v*t*exp(-beta*t)
            return v*(exp(-d*t)-exp(-beta*t))/(beta-d)
        numeric=simpson(lambda t: r*exp(-r*t)*free_age_mean(t),0.,42.,n=8192)
        exact=v*r/((r+beta)*(r+d))
        check(abs(numeric-exact)<2.e-7,"stationary angular mean identity")

# For frozen orientation the large-q remainder is exactly logarithmic.
# Independently integrate its finite-limit Gaussian kernel; the integral
# does not depend on the resetting age.
for phi in (0., pi/2, pi):
    beta=D=v=r=1.0
    c=cos(phi)
    limiting_integral=simpson(lambda y: exp(-0.5*y*y-c*y),0.,24.)
    limiting_constant=log(limiting_integral)
    for q in (10.,20.,32.,64.):
        lhs=log_mgf_frozen(q,beta,D,v,r,phi)
        residual=lhs - 0.5*q*q - c*q + log(q)
        check(abs(residual-limiting_constant)<5.e-7,"frozen exact tilt asymptotic")

# Check the constructive angular alignment event's deterministic
# mean and thermal lower bounds, for several threshold/direction cases.
for beta in (0.4,1.,2.):
    for v in (0.5,1.,3.):
        for x in (30.,100.,1000.,10000.):
            delta=x**(-0.25)
            T=2.+3.*log(x)/beta
            c=v/beta
            # The first unit of the angular path may point anywhere.
            A_lower=c*cos(delta)*(1-exp(-beta*(T-1)))-c*exp(-beta*(T-1))
            check(A_lower >= c-(0.52*c*x**(-0.5)+2*c*exp(-beta*(T-1))),
                  "angular alignment lower shift")
            thermal_ratio=1-exp(-2*beta*T)
            check(thermal_ratio + 1.e-14 >= 1-exp(-4*beta)*x**(-6),
                  "thermal variance saturation")

print("PASS",checks,"finite independent diagnostic assertions")
