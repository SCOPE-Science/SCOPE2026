#!/usr/bin/env python3
"""Reproduce exact algebra and finite-sample diagnostics for sparse histogram evidence.

Standard-library only. The probability-limit statements are proved mathematically
in RESULT.md; random simulations here check implementations rather than proving limits.
"""
import itertools
import math
import random
from collections import Counter
from fractions import Fraction

CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def factor(n):
    return math.factorial(n)


def exact_evidence(labels, k):
    n = len(labels)
    counts = Counter(labels)
    numerator = k**n * factor(k-1)
    for amount in counts.values():
        numerator *= factor(amount)
    return Fraction(numerator, factor(k+n-1))


def online_evidence(labels, k):
    counts = Counter()
    e = Fraction(1)
    for i, label in enumerate(labels):
        e *= Fraction(k*(1+counts[label]), k+i)
        counts[label] += 1
    return e


def collision_count(labels):
    return sum(b*(b-1)//2 for b in Counter(labels).values())


def triple_count(labels):
    return sum(b*(b-1)*(b-2)//6 for b in Counter(labels).values())


def log_evidence(labels, k):
    n = len(labels)
    return sum(math.lgamma(v+1) for v in Counter(labels).values()) - sum(math.log1p(i/k) for i in range(n))


def small_enumerations():
    for k in (2,3,4):
        for n in range(1,6):
            sum_e = Fraction(0)
            for labels in itertools.product(range(k),repeat=n):
                x = exact_evidence(labels,k)
                y = online_evidence(labels,k)
                require(x==y, 'posterior predictive identity')
                sum_e+=x
            require(sum_e==k**n, 'unit expectation under uniform iid null')
    p = (Fraction(1,2),Fraction(1,3),Fraction(1,6))
    s2 = sum(q*q for q in p)
    s3 = sum(q*q*q for q in p)
    for n in (3,4,5):
        e = Fraction(0)
        e2 = Fraction(0)
        for seq in itertools.product(range(3),repeat=n):
            weight = math.prod(p[t] for t in seq)
            c=collision_count(seq)
            e+=weight*c
            e2+=weight*c*c
        lam = math.comb(n,2)
        pred_mean = lam*s2
        pred_var = lam*(s2-s2*s2)+6*math.comb(n,3)*(s3-s2*s2)
        require(e==pred_mean, 'exact nonuniform collision mean')
        require(e2-e*e==pred_var, 'exact nonuniform collision variance')
    for b in range(3,100):
        bound= (3+3*math.log(2))*math.comb(b,3)
        error=abs(math.lgamma(b+1)-math.comb(b,2)*math.log(2))
        require(error<=bound, 'triple occupancy residual bound')


def cos_bin_probs(d,a):
    h=math.sin(math.pi/d)/math.pi
    return [1/(d*d)+a*h*h*math.cos(2*math.pi*(i-j)/d)
            for i in range(d) for j in range(d)]


def cosine_exact():
    a=0.94
    threshold = math.sqrt(2*(1/math.log(2)-1))
    require(0.94<threshold<0.95,'analytic family threshold')
    for d in range(3,31):
        p=cos_bin_probs(d,a)
        require(abs(sum(p)-1)<1e-12,'copula cells sum to one')
        require(min(p)>0,'copula cells positive')
        Jd=d*d*sum(v*v for v in p)
        formula=1+.5*a*a*(d*math.sin(math.pi/d)/math.pi)**4
        require(abs(Jd-formula)<1e-12,'exact grid squared-mass integral')
    require(abs((1+.5*threshold**2)*math.log(2)-1)<1e-14, 'detection threshold equation')


def draw_copula(rng,a):
    u=rng.random()
    while True:
        v=rng.random()
        if rng.random()*(1+a) <=1+a*math.cos(2*math.pi*(u-v)):
            return u,v


def critical_simulation():
    rng=random.Random(329011)
    n=450
    d=450
    k=d*d
    tau=n*(n-1)/(2*k)
    for a in (0.0,0.8,0.98):
        repeats=1150
        cs=[]
        triple=0
        abs_approx=[]
        for _ in range(repeats):
            bins=[]
            if not a:
                bins=[rng.randrange(k) for _ in range(n)]
            else:
                for j in range(n):
                    u,v=draw_copula(rng,a)
                    bins.append(min(int(d*u),d-1)*d+min(int(d*v),d-1))
            c=collision_count(bins)
            cs.append(c)
            triple+=triple_count(bins)
            abs_approx.append(abs(log_evidence(bins,k)-(c*math.log(2)-tau)))
        J=1+a*a/2
        actual=sum(cs)/repeats
        target=tau*J
        tolerance=5*math.sqrt((target+0.1)/repeats)+0.035
        require(abs(actual-target)<tolerance, 'Poisson collision intensity numerical check')
        require(sum(abs_approx)/repeats<0.03, 'Poisson-log-evidence approximation')
        require(triple<=16, 'critical triple collisions rare')
        print('critical a=%.2f: mean collisions %.5f vs %.5f, triples %d, mean error %.5f' % (
            a,actual,target,triple,sum(abs_approx)/repeats))


def test_phase_signs():
    for a in (0.1,0.6,0.8,0.94,0.95,0.99):
        J=1+a*a/2
        sign=J*math.log(2)-1
        require((sign>0)==(a>math.sqrt(2*(1/math.log(2)-1))), 'exact phase sign')
    for n,d in ((100,400),(200,700),(300,1000)):
        k=d*d
        lam=n*(n-1)/(2*k)
        rng=random.Random(n+d)
        vals=[log_evidence([rng.randrange(k) for _ in range(n)],k) for _ in range(300)]
        require(abs(sum(vals)/len(vals)-(math.log(2)-1)*lam)<0.085,
                'expected null log evidence sparse approximation')

if __name__=='__main__':
    small_enumerations()
    cosine_exact()
    critical_simulation()
    test_phase_signs()
    print('PASS %d assertions' % CHECKS)
