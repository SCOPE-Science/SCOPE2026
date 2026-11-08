"""Self-contained numerical diagnostics for a renewal-reset Kuramoto amplitude.

Requires only Python 3 standard library. Assertions supplement the analytical proof.
"""
import math


def flow(t, sigma, K, r0):
    b = K / 2.0
    a = b - sigma
    if a < 0.0:
        d = -a
        z = math.exp(-2.0 * d * t)
        return r0 * math.sqrt(z) / math.sqrt(1.0 + b * r0 * r0 / d * (1.0 - z))
    if a > 0.0:
        rs = math.sqrt(a / b)
        B = rs * rs / (r0 * r0) - 1.0
        return rs / math.sqrt(1.0 + B * math.exp(-2.0 * a * t))
    return r0 / math.sqrt(1.0 + 2.0 * b * r0 * r0 * t)


def inverse(r, sigma, K, r0):
    b = K / 2.0
    a = b - sigma
    if a == 0.0:
        return (1.0 / (r * r) - 1.0 / (r0 * r0)) / (2.0 * b)
    return math.log((1.0 / (r0 * r0) - b / a) / (1.0 / (r * r) - b / a)) / (2.0 * a)


def speed(r, sigma, K):
    return (K / 2.0 - sigma) * r - K * r * r * r / 2.0


def density(r, sigma, K, r0, tau, q):
    t = inverse(r, sigma, K, r0)
    return (q - 1.0) / tau * (1.0 + t / tau) ** (-q) / abs(speed(r, sigma, K))


def age_cdf(t, tau, q):
    return 1.0 - (1.0 + t / tau) ** (1.0 - q)


def near_attractor_mass(r, sigma, K, r0, tau, q):
    return (1.0 + inverse(r, sigma, K, r0) / tau) ** (1.0 - q)


def close(a, b, tol=1e-8):
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)


checks = 0
for K in (0.4, 1.0, 1.9, 2.0, 2.1, 3.0, 4.5):
    for r0 in (0.2, 0.8, 1.0):
        b = K / 2.0
        a = b - 1.0
        if a > 0 and abs(r0 - math.sqrt(a / b)) < 1e-10:
            continue
        for t in (0.001, 0.03, 0.3, 2.0, 5.0, 12.0):
            r = flow(t, 1.0, K, r0)
            if not (a > 0.0 and abs(r-math.sqrt(a/b)) < 1e-7):
                close(inverse(r, 1.0, K, r0), t, 1e-6)
                checks += 1
            h = 1e-5
            if t > h:
                slope = (flow(t+h, 1.0, K, r0)-flow(t-h, 1.0, K, r0))/(2*h)
                close(slope, speed(r, 1.0, K), 2e-7)
                checks += 1
            for tau, q in ((0.5, 1.3), (0.5, 1.5), (1.5, 2.8)):
                if a > 0.0 and abs(r-math.sqrt(a/b)) < 1e-7:
                    continue
                p = density(r, 1.0, K, r0, tau, q)
                analytic = (q - 1.0)/tau * (1.0+t/tau)**(-q) / abs(speed(r,1.0,K))
                close(p, analytic, 1e-7)
                checks += 1

# Normalization: exact push-forward integral in age coordinates, midpoint rule.
for q in (1.2, 1.5, 2.3, 5.0):
    for tau in (0.2, 1.0, 4.0):
        stop = 100*tau
        n = 30000
        dt = stop / n
        def f(s):
            return (q-1.0)/tau*(1.0+s/tau)**(-q)
        acc = dt/3.0*(f(0.0)+f(stop)+4.0*sum(f(i*dt) for i in range(1,n,2))+2.0*sum(f(i*dt) for i in range(2,n,2)))
        tail = (1+stop/tau)**(1-q)
        close(acc+tail,1.0,2e-9)
        checks += 1

