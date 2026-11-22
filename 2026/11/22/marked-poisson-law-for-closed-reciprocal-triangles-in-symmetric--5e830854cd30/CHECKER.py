"""Standalone finite checks for reciprocal top-two triangle sink law."""
from itertools import combinations, permutations
from math import comb, exp
from fractions import Fraction


def count_sinks(n, ranks):
    pairs=list(combinations(range(n),2))
    weights={pair:rank for rank,pair in enumerate(ranks)}
    chosen=[]
    for v in range(n):
        neighbors=sorted((weights[tuple(sorted((v,w)))],w) for w in range(n) if w!=v)
        chosen.append(frozenset(w for _,w in neighbors[:2]))
    return sum(all(chosen[v]==frozenset(set(t)-{v}) for v in t)
               for t in combinations(range(n),3))


def expectation(n):
    return Fraction(n*(n-1)*(n-2),(2*n-5)*(3*n-7)*(3*n-6))


def lambda_threshold(t):
    return Fraction(1,18) - exp(-2*t)/2 + (t/3+Fraction(4,9))*exp(-3*t)


def main():
    assert expectation(3)==1
    pairs=list(combinations(range(4),2))
    counts=[count_sinks(4,p) for p in permutations(pairs)]
    assert len(counts)==720
    got=Fraction(sum(counts),720)
    assert got==expectation(4)==Fraction(4,15), (got,expectation(4))
    assert max(counts)==1
    for n in range(3,250):
        z=expectation(n)
        assert 0 < z <=1
    for t in [0,0.1,0.25,0.5,1,2,3,5,10,20]:
        val=float(lambda_threshold(t))
        assert -1e-14<=val<=1/18+1e-14
    for t in [0.01,0.2,1,2,3,7,15]:
        h=1e-5
        deriv=(lambda_threshold(t+h)-lambda_threshold(t-h))/(2*h)
        expect=exp(-2*t)*(1-(t+1)*exp(-t))
        assert abs(deriv-expect)<2e-9
    assert abs(lambda_threshold(25)-1/18)<1e-20
    print('PASS: exhaustive n=4 edge rankings (720); rational exact means n=3,4; mark CDF/rate; 270+ finite checks')

if __name__=='__main__':main()
