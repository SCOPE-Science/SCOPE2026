"""Finite checks for canonical near-close-packing Fourier diffraction.
Run with Python 3 standard library: python3 verify_diffraction.py
The infinite-size convergence requires the analytic proof in RESULT.md.
"""
from math import comb, cos, pi, isclose
from itertools import combinations


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def arc(d, t):
    return choose(d-t-2, t)


def pair_count(n, k, d):
    return sum(arc(d, t) * arc(n-d, k-2-t) for t in range(k-1))


def exact_covariance(n, k):
    count = n * choose(n-k-1, k-1) // k
    assert count > 0 and n >= 2*k+1
    p = k/n
    return [p*(1-p)] + [pair_count(n,k,d)/count-p*p for d in range(1,n)]


def eigenvalues(n, k):
    cov = exact_covariance(n,k)
    return [sum(cov[d]*cos(2*pi*j*d/n) for d in range(n)) for j in range(n)]


def brute_covariance(n,k):
    sets = [set(t) for t in combinations(range(n),k) if all((i+1)%n not in t for i in t)]
    N = len(sets)
    p = k/n
    return [p*(1-p)] + [sum((0 in s and d in s) for s in sets)/N-p*p for d in range(1,n)]


def profile(m,r):
    # Exact values in the first two nontrivial defect strata.
    omega = 2*pi*(r-(m%2)/2)
    if m==1:
        return 1/(omega*omega)
    if m==2:
        return 1/12 if r==0 else 2/(omega*omega)
    # Higher defect count: composite Simpson rule on a polynomial times cosine.
    K=1000
    f=lambda t: (1-t)*(1-2*t)**m*cos(omega*t)
    return (f(0)+f(1)+4*sum(f((2*i-1)/K) for i in range(1,K//2+1))
            +2*sum(f(2*i/K) for i in range(1,K//2)))/(6*K)


def main():
    assertions=0
    for n in range(3,16):
        for k in range(1,n//2+1):
            if n==2*k:
                continue
            a=exact_covariance(n,k)
            b=brute_covariance(n,k)
            assert all(isclose(x,y,abs_tol=2e-13) for x,y in zip(a,b)),(n,k)
            assertions += n
            ev=eigenvalues(n,k)
            assert abs(ev[0])<2e-12
            assert min(ev[1:])>1e-10,(n,k,min(ev[1:]))
            assertions += n
    for m in (1,2,3,4,5):
        for k in (30,60):
            n=2*k+m
            ev=eigenvalues(n,k)
            for r in (-2,-1,0,1,2):
                j=n//2+r
                actual=ev[j]/n
                target=profile(m,r)
                tolerance=0.0018 if k==30 else 0.0009
                assert abs(actual-target)<tolerance, (m,k,r,actual,target)
                assertions+=1
    for m in (1,2,3,4):
        for r in range(-70,71):
            v=profile(m,r)
            assert v> -1e-7,(m,r,v)
            assertions+=1
    print(f'PASS: {assertions} checked equalities, inequalities, and limiting-profile approximations.')

if __name__=='__main__':
    main()
