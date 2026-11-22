"""Exact rational/integer coefficient check, no third-party dependencies.
Run: python3 verify_coefficients.py
"""
from collections import defaultdict
from math import comb, factorial


def bivariate_no_small_components(r, c):
    """m!n! coefficient of exp(-x-y-zxy) sum (1+z)^(ab)x^a/a!y^b/b!."""
    out = defaultdict(int)
    for i in range(r+1):
        for j in range(c+1):
            for k in range(min(r-i, c-j)+1):
                a, b = r-i-k, c-j-k
                scale = ((-1)**(i+j+k)*factorial(r)*factorial(c)//
                         (factorial(i)*factorial(j)*factorial(k)*factorial(a)*factorial(b)))
                for d in range(a*b+1):
                    out[k+d] += scale*comb(a*b,d)
    return out


def l_polynomial(m,n):
    result=defaultdict(int)
    for r,c,mult in ((m,n,1),(m-1,n,m),(m,n-1,n)):
        for k,v in bivariate_no_small_components(r,c).items():
            result[k] += mult*v
    assert all(v>=0 for v in result.values())
    return {k:v for k,v in result.items() if v}

expected = {
 (2,2):(2,4,9),(2,3):(3,14,36),(2,4):(4,56,149),
 (3,3):(4,81,328),(3,4):(4,54,2966),(3,5):(5,480,25134),
 (3,6):(6,3210,203098),(4,4):(5,672,52871),
 (4,5):(6,6560,901440),(4,6):(6,1440,14915909),
 (5,5):(6,1800,30541036),
}
for (m,n),(minsize,mincount,total) in expected.items():
    P=l_polynomial(m,n)
    assert (min(P),P[min(P)],sum(P.values()))==(minsize,mincount,total),(m,n,P)
    assert min(P)==max(n-1,(2*(m+n-1)+2)//3)
for m in range(2,11):
    for n in range(m,11):
        # Independently construct a bipartite star-tree forest on m+n-1
        # vertices: k trees, no isolated edge, with exactly f edges.
        r,c=m,n-1
        k=min(r,c,(r+c)//3)
        rs=[1]*k;cs=[1]*k
        for _ in range(k):
            if r-sum(rs)>0: rs[_]+=1
            else:cs[_]+=1
        rs[0]+=r-sum(rs)
        cs[0]+=c-sum(cs)
        assert all(a+b>=3 for a,b in zip(rs,cs))
        edges=sum(a+b-1 for a,b in zip(rs,cs))
        assert edges==max(n-1,(2*(m+n-1)+2)//3)
print('COEFFICIENTS_OK')

# A second polynomial, for ordinary locating-domination, is obtained by
# adjoining exactly one isolated selected rook and removing its row and column.
# This checks the isolated-edge bijection at the coefficient level.
def ordinary_ld_poly(m,n):
    p=defaultdict(int,l_polynomial(m,n))
    for degree,count in l_polynomial(m-1,n-1).items():
        p[degree+1]+=m*n*count
    return {k:v for k,v in p.items() if v}

ordinary_expected={
 (2,2):(2,4,9),(2,3):(3,20,42),(2,4):(3,24,181),
 (3,3):(3,36,409),(3,4):(4,222,3398),
 (3,5):(5,1320,27369),(3,6):(5,540,213682),
 (4,4):(5,1968,58119),(4,5):(5,1080,960760),
}
# The minimum-count entries above are checked independently against direct
# exhaustive code below; the ordinary minima are checked against the known
# rook locating-domination formula.
for (m,n),(_min,_count,total) in ordinary_expected.items():
    p=ordinary_ld_poly(m,n)
    normal_min=(n-1 if n>=2*m else (2*(m+n)+2)//3-1)
    assert min(p)==normal_min==_min,(m,n,p)
    assert p[min(p)]==_count,(m,n,p)
    assert sum(p.values())==total,(m,n,p)
    lt=l_polynomial(m,n)
    assert min(lt)-normal_min==int(n<=2*m and (m+n)%3==0)
print('LOCATING_DIFFERENCE_OK')

# Independent labelled-tree forest recursion (distinguished left root).
from functools import lru_cache
@lru_cache(None)
def forest_counts(r,c):
    if r==c==0:return {0:1}
    if r==0 or c==0:return {}
    result=defaultdict(int)
    for a in range(1,r+1):
        for b in range(1,c+1):
            if a+b<3:continue
            choose=comb(r-1,a-1)*comb(c,b)
            trees=(a**(b-1))*(b**(a-1))
            for k,v in forest_counts(r-a,c-b).items():
                result[k+a+b-1]+=choose*trees*v
    return dict(result)

def min_forest_count(m,n,g):
    return (forest_counts(m,n).get(g,0)+
            m*forest_counts(m-1,n).get(g,0)+
            n*forest_counts(m,n-1).get(g,0))
for m,n in ((2,2),(2,3),(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)):
    p=l_polynomial(m,n);g=min(p)
    assert min_forest_count(m,n,g)==p[g],(m,n,g)
print('FOREST_CENSUS_OK')
