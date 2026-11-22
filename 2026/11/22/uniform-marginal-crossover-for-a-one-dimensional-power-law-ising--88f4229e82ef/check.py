"""Standalone numerical consistency checks for the marginal Ising droplet crossover.
Uses mpmath >=1.2. Exact energies use convergent power sums and Hurwitz zeta.
No finite sample is a proof of the uniform asymptotics.
"""
from mpmath import mp
mp.dps = 60

def droplet_energy(n, sigma, h):
    if n == 0:
        return mp.mpf('0')
    return 4 * (mp.fsum(mp.power(r, -sigma) for r in range(1, n+1)) + n*mp.zeta(1+sigma, n+1)) - 2*h*n

def energy_fast(n, sigma, h):
    if n == 0:
        return mp.mpf('0')
    if sigma == 1:
        harmonic = mp.digamma(n+1) + mp.euler
        return 4*(harmonic + n*mp.zeta(2, n+1)) - 2*h*n
    return 4*(mp.zeta(sigma) - mp.zeta(sigma,n+1) + n*mp.zeta(1+sigma,n+1)) - 2*h*n

def increment(n, sigma, h):
    return 4*mp.zeta(1+sigma,n+1) - 2*h

def maximizer(sigma,h):
    # E(n+1)-E(n) = increment(n). Strictly decreasing with n.
    lo, hi = 0, 1
    while increment(hi,sigma,h)>0:
        hi *= 2
    while hi-lo>1:
        md = (lo+hi)//2
        if increment(md,sigma,h)>0: lo=md
        else: hi=md
    return hi if increment(lo,sigma,h)>0 else lo

def phi(t):
    return -mp.expm1(-t)/t if t else mp.mpf(1)

def predicted(ell,t):
    return ell*phi(t)+mp.euler-t*mp.exp(-t)

def reduced_barrier(ell,t):
    sigma=1+mp.mpf(t)/ell
    h=2*mp.exp(-ell)
    n=maximizer(sigma,h)
    return energy_fast(n,sigma,h)/4, n

def test():
    count = 0
    # Independently check the exact infinite-chain count of wall-crossing bonds
    for sigstr in ['0.65','1.0','1.35']:
        sig=mp.mpf(sigstr)
        for n in range(1,11):
            slow=droplet_energy(n,sig,mp.mpf('.03'))
            fast=energy_fast(n,sig,mp.mpf('.03'))
            assert mp.almosteq(slow,fast,rel_eps=mp.mpf('1e-45'))
            count+=1
    # Verify strict discrete concavity and exact critical index for several regimes
    for ell in [6,8,10,13]:
        for t in [-2,-1,0,1,2]:
            sig=1+mp.mpf(t)/ell; h=2*mp.exp(-ell)
            val,n=reduced_barrier(ell,t)
            assert increment(n,sig,h)<=0
            assert n==0 or increment(n-1,sig,h)>=0
            if n>0:
                assert energy_fast(n,sig,h)>=energy_fast(n-1,sig,h)
            assert energy_fast(n,sig,h)>=energy_fast(n+1,sig,h)
            xstar=(mp.exp(ell)/sig)**(1/sig)
            assert abs(n-xstar)<4
            count+=5
    # Convergence in bounded marginal-window t, including both sides of sigma=1
    for t in [-2,-1,0,1,2]:
        errors=[]
        for ell in [10,16,24,40]:
            b,n=reduced_barrier(ell,t)
            errors.append(abs(b-predicted(ell,mp.mpf(t))))
            count+=1
        if t==0:
            assert max(errors)<mp.mpf('0.00001')
        else:
            assert errors[-1]<errors[0]
        count+=1
    # Exact large-n Euler-Maclaurin cancellation coefficient is 1/12.
    for sigstr in ['0.7','0.9','1.1','1.4']:
        sig=mp.mpf(sigstr); n=500
        intf=mp.zeta(sig)-mp.power(n,1-sig)/(sig*(sig-1))
        exact=energy_fast(n,sig,0)/4
        assert abs((exact-intf)*n**(1+sig)-mp.mpf(1)/12)<mp.mpf('.00001')
        count+=1
    print('PASS',count,'deterministic consistency checks')
    for t in [-2,-1,0,1,2]:
        v1,_=reduced_barrier(10,t);v2,_=reduced_barrier(40,t)
        print('t=',t,'error ell=10',mp.nstr(v1-predicted(10,mp.mpf(t)),7),'ell=40',mp.nstr(v2-predicted(40,mp.mpf(t)),7))
if __name__=='__main__': test()