# Edge asymptotics at subcritical and supercritical coupling.
for q in (1.2, 1.5, 2.4):
    for K, r0 in ((1.0,0.8), (3.0,0.8), (3.0,0.2)):
        b = K/2
        a=b-1
        tau=0.9
        if a < 0:
            rate=-a
            C=r0/math.sqrt(1+b*r0*r0/rate)
            for t in (60.,120.,240.,480.):
                r=flow(t,1.,K,r0)
                mass=near_attractor_mass(r,1.,K,r0,tau,q)
                limit=(rate*tau)**(q-1)*math.log(C/r)**(1-q)
                assert 0.8 < mass/limit < 1.1
                checks+=1
        else:
            rate=2*a
            rs=math.sqrt(a/b)
            B=rs*rs/r0**2-1
            C=rs*abs(B)/2
            for t in (8.,12.,16.,20.):
                r=flow(t,1.,K,r0)
                d=abs(r-rs)
                mass=near_attractor_mass(r,1.,K,r0,tau,q)
                limit=(rate*tau)**(q-1)*math.log(C/d)**(1-q)
                assert 0.5 < mass/limit < 1.15, (K,r0,t,mass,limit)
                checks+=1

# Exact critical density, its exponent, its prefactor, and the CDF exponent.
for q in (1.2,1.49,1.5,1.51,2.1,3.0):
    K=2.0
    b=1.0
    r0=0.8
    tau=1.25
    coefficient=2*(q-1)*(2*b*tau)**(q-1)
    for r in (0.01,0.005,0.001):
        p=density(r,1.,K,r0,tau,q)
        asy=coefficient * r**(2*q-3)
        close(p/asy,1.,0.001)
        checks+=1
        mass=near_attractor_mass(r,1.,K,r0,tau,q)
        cdf=(2*b*tau)**(q-1)*r**(2*(q-1))
        close(mass/cdf,1.,0.001)
        checks+=1

# Contrasts with Poisson resets: at critical coupling every exponential-clock
# density vanishes at zero, unlike Pareto clocks with 1<q<3/2.
for r in (0.1,0.05,0.02):
    b=1.0
    lam=0.5
    r0=0.8
    pois=lam/(b*r**3)*math.exp(-lam/(2*b)*(r**-2-r0**-2))
    pareto=density(r,1.0,2.0,r0,1.0,1.2)
    assert pareto > pois
    checks+=1

# A second, non-Lomax clock verifies the universal tail coefficient.
# Survival S(t)=0.5 (1+t)^(-q)+0.5 (1+t/3)^(-(q+1)).
for q in (1.25,1.5,1.85,2.5):
    mu=0.5/(q-1)+1.5/q
    c=0.5
    def gen_survival(t):
        return 0.5*(1+t)**(-q)+0.5*(1+t/3)**(-q-1)
    for r in (0.005,0.002,0.001):
        b=1.0
        t=(r**-2-0.8**-2)/(2*b)
        p=gen_survival(t)/(mu*b*r**3)
        asymptotic=2*c*(2*b)**(q-1)/mu*r**(2*q-3)
        close(p/asymptotic, 1.0, 0.004)
        checks+=1

# Universal two-sided near-critical boundary-layer law for Lomax clocks.
for q in (1.3,1.6,2.4):
    tau=0.8
    r0=0.7
    mu=tau/(q-1)
    c=tau**q
    for z in (0.2,0.8,2.5):
        L=math.log1p(1/z)
        coefficient=c*2**(q-1)/(mu*(q-1))*L**(1-q)
        for eta in (0.001,0.0002):
            for sign in (-1,1):
                K=2*(1+sign*eta)
                b=K/2
                r=math.sqrt(eta*(z if sign<0 else (1+z))/b)
                actual=near_attractor_mass(r,1.0,K,r0,tau,q)
                ratio=actual/(eta**(q-1)*coefficient)
                assert abs(ratio-1)<0.06, (q,z,eta,sign,ratio)
                checks+=1

print('PASS: %d numerical diagnostic assertions; three coupling regimes, exact densities, critical exponents and stationary normalization.' % checks)
