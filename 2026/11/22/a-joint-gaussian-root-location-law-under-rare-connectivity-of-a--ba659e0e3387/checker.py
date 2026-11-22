"""Exact finite checks for a connected one-dimensional nearest-neighbor graph.

Only standard-library rational arithmetic; independent rank enumeration and
independent exponential-order-statistic integration. Run python checker.py.
"""
from fractions import Fraction as F
from itertools import permutations, product
from collections import Counter
from math import comb, factorial


def rational_moments(n):
    """Integrate over independent Exp order-statistic increments and Bernoulli end choices.

    The unnormalised gap vector has n+1 independent unit exponentials.
    Its total S is Gamma(n+1,1) and is independent of the normalized vector.
    Hence E(Q/S)=E(Q)/(n+1), E(Q^2/S^2)=E(Q^2)/((n+1)(n+2)).
    """
    m=n-1
    ncases=2**(m-1)
    EJ=EQ=EJQ=EQ2=EJ2=F(0)
    rates=[F(m-j) for j in range(m)]
    for b in product((0,1),repeat=m-1):
        j=1+sum(b)
        # Q = left outer spacing + half the smallest gap + left-allocated gaps.
        # The m interior sorted exponential spacings W_0,...,W_(m-1)
        # are cumulative sums of independent D_j ~ Exp(rate m-j).
        coeff=[F(1,2) if t==0 else F(0) for t in range(m)]
        for r,bit in enumerate(b,1):
            if bit:
                for t in range(m-r+1): coeff[t]+=1
        meanq=F(1)+sum((c/r for c,r in zip(coeff,rates)),F(0))
        varq=F(1)+sum((c*c/(r*r) for c,r in zip(coeff,rates)),F(0))
        sq=meanq*meanq+varq
        EJ+=j; EQ+=meanq; EJQ+=j*meanq; EQ2+=sq; EJ2+=j*j
    EJ/=ncases; EQ/=ncases; EJQ/=ncases; EQ2/=ncases; EJ2/=ncases
    N=n+1
    EM=EQ/N
    varJ=EJ2-EJ*EJ
    cov=EJQ/N-EJ*EM
    varM=EQ2/(N*(N+1))-EM*EM
    return EJ,EM,varJ,cov,varM


def verify():
    cases=0
    for n in range(2,10):
        m=n-1
        counts=Counter()
        accepted=0
        for rank_sequence in permutations(range(1,m+1)):
            if all(not(rank_sequence[k]>rank_sequence[k-1] and rank_sequence[k]>rank_sequence[k+1])
                   for k in range(1,m-1)):
                accepted+=1
                counts[rank_sequence.index(1)+1]+=1
        assert accepted==2**(m-1)
        assert F(accepted,factorial(m))==F(2**(n-2),factorial(n-1))
        for j in range(1,m+1):
            assert counts[j]==comb(n-2,j-1)
        got=rational_moments(n)
        expected=(F(n,2),F(1,2),F(n-2,4),
                  F(m*m-1,4*m*(n+1)),
                  (F(n)-F(1,m*m))/(2*(n+1)*(n+2)))
        assert got==expected,(n,got,expected)
        cases+=1
    print('PASS:',cases,'sizes n=2..9; all rank permutations enumerated;')
    print('exact conditional rank distribution and five joint moments independently integrated.')

if __name__=='__main__':
    verify()
