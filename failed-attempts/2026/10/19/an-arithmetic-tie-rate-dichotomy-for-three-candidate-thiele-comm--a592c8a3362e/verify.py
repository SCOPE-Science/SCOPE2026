"""Reproducible finite checks for two-seat Thiele tie arithmetic.
Run: python verify.py
No external packages required. Each ballot is one of the eight equally likely subsets
of three candidates. Weighted anonymous-profile enumeration is exact.
"""
from math import factorial, comb, gcd, sqrt, pi
from fractions import Fraction

COMMITTEES = (3, 5, 6)  # {A,B}, {A,C}, {B,C}; candidate bits 1,2,4.
BALLOTS = tuple(range(8))


def sign_int(x):
    return (x > 0) - (x < 0)


def sign_sqrt2(x, y):
    """Exact sign of x + y*sqrt(2) for integer x,y."""
    if y == 0:
        return sign_int(x)
    if x == 0:
        return sign_int(y)
    if x*y > 0:
        return sign_int(x)
    diff = x*x - 2*y*y
    assert diff != 0  # sqrt(2) is irrational.
    return sign_int(diff) if x > 0 else -sign_int(diff)


def compare_pairs(first, second, mode):
    base, both = first[0]-second[0], first[1]-second[1]
    if mode == 'irrational':
        return sign_sqrt2(base-both, both)  # alpha=sqrt(2)-1
    p, q = mode
    return sign_int(q*base + p*both)


def profile_scores(counts):
    ans=[]
    for committee in COMMITTEES:
        any_app=both_app=0
        for ballot, freq in enumerate(counts):
            approved=(ballot & committee).bit_count()
            if approved:
                any_app+=freq
            if approved == 2:
                both_app+=freq
        ans.append((any_app,both_app))
    return ans


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for j in range(total+1):
            for t in compositions(total-j,length-1):
                yield (j,)+t


def exact_census(n, modes):
    f=[factorial(k) for k in range(n+1)]
    counts={mode:0 for mode in modes}
    pair_irr=0
    triple_irr=0
    for h in compositions(n,8):
        m=f[n]
        den=1
        for x in h:
            den*=f[x]
        m=f[n]//den
        scores=profile_scores(h)
        if scores[0] == scores[1]:
            pair_irr += m
            if scores[1] == scores[2]:
                triple_irr += m
        for mode in modes:
            best=0
            winners=1
            for t in range(1,3):
                c=compare_pairs(scores[t],scores[best],mode)
                if c>0:
                    best=t
                    winners=1
                elif c==0:
                    winners+=1
            if winners>=2:
                counts[mode]+=m
    total=8**n
    return {mode:Fraction(k,total) for mode,k in counts.items()},Fraction(pair_irr,total),Fraction(triple_irr,total)


def exact_pair_irr(n):
    # Condition on the number whose A-coordinate is absent; B,C independent.
    return Fraction(sum(comb(n,k)*comb(2*k,k)*comb(2*(n-k),n-k)
                        for k in range(n+1)), 8**n)


def covariance_checks():
    # 4-dimensional comparison increment for the two score differences
    xs=[]
    for ballot in BALLOTS:
        a,b,c=((ballot >> i)&1 for i in range(3))
        xs.append(((1-a)*(b-c),a*(b-c), (1-b)*(a-c), b*(a-c)))
    assert sum(x[0] for x in xs)==sum(x[1] for x in xs)==0
    assert sum(x[2] for x in xs)==sum(x[3] for x in xs)==0
    cov=[[Fraction(sum(x[i]*x[j] for x in xs),8) for j in range(4)]
         for i in range(4)]
    assert cov == [
        [Fraction(1,4),Fraction(0),Fraction(1,8),Fraction(0)],
        [Fraction(0),Fraction(1,4),Fraction(0),Fraction(1,8)],
        [Fraction(1,8),Fraction(0),Fraction(1,4),Fraction(0)],
        [Fraction(0),Fraction(1,8),Fraction(0),Fraction(1,4)],
    ]
    print('Exact 4-dimensional increment covariance:', cov)


def main():
    covariance_checks()
    modes=((0,1),(1,1),(1,2),(2,3),'irrational')
    for n in (1,2,3,4,5,6,8,10,12):
        probs,pair,triple=exact_census(n,modes)
        assert pair == exact_pair_irr(n)
        assert triple <= pair
        for mode,pr in probs.items():
            assert 0<=pr<=1
        # For reduced fraction with denominator q>n, equality conditions coincide.
        # Exact pair counts below demonstrate this separately via all pairs of scores.
        print('n=',n,' pair_irr=',str(pair),' triple_irr=',str(triple),
              ' tie_CC=',str(probs[(0,1)]),
              ' tie_PAV=',str(probs[(1,2)]),
              ' tie_irr=',str(probs['irrational']),
              ' scaled_irr=',round(n*float(probs['irrational']),6))
    # Check the rational comparison kernel for all possible integer differences.
    for n in range(1,20):
        for q in (n+1,n+3,2*n+1):
            for p in range(1,q):
                if gcd(p,q)!=1:
                    continue
                for u in range(-n,n+1):
                    for v in range(-n,n+1):
                        if q*u+p*v==0:
                            assert (u,v)==(0,0)
    print('All exact-arithmetic checks passed.')
    print('Asymptotic constants: CC=',1.5*sqrt(2/pi),
          'PAV=',1.5*sqrt(2/(5*pi)),
          'AV=',1.5/sqrt(pi),'irrational=',3/pi)

if __name__=='__main__':
    main()
