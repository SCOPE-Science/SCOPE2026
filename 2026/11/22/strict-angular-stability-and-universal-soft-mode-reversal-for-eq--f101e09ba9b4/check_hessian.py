"""Reproducibility checks for equiradial Blaschke angular-speed variance.

Uses only Python's standard library. Finite tests support, but do not replace,
the analytic arguments in RESULT.md.
"""
import math
import cmath


def a(n, k, u):
    t = u**n
    return u**k * (k*k/(1-t) + 2*k*n*t/(1-t)**2 + n*n*t*(1+t)/(1-t)**3)


def kappa(n, k, u):
    return n*(a(n,k,u)+a(n,n-k,u)-2*a(n,0,u))


def variance(n, u, angles):
    # Direct integral of the pairwise Poisson autocorrelation.
    total = 0.0
    for alpha in angles:
        for beta in angles:
            total += (1-u*u)/(1-2*u*math.cos(alpha-beta)+u*u)
    return total - n*n


def check():
    count = 0
    for n in range(5, 18):
        for u in (0.035, 0.13, 0.38, 0.71, 0.94):
            eigs = [kappa(n,k,u) for k in range(1,n)]
            assert all(v > 0 for v in eigs), (n,u,eigs)
            count += n-1
            for k in range(1,n):
                assert abs(eigs[k-1]-eigs[n-k-1]) < 2e-7*max(1,eigs[k-1])
                count += 1
            base_angles = [2*math.pi*j/n for j in range(n)]
            exact = 2*n*n*u**n/(1-u**n)
            direct = variance(n,u,base_angles)
            assert abs(direct-exact) < 1e-6*max(1,exact)
            count += 1
    # Quadratic perturbation tested against independent pair-kernel formula.
    for n,k,u in [(5,1,.5),(5,2,.5),(6,3,.7),(7,2,.35),
                  (8,1,.85),(9,3,.55),(11,5,.25),(16,4,.8)]:
        theta=[2*math.pi*j/n for j in range(n)]
        vector=[math.cos(k*t) for t in theta]
        mean=sum(vector)/n
        vector=[v-mean for v in vector]
        norm=math.sqrt(sum(v*v for v in vector))
        vector=[v/norm for v in vector]
        h=0.0004
        v0=variance(n,u,theta)
        vp=variance(n,u,[t+h*v for t,v in zip(theta,vector)])
        vm=variance(n,u,[t-h*v for t,v in zip(theta,vector)])
        finite=(vp+vm-2*v0)/(2*h*h)
        exact=kappa(n,k,u)
        assert abs(finite-exact) < 2e-5*max(1,exact), (n,k,u,finite,exact)
        count += 1
    # Check endpoint ordering at representative sufficiently separated radii.
    for n in range(5,18):
        ks=range(1,n//2+1)
        small={k:kappa(n,k,.005) for k in ks}
        near={k:kappa(n,k,.999) for k in ks}
        assert min(small, key=small.get)==n//2, n
        assert min(near, key=near.get)==1, n
        count += 2
    print(f'PASS: {count} finite formula, symmetry, positivity, curvature and mode diagnostics')


if __name__=='__main__':
    check()
