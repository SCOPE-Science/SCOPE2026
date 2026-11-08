"""Reproducibility checks for the Poisson law of distinctive representation.
All source results are established analytically; these finite checks test definitions,
probability inequalities, and limiting-constant computations.
"""
from itertools import combinations, product
from math import comb, ceil, exp, factorial, pi, sqrt, lgamma, log
from fractions import Fraction


def dr_count(supports, n, k):
    q = (n+k-1)//k
    eligible = [i for i, s in enumerate(supports) if s.bit_count() == q]
    allv = (1 << n) - 1
    count = 0
    for W in combinations(eligible,k):
        represented = 0
        for i in W:
            represented |= supports[i]
        uncovered = allv ^ represented
        # JR iff no candidate enjoys q uncovered supporters.
        if all((s & uncovered).bit_count() < q for s in supports):
            count += 1
    return count, len(eligible)


def literal_jr(supports,n,k,W):
    """Independent reference implementation enumerating all cohesive voter groups."""
    q=(n+k-1)//k
    for voters in range(1,1<<n):
        if voters.bit_count()<q:
            continue
        if any((s & voters)==voters for s in supports):
            if all((supports[w] & voters)==0 for w in W):
                return False
    return True


def literal_dr_count(supports,n,k):
    q=(n+k-1)//k
    eligible=[i for i,s in enumerate(supports) if s.bit_count()==q]
    return sum(literal_jr(supports,n,k,W) for W in combinations(eligible,k))


def pair_obstruction(supports,n,k):
    q=(n+k-1)//k
    full=(1<<n)-1
    for i,a in enumerate(supports):
        if a.bit_count()!=q:
            continue
        for j,b in enumerate(supports):
            if i != j and (b & (full ^ a)).bit_count() >= q:
                return True
    return False


def exact_small(n,m,k):
    q=(n+k-1)//k
    buckets={}
    bad=0
    bad_discrepancy=0
    total= (1<<n)**m
    for supports in product(range(1<<n),repeat=m):
        real,z=dr_count(supports,n,k)
        if n<=4 and m<=3:
            assert real==literal_dr_count(supports,n,k)
        ideal=comb(z,k) if z>=k else 0
        obs=pair_obstruction(supports,n,k)
        if real!=ideal:
            bad_discrepancy+=1
            assert obs
        if obs: bad+=1
        assert real<=ideal
        buckets[real]=buckets.get(real,0)+1
    p=Fraction(1,2)
    b=Fraction(comb(n,q),2**n)
    tau=sum((Fraction(comb(n-q,j),2**(n-q)) for j in range(q,n-q+1)),Fraction(0))
    rhs=m*(m-1)*b*tau
    assert Fraction(bad_discrepancy,total) <= rhs
    assert Fraction(bad,total) <= rhs
    print('exhaustive',n,m,k,'profiles',total,'JR-discrepancy',bad_discrepancy,'pair-obstructions',bad,'union-bound',str(rhs),'DR-distribution',buckets)


def exact_biased_case():
    # Exact weighted enumeration, independent of the fair-bit cases above.
    n,m,k=4,3,2
    den=3**(n*m)
    mismatch_weight=0
    obs_weight=0
    for supports in product(range(1<<n),repeat=m):
        ones=sum(s.bit_count() for s in supports)
        weight=2**(n*m-ones)
        real,z=dr_count(supports,n,k)
        if real!=(comb(z,k) if z>=k else 0):
            mismatch_weight+=weight
        if pair_obstruction(supports,n,k):
            obs_weight+=weight
    p=Fraction(1,3)
    q=(n+k-1)//k
    b=Fraction(comb(n,q),1)*p**q*(1-p)**(n-q)
    tau=sum(Fraction(comb(n-q,j),1)*p**j*(1-p)**(n-q-j) for j in range(q,n-q+1))
    bound=m*(m-1)*b*tau
    assert Fraction(mismatch_weight,den)<=Fraction(obs_weight,den)<=bound
    print('biased',n,m,k,'p=1/3','weighted-discrepancy',str(Fraction(mismatch_weight,den)), 'weighted-obstruction',str(Fraction(obs_weight,den)),'upper-bound',str(bound))


def poisson_tail(mu,k):
    return 1-exp(-mu)*sum(mu**j/factorial(j) for j in range(k))


def critical_constants(k,c,beta):
    mu=c*k/sqrt(2*pi*(k-1))*exp(-(k*k*beta*beta)/(2*(k-1)))
    return mu,poisson_tail(mu,k)


def test_critical_windows():
    for k in (2,3,4):
        for beta in (-1.,0.,0.75):
            c=2.0
            mu,p=critical_constants(k,c,beta)
            print('Poisson',k,c,beta,'mean',format(mu,'.10f'),'existence',format(p,'.10f'))
        # Direct binomial local-mass ratio for n multiples of k.
        for n in (100*k,400*k,1600*k):
            q=n//k
            mass=exp(lgamma(n+1)-lgamma(q+1)-lgamma(n-q+1)+q*log(1/k)+(n-q)*log(1-1/k))
            asym=k/sqrt(2*pi*(k-1)*n)
            assert abs(mass/asym-1)<.03

if __name__=='__main__':
    for row in ((3,3,2),(4,3,2),(4,4,2),(5,3,2),(6,3,3)):
        exact_small(*row)
    exact_biased_case()
    test_critical_windows()
    print('ALL CHECKS PASSED')
