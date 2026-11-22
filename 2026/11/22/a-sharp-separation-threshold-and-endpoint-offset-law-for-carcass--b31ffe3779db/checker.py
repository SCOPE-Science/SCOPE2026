"""Numerical diagnostics for the exponential-persistence carcass-calendar theorem.

Python 3 standard library only. The mathematical proof is in RESULT.md;
the finite diagnostics here do not establish global optimality.
"""
from fractions import Fraction
from math import exp, log
from random import Random

checks = 0

def near(a, b, atol=2e-10, rtol=2e-10):
    global checks
    checks += 1
    assert abs(a - b) <= atol + rtol * max(abs(a), abs(b)), (a, b)


def objective(gaps, p):
    """Mean discoveries in units of arrival intensity / removal hazard."""
    present = 0.0
    total = 0.0
    for d in gaps:
        q = exp(-d)
        present = (1-q)+(1-p)*q*present
        total += present
    return p*total


def direct_objective(gaps, p):
    """Independently sum arrival cohorts and later opportunities."""
    n = len(gaps)
    ans = 0.0
    for i in range(n):
        future = 1.0
        surv = 1.0
        for j in range(i, n):
            if j > i:
                surv *= (1-p)*exp(-gaps[j])
            future += 0 if j == i else surv
        ans += p*(1-exp(-gaps[i]))*future
    return ans


def threshold(n, p):
    return (n-2)*log(2-p)-log(p)


def optimizer(n, p, horizon):
    """Return optimal gaps when the separation threshold is met."""
    assert n >= 2 and 0 < p < 1 and horizon >= threshold(n,p)-1e-12
    upper=1/(2-p)
    lower=1e-14
    def eq(q):
        return -n*log(q)+2*log(1-(1-p)*q)-log(p)-horizon
    assert eq(lower)>0 and eq(upper)<=1e-10
    for _ in range(150):
        mid=(lower+upper)/2
        if eq(mid)>0:
            lower=mid
        else:
            upper=mid
    q=(lower+upper)/2
    A=1-(1-p)*q
    gaps=[-log(p*q/A)]+[-log(q)]*(n-2)+[-log(q/A)]
    return gaps, q


def grad_component(gaps,p,i):
    e=3e-6
    fwd=list(gaps);fwd[i]+=e
    back=list(gaps);back[i]-=e
    return (objective(fwd,p)-objective(back,p))/(2*e)

rng=Random(74567)
for n in range(2, 10):
    for p in (.05,.12,.35,.5,.73,.91,.98):
        critical=threshold(n,p)
        for extra in (0.001,0.15,1.0,3.0,8.0):
            H=critical+extra
            d,q=optimizer(n,p,H)
            near(sum(d),H)
            assert min(d)>0
            near(d[0]-d[-1],-log(p))
            for interior in d[1:-2]:
                near(interior,d[1])
            near(objective(d,p),direct_objective(d,p))
            slopes=[grad_component(d,p,i) for i in range(n)]
            for slope in slopes:
                near(slope,slopes[0],atol=5e-8,rtol=4e-8)
            # All finite perturbations are merely diagnostics, not proof.
            for _ in range(14):
                raw=[rng.random()+.01 for _ in range(n)]
                alt=[H*v/sum(raw) for v in raw]
                checks+=1
                assert objective(d,p)>=objective(alt,p)-2e-9
                near(objective(alt,p),direct_objective(alt,p))
                t=rng.random()
                mix=[t*x+(1-t)*y for x,y in zip(d,alt)]
                checks+=1
                assert objective(mix,p)+1e-10 >= t*objective(d,p)+(1-t)*objective(alt,p)
        edge,_=optimizer(n,p,critical)
        near(edge[-1],0,atol=1e-10)
        near(sum(edge),critical)

# Rational checks of the recursion against independent cohort enumeration.
for n in range(2,11):
    for pp in (Fraction(1,2),Fraction(1,3),Fraction(3,5)):
        qs=[Fraction(1,k+2) for k in range(n)]
        r=Fraction(0); total=Fraction(0)
        for q in qs:
            r=1-q+(1-pp)*q*r
            total+=pp*r
        direct=Fraction(0)
        for i in range(n):
            contribution=Fraction(0)
            surv=Fraction(1)
            for j in range(i,n):
                if j>i:
                    surv*=(1-pp)*qs[j]
                contribution+=surv
            direct+=pp*(1-qs[i])*contribution
        checks+=1
        assert total==direct

example,_=optimizer(4,.5,3)
for a,b in zip(example,[1.12988253,.71669106,.71669106,.43673535]):
    near(a,b,atol=1e-7)
near(objective(example,.5),1.3016700899669418)
near(objective([.75]*4,.5),1.2751026826211755)
print(f"PASS: {checks} diagnostics; finite checks supplement the analytical proof")
