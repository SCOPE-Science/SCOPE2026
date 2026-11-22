"""Exact-rational diagnostics for a common-influence median update model.

The program checks finite configurations; the accompanying analytic proof
establishes the statements for every finite population size.
"""
from fractions import Fraction as F
from itertools import product, permutations
from math import comb


def interval(weights, opinions):
    """Closed weighted-median minimizer interval for strictly positive integer weights."""
    order=sorted(range(len(weights)),key=lambda i:(opinions[i],i))
    total=sum(weights)
    s=0
    for j,i in enumerate(order):
        s+=weights[i]
        if 2*s>=total:
            lower=opinions[i]
            if 2*s==total and j+1<len(order):
                upper=opinions[order[j+1]]
            else: upper=lower
            return lower,upper
    raise AssertionError


def project(v,lo,hi):return max(lo,min(v,hi))


def simulate(weights,initial,gammas,steps):
    x=list(initial)
    lo,hi=interval(weights,x)
    targets=[project(y,lo,hi) for y in initial]
    for k in range(steps+1):
        formula=[targets[i]+(1-gammas[i])**k*(initial[i]-targets[i]) for i in range(len(x))]
        assert x==formula,(weights,initial,gammas,k,x,formula)
        assert interval(weights,x)==(lo,hi),(weights,initial,k,x,(lo,hi),interval(weights,x))
        responses=[project(y,*interval(weights,x)) for y in x]
        x=[(1-gammas[i])*x[i]+gammas[i]*responses[i] for i in range(len(x))]


def p_exact(weights):
    from itertools import combinations
    n=len(weights); total=sum(weights)
    p=F(0)
    for k in range(1,n):
        for subset in combinations(range(n),k):
            if 2*sum(weights[i] for i in subset)==total:
                p+=F(1,comb(n,k))
    return p


def p_by_ranks(weights):
    n=len(weights); total=sum(weights)
    polarized=0
    for perm in permutations(range(n)):
        c=0
        for j in perm[:-1]:
            c+=weights[j]
            if 2*c==total:
                polarized+=1;break
    from math import factorial
    return F(polarized,factorial(n))


def run():
    tested=0; probs=0
    for n in range(2,7):
        for weights in product((1,2,3),repeat=n):
            # Distinct and tied configurations with heterogeneous damping.
            for pattern in (tuple(range(n)), tuple(range(n-1,-1,-1)),
                            tuple(i//2 for i in range(n))):
                initial=tuple(F(pattern[i],n+1) for i in range(n))
                gammas=tuple(F(1+(i%3),5) for i in range(n))
                simulate(weights,initial,gammas,6)
                tested+=1
    for n in range(2,7):
        for weights in product((1,2,3),repeat=n):
            assert p_exact(weights)==p_by_ranks(weights),(n,weights)
            probs+=1
    assert p_exact((1,1,1,3))==F(1,2)
    assert p_exact((1,1,2))==F(2,3)
    assert p_exact((1,1,1,1,2))==F(4,5)
    for n in range(2,8):
        assert p_exact((1,)*n)==int(n%2==0)
    print(f'PASS: {tested} exact orbit/interval checks, {probs} exact probability/permutation comparisons.')
    print('PASS: illustrative probabilities (1,1,1,3)->1/2; (1,1,2)->2/3; (1,1,1,1,2)->4/5.')
    print('PASS: uniform-weight parity n=2..7.')

if __name__=='__main__':run()
