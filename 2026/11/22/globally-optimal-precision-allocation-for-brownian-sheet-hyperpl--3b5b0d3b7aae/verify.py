"""Independent covariance and optimization checks for orthogonal Brownian-sheet slice cubature.
Run: python3 verify.py (Python standard library only).
Exact rational arithmetic is used for the covariance identities and Gaussian conditioning checks.
Numerical experiments are supplemental and do not prove the global theorem.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random


def c(x):
    return x-x*x/2


def solve(a,b):
    n=len(b)
    m=[list(a[i])+[b[i]] for i in range(n)]
    for j in range(n):
        i=max(range(j,n),key=lambda i:abs(m[i][j]))
        m[j],m[i]=m[i],m[j]
        pivot=m[j][j]
        assert pivot!=0
        m[j]=[z/pivot for z in m[j]]
        for i in range(n):
            if i != j:
                m[i]=[m[i][k]-m[i][j]*m[j][k] for k in range(n+1)]
    return [m[i][-1] for i in range(n)]


def exact_risk_from_covariance(xs,ps):
    d=len(xs)
    K=[]
    for i in range(d):
        row=[]
        for j in range(d):
            if i==j:
                row.append(xs[i]/3**(d-1)+1/ps[i])
            else:
                row.append(c(xs[i])*c(xs[j])/3**(d-2))
        K.append(row)
    k=[c(x)/3**(d-1) for x in xs]
    w=solve(K,k)
    return F(1,3**d)-sum(k[i]*w[i] for i in range(d))


def exact_risk_from_independent_residuals(xs,ps):
    d=len(xs)
    prec=F(3**d,1)
    for x,p in zip(xs,ps):
        prec+=9*c(x)**2/(F(1,3**(d-1))*(x-3*c(x)**2)+1/p)
    return 1/prec


def r_star(d,P):
    C=4*d*3**(d-1)
    disc=(C-2*P)**2+12*P*C
    # Stable branches of the positive quadratic root.
    if P<C:
        return 2*C/(sqrt(disc)+C-2*P)
    return (2*P-C+sqrt(disc))/(6*P)


def risk_star(d,P):
    r=r_star(d,P)
    z=c(r)**2
    num=3**(d-1)+P/d*(r-3*z)
    den=3**(d-1)+P/d*(r+3*(d-1)*z)
    return num/(3**d*den)


def fl_risk(xs,ps):
    d=len(xs)
    prec=3.**d
    for x,p in zip(xs,ps):
        if p>0:
            prec+=9*c(x)**2/(3.**(-(d-1))*(x-3*c(x)**2)+1/p)
    return 1/prec


def test():
    rng=Random(20201118)
    exact=0
    for d in range(2,7):
        for trial in range(25):
            xs=[F(rng.randrange(1,19),20) for _ in range(d)]
            ps=[F(rng.randrange(1,15),3) for _ in range(d)]
            lhs=exact_risk_from_covariance(xs,ps)
            rhs=exact_risk_from_independent_residuals(xs,ps)
            assert lhs==rhs,(d,xs,ps,lhs,rhs)
            # Covariance of distinct residual slices conditional on J equals zero.
            for i in range(d):
                for j in range(i+1,d):
                    cross=c(xs[i])*c(xs[j])/3**(d-2)
                    projected=(c(xs[i])/3**(d-1))*(c(xs[j])/3**(d-1))*3**d
                    assert cross==projected
            exact+=1
    root_count=0
    grid_count=0
    for d in range(2,11):
        C=4*d*3**(d-1)
        for P in [0.001,0.1,1.,3.,10.,100.,1000.,10**6,0.1*C,C,10*C]:
            r=r_star(d,P)
            assert 2/3<r<1
            assert isclose(C*(1-r),P*r*(3*r-2),rel_tol=3e-8,abs_tol=1e-7)
            expected=risk_star(d,P)
            actual=fl_risk([r]*d,[P/d]*d)
            assert isclose(expected,actual,rel_tol=3e-12,abs_tol=1e-15),(d,P,expected,actual)
            for _ in range(50):
                raw=[rng.random()+0.001 for _ in range(d)]
                ps=[P*v/sum(raw) for v in raw]
                xs=[rng.random() for _ in range(d)]
                observed=fl_risk(xs,ps)
                assert observed >= expected-2e-14,(d,P,xs,ps,observed,expected)
                grid_count+=1
            root_count+=1
    # Noiseless posterior fraction (noise variance exactly zero).
    for d in range(2,8):
        xs=[F(2,3)]*d
        zeros=[F(10**20,1)]*d
        approx=exact_risk_from_covariance(xs,zeros)
        limit=F(1,3**d*(8*d+1))
        assert abs(approx-limit)<F(1,10**12)
    # One-coordinate stationary derivative is strictly decreasing in x.
    for x in [F(2,3),F(3,4),F(7,8),F(1)]:
        A=3*x**3-9*x*x+6*x-1
        Q=9*x**4-12*x**3+6*x-2
        assert A<0 and Q>0
    print('PASS',exact,'exact rational covariance/conditioning cases;',root_count,
          'stationary-root/risk cases;',grid_count,'supplementary global comparisons; asymptotic limit checks')

if __name__=='__main__':
    test()
