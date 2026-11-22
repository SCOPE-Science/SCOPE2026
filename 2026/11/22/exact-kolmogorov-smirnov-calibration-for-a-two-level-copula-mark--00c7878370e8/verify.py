"""Numerical consistency checks for the two-level copula KS calibration.

Requires NumPy and SciPy. Executable with ``python3 verify.py``.
Exact analytical arguments are given in RESULT.md; this finite calculation is not a proof.
"""
import math
import numpy as np
from scipy.integrate import quad


def normal_density(var, x):
    return math.exp(-x*x/(2*var))/math.sqrt(2*math.pi*var)


def killed_kernel(z,t,y,terms=150):
    return sum(
        math.sin(j*math.pi/2)*math.sin(j*math.pi*(y+z)/(2*z))
        *math.exp(-j*j*math.pi*math.pi*t/(8*z*z))/z
        for j in range(1,terms+1)
    )


def cdf(z,p,lam):
    v=p*(1-p)
    sigma2=(1+lam)/(1-lam)
    def integrand(y):
        return (normal_density(v*sigma2,y)
                * killed_kernel(z,p,y)/normal_density(p,y)
                * killed_kernel(z,1-p,y)/normal_density(1-p,y))
    return quad(integrand,-z,z,epsabs=2e-11,epsrel=2e-11,limit=300)[0]


def classical_kolmogorov(z):
    return 1-2*sum((-1)**(k-1)*math.exp(-2*k*k*z*z) for k in range(1,60))


def simulate_ks(p, lam, n=1000, repetitions=3000, seed=13278):
    rng = np.random.default_rng(seed)
    states = rng.random(repetitions) < p
    obs = np.empty((repetitions,n))
    for j in range(n):
        if j:
            t = rng.random(repetitions)
            states = t < np.where(states,p+lam*(1-p),p*(1-lam))
        w = rng.random(repetitions)
        obs[:,j]=np.where(states,p*w,p+(1-p)*w)
    sorted_obs=np.sort(obs,axis=1)
    ranks=np.arange(1,n+1,dtype=float)/n
    D=np.maximum(np.max(ranks-sorted_obs,axis=1),
                 np.max(sorted_obs-(ranks-1/n),axis=1))
    return np.sqrt(n)*D


def main():
    for alpha, lam in [(1.0,-.3),(1.0,0.4),(7/3,-.3),(7/3,0.4),(.2,-.1),(5,-.1)]:
        p=1/(1+alpha)
        assert lam>=-min(alpha,1/alpha) and lam<1
        mat=np.array([[p+lam*(1-p),(1-p)*(1-lam)],
                      [p*(1-lam),1-p+lam*p]])
        assert np.max(abs(mat.sum(axis=1)-1))<1e-13
        assert np.max(abs(np.array([p,1-p])@mat-np.array([p,1-p])))<1e-13
        assert abs(np.linalg.det(mat)-lam)<1e-13
        for x in np.linspace(0,1,20):
            g=min(x,p)-x*p
            phi_int=(math.sqrt(alpha)*x if x<=p else (1-x)/math.sqrt(alpha))
            assert abs(g/math.sqrt(p*(1-p))-phi_int)<1e-12
    for z in [0.4,0.65,1.0]:
        for p in [.3,.5]:
            low,center,high=[cdf(z,p,lam) for lam in [-.3,0,.4]]
            assert low>center>high>0,(z,p,low,center,high)
            assert abs(center-classical_kolmogorov(z))<2e-10,(z,p,center)
        periodic_limit=classical_kolmogorov(math.sqrt(2)*z)**2
        assert abs(cdf(z,.5,-.9999)-periodic_limit)<7e-5
    z,p,lam=.65,.3,.4
    q=cdf(z,p,lam)
    sim=simulate_ks(p,lam)
    empirical=np.mean(sim<=z)
    # Conservative test: 3000 replicates with Bernoulli standard error ~.0065.
    assert abs(empirical-q)<.035,(empirical,q)
    print('PASS algebra, Kolmogorov identity, monotonicity, periodic limit, simulation')
    print('Example: p=0.3, z=0.65, lambda=0.4: analytic CDF',round(q,9),
          'simulated n=1000 CDF',round(float(empirical),5))

if __name__=='__main__':
    main()
