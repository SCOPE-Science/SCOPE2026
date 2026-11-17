"""Exact standalone checks for centered-cell perturbations of Bernstein averages.

Requires only Python's standard library. Each finite rational check is a
corroboration; analytical proofs are provided separately.
"""
from fractions import Fraction as F
from math import comb


def weights(n,x):
    return [F(comb(n,j))*x**j*(1-x)**(n-j) for j in range(n+1)]


def sharp_formula(n,p,nu):
    return sum((w*q*abs(F(j,n)-u) for j,w in enumerate(p)
                for u,q in nu),F(0))/(n+1)


def w1_independent(n,p,nu):
    dif={}
    for j,w in enumerate(p):
        dif[F(j,n)]=dif.get(F(j,n),F(0))+w
        for u,q in nu:
            t=F(j, n+1)+u/F(n+1)
            dif[t]=dif.get(t,F(0))-w*q
    x=sorted(dif)
    flux=F(0);out=F(0)
    for i,t in enumerate(x[:-1]):
        flux+=dif[t]
        out+=abs(flux)*(x[i+1]-t)
    return out


def spline(n,t):
    assert F(0)<=t<=F(1)
    result=F(0)
    for j in range(n+1):
        left=F(j,n+1);right=F(j+1,n+1);pivot=F(j,n)
        if t>=right:
            result+=(pivot-left)-(right-pivot)
        elif t>left:
            result+=min(t,pivot)-left-max(F(0),t-pivot)
            break
        else: break
    return result


def binmad(n,x):
    return sum((w*abs(F(j,n)-x) for j,w in enumerate(weights(n,x))),F(0))


def de_moivre(n,x):
    if x==0 or x==1:return F(0)
    k=min(n-1,(n*x).numerator//(n*x).denominator)
    return 2*comb(n-1,k)*x**(k+1)*(1-x)**(n-k)


def peak(n):
    if n%2:
        r=(n-1)//2
        return [F(1,2)],F(comb(2*r,r),2**(2*r+1))
    r=n//2
    pts=[F(r,2*r+1),F(r+1,2*r+1)]
    return pts,de_moivre(n,pts[0])

checks=0
for n in range(1,10):
    for x in [F(0),F(1),F(1,2),F(1,3),F(2,5),F(7,11)]:
        p=weights(n,x)
        nus=[[(x,F(1))],[(F(0),1-x),(F(1),x)],[(F(0),F(1,2)*(1-x)),(x,F(1,2)),(F(1),F(1,2)*x)],[(F(1,2),F(1))]]
        for nu in nus:
            assert sum((q for _,q in nu),F(0))==1
            predicted=sharp_formula(n,p,nu)
            assert predicted==w1_independent(n,p,nu),(n,x,nu)
            actual=sum((w*q*(spline(n,F(j,n))-spline(n,(j+u)/F(n+1))) for j,w in enumerate(p) for u,q in nu),F(0))
            assert actual==predicted,(n,x,nu,actual,predicted)
            if sum(u*q for u,q in nu)==x:
                assert predicted>=binmad(n,x)/F(n+1)
            checks+=1
print('INDEPENDENT_RATIONAL_CDF_W1_AND_UNIVERSAL_SPLINE',checks,'PASS')
checks=0
for n in range(1,55):
    pts,pv=peak(n)
    for x in [F(0),F(1),F(1,2),F(1,3),F(2,5),F(7,11)]+pts:
        assert binmad(n,x)==de_moivre(n,x)
        assert binmad(n,x)<=pv
        checks+=1
    for k in range(n):
        x=F(k+1,n+1)
        assert de_moivre(n,x)<=pv
        checks+=1
    assert all(de_moivre(n,z)==pv for z in pts)
    # Every conditional cell max occurs at x=(k+1)/(n+1);
    # the grid of k includes every possible global maximizer.
print('EXACT_BINOMIAL_MAD_ALL_CELLS_AND_PARITY_MAXIMA',checks,'PASS')
# Weighted distributions beyond binomial, and arbitrary finitely supported jitter.
checks=0
for n in range(1,11):
    for i in range(7):
        un=[F((j+1)*(j+i+2)) for j in range(n+1)]
        norm=sum(un);p=[v/norm for v in un]
        nu=[(F(0),F(i+1,2*(i+2))),(F(2,3),F(1,2)),(F(1),F(1,2*(i+2)))]
        assert sharp_formula(n,p,nu)==w1_independent(n,p,nu)
        checks+=1
print('ARBITRARY_CELL_MIXTURE_TRANSPORT',checks,'PASS')
# Asymptotic benchmark based on Stirling, numerically corroborative only.
import math
for n in [100,200,500,1000]:
    _,v=peak(n)
    ratio=float(v)*math.sqrt(2*math.pi*n)
    assert abs(ratio-1)<0.025,(n,ratio)
print('ASYMPTOTIC_STIRLING_BENCHMARK_PASS')
print('ALL_CENTERED_BERNSTEIN_JITTER_CHECKS_PASS')
