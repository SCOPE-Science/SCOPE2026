"""Independent exact canonical-simplex checks of rooted-forest chain-polytope moments.

Python 3 standard library only. Enumerates every increasing-label rooted forest
through size six, integrates first and second moments over canonical order-polytope
simplices, and compares with the claimed beta moment product and covariance signs.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def subtree_sizes(parent):
    s = [1]*len(parent)
    for v in reversed(range(len(parent))):
        p=parent[v]
        if p>=0: s[p]+=s[v]
    return s


def beta_moment(parent, s, exponents):
    total = [0]*len(parent)
    for v in reversed(range(len(parent))):
        p=parent[v]
        if p>=0: total[p]+=total[v]+exponents[v]
    out=F(1)
    for i, a in enumerate(exponents):
        d=total[i]
        numerator=factorial(a)
        for j in range(d): numerator*=s[i]+j
        denominator=1
        for j in range(a+d): denominator*=s[i]+1+j
        out*=F(numerator, denominator)
    return out


def canonical_extensions(parent):
    n=len(parent)
    def recur(prefix,used):
        if len(prefix)==n:
            yield tuple(prefix)
            return
        for v in range(n):
            if v not in used and (parent[v]<0 or parent[v] in used):
                prefix.append(v)
                yield from recur(prefix,used|{v})
                prefix.pop()
    yield from recur([], set())


def independent_moments(parent):
    n=len(parent)
    means=[F(0)]*n
    seconds=[[F(0)]*n for _ in range(n)]
    ext=0
    for perm in canonical_extensions(parent):
        ext+=1
        ranks=[0]*n
        for i,v in enumerate(perm,1): ranks[v]=i
        lower=[ranks[parent[v]] if parent[v]>=0 else 0 for v in range(n)]
        widths=[ranks[v]-lower[v] for v in range(n)]
        for v in range(n):
            means[v]+=F(widths[v],n+1)
        for v in range(n):
            for w in range(n):
                overlap=max(0,min(ranks[v],ranks[w])-max(lower[v],lower[w]))
                seconds[v][w]+=F(widths[v]*widths[w]+overlap,(n+1)*(n+2))
    return ext,[m/ext for m in means],[[a/ext for a in row] for row in seconds]


def classify_pair(parent, u, v):
    def ancestors(t):
        out={t}
        while parent[t]>=0:
            t=parent[t]
            out.add(t)
        return out
    au=ancestors(u);av=ancestors(v)
    if u in av or v in au: return -1
    return 1 if au & av else 0


def check_all(nmax=6):
    forests=0; moment_comparisons=0; signs=0; extensions=0
    for n in range(1,nmax+1):
        for pa in product(*(range(-1,i) for i in range(n))):
            s=subtree_sizes(pa)
            e,means,seconds=independent_moments(pa)
            extensions+=e
            assert F(e,factorial(n)) == F(1,1) / product_frac(s), (pa,'volume',e,s)
            for i in range(n):
                a=[0]*n;a[i]=1
                assert means[i]==beta_moment(pa,s,a),(pa,i,'first')
                moment_comparisons+=1
                for j in range(n):
                    b=a.copy();b[j]+=1
                    assert seconds[i][j]==beta_moment(pa,s,b),(pa,i,j,'second')
                    moment_comparisons+=1
                    if i!=j:
                        cov=seconds[i][j]-means[i]*means[j]
                        assert (cov>0)-(cov<0)==classify_pair(pa,i,j),(pa,i,j,'sign',cov)
                        signs+=1
            forests+=1
    print('ROOTED_FOREST_CHAIN_MOMENTS_EXACT_PASSED', forests, extensions, moment_comparisons, signs)


def product_frac(s):
    out=1
    for x in s: out*=x
    return out

if __name__=='__main__': check_all()
