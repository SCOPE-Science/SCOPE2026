"""Deterministic finite checks for two-scale triangular block semigroups.

The exact theorem and its infinite-dimensional conclusions are proved in RESULT.md;
finite checks here are numerical diagnostics, not substitutes for those proofs.
"""
import cmath
import math

ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def mu(u):
    """Smallest singular value of the shear [[1,u],[0,1]], u >= 0."""
    return 2.0 / (math.hypot(u, 2.0) + u)


def log_block_min(t, a, c, beta, gamma, n):
    u = c*t / n**gamma
    return a*t / n**beta + math.log(mu(u))


def block_time_vector(n, t, tstar, a, c, beta, gamma, omega):
    ustar = c*tstar / n**gamma
    den = math.hypot(ustar, 1)
    z = cmath.exp((a/n**beta + 1j*omega)*t)
    return (z*c*(t-tstar)/n**gamma/den, z/den)


def distance(v, w):
    return math.hypot(abs(v[0]-w[0]), abs(v[1]-w[1]))


def witness_error(n, a, c, beta, gamma):
    omega = a+c+1
    tau = 2*math.pi/omega
    q = gamma/beta
    tstar = q*n**beta/a
    check(tstar > 3*tau, "witness switch must lie in positive time")
    x0 = block_time_vector(n, 0, tstar, a,c,beta,gamma,omega)
    y0 = block_time_vector(n, -tau, tstar, a,c,beta,gamma,omega)
    errors = []
    # Before switch: sampled whole interval; after switch exact by semigroup law.
    for j in range(121):
        t=(tstar-tau)*j/120
        tx=block_time_vector(n,t,tstar,a,c,beta,gamma,omega)
        ty=tuple(cmath.exp((a/n**beta+1j*omega)*t)*
                 (y0[0] + c*t/n**gamma*y0[1]) if k==0 else
                 cmath.exp((a/n**beta+1j*omega)*t)*y0[1]
                 for k in range(2))
        errors.append(distance(tx,ty))
    for j in range(81):
        t=tstar-tau+tau*j/80
        h=2*t-tstar+tau
        tx=block_time_vector(n,t,tstar,a,c,beta,gamma,omega)
        thy=block_time_vector(n,h-tau,tstar,a,c,beta,gamma,omega)
        errors.append(distance(tx,thy))
    # Check witness x is exactly a unit vector, and the analytic envelope.
    check(abs(math.hypot(abs(x0[0]),abs(x0[1]))-1)<2e-12,"witness unit")
    bn=c/n**gamma;an=a/n**beta
    pre=math.exp(q)*(abs(1-math.exp(-an*tau)) + math.exp(-an*tau)*bn*tau)
    trans=2*math.exp(q)*math.hypot(2*bn*tau,1)/math.hypot(bn*tstar,1)
    check(max(errors) < pre+trans+2e-12,"analytic supremum bound")
    return max(errors),pre+trans


def run():
    # Algebraic shear singular-value identity: product of squared singular
    # values is 1 and their sum is 2+u^2.
    for u in (0,0.01,0.2,1,3,50,1e3):
        small=mu(u);large=1/small
        check(abs(small*large-1)<1e-12,"shear determinant")
        check(abs((small**2+large**2)-(u*u+2)) < 1e-7*max(1,u*u),"shear trace")
    # Subcritical lower singular asymptotic and maximizing block localization.
    for a,c,beta,gamma in ((1,1,2,1),(2,3,2,1),(1.5,2,3,1),(1,1.4,3,2)):
        q=gamma/beta
        K=math.exp(q)*a**q/(c*q**q)
        for t in (1e4,1e5,1e6):
            n0=(a*t/q)**(1/beta)
            cand=range(max(1,int(n0*0.4)),int(n0*2.0)+5)
            val,nstar=min((log_block_min(t,a,c,beta,gamma,n),n) for n in cand)
            metric=math.exp(val)*t**(1-q)
            check(abs(metric/K-1)<0.065,"subcritical constant")
            check(abs(nstar/n0-1)<0.15,"saddle localization")
    # Critical plateau: below, at and above the accretivity ratio c=2a.
    for a,c in ((1,1.8),(1,2),(1,3),(2,7)):
        d=math.sqrt(max(0,1-(2*a/c)**2)) if c>2*a else 0
        plateau=(math.exp(d)*(2*a/c)/(1+d)) if c>2*a else 1.0
        for t in (100,1000,10000):
            if c>2*a:
                xstar=(2*d/math.sqrt(1-d*d))/c
                n0=(t/xstar)
                cand=range(max(1,int(n0)-10),int(n0)+11)
                val=min(math.exp(log_block_min(t,a,c,1,1,n)) for n in cand)
                check(abs(val-plateau)<0.005,"critical plateau")
            else:
                for n in (1,3,30,1000):
                    check(log_block_min(t,a,c,1,1,n)>-1e-10,"critical accretive")
    # Supercritical: finitely many potentially contracting low-index blocks.
    for a,c,beta,gamma in ((1,3,1,2),(2,5,1,3),(1,1,2,3)):
        for n in (1,2,3,4,10,30,100):
            for t in (1e3,1e4):
                check(log_block_min(t,a,c,beta,gamma,n) >=-1e-12,"eventual noncontraction")
    # Explicit reparametrization witness in the failing branch.
    last=1e3
    for n in (25,80,200,500):
        e,ub=witness_error(n,1,1,2,1)
        check(e<last,"witness discrepancy shrinks with block index")
        check(ub<last,"analytic witness envelope shrinks")
        last=e
    print(f"CHECKS_OK {ASSERTIONS} finite assertions")
    print("Critical plateau a=1,c=3:",math.exp(math.sqrt(5)/3)*(2/3)/(1+math.sqrt(5)/3))
    print("Subcritical leading constant a=c=1,beta=2,gamma=1:",math.exp(.5)/math.sqrt(.5))
    for n in (25,80,200,500):
        e,ub=witness_error(n,1,1,2,1)
        print(f"Witness n={n}: sampled discrepancy {e:.9g}, analytical upper bound {ub:.9g}")

if __name__ == "__main__":
    run()
