"""Reproduce finite exact identities and independent hull-area checks for capped cubes.

Not a proof of the general optimization theorem.
"""
from fractions import Fraction
from math import comb, factorial, sqrt
from itertools import product, combinations
import numpy as np
from scipy.spatial import ConvexHull
from scipy.stats import irwinhall


def cdf(n, t):
    t = Fraction(t)
    return sum(((-1)**j)*comb(n, j)*max(t-j, Fraction(0))**n
               for j in range(n+1))/factorial(n)


def density(n, t):
    t = Fraction(t)
    return sum(((-1)**j)*comb(n, j)*max(t-j, Fraction(0))**(n-1)
               for j in range(n+1))/factorial(n-1)


def density_derivative(n, t):
    t = Fraction(t)
    assert n >= 3
    return sum(((-1)**j)*comb(n, j)*max(t-j, Fraction(0))**(n-2)
               for j in range(n+1))/factorial(n-2)


def vertices(n, t):
    t=float(t)
    q=int(t)
    v=[list(bits) for bits in product((0.,1.), repeat=n) if sum(bits)<=t+1e-10]
    r=t-q
    if 1e-10 < r < 1-1e-10:
        for inds in combinations(range(n), q):
            for j in range(n):
                if j in inds:
                    continue
                z=[0.]*n
                for i in inds:z[i]=1.
                z[j]=r
                v.append(z)
    return np.array(v)


def geometry(n,t):
    x=vertices(n,t)
    h=ConvexHull(x)
    F=float(cdf(n,Fraction(str(t))))
    S=n*(float(cdf(n-1,Fraction(str(t))))+float(cdf(n-1,Fraction(str(t))-1)))+sqrt(n)*float(density(n,Fraction(str(t))))
    return abs(h.volume-F),abs(h.area-S),h.volume,h.area

count=0
for n in range(2,36):
    for k in range(1,14):
        t=Fraction(n*7*k, 14*17)
        if not (0<t<n):continue
        F=cdf(n,t);f=density(n,t)
        assert n*(cdf(n-1,t)-F)==(n-t)*f
        assert n*(F-cdf(n-1,t-1))==t*f
        if n>=3 and t.denominator !=1:
            fd=density_derivative(n,t)
            # Verify shape derivative sign using a direct exact difference expression.
            B=F*fd-Fraction(n-1,n)*f*f
            assert B<=0
        count+=1
print('EXACT_BSPLINE_IDENTITIES',count)

hull_count=0
for n in range(2,6):
    values=[.4,.9,1.,1.35,n-.35, (n+sqrt(n))/2, float(n)]
    for t in values:
        if not 0<t<=n:continue
        dv,da,_,_=geometry(n,t)
        assert dv<1e-7,(n,t,'volume',dv)
        assert da<2e-7,(n,t,'area',da)
        hull_count+=1
print('INDEPENDENT_CONVEX_HULL_AREA_VOLUME',hull_count)

opt_count=0
for n in [2,3,4,5,6,7,8,10,15,20,30,50,100,200]:
    tstar=(n+sqrt(n))/2
    t=np.linspace(max(.06,n/2-3*sqrt(n)),n,3000)
    F=irwinhall(n).cdf(t)
    f=irwinhall(n).pdf(t)
    Q=np.divide(2*n*F+(n-2*t+sqrt(n))*f, F**((n-1)/n), out=np.full_like(F,np.inf), where=F>1e-200)
    m=np.argmin(Q)
    assert abs(t[m]-tstar) < max(.07,n/2999*1.1), (n,t[m],tstar)
    opt_count+=1
print('NUMERICAL_OPTIMUM',opt_count)
print('CAPPED_CUBE_SURFACE_PASS')
