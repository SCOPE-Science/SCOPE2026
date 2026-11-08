#!/usr/bin/env python3
"""Standalone finite checks of exact identities in the capped Pareto clustering theorem."""
import math

checks = 0

def close(x, y, tol=1e-8):
    global checks
    assert math.isfinite(x) and math.isfinite(y)
    assert abs(x-y) <= tol*(1+abs(x)+abs(y)), (x,y)
    checks += 1

# Composite Simpson integration on a bounded interval, with independently
# controlled exponentially small tails for the mixture integral.
def simpson(f, a, b, m=20000):
    assert m % 2 == 0
    h=(b-a)/m
    s=f(a)+f(b)
    for j in range(1,m):
        s += (4 if j%2 else 2)*f(a+j*h)
    return s*h/3

for alpha in (0.2,0.5,0.8):
    for lam in (0.3,1.0,3.0):
        c=lam/(1-alpha)
        # Analytic integral for truncated Pareto:
        # E[min(z W,1)] = (z^alpha - alpha*z)/(1-alpha), z <= 1.
        for z in (0.01,0.1,0.5,0.95):
            rhs=(z**alpha-alpha*z)/(1-alpha)
            # direct Pareto piece integral (integration of W truncated at 1/z)
            lhs=z*alpha*((1/z)**(1-alpha)-1)/(1-alpha)+z**alpha
            close(lhs,rhs,1e-12)
        for w in (1.,2.,3.):
            # PPP intensity of Bernoulli successes under min(wt,1):
            val=lam*alpha*(w*(1/w)**(1-alpha)/(1-alpha)
                            + (1/w)**(-alpha)/alpha)
            close(val, c*w**alpha,1e-12)
        # Integrate P(D<=1) with U=W^alpha ~ Pareto(1).
        # Tail integral beyond u=90/c is << 1e-30 for all tested cases.
        b=max(100.,90./c)
        integral=simpson(lambda u:math.exp(-c*u)*(1+c*u)/u**2,1.,b)
        close(integral,math.exp(-c),7e-8)
        # The unit atom is exactly the Poisson tail for >=2 full hubs.
        pfull=1-math.exp(-lam)*(1+lam)
        p0=math.exp(-lam)
        p1=lam*math.exp(-lam)
        close(pfull,1-p0-p1,1e-12)
        assert 0 < pfull < 1
        checks += 1

# For any two hubs with weights exceeding 1/epsilon, edge saturation is exact.
for epsilon in (0.001,0.05,0.2):
    for multiplier1 in (1.,2.,5.):
        for multiplier2 in (1.,3.,7.):
            w1=multiplier1/epsilon
            w2=multiplier2/epsilon
            close(min(1.,epsilon*w1*w2),1.,1e-12)

# Tiny-ratio check of finite-n conditional degree intensity.
for alpha in (0.2,0.5,0.8):
    for lam in (0.1,1.,5.):
        for w in (1.,2.):
            n=10**12
            epsilon=(lam/n)**(1./alpha)
            z=epsilon*w
            val=(z**alpha-alpha*z)/(1-alpha)
            target=lam*w**alpha/(1-alpha)
            # The finite-n error is explicit and only decays as n^(1-1/alpha).
            exact_error=target/n+(n-1)*alpha*z/(1-alpha)
            close(target-(n-1)*val,exact_error,1e-10)
            assert (n-1)*val <= target
            checks += 1

print(f"PASS: {checks} finite deterministic assertions")
