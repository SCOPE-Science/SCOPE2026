"""Exact reproducible checks for the vertex-covariance formula for panhandle base polytopes.

Run with Python 3 (standard library only). Finite checks supplement, not replace,
the all-parameter algebraic argument in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations


def predicted(r, s, t):
    assert 2 <= r <= s and t >= 2
    d = s-r+1
    p = Q(t*r,d+t*r)
    lam_h = Q(r*d*((d-1)+t*(r-1)),s*(s-1)*(d+t*r))
    lam_t = Q(r,d+t*r)
    lam_b = Q(r*d*(s+t),s*(d+t*r)**2)
    assert lam_b == p*(1-p)*(Q(1,s)+Q(1,t))
    assert lam_h == ((1-p)*r*(s-r)+p*(r-1)*(s-r+1))/(s*(s-1))
    assert lam_t == p/t
    assert 0 < lam_b < min(lam_h, lam_t)
    # The sign of the handle-tail eigenvalue gap, and exact crossover.
    assert (lam_h > lam_t) == (t*d > 2*d+r-2)
    assert (lam_h == lam_t) == (t*d == 2*d+r-2)
    return lam_h, lam_t, lam_b


def matvec(a, v):
    return [sum(row[j]*v[j] for j in range(len(v))) for row in a]


def enumerate_exact(r, s, t):
    n = s+t
    bases = []
    for b in combinations(range(n),r):
        if sum(j<s for j in b)>=r-1:
            bases.append(set(b))
    assert len(bases) == __import__('math').comb(s,r)+t*__import__('math').comb(s,r-1)
    means = [Q(sum(j in b for b in bases),len(bases)) for j in range(n)]
    cov = [[Q(sum((i in b) and (j in b) for b in bases),len(bases))-means[i]*means[j]
            for j in range(n)] for i in range(n)]
    vals = predicted(r,s,t)
    vectors = [
        [Q(int(j==0)-int(j==1)) for j in range(n)],
        [Q(int(j==s)-int(j==s+1)) for j in range(n)],
        [Q(1,s) if j<s else -Q(1,t) for j in range(n)],
        [Q(1) for j in range(n)],
    ]
    for v, eig in zip(vectors, [*vals,Q(0)]):
        assert matvec(cov,v)==[eig*z for z in v], (r,s,t,eig)
    assert means[:s]==[Q(r-Q(t*r,s-r+1+t*r),s)]*s
    assert means[s:]==[Q(r,s-r+1+t*r)]*t


def asymptotic_test():
    from math import isclose
    rho=Q(2,5); tau=Q(3,4)
    for s in [400,1600,6400]:
        r=int(rho*s); t=int(tau*s)
        h,tail,mix=predicted(r,s,t)
        limits=(float(rho*(1-rho)),float(1/tau),float((1-rho)*(1+tau)/(tau*tau*rho)))
        scaled=(float(h),float(s*tail),float(s*s*mix))
        relative=max(abs(x/y-1) for x,y in zip(scaled,limits))
        assert relative < 10/s, (s,scaled,limits,relative)
        cond=float(max(h,tail)/mix)/(s*s)
        target=float(rho*rho*tau*tau/(1+tau))
        assert abs(cond/target-1)<10/s


def main():
    count=0
    for s in range(2,7):
        for r in range(2,s+1):
            for t in range(2,6):
                enumerate_exact(r,s,t)
                count+=1
    for s in range(2,35):
        for r in range(2,s+1):
            for t in range(2,40):
                predicted(r,s,t)
    asymptotic_test()
    print('PANHANDLE_VERTEX_COVARIANCE_SPECTRAL_CHECKS_PASSED', count)

if __name__=='__main__':
    main()
