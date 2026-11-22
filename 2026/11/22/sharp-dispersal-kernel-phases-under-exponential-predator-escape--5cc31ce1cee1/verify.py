"""Reproducible numerical checks for a mean-constrained seed dispersal envelope.

This script tests examples and finite grids; the global theorem is analytic.
No external Python modules are required.
"""
import math

checks = 0


def check(condition, message="check failed"):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def f(r, c, beta):
    return math.exp(-c*r-beta*math.exp(-r))


def fp(r, c, beta):
    return (beta*math.exp(-r)-c)*f(r, c, beta)


def fpp(r, c, beta):
    z = beta*math.exp(-r)
    return ((z-c)*(z-c)-z)*f(r, c, beta)


def parameters(c, beta):
    threshold = c+0.5+math.sqrt(c+0.25)
    if beta <= c:
        return (0, threshold, 0, None, None)
    rstar = math.log(beta/c)
    if beta <= threshold:
        return (1, threshold, rstar, None, None)
    ri = math.log(beta/threshold)
    def N(t):
        return t*fp(t, c, beta)-f(t, c, beta)+f(0., c, beta)
    a, b = ri, rstar
    check(N(a) > 0 and N(b) < 0, 'tangency bracket')
    for _ in range(96):
        mid = (a+b)/2
        if N(mid) > 0:
            a = mid
        else:
            b = mid
    return (2, threshold, rstar, (a+b)/2, ri)


def upper(m, c, beta):
    regime, _, rstar, t, _ = parameters(c, beta)
    if regime == 0:
        return f(0, c, beta)
    if m >= rstar:
        return f(rstar, c, beta)
    if regime == 2 and m < t:
        return f(0, c, beta)+m*(f(t, c, beta)-f(0, c, beta))/t
    return f(m, c, beta)


cs = (0.15, 0.4, 1., 2.2, 4.5)
for c in cs:
    threshold = c+0.5+math.sqrt(c+0.25)
    betas = (0.2*c, c, 1.04*c, (c+threshold)/2,
             threshold, threshold*1.07, threshold*1.6, 6*c+5)
    for beta in betas:
        regime, _, rstar, t, ri = parameters(c, beta)
        if regime == 0:
            check(beta <= c)
            check(rstar == 0)
        elif regime == 1:
            check(c < beta <= threshold)
            for j in range(1, 100):
                r = rstar*j/100
                check(fpp(r,c,beta) < 1e-12, 'concave branch')
        else:
            check(beta > threshold)
            check(0 < ri < t < rstar)
            check(abs(t*fp(t,c,beta)-f(t,c,beta)+f(0,c,beta)) < 4e-13)
            for j in range(1, 100):
                r = rstar*j/100
                check(fpp(r,c,beta)>0 if r < ri-1e-9 else
                      fpp(r,c,beta)<0 if r > ri+1e-9 else True)
        xmax = max(4.0, 5*rstar)
        for j in range(351):
            r = xmax*j/350
            check(f(r,c,beta) <= upper(r,c,beta)+2e-13, 'envelope dominates')
        for m in (0.,.025,.1,.25,.7,1.,1.5,3.,5.):
            G = upper(m,c,beta)
            check(G>=f(m,c,beta)-2e-13)
            # Two-point laws: each has the given mean exactly.
            if m:
                for j in range(0,30):
                    left = m*j/30
                    for k in range(1,20):
                        right=m+max(0.5,2*m)*(k/5)
                        p=(right-m)/(right-left)
                        avg=p*f(left,c,beta)+(1-p)*f(right,c,beta)
                        check(avg<=G+2e-13,'two-point convex bound')
            if regime==2 and m>0 and m<t:
                p=m/t
                check(abs((1-p)*f(0,c,beta)+p*f(t,c,beta)-G)<2e-13)
            if regime and m>=0 and m<=rstar and (regime==1 or regime==2 and m>=t):
                check(abs(f(m,c,beta)-G)<2e-13)
            # For means beyond the pointwise maximizer, near-optimal
            # distributions carry a vanishing mass at enormous distances.
            if m>rstar:
                x=rstar if regime else 0.0
                for big in (1.e3,1.e5):
                    tail_mass=(m-x)/(big-x)
                    check(0<tail_mass<1)
                    avg=(1-tail_mass)*f(x,c,beta)+tail_mass*f(big,c,beta)
                    check(0< G-avg < 2*(m-x)/(big-x))

# A dimorphic example with known unique tangency and quantitative gain.
c,beta=1.,4.
reg,threshold,rstar,t,ri=parameters(c,beta)
check(reg==2 and abs(threshold-(3+math.sqrt(5))/2)<1e-14)
check(abs(t-0.6329929689212394)<1e-12)
m=.25
p=m/t
G=upper(m,c,beta)
assert abs(G-0.036154185087598004)<2e-14
assert abs(f(m,c,beta)-0.03455499616968765)<2e-14
check(G>f(m,c,beta)*1.046)
print('PASS:', checks, 'finite-grid assertions; independent analytic proof required')
print('Example: threshold=',threshold, 'tangency=',t, 'rstar=',rstar,
      'far_fraction=',p, 'value=',G, 'deterministic=',f(m,c,beta))
