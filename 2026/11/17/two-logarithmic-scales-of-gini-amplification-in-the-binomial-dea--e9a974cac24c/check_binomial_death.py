"""Exact rational checks for finite binomial-death Gini estimates.

Only finite instances are checked. Infinite statements require the proof.
"""
from fractions import Fraction as Q
from math import comb


def kernel(n, p):
    q=1-p
    return [[Q(comb(i,j))*p**j*q**(i-j) if j<=i else Q(0)
             for j in range(n+1)] for i in range(n+1)]


def gini(x):
    return sum((abs(x[i]-x[j]) for i in range(len(x))
                for j in range(i+1,len(x))),Q(0))


def exact_norm(n,p):
    mat=kernel(n,p)
    best=Q(0)
    witness=None
    for mask in range(1,1<<(n+1)):
        k=mask.bit_count()
        if k> (n+1)//2:continue
        x=[(mask>>j)&1 for j in range(n+1)]
        y=[sum((mat[i][j]*x[j] for j in range(n+1)),Q(0)) for i in range(n+1)]
        score=gini(y)/Q(k*(n+1-k))
        if score>best:best=score;witness=mask
    return best,witness


def linear_bound(n,p):
    L=p*Q((n+1)*(n+2),6)
    err=Q(n*(n+1)*(n-1),2)*p**2
    return L,err


def endpoint(n,p):
    return gini([(1-p)**i for i in range(n+1)])/n


def check():
    total=0
    for n in range(2,9):
        for p in [Q(1,7),Q(1,3),Q(1,2),Q(4,5),Q(9,10)]:
            norm,witness=exact_norm(n,p)
            low=endpoint(n,p)
            L,err=linear_bound(n,p)
            universal=Q(1)/p
            diameter=Q((n+1)**2//4,n)
            assert low<=norm<=min(universal,diameter)
            assert abs(norm-L)<=err
            # For each tested dimension and parameter, an endpoint singleton
            # happens to attain the norm; this is NOT used as an all-n theorem.
            assert norm==low,(n,p,norm,low)
            total+=1
    print('EXACT_BINARY_CUT_GINI_BOUNDS_PASSED',total)
    # Semigroup identity checked on matrix coefficients with exact rationals.
    total=0
    for n in range(1,14):
        for p,q in [(Q(1,3),Q(2,5)),(Q(3,4),Q(4,7))]:
            a,b,c=kernel(n,p),kernel(n,q),kernel(n,p*q)
            for i in range(n+1):
                for j in range(n+1):
                    assert sum((a[i][k]*b[k][j] for k in range(n+1)),Q(0))==c[i][j]
                    total+=1
    print('EXACT_BINOMIAL_SEMIGROUP_IDENTITIES_PASSED',total)
    # Dobrushin coefficient is attained by states zero and n.
    total=0
    for n in range(2,14):
        p=Q(3,7);mat=kernel(n,p)
        d=max((sum((abs(mat[i][j]-mat[k][j]) for j in range(n+1)),Q(0))/2
                 for i in range(n+1) for k in range(i+1,n+1)))
        assert d==1-(1-p)**n
        total+=1
    print('EXACT_DOBRUSHIN_COEFFICIENTS_PASSED',total)
    print('ALL_BINOMIAL_DEATH_GINI_CHECKS_PASSED')

if __name__=='__main__':check()
