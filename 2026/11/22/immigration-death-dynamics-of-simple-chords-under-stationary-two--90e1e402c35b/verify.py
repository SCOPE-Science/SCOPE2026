"""Exact verification of adjacent pairs under forced two-pair switch.
Self-contained, Python 3 standard library. No external files are needed.
"""
from fractions import Fraction
from itertools import combinations
from collections import Counter
from math import comb


def perfect_matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for i in range(1,len(vertices)):
        b = vertices[i]
        for rest in perfect_matchings(vertices[1:i]+vertices[i+1:]):
            yield tuple(sorted(((a,b),)+rest))


def s_count(matching):
    m=2*len(matching)
    return sum((b-a==1 or (a==0 and b==m-1)) for a,b in matching)


def alternatives(pair1,pair2):
    a,b=pair1;c,d=pair2
    return [tuple(sorted(((min(a,c),max(a,c)),(min(b,d),max(b,d))))),
            tuple(sorted(((min(a,d),max(a,d)),(min(b,c),max(b,c)))))]


def check(n):
    states=list(perfect_matchings(tuple(range(2*n))))
    assert len(states)==__import__('math').prod(range(1,2*n,2))
    vals=Counter(s_count(m) for m in states)
    N=len(states); mean=sum(k*v for k,v in vals.items())/N
    exact_mean=Fraction(2*n,2*n-1)
    assert Fraction(sum(k*v for k,v in vals.items()),N)==exact_mean
    exact_var=Fraction(4*n*(n-1),(2*n-1)**2)
    variance=Fraction(sum(k*k*v for k,v in vals.items()),N)-exact_mean**2
    assert variance==exact_var
    alpha=Fraction(1,1)-Fraction(2*n-1,n*(n-1))
    beta=Fraction(1,n*(n-1))
    moment2=Fraction(0)
    for M in states:
        s=s_count(M)
        neighbors=[]
        for i,j in combinations(range(n),2):
            a,b=M[i],M[j]
            for alt in alternatives(a,b):
                mm=tuple(sorted([M[z] for z in range(n) if z not in (i,j)]+list(alt)))
                neighbors.append(s_count(mm))
        assert len(neighbors)==n*(n-1)
        av=Fraction(sum(neighbors),len(neighbors))
        assert av==exact_mean+alpha*(s-exact_mean)==(1-Fraction(2,n))*s+beta*(2*n-s)
        moment2+=Fraction(s*sum(neighbors),len(neighbors)*N)
    assert moment2-exact_mean**2==exact_var*alpha
    print(f'n={n}: {N} matchings; mean={exact_mean}, variance={exact_var}, eigenvalue={alpha}, lag-one covariance={exact_var*alpha}; verified')

if __name__=='__main__':
    for n in range(2,7):
        check(n)
    print('ALL EXACT ENUMERATION CHECKS PASSED')
