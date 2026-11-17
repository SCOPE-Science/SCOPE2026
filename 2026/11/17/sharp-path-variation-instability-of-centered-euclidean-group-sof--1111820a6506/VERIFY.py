"""Reproducible finite checks for the centered Euclidean shrinkage result.

Only Python's standard library is required. These finite checks are not
substitutes for the dimension-uniform proof in RESULT.md.
"""
from itertools import product
from math import sqrt, floor
from random import Random


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def length(a):
    return sqrt(dot(a,a))


def variation(a):
    return sum(abs(a[i+1]-a[i]) for i in range(len(a)-1))


def shrink(x, lam):
    m=sum(x)/len(x)
    z=[v-m for v in x]
    r=length(z)
    f=max(0.,1-lam/r) if r else 0.
    return [m+f*v for v in z]


def formula(n):
    return (1.+sqrt((4*n-6)*floor(n*n/4)/n))/2


def grad_transpose(e):
    return [-e[0]]+[e[i-1]-e[i] for i in range(1,len(e))]+[e[-1]]


def witness(n):
    j=n//2
    e=[1 if i%2==0 else -1 for i in range(n-1)]
    if e[j-1]<0: e=[-v for v in e]
    a=grad_transpose(e)
    h=[0.]*j+[1.]*(n-j)
    b=[v-sum(h)/n for v in h]
    assert abs(dot(a,b)-1.)<1e-10
    aa=length(a); bb=length(b)
    u=[v/aa+w/bb for v,w in zip(a,b)]
    uu=length(u)
    u=[v/uu for v in u]
    return u,h


def run():
    checked=0
    for n in range(2,11):
        biggest=0.0
        for e in product((-1.,1.),repeat=n-1):
            a=grad_transpose(e)
            assert abs(length(a)**2 - (2+sum((e[i-1]-e[i])**2 for i in range(1,n-1))))<1e-8
            for j in range(1,n):
                h=[0.]*j+[1.]*(n-j)
                b=[v-(n-j)/n for v in h]
                assert abs(dot(a,b)-e[j-1])<1e-9
                candidate=(length(a)*length(b)+abs(dot(a,b)))/2
                biggest=max(biggest,candidate)
                checked+=1
        assert abs(biggest-formula(n))<1e-9,(n,biggest,formula(n))
    print('EXACT_SIGN_CHAMBER_FORMULA_DEPTHS_2_TO_10_PASS',checked)

    for n in range(2,101):
        u,h=witness(n)
        lhs=variation(u)*abs(dot(u,h))
        assert abs(lhs-formula(n))<2e-11,(n,lhs,formula(n))
    print('EXPLICIT_BOUNDARY_WITNESSES_DEPTHS_2_TO_100_PASS')

    rng=Random(20261112)
    trials=0
    for n in range(2,31):
        c=formula(n)
        for k in range(260):
            lam=rng.choice((0.,0.1,0.5,1.,3.))
            x=[rng.gauss(0,rng.choice((.03,1.,6.))) for _ in range(n)]
            y=[rng.gauss(0,rng.choice((.03,1.,6.))) for _ in range(n)]
            dx=variation([s-t for s,t in zip(x,y)])
            if dx>1e-12:
                dy=variation([s-t for s,t in zip(shrink(x,lam),shrink(y,lam))])
                assert dy<=((1 if lam==0 else c)+1e-9)*dx,(n,lam,dy/dx,c)
                trials+=1
    print('RANDOM_TWO_INPUT_BV_BOUND_CHECKS_PASS',trials)

    for n in range(2,101):
        u,h=witness(n)
        for lam in (0.25,1.,3.):
            # One-sided difference quotients at the shrinkage boundary.
            for delta in (1.e-4,1.e-6):
                x=[lam*v for v in u]
                y=[s+delta*t for s,t in zip(x,h)]
                gain=variation([s-t for s,t in zip(shrink(y,lam),shrink(x,lam))])/(delta*variation(h))
                assert abs(gain-formula(n))<max(.002,5*delta*n*n),(n,lam,delta,gain,formula(n))
    print('BOUNDARY_APPROACH_ALL_DIMENSIONS_2_TO_100_PASS')
    print('ALL_CENTERED_GROUP_SHRINK_CHECKS_PASS')

if __name__=='__main__':
    run()
