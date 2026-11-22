"""Independent standard-library finite checks for the mean-preserving group shrinker BV formula.

Checks finite-dimensional identities and sample perturbations. The all-n statement is
established by the analytical argument in RESULT.md, not by these computations.
"""
import itertools
import math
import random
from fractions import Fraction


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def variation(a):
    return sum(abs(b-a0) for a0, b in zip(a, a[1:]))


def center(a):
    m = sum(a)/len(a)
    return [x-m for x in a]


def shrink(a, lam):
    m = sum(a)/len(a)
    c = [x-m for x in a]
    r = norm(c)
    k = max(0., 1-lam/r) if r else 0.
    return [m+k*v for v in c]


def formula(n):
    return (1+math.sqrt((4*n-6)*(n*n//4)/n))/2


def test_one(n):
    # Exhaustive exact signs and cut positions, n<=9.
    worst = 0.
    max_a2 = 0
    for ss in itertools.product([-1,1], repeat=n-1):
        a = [-ss[0]]+[ss[i-1]-ss[i] for i in range(1,n-1)]+[ss[-1]]
        a2 = sum(z*z for z in a)
        max_a2 = max(max_a2, a2)
        for j in range(1,n):
            b = [Fraction(n-j,n) if i<j else Fraction(-j,n) for i in range(n)]
            inner = abs(sum(ai*bi for ai,bi in zip(a,b)))
            assert inner==1
            b2 = Fraction(j*(n-j),n)
            candidate=(math.sqrt(a2*float(b2))+float(inner))/2
            worst=max(worst,candidate)
    assert max_a2==4*n-6
    assert math.isclose(worst,formula(n),abs_tol=1e-12)
    # Construct a norming u and a unit-variation centered step h.
    j=n//2
    ss=[-1 if (i-j+1)%2==0 else 1 for i in range(n-1)]
    # Force sigma_(j-1)=-1, hence (D^T sigma) dot centered-left-step =1.
    ss=[-1 if (i-(j-1))%2==0 else 1 for i in range(n-1)]
    a=[-ss[0]]+[ss[i-1]-ss[i] for i in range(1,n-1)]+[ss[-1]]
    b=[(n-j)/n if i<j else -j/n for i in range(n)]
    assert abs(dot(a,b)-1)<1e-13
    u0=[z/norm(a)+v/norm(b) for z,v in zip(a,b)]
    u=[z/norm(u0) for z in u0]
    rankone=variation(u)*abs(dot(u,b))
    assert math.isclose(rankone, formula(n),rel_tol=5e-13,abs_tol=2e-12)
    # Difference quotient at exterior radius just above threshold.
    lam=1.
    delta=0.0002
    eps=1e-8
    x=[(1+delta)*lam*t for t in u]
    y=[v+eps*e for v,e in zip(x,b)]
    q=variation([p-q for p,q in zip(shrink(y,lam),shrink(x,lam))])/eps
    assert abs(q-formula(n)) < 0.004, (n,q,formula(n))
    return worst,q


def test_random():
    rng=random.Random(143415)
    total=0
    for n in range(2,19):
        lim=formula(n)
        for _ in range(150):
            x=[rng.uniform(-4,4) for _ in range(n)]
            y=[rng.uniform(-4,4) for _ in range(n)]
            lam=10**rng.uniform(-2,2)
            d=variation([p-q for p,q in zip(x,y)])
            if d>1e-12:
                out=variation([p-q for p,q in zip(shrink(x,lam),shrink(y,lam))])
                assert out<=lim*d+1e-10
            assert variation(shrink(x,lam))<=variation(x)+1e-10
            total+=1
    return total


def run():
    for n in range(2,10):
        k,w=test_one(n)
        print(f'EXACT_SIGN_CUT_ENUMERATION_AND_NEAR_THRESHOLD_WITNESS_PASS n={n} K={k:.12f} measured={w:.12f}')
    cnt=test_random()
    assert abs(formula(2)-1)<1e-12
    assert abs(formula(3)-1.5)<1e-12
    assert abs(formula(4)-(1+math.sqrt(10))/2)<1e-12
    print(f'FINITE_TWO_INPUT_AND_ONE_INPUT_STRESS_PASS cases={cnt}')
    print('ALL_CENTERED_GROUP_SHRINKAGE_BV_CHECKS_PASS')


if __name__=='__main__':
    run()
