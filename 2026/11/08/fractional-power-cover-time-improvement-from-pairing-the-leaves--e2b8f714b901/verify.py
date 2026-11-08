"""Exact reproducibility checks for cover times on friendship graphs.

Python 3, SymPy (for independent finite-state linear equations).
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, gamma
import sympy as sp


def exact_from_integral(m):
    """Exact finite binomial expansion of the survival integral."""
    total = Q(0)
    for j in range(1, m + 1):
        for k in range(j + 1):
            total += Q(4 * (-1)**(j+1+k) * comb(m, j) * comb(j, k) * 2**(j-k), 3*j + k)
    return 3*m*total - 2


def exact_from_petal_chain(m):
    """Independent coupon-state first-step rational recurrence."""
    @lru_cache(None)
    def exp(a, b):
        if a == b == 0: return Q(0)
        progress = Q(a,m) + Q(3*b,4*m)
        forward = Q(a,2*m) * (exp(a-1,b+1) + exp(a-1,b)) if a else Q(0)
        if b: forward += Q(3*b,4*m)*exp(a,b-1)
        return (1+forward)/progress
    return 3*exp(m,0)-2


def exact_from_full_walk(m):
    """Separate vertex-level hitting-time equations over all visited sets."""
    n=2*m+1
    nbrs = [[] for _ in range(n)]
    for i in range(m):
        a,b=2*i+1,2*i+2
        nbrs[0].extend([a,b]); nbrs[a].extend([0,b]); nbrs[b].extend([0,a])
    full=(1<<n)-1
    f={(full,v):sp.Rational(0) for v in range(n)}
    for mask in range(full-1,0,-1):
        if mask&1==0: continue
        known=[v for v in range(n) if mask>>v&1]
        index={v:i for i,v in enumerate(known)}
        A=sp.eye(len(known)); B=sp.ones(len(known),1)
        for v in known:
            i=index[v]
            for w in nbrs[v]:
                if mask>>w&1:
                    A[i,index[w]]-=sp.Rational(1,len(nbrs[v]))
                else:
                    B[i,0]+=sp.Rational(f[(mask|(1<<w),w)],len(nbrs[v]))
        result=A.LUsolve(B)
        for v in known: f[mask,v]=result[index[v],0]
    return Q(int(f[1,0].p),int(f[1,0].q))


def main():
    for m in range(1, 11):
        integral=exact_from_integral(m)
        chain=exact_from_petal_chain(m)
        assert integral==chain,(m,integral,chain)
        if m<=4:
            walk=exact_from_full_walk(m)
            assert integral==walk,(m,integral,walk)
        if m<=6: print('m',m,'friend_cover',integral,'star_cover',4*m*sum((Q(1,k) for k in range(1,2*m+1)),Q(0))-1)
    c=2**(2/3)*gamma(4/3)
    assert 1.41<c<1.43
    from scipy.integrate import quad
    from math import exp, log, expm1, log1p
    from scipy.special import digamma
    from numpy import euler_gamma
    for m in (100, 1000, 10000, 100000):
        def integrand(t):
            survival = 2*exp(-0.75*t) - exp(-t)
            return -expm1(m*log1p(-survival))
        base=4/3*log(2*m)
        # Integrate finite domain, with exponential tail controlled by the rate 3/4.
        res=quad(integrand,0,max(2*base,50),epsabs=1e-9,limit=400)[0]
        tail=quad(integrand,max(2*base,50),max(2*base,50)+60,epsabs=1e-9,limit=400)[0]
        actual=3*m*(res+tail)-2
        harmonic=digamma(2*m+1)+euler_gamma
        star=4*m*harmonic-1
        scaled=(star-actual)/m**(2/3)
        assert abs(scaled-c) < 1.2/m**(1/3), (m,scaled,c)
        print('numerical_asymptotic_check',m,format(scaled,'.9f'))
    print('asymptotic_difference_coefficient',format(c,'.14f'))
    print('PASS: independent full-walk equations, petal-chain recursion, exact integral, coefficient')

if __name__=='__main__': main()
