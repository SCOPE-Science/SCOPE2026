"""Numerical checks for a two-window squared-increment law in tempered fractional Laplace motion.

Python 3 standard library only. These finite checks support, but do not replace,
the analytical proof and its uniform estimates.
"""
import math

checks = 0

def close(a, b, atol=1e-10, rtol=1e-10):
    global checks
    assert math.isfinite(a) and math.isfinite(b), (a,b)
    assert abs(a-b) <= atol + rtol*max(abs(a), abs(b)), (a,b,abs(a-b))
    checks += 1

def v_h1(s,tau):
    return 2*tau*(s-tau*(1-math.exp(-s/tau)))

def clock_transform(t, eta, rate):
    return (eta/(eta+rate))**(eta*t)

def exact_h1(length,gap,alpha,eta,tau):
    q1=clock_transform(length,eta,1/tau)
    q2=clock_transform(length,eta,2/tau)
    m=length-tau+tau*q1
    mean_v=2*tau*m
    second_v=4*tau*tau*(length**2+length/eta-2*tau*length+tau*tau
                +2*tau*(length*eta/(eta+1/tau)-tau)*q1+tau*tau*q2)
    cov_square=tau**4*(1-2*q1+q2)**2*clock_transform(gap,eta,2/tau)
    den=3*(alpha+1)*second_v-alpha*mean_v**2
    return (mean_v**2+2*(alpha+1)*cov_square)/den

# The conditional two-increment covariance must agree with the variogram identity.
for tau in (0.6,1.,2.3):
    for a in (0.2,1.,4.):
        for b in (0.5,1.7):
            for z in (0.,0.8,3.):
                gauss_cov=0.5*(v_h1(a+z+b,tau)+v_h1(z,tau)
                               -v_h1(a+z,tau)-v_h1(z+b,tau))
                direct=tau*tau*(1-math.exp(-a/tau))*(1-math.exp(-b/tau))*math.exp(-z/tau)
                close(gauss_cov,direct,atol=5e-13)

# In the exponential-kernel case, the exact finite-time formula shows
# strict reduction with physical separation and a strictly positive floor.
for alpha in (0.4,1.0,2.0,6.0):
    for eta in (0.5,1.5,3.):
        for tau in (0.5,1.,2.):
            for length in (0.4,2.,20.):
                values=[exact_h1(length,g,alpha,eta,tau) for g in (0.,0.1,0.5,2.,10.,200.)]
                assert all(0<values[i+1]<values[i]<1 for i in range(len(values)-1))
                checks += len(values)-1

# Confirm the universal first correction independently of the kernel timescale
# and of arbitrarily different observation gaps.
for alpha in (0.4,1.0,2.0,6.0):
    for eta in (0.5,1.5,3.):
        for tau in (0.5,1.,2.):
            K=2*alpha+3
            limit=-3*(alpha+1)/(K*K*eta)
            for gap in (0.,1.,50.):
                length=5000.
                measured=length*(exact_h1(length,gap,alpha,eta,tau)-1/K)
                close(measured,limit,atol=1.8e-3)

# The gap-dependent term is of order length**(-2), with a fully explicit
# limit for the exponential kernel, including finite and zero gaps.
for alpha in (0.4,1.,2.,6.):
    for eta in (0.5,1.5,3.):
        for tau in (0.5,1.,2.):
            for gap in (0.,0.5,2.):
                length=5000.
                actual=length*length*(exact_h1(length,gap,alpha,eta,tau)
                           -exact_h1(length,100000.,alpha,eta,tau))
                predicted=(alpha+1)*tau*tau/(2*(2*alpha+3))*clock_transform(gap,eta,2/tau)
                close(actual,predicted,atol=8e-4,rtol=1.5e-3)

# Verify the nondecaying square-correlation floor is the superstatistical
# contribution extracted from the one-window kurtosis, for the H=1 model.
for alpha in (.5,2.,9.):
    for eta in (.6,2.):
        for tau in (.75,1.5):
            for length in (1.,5.,80.):
                q1=clock_transform(length,eta,1/tau)
                q2=clock_transform(length,eta,2/tau)
                mean_v=2*tau*(length-tau+tau*q1)
                second_v=4*tau*tau*(length**2+length/eta-2*tau*length+tau*tau
                    +2*tau*(length*eta/(eta+1/tau)-tau)*q1+tau*tau*q2)
                kurtosis=3*(alpha+1)/alpha*second_v/(mean_v*mean_v)
                close(exact_h1(length,1.e6,alpha,eta,tau),1/(alpha*(kurtosis-1)),atol=1e-12)

print(f"PASS: {checks} deterministic analytical-identity, monotonicity and asymptotic checks")
