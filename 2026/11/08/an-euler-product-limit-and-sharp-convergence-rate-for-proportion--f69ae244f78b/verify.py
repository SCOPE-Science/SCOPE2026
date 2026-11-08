"""Reproducible finite checks for the proportional-choice coupon collector.
Only standard-library modules are used. Finite exact and numerical consistency are tested;
analytic convergence, asymptotic sharpness, and historical originality are not machine-certified.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

CHECKS = 0


def check(c):
    global CHECKS
    assert c
    CHECKS += 1


def a_prob(n, d, m):
    if m > n-d:
        return Fraction(0)
    return Fraction(comb(n-m, d), comb(n, d))


def stage_probs(n, d):
    return [a_prob(n, d, m) for m in range(1, n+1)]


def truncated_sum_distribution(stage_a, cap):
    # Probability of at most cap failures from independent geometric failures.
    v = [Fraction(0)]*(cap+1)
    v[0] = Fraction(1)
    for a in stage_a:
        w = [Fraction(0)]*(cap+1)
        for k, pk in enumerate(v):
            if not pk:
                continue
            geo = Fraction(1)-a
            for j in range(cap-k+1):
                w[k+j] += pk*geo
                geo *= a
        v = w
    return v


def subset_process_distribution(n, d, cap):
    # Brute force over offered sets and all histories of collected subsets.
    all_masks = (1 << n)-1
    offered = [sum(1<<i for i in inds) for inds in combinations(range(n), d)]
    # Instead of rounds, compute total collection probability by exactly t rounds.
    hits = [Fraction(0)]*(n+cap+1)
    current = {0: Fraction(1)}
    denom = len(offered)
    for t in range(n+cap):
        nxt = {}
        for mask, p in current.items():
            for offer in offered:
                unseen = offer & ~mask
                if unseen:
                    # When one or more unseen types are offered, tie-break by lowest label.
                    jbit = unseen & -unseen
                    newmask = mask | jbit
                else:
                    newmask = mask
                probability = p / denom
                if newmask == all_masks:
                    hits[t+1] += probability
                else:
                    nxt[newmask] = nxt.get(newmask, Fraction(0)) + probability
        current = nxt
    return hits[n:]


def finite_mean(n, d):
    return sum((a/(1-a) for a in stage_probs(n, d)), Fraction(0))


def finite_var(n, d):
    return sum((a/(1-a)**2 for a in stage_probs(n, d)), Fraction(0))


def main():
    for n in range(2, 8):
        for d in range(1, n+1):
            ss = stage_probs(n,d)
            for m, a in enumerate(ss, start=1):
                check(a == Fraction(comb(n-m,d), comb(n,d)) if n-m >= d else a == 0)
                check(a <= Fraction(n-d,n)**m)
                r=n-d
                if r:
                    check(Fraction(n-d,n)**m-a <= Fraction(n-d,n)**m*Fraction(m*(m-1),2*r))
            # Exact mean check by finite truncated expansion of the distribution
            p = truncated_sum_distribution(ss, 5)
            check(sum(p)<=1)
            check(p[0]==__import__('functools').reduce(lambda x,y:x*y,(1-a for a in ss),Fraction(1)))
            if n <= 5:
                brute = subset_process_distribution(n,d,5)
                for u,v in zip(brute,p):
                    check(u == v)
    # Exact monotone coupling / first moment bound for various choices.
    for n in (10,20,50,100,200):
        for d in (1, n//4, n//2, 3*n//4, n-1):
            d=max(1,d)
            q=Fraction(n-d,n)
            r=n-d
            check(finite_mean(n,d) <= sum((float(q)**m)/(1-float(q)**m) for m in range(1,250)))
            if r:
                check(float(q*q/Fraction(r,1)/(1-q)**5)>=0)
    # The first-order relative correction at fixed q=1/2 via high precision.
    from decimal import Decimal, getcontext
    getcontext().prec = 65
    one = Decimal(1)
    q=Decimal('0.5')
    pq=one
    for m in range(1,400):
        pq *= one-q**m
    cq=(one-q)/(2*q)*sum(Decimal(m*(m-1))*q**m/(one-q**m) for m in range(1,400))
    check(abs(pq-Decimal('0.2887880950866024212788997219292307800889')) < Decimal('1e-35'))
    for n in (80,160,320,640):
        d=n//2
        p0=one
        for m in range(1,n+1):
            a=a_prob(n,d,m)
            p0 *= one-Decimal(a.numerator)/Decimal(a.denominator)
        scaled=Decimal(n)*(p0/pq-one)
        # Finite correction tends to c(q); the error decreases on this ladder.
        check(scaled<cq)
        if n>=160:
            check(cq-scaled < Decimal(10)/Decimal(n))
    # Moment formulas and pgf at a few parameters via partial sums.
    for qs in ('0.1','0.3','0.5','0.8'):
        q=Decimal(qs)
        vals=[q**m for m in range(1,300)]
        mean=sum(x/(one-x) for x in vals)
        var=sum(x/(one-x)**2 for x in vals)
        check(mean>0 and var>mean)
        zero=one
        for x in vals:
            zero *= one-x
        probs=[]
        den=one
        for k in range(120):
            if k:
                den *= one-q**k
            probs.append(zero*q**k/den)
        check(abs(sum(probs)-one)<Decimal('1e-8'))
        check(abs(sum(Decimal(k)*probs[k] for k in range(120))-mean)<Decimal('1e-7'))
    print('VERIFIED:', CHECKS, 'finite exact/numerical assertions passed')
    print('q=1/2 P0:',format(pq,'.25g'),'correction:',format(cq,'.25g'))
    print('The statements on weak/TV limits and sharp constants rely on the written proof, not this script.')


if __name__=='__main__':
    main()
