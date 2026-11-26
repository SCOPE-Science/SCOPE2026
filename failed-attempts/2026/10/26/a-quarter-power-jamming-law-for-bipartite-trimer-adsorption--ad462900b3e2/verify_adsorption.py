"""Independent reproducibility checks for balanced bipartite trimer adsorption.

Requires Python 3.10+ standard library. Prints results; no external files needed.
The infinite-size theorem is proved analytically in RESULT.md.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
from math import comb, gamma, isclose, sqrt, pi

@lru_cache(None)
def reduced(x,y):
    A=comb(x,2)*y if x>=2 else 0
    B=x*comb(y,2) if y>=2 else 0
    if not A+B:
        return {x+y:Fraction(1)}
    result=defaultdict(Fraction)
    for (xx,yy), weight in [((x-2,y-1),Fraction(A,A+B)) if A else ((0,0),Fraction(0)),
                           ((x-1,y-2),Fraction(B,A+B)) if B else ((0,0),Fraction(0))]:
        if weight:
            for r,v in reduced(xx,yy).items():result[r]+=weight*v
    return dict(result)

def labeled(n):
    N=2*n
    edges=[]
    for tri in combinations(range(N),3):
        a=sum(v<n for v in tri)
        if a in (1,2): edges.append(sum(1<<i for i in tri))
    @lru_cache(None)
    def f(mask):
        valid=[e for e in edges if e&mask==e]
        if not valid:return {mask.bit_count():Fraction(1)}
        z=defaultdict(Fraction)
        for e in valid:
            for r,p in f(mask^e).items():z[r]+=p/Fraction(len(valid))
        return dict(z)
    return f((1<<N)-1)

checks=0
for n in range(1,8):
    a,b=reduced(n,n),labeled(n)
    assert a==b,(n,a,b)
    assert sum(a.values())==1
    assert all((2*n-r)%3==0 for r in a)
    checks+=3

for x in range(1,18):
    for y in range(1,18):
        s=x+y
        if s>=3:
            A=comb(x,2)*y if x>=2 else 0
            B=x*comb(y,2) if y>=2 else 0
            assert A+B==x*y*(s-2)//2
            assert Fraction(A,A+B)==Fraction(x-1,s-2)
            checks+=2

for n in (12,45,123,901):
    for k in (0,1,n//10,n//5,n//2):
        s=2*n-3*k
        if s>=4:
            prod=1.
            for i in range(k):prod*=(2*n-3*i-3)/(2*n-3*i-2)
            # Gamma-ratio expression evaluated by lgamma to avoid overflow.
            from math import lgamma,exp
            alt=exp(lgamma(2*n/3)-lgamma((2*n+1)/3)
                   +lgamma((s+1)/3)-lgamma(s/3))
            assert isclose(prod,alt,rel_tol=1e-10,abs_tol=1e-11),(n,k,prod,alt)
            checks+=1

for n in (4,12,32,80,160):
    d=reduced(n,n)
    assert all(r>=0 and (2*n-r)%3==0 for r in d)
    checks+=1

print('All',checks,'exact-rational and Gamma-product checks passed.')
print('Exact terminal residual distributions for initial class sizes n=2..7:')
for n in range(2,6):
    print('n=',n,[(r,str(p)) for r,p in sorted(reduced(n,n).items())])
print('Theorem established analytically in RESULT.md: R_n/(2n)^(1/4) -> |N(0,1)|^(3/2).')
print('Limiting distribution function F(y)=erf(y^(2/3)/sqrt(2)), y>=0.')
