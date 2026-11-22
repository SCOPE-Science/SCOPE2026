"""Reproducible finite checks of the random-interval extremal geometry.
These checks do not establish the asymptotic theorem or publication priority.
"""
import itertools
import math
import random
from collections import Counter


def pairings(xs):
    if not xs:
        yield ()
        return
    a = xs[0]
    for j in range(1, len(xs)):
        b = xs[j]
        for rest in pairings(xs[1:j] + xs[j+1:]):
            yield ((a, b),) + rest


def degrees(pairs):
    n = len(pairs)
    return [sum(1 for j in range(n) if j != i and max(pairs[i][0], pairs[j][0]) < min(pairs[i][1], pairs[j][1])) for i in range(n)]


def exact_nondegenerate(n):
    counts = Counter()
    for pairs in pairings(tuple(range(2*n))):
        d = degrees(pairs)
        counts[d.count(n-1)] += 1
        # Degree can also be read from the two disjoint endpoint tails.
        for i, (a,b) in enumerate(pairs):
            left = sum(1 for j,(_,r) in enumerate(pairs) if j!=i and r<a)
            right = sum(1 for j,(l,_) in enumerate(pairs) if j!=i and l>b)
            assert d[i] == n-1-left-right
    den = sum(counts.values())
    assert den == math.prod(range(1,2*n,2))
    if n >= 2:
        # Known universal-existence probability (external baseline).
        assert counts[0]*3 == den
    return counts,den


def rayleigh_small_count_mean(t):
    return t*t/2


def tri_area_side(a):
    return a*a


def p(a,b):
    return 1-a*a-(1-b)**2


def main():
    checked=0
    for n in range(2,7):
        c,den=exact_nondegenerate(n)
        assert c.get(n-1,0)==0
        assert c[n]*math.comb(2*n,n)==den*2**n
        checked+=den
    for a in (0.01,.1,.25,.49,.51,.8,.99):
        for b in (a,(1+a)/2,1):
            assert p(a,b)+1e-12>=min(b,1-a)
            checked+=1
    for t in (.25,.5,1,2,3):
        # Side PPP mean is t^2/4; both sides together t^2/2.
        assert math.isclose(2*tri_area_side(t/2),rayleigh_small_count_mean(t))
        checked+=1
    # Independent midpoint-Simpson evaluation of the angular integral
    # controlling the limiting low-degree / universal covariance.
    m=4096
    h=(math.pi/2)/m
    g=lambda th: math.cos(th)**2*math.sin(th)**2*min(math.cos(th),math.sin(th))
    angular=h/3*(g(0)+g(math.pi/2)+4*sum(g(h*j) for j in range(1,m,2))+2*sum(g(h*j) for j in range(2,m,2)))
    angular_exact=4/15-7/(30*math.sqrt(2))
    assert abs(angular-angular_exact)<2e-7
    cov=math.sqrt(math.pi)*(4-(7+math.pi)/(2*math.sqrt(2)))
    assert cov>.7 and cov<.8
    checked+=2
    rng=random.Random(321654)
    n=800
    reps=400
    val=[]
    for _ in range(reps):
        xy=[sorted((rng.random(),rng.random())) for _ in range(n)]
        ss=sorted(a for a,b in xy)
        rr=sorted(b for a,b in xy)
        import bisect
        deg=[]
        for a,b in xy:
            deg.append(n-1-bisect.bisect_left(rr,a)-(n-bisect.bisect_right(ss,b)))
        val.append(min(deg)/math.sqrt(n))
    # Loose seeded numerical check, deliberately not a proof.
    assert abs(sum(val)/reps-math.sqrt(math.pi/2))<.22
    print('PASS: exact pairings and endpoint identity, localization inequality, intensity, seeded sanity; checks >=',checked)

if __name__ == '__main__':
    main()
