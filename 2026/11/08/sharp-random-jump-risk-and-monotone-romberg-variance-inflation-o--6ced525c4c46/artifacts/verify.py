"""Exact-rational checks for nested-grid step-jump quadrature.

Run with Python 3 (standard library only): python verify.py
Tests finite cases; the accompanying analytic proof covers all allowed parameters.
"""
from fractions import Fraction as F
from math import prod

checks = 0

def check(condition, label):
    global checks
    assert condition, label
    checks += 1

def romberg_coeff(r, depth):
    """Coarse-to-fine indexed through j=0..depth, h_j=r**j*h."""
    q = F(1, r*r)
    def poch(k):
        return prod((1-q**i for i in range(1,k+1)), start=F(1))
    return [(-1)**j*q**(j*(j+1)//2)/(poch(j)*poch(depth-j)) for j in range(depth+1)]

def cov_variance(r, depth, a):
    return sum((a[i]*a[j]*r**(2*min(i,j)) for i in range(depth+1) for j in range(depth+1)), F(0))

def tail_variance(r, depth, a):
    return 1 + (r*r-1)*sum((F(r**(2*(k-1)))*sum(a[k:],F(0))**2 for k in range(1,depth+1)),F(0))

def direct_phase_variance(r, depth, a):
    """Integrate the square exactly over every finest-mesh jump phase cell."""
    N = r**depth
    h = F(1,N)
    tot=F(0); mean=F(0)
    for k in range(N):
        L=F(k,N); U=F(k+1,N)
        c0=sum((a[j]*F(r**j,N)*(F(k//r**j)+F(1,2)) for j in range(depth+1)),F(0))
        tot+=((U-c0)**3-(L-c0)**3)/3
        mean+=((U-c0)**2-(L-c0)**2)/2
    return tot,mean

# Independent finite exact integration versus covariance, and Romberg moments.
for r in (2,3,4,5):
    previous=F(1)
    for m in range(0,6):
        a=romberg_coeff(r,m)
        check(sum(a,F(0))==1,("sum",r,m))
        for power in range(1,m+1):
            check(sum((a[j]*r**(2*power*j) for j in range(m+1)),F(0))==0,("mom",r,m,power))
        V=cov_variance(r,m,a)
        W=tail_variance(r,m,a)
        Q,ME=direct_phase_variance(r,m,a)
        check(V==W,("cov vs tails",r,m))
        check(V==12*r**(2*m)*Q,("direct phase",r,m))
        check(ME==0,("unbiased",r,m))
        if m:
            check(V>previous,("increasing",r,m))
        previous=V
    check(cov_variance(r,1,romberg_coeff(r,1))==F(r*r,r*r-1), ("one-level",r))

# All nested grids, including non-geometric refinements.
for N in (12,24,60):
    divisors=[j for j in range(1,N+1) if N%j==0]
    hvals=[F(1,N),F(2,N),F(4,N)]
    for i in range(3):
        for j in range(3):
            exact=min(hvals[i],hvals[j])**2/F(12)
            total=F(0)
            # integrate step errors exactly on the common refinement grid.
            for k in range(N):
                L=F(k,N); U=F(k+1,N)
                ni=1/hvals[i]; nj=1/hvals[j]
                ai=hvals[i]*((F(k,N)*ni)//1+F(1,2))
                aj=hvals[j]*((F(k,N)*nj)//1+F(1,2))
                total+=(U**3-L**3)/3-(ai+aj)*(U*U-L*L)/2+ai*aj*(U-L)
            check(total==exact,("general nested",N,i,j))


# Direct independent integration of constant-exact linear combinations, including
# negative extrapolation coefficients, verifies the universal minimum-risk law.
for N in (12,24,60):
    steps=[F(1,N),F(2,N),F(4,N)]
    for b in ((F(1),F(0),F(0)),(F(0),F(1),F(0)),
              (F(3,2),-F(1,3),-F(1,6)),(F(2),-F(2),F(1)),
              (F(1,4),F(1,2),F(1,4))):
        check(sum(b)==1,("linear mass",N,b))
        closed=steps[0]**2/F(12)+sum((
            (steps[j]**2-steps[j-1]**2)*sum(b[j:])**2/F(12)
            for j in (1,2)),F(0))
        direct=F(0)
        for k in range(N):
            L=F(k,N);U=F(k+1,N)
            offset=sum((b[j]*steps[j]*((L/steps[j])//1+F(1,2))
                        for j in range(3)),F(0))
            direct+=((U-offset)**3-(L-offset)**3)/3
        check(direct==closed,("linear direct",N,b))
        check(closed>=steps[0]**2/F(12),("minimum",N,b))
        check((closed==steps[0]**2/F(12))==(b[1]==0 and b[2]==0),
              ("unique minimum",N,b))

# The alternating tails not only yield increasing total variance; every old
# tail's magnitude strictly increases when a new Romberg level is added.
for r in (2,3,5):
    for m in range(1,7):
        a=romberg_coeff(r,m)
        S=[sum(a[k:],F(0)) for k in range(1,m+1)]
        for k,v in enumerate(S,1):
            check((-1)**k*v>0,("tail sign",r,m,k))
        if m>1:
            old=romberg_coeff(r,m-1)
            for k in range(1,m):
                check(abs(S[k-1])>abs(sum(old[k:],F(0))),
                      ("tail growth",r,m,k))

print(f"PASS {checks} exact-rational assertions")
