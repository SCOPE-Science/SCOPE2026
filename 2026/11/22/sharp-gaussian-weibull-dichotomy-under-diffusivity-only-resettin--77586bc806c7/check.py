#!/usr/bin/env python3
"""Independent deterministic calculations for environmental-only diffusivity resetting.

Run: python3 check.py. This file supplies reproducibility diagnostics, not a
substitute for the analytical Gaussian-mixture and large-deviation proofs.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar

passed = 0
def check(cond, label):
    global passed
    assert bool(cond), label
    passed += 1

def excess(z):
    return 30.0 * (z - 1.0 + math.exp(-z)) / z**2

def tail_constant(rate, amplitude, t):
    return 3.0 / 2.0**(4.0/3.0) * (rate/(amplitude**2 * t))**(1.0/3.0)

for rate in [0.3, 1.0, 3.7]:
    for amp in [0.4, 1.0, 2.2]:
        m2 = 2*amp**2/rate
        m4 = 24*amp**4/rate**2
        check(abs(2*amp**2-rate*m2)<1e-12, 'generator second moment')
        check(abs(12*amp**2*m2-rate*m4)<1e-10, 'generator fourth moment')
        varD = m4-m2**2
        check(abs(varD-20*amp**4/rate**2)<1e-10, 'diffusivity variance')
        for t in [0.2, 0.7, 1.0, 3.0]:
            qvar = 2*varD*(t/rate-(1-math.exp(-rate*t))/rate**2)
            xvar = 2*m2*t
            kappa4 = 12*qvar
            check(abs(kappa4/xvar**2-excess(rate*t))<1e-10, 'kurtosis exact')
            c = tail_constant(rate,amp,t)
            a = math.sqrt(rate)/amp
            opt = minimize_scalar(lambda y: a*y + 1.0/(4*t*y*y),
                                  bounds=(1e-8, 50*(1+1/a)), method='bounded',
                                  options={'xatol':1e-12})
            check(opt.success and abs(opt.fun-c)<2e-7*(1+c), 'tail variational constant')
            check(abs(opt.x-(1/(2*a*t))**(1/3))<2e-5, 'tail minimizer')

for rate in [0.3,1.0,3.0]:
    for t in [0.01,0.1,1.,3.,10.]:
        z=rate*t
        check(excess(z)>0, 'strictly positive excess')
        # The excess is strictly decreasing in elapsed time.
        check(excess(1.05*z)<excess(z), 'strict monotonicity of excess')
        check(abs(excess(z)-30*(z-1+math.exp(-z))/z**2)<1e-11,'reference expression')

# Independently integrate the Feynman-Kac Riccati equations instead of
# substituting their known trigonometric solution.
for amp in [0.5,1.,2.]:
    for k in [0.1,0.25,0.7]:
        critical=math.pi/(4*amp*k)
        for fraction in [0.1,0.4,0.85]:
            t=critical*fraction
            def eq(s,y):
                A, B=y
                return [4*amp**2*A*A+k*k,2*amp**2*A]
            sol=solve_ivp(eq,[0,t],[0.,0.],rtol=3e-12,atol=3e-14)
            exact=1/math.sqrt(math.cos(2*amp*k*t))
            check(sol.success and abs(math.exp(sol.y[1,-1])-exact)<1e-9,
                  'Feynman-Kac analytic continuation')

# Independent time-discretized simulation of the stationary bath and integrated
# variance (not of the rare tail, whose coefficient is proved analytically).
rng=np.random.default_rng(20261117)
n=120000
rate=amp=t=1.0
steps=300
dt=t/steps
omega=rng.laplace(0.,amp/math.sqrt(rate),n)
area=np.zeros(n)
for j in range(steps):
    z=rng.normal(size=n)
    nextomega=omega+math.sqrt(2)*amp*math.sqrt(dt)*z
    # Trapezoidal Brownian-square integration reduces deterministic mesh bias.
    area+=(omega**2+nextomega**2)*0.5*dt
    omega=nextomega
    flags=rng.random(n)<1-math.exp(-rate*dt)
    omega[flags]=0.
expected_area=2*amp**2*t/rate
expected_var=40*amp**4/rate**2*(t/rate-(1-math.exp(-rate*t))/rate**2)
check(abs(np.mean(area)-expected_area)<0.075*expected_area,'independent Monte Carlo mean area')
check(abs(np.var(area)-expected_var)<0.15*expected_var,'independent Monte Carlo variance area')
print(f'PASS: {passed} deterministic/numerical assertions')
print(f'Stationary-bath integrated variance: MC={np.var(area):.6f}, formula={expected_var:.6f}')
print(f'At rate=amplitude=t=1: tail C={tail_constant(1,1,1):.9f}; excess kurtosis={excess(1):.9f}')
