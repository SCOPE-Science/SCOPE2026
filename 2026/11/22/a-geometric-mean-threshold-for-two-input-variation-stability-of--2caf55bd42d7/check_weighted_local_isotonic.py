"""Standalone exact-rational checks for weighted local isotonic variation law.
All tests are finite; the universal theorem rests on the accompanying proof.
"""
from fractions import Fraction as F
from random import Random


def midpoint_iso(u, weights):
    a,b,c=weights
    x,y,z=u
    if x<=y<=z:
        return y
    if x>y and (a*x+b*y)/(a+b)<=z:
        return (a*x+b*y)/(a+b)
    if y>z and x<=(b*y+c*z)/(b+c):
        return (b*y+c*z)/(b+c)
    return (a*x+b*y+c*z)/(a+b+c)


def T(u,weights):
    n=len(u)
    return [midpoint_iso((u[(i-1)%n],u[i],u[(i+1)%n]),weights) for i in range(n)]


def var(u):
    return sum((abs(u[(i+1)%len(u)]-u[i]) for i in range(len(u))),F(0))


def bound(weights):
    a,b,c=weights
    return max(F(1),2*(a/(a+b)+c/(b+c))-1)


def exact_random_checks():
    rng=Random(410028)
    cases=0
    for n in (8,9,11,14):
        for _ in range(1250):
            weights=tuple(F(rng.randint(1,12),rng.randint(1,7)) for j in range(3))
            x=[F(rng.randint(-8,8),rng.randint(1,4)) for j in range(n)]
            y=[F(rng.randint(-8,8),rng.randint(1,4)) for j in range(n)]
            dif=[y[j]-x[j] for j in range(n)]
            outx=T(x,weights);outy=T(y,weights)
            lhs=var([outy[j]-outx[j] for j in range(n)])
            rhs=bound(weights)*var(dif)
            assert lhs<=rhs,(n,weights,x,y,lhs,rhs)
            cases+=1
    print('EXACT_TWO_INPUT_VARIATION_INEQUALITIES_PASS', cases)


def exact_sharpness_checks():
    wlists=[(F(2),F(1),F(2)),(F(1),F(2),F(1)),(F(3),F(1),F(1)),
            (F(1),F(1),F(3)),(F(1,10),F(1),F(50)),(F(2),F(1),F(3))]
    cases=0
    for n in (8,9,10,13,20):
        for weights in wlists:
            x=[F(i%2) if i<8 else F(0) for i in range(n)]
            z=[F(1) if 2<=i<=5 else F(0) for i in range(n)]
            eps=F(1,10000)
            y=[x[i]+eps*z[i] for i in range(n)]
            lhs=var([a-b for a,b in zip(T(y,weights),T(x,weights))])
            rhs=bound(weights)*eps*var(z)
            assert lhs==rhs,(n,weights,lhs,rhs)
            cases+=1
    print('EXACT_FINITE_PAIR_SHARPNESS_PASS',cases)


def exact_local_branch_checks():
    weights=(F(4),F(2),F(3))
    assert midpoint_iso((F(0),F(1),F(2)),weights)==1
    assert midpoint_iso((F(3),F(0),F(4)),weights)==2
    assert midpoint_iso((F(0),F(3),F(0)),weights)==F(6,5)
    assert midpoint_iso((F(3),F(2),F(0)),weights)==F(16,9)
    print('EXACT_PAV_BRANCH_CHECKS_PASS',4)

if __name__=='__main__':
    exact_local_branch_checks()
    exact_random_checks()
    exact_sharpness_checks()
    print('ALL_WEIGHTED_LOCAL_ISOTONIC_CHECKS_PASS')
