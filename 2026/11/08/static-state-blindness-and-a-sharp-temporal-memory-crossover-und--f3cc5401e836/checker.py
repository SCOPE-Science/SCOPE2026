"""Numerical cross-checks for stationary run-and-tumble temporal covariance.
Independent event-driven Monte Carlo is used alongside generator formulas.
No simulation is a substitute for the analytic proof.
"""
import math
import random
import numpy as np
from scipy.linalg import expm


def formula(t, v, D, alpha, rate, eta):
    v2 = 2 * D / rate + 2 * v * v / (rate * (rate + 2 * alpha))
    z = rate - 2 * (alpha + eta * rate)
    if abs(z) < 1.e-12:
        g = t * math.exp(-rate * t)
    else:
        g = math.exp(-rate * t) * math.expm1(z * t) / z
    return v2 * math.exp(-rate * t) + v * v / (rate + 2 * alpha) * g


def gen_expm(t, v, D, alpha, rate, eta):
    # Independent moment semigroup on affine observable basis (X,S).
    M = np.array([[-rate, v], [0., -2*(alpha+eta*rate)]], dtype=float)
    K = expm(M * t)
    varx = 2*D/rate + 2*v*v/(rate*(rate+2*alpha))
    cross = v/(rate+2*alpha)
    return K[0,0]*varx + K[0,1]*cross


def stationary_state(rng, v,D,alpha,rate):
    # Exact stationary backward-age sampler, with a fair reset orientation.
    age = rng.expovariate(rate)
    x=0.; s = 1 if rng.random()<0.5 else -1
    t=0.
    while t<age:
        tau=rng.expovariate(alpha)
        dt=min(tau,age-t)
        x+=s*v*dt
        t+=dt
        if t<age: s=-s
    x+=math.sqrt(2*D*age)*rng.gauss(0,1)
    return x,s


def future_conditional_position(rng, x, s, t, v,alpha,rate,eta):
    # Exact future event simulation; omit zero-mean future Brownian increments
    # (Rao-Blackwellization for E[X_0 X_t]).
    rem=t
    while rem>0:
        tau=rng.expovariate(rate+alpha)
        dt=min(tau,rem)
        x+=s*v*dt
        rem-=dt
        if rem<=0: break
        if rng.random()<rate/(rate+alpha):
            x=0.
            if rng.random()<eta: s=-s
        else: s=-s
    return x


def main():
    n=0
    for v in (.3, 1.2, 4.4):
      for D in (.02, 1.5):
       for alpha in (.03, .37, 1.3):
        for rate in (.2, 1.0, 2.8):
         for eta in (0., .14, .5, 1.):
          for t in (0., .09, .7, 1.8, 4.):
            a=formula(t,v,D,alpha,rate,eta)
            b=gen_expm(t,v,D,alpha,rate,eta)
            assert math.isclose(a,b,rel_tol=8e-13,abs_tol=8e-13),(v,D,alpha,rate,eta,t,a,b)
            n+=1
    assert n==1080
    # Verify stationary CF from the two-state characteristic generator.
    for v,D,alpha,rate in ((1.2,.3,.12,1.), (3.7,1.,.4,.7),(.5,.7,2.,1.6)):
      for k in (.1,.6,2.):
        L=np.array([[-D*k*k,1j*k*v],[1j*k*v,-(D*k*k+2*alpha)]],dtype=complex)
        stationary_cf=(rate*np.linalg.inv(rate*np.eye(2)-L)[0,0]).real
        closed=rate*(rate+D*k*k+2*alpha)/((rate+D*k*k)*(rate+D*k*k+2*alpha)+v*v*k*k)
        assert abs(stationary_cf-closed)<1e-13
    # Exact event-level simulation verifies that altering eta leaves one-time moments
    # unchanged but changes two-time covariances.
    rng=random.Random(20261107)
    v,D,alpha,rate,t=2.1,.4,.17,1.,1.5
    N=100000
    stat=[stationary_state(rng,v,D,alpha,rate) for _ in range(N)]
    sx=np.array([q[0] for q in stat]); ss=np.array([q[1] for q in stat]);
    varx=2*D/rate+2*v*v/(rate*(rate+2*alpha))
    covxs=v/(rate+2*alpha)
    assert abs(np.mean(sx*sx)-varx)<.08*varx
    assert abs(np.mean(sx*ss)-covxs)<.07*covxs
    outcomes=[]
    for eta in (0.,.4,1.):
      future=np.array([future_conditional_position(rng,x,s,t,v,alpha,rate,eta) for x,s in stat])
      mc=float(np.mean(sx*future)); analytic=formula(t,v,D,alpha,rate,eta)
      # 7% of stationary variance: loose bound justified by MC stochastic error.
      assert abs(mc-analytic)<.07*varx,(eta,mc,analytic)
      outcomes.append((eta,mc,analytic))
    assert outcomes[0][1]>outcomes[1][1]>outcomes[2][1]
    print('PASS: 1080 independent matrix-exponential comparisons, 9 characteristic resolvent comparisons,')
    print('and 3 independent 100000-sample event-driven Monte Carlo covariance comparisons.')
    print('observed eta, Monte Carlo C(t), theorem C(t):')
    for row in outcomes:print(row)

if __name__=='__main__': main()
