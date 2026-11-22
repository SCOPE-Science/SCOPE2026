"""Independent event-clock Monte Carlo of three-time latent-energy cumulants.
Requires numpy. Run: python simulate.py
"""
import numpy as np

def step(u, dt, theta, q, rng):
    n = rng.poisson(theta*dt, len(u))
    m = int(n.max())
    if m:
        raw = rng.uniform(0.0,dt,size=(len(u),m))
        times = np.sort(np.where(np.arange(m)[None,:]<n[:,None], raw, np.inf),axis=1)
        last=np.zeros(len(u))
        for j in range(m):
            sel=n>j
            if np.any(sel):
                h=times[sel,j]-last[sel]
                u[sel]=q*(1-(1-u[sel])*np.exp(-h))
                last[sel]=times[sel,j]
        u=1-(1-u)*np.exp(-(dt-last))
    else:
        u=1-(1-u)*np.exp(-dt)
    return u

def run(q,theta,s,t,samples=200000,seed=2026):
    rng=np.random.default_rng(seed)
    u=np.zeros(samples)
    # Stationary skeleton directly after jumps, using 80 independent gaps.
    for _ in range(80):
        gaps=rng.exponential(1/theta,samples)
        u=q*(1-(1-u)*np.exp(-gaps))
    ages=rng.exponential(1/theta,samples)
    u0=1-(1-u)*np.exp(-ages)
    u1=step(u0.copy(),s,theta,q,rng)
    u2=step(u1.copy(),t,theta,q,rng)
    mu=1/(1+theta*(1-q))
    observed=np.mean((u0-mu)*(u1-mu)*(u2-mu))
    a=1+theta*(1-q);b=2+theta*(1-q*q);c=3+theta*(1-q**3)
    var=theta*(1-q)**2/(a*a*b)
    h=2*theta*(1-q)**2/(a*(b-a))
    tt=2*theta*(1-q)**3/(a*b*(b-a)*c)
    predicted=np.exp(-a*(s+t))*(h*var-tt*np.exp(-(b-a)*s))
    stderr=np.std((u0-mu)*(u1-mu)*(u2-mu),ddof=1)/np.sqrt(samples)
    print('q,theta,s,t=',q,theta,s,t,'MC=',observed,'exact=',predicted,'SE=',stderr)
    assert abs(observed-predicted)<5*stderr +0.0001

if __name__=='__main__':
    for q,theta,s,t in [(0.25,0.5,0.1,0.6),(0.25,0.5,0.9,0.6),(0.25,2.0,0.2,0.6),(0.0,0.5,0.6,0.2)]:
        run(q,theta,s,t)
