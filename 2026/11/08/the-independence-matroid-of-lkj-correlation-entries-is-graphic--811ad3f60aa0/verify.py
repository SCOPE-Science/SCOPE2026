"""Exact finite Gaussian-Wishart moment comparisons for the stated graph law.
No random sampling is used. This corroborates, but does not replace, the general proof.
"""
from fractions import Fraction
from itertools import product
from math import prod

def odd_double_factorial(t):
    if t in (0, -1): return 1
    assert t % 2 == 0 and t >= 0
    return prod(range(1, t, 2))

def wishart_monomial_moment(nu, edges):
    """Exact E[product W_ij], W=GG^T, G n by nu standard iid."""
    vertices=sorted(set(v for e in edges for v in e))
    ans=0
    for assignment in product(range(nu), repeat=len(edges)):
        powers={}
        for c,(a,b) in zip(assignment,edges):
            powers[a,c]=powers.get((a,c),0)+1
            powers[b,c]=powers.get((b,c),0)+1
        if any(p%2 for p in powers.values()): continue
        ans+=prod(odd_double_factorial(p) for p in powers.values())
    return ans

def chi_sq_moment(nu,k):
    return prod(nu+2*j for j in range(k))

def correlation_moment(nu,edges):
    deg={}
    for a,b in edges:
        deg[a]=deg.get(a,0)+1;deg[b]=deg.get(b,0)+1
    if any(d%2 for d in deg.values()): return Fraction(0)
    return Fraction(wishart_monomial_moment(nu,edges), prod(chi_sq_moment(nu,d//2) for d in deg.values()))

def run():
    tests=0
    for nu in range(4,7):
        for k in range(3,min(nu,6)+1):
            cycle=[(i,(i+1)%k) for i in range(k)]
            assert correlation_moment(nu,cycle)==Fraction(1,nu**(k-1))
            tests+=1
        for k in range(1,min(nu,4)):
            path=[(i,i+1) for i in range(k)]
            for powers in product((0,1,2),repeat=k):
                edges=[e for e,p in zip(path,powers) for _ in range(p)]
                expected=prod((Fraction(1,nu) if p==2 else (Fraction(0) if p==1 else Fraction(1))) for p in powers)
                assert correlation_moment(nu,edges)==expected,(nu,k,powers)
                tests+=1
    return tests

if __name__=='__main__':
    print('PASS',run(),'exact finite Wishart moment comparisons')
