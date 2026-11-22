"""Numerical diagnostics for collective ballistic first-passage resetting.
Run: python3 checker.py. Python standard library only.
These finite diagnostics do not replace the proofs for arbitrary population size.
"""
import math
import random

rng = random.Random(20261117)


def sample_cycle(n):
    speeds = [rng.expovariate(1.0) for _ in range(n)]
    top = max(speeds)
    u = rng.random()
    return speeds, top, u


def integral_midpoint(fun, a, b, steps):
    h = (b-a)/steps
    return h*sum(fun(a+(i+0.5)*h) for i in range(steps))


# An independent quadrature for the reciprocal maximum for n=2:
# E[1/M_2]=2*integral_0^infty (exp(-x)-exp(-2x))/x dx=2 log 2.
# Integrate with the substitution y=exp(-x), avoiding an infinite endpoint.
quad = integral_midpoint(lambda y: 2.0/(2.0-y), 0., 1., 50000)
assert abs(quad-2.0*math.log(2.0)) < 1e-10

# Exact renewal survival: for n iid Exp(1) speeds and L=1,
# P(tau>t)=(1-exp(-1/t))**n; compare to direct Monte Carlo.
for n,t in [(2,0.8),(3,1.5),(5,2.0)]:
    m=120000
    freq=sum(1 for _ in range(m) if 1/max(rng.expovariate(1) for j in range(n))>t)/m
    exact=(-math.expm1(-1/t))**n
    err=4.5*math.sqrt(max(exact*(1-exact),1e-6)/m)+.004
    assert abs(freq-exact)<err,(n,t,freq,exact)

# The stationary-cycle formula uses duration weights 1/max speed.
# At any size, conditional on the cycle speeds, the phase is uniform.
# Check the exact uniform minimum and the size-biased marginal using
# distinct random sampling calculations.
for n in (3, 6, 12):
    num=0.0; den=0.0; mm=0.0
    k=30000
    for _ in range(k):
        speeds,top,u=sample_cycle(n)
        w=1/top
        den+=w
        num+=w*(1-u*speeds[0]/top)
        mm+=w*(1-u)
    estimated_mean=num/den
    estimated_min=mm/den
    assert abs(estimated_min-0.5)<0.023,(n,estimated_min)
    assert 0.5<estimated_mean<1,(n,estimated_mean)

# Extreme--bulk separation and the random, non-self-averaging fraction.
# Sampling original iid marks with importance weights 1/M exactly
# evaluates stationary expectations; no approximation to the weighting.
n=4000
runs=1200
sum_w=0.; sum_gap=0.; sum_count=0.; sum_count2=0.
for _ in range(runs):
    speeds,top,u=sample_cycle(n)
    w=1/top
    scale=math.log(n)/top
    gap = u*scale*sum(speeds)/n
    proportion = sum(1 for v in speeds if u*scale*v>1.0)/n
    sum_w+=w
    sum_gap+=w*gap
    sum_count+=w*proportion
    sum_count2+=w*proportion**2
mean_gap=sum_gap/sum_w
mean_tail=sum_count/sum_w
variance_tail=sum_count2/sum_w-mean_tail*mean_tail
assert 0.35<mean_gap<0.60,mean_gap
# The limiting mean, obtained by integrating over U~Uniform(0,1), is
# integral_0^1 exp(-1/u) du ~ 0.1484955.
limit_mean=integral_midpoint(lambda u: math.exp(-1/u),0.0,1.0,50000)
limit_second=integral_midpoint(lambda u: math.exp(-2/u),0.0,1.0,50000)
limit_variance=limit_second-limit_mean*limit_mean
assert abs(mean_tail-limit_mean)<0.038,(mean_tail,limit_mean)
assert abs(variance_tail-limit_variance)<0.009,(variance_tail,limit_variance)
assert limit_variance>0.015

# The CDF of Q_z=exp(-z/U), U uniform, is z/(-log(q)) on (0,e^-z).
z=1.0
for q in (0.02,0.08,0.20,0.35):
    exact=z/(-math.log(q))
    empirical=sum(1 for _ in range(40000) if math.exp(-z/rng.random())<=q)/40000
    assert abs(empirical-exact)<0.018,(q,empirical,exact)

print('PASS: reciprocal-maximum normalization, reset-interval tails,')
print('stationary uniform extreme, tilted bulk means, and random-limit diagnostics.')
print('n=4000 stationary weighted scaled mean gap:',round(mean_gap,6))
print('n=4000 stationary weighted exceedance mean:',round(mean_tail,6),
      'limiting mean:',round(limit_mean,6))
print('n=4000 stationary weighted exceedance variance:',round(variance_tail,6),
      'limiting variance:',round(limit_variance,6))
