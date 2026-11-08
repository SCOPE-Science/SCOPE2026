"""Reproducibility checks for uniform-circle facility mechanism cost laws.
Requires standard-library Python 3 only. This checks exact combinatorial
identities and small-system numerical integrals, not the infinite limit proof.
"""
from fractions import Fraction
from math import comb, pi, cos, isclose
from random import Random


def exact_advantage(n):
    assert n >= 3 and n % 2 == 1
    k = (n-1)//2
    return Fraction(1,4)-Fraction(comb(n,k),2**(n+1))


def binomial_formula(n):
    k=(n-1)//2
    return sum((Fraction(comb(n,b),2**n) * Fraction((k-b)*(k-b+1),n-b+1) for b in range(k)),Fraction())


def abs_center_identity(s):
    m=2*s
    lhs=sum(Fraction(comb(m,j)*abs(j-s),2**m) for j in range(m+1))
    rhs=Fraction(s*comb(m,s),2**m)
    return lhs,rhs


def distance(x,y):
    u=abs(x-y)
    return min(u,1-u)


def costs(points):
    return [sum(distance(x,y) for y in points) for x in points]


def pcd_probs(points):
    n=len(points)
    assert n>=3
    g=[(points[(i+1)%n]-points[i])%1.0 for i in range(n)]
    if n%2:
        k=n//2
        p=[g[(i+k)%n] for i in range(n)]
    else:
        k=n//2
        p=[(g[(i+k-1)%n]+g[(i+k)%n])/2 for i in range(n)]
    assert abs(sum(p)-1)<1e-12 and min(p)>=0
    return p


def sample_costs(rng,n):
    xs=sorted(rng.random() for _ in range(n))
    sc=costs(xs)
    rd=sum(sc)/n
    p=pcd_probs(xs)
    alt=sum(a*b for a,b in zip(p,sc))
    return rd,alt,min(sc)


def numeric_cov(h,steps=200000):
    z=0.0
    for i in range(steps):
        x=(i+.5)/steps
        z+=(distance(x,0)-.25)*(distance(x,h)-.25)
    return z/steps


def theory_cov(h):
    h=min(h%1,(-h)%1)
    return 1/48-h*h/2+2*h*h*h/3


def main():
    count=0
    for n in range(3,102,2):
        a=exact_advantage(n)
        assert a==binomial_formula(n),n
        assert 0<a<Fraction(1,4)
        count+=1
    for s in range(1,51):
        lhs,rhs=abs_center_identity(s)
        assert lhs==rhs
        count+=1
    for h in [0,.05,.125,.2,.25,.375,.5,.65,.91]:
        a=numeric_cov(h,steps=20000)
        b=theory_cov(h)
        assert abs(a-b)<2e-8,(h,a,b)
        count+=1
    rng=Random(435016)
    for n in (3,4,5,6,7,8,9,10,11,12,19,20,31,32):
        reps=1800
        dr=0.0;dp=0.0
        for _ in range(reps):
            rd,pcd,opt=sample_costs(rng,n)
            assert 0<opt<=min(rd,pcd)+1e-10
            dr+=rd;dp+=pcd
        dr/=reps;dp/=reps
        target_rd=(n-1)/4
        target_adv=float(exact_advantage(n if n%2 else n-1))
        assert abs(dr-target_rd)<.07,(n,dr,target_rd)
        assert abs((dr-dp)-target_adv)<.07,(n,dr-dp,target_adv)
        print(f'n={n:3d} observed advantage={dr-dp:.5f} exact={target_adv:.5f}')
        count+=reps
    print('PASS',count,'exact identities, covariance evaluations and seeded finite-sample profile tests')

if __name__=='__main__':main()
