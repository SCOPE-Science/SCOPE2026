"""Reproducible exact checks for Yule--Harding shared rooted clades.

Run: python verify.py . All calculations use integer or rational arithmetic.
The infinite limit rests on the accompanying proof, not on these finite checks.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def fall(x, r):
    z = 1
    for j in range(r):
        z *= x-j
    return z


def all_splits(labels):
    m = len(labels)
    if m < 2:
        return
    first = labels[0]
    other = labels[1:]
    for r in range(m-1):
        for c in combinations(other, r):
            left = (first,)+c
            right = tuple(x for x in labels if x not in left)
            yield left, right


@lru_cache(None)
def yule_trees(labels):
    m = len(labels)
    if m == 1:
        return (((labels[0], F(1)),))
    out = []
    for left, right in all_splits(labels):
        prob = F(2, (m-1)*comb(m,len(left)))
        for tl, pl in yule_trees(left):
            for tr, pr in yule_trees(right):
                out.append(((tl,tr), prob*pl*pr))
    assert sum((p for t,p in out), F(0)) == 1
    return tuple(out)


def clades(tree):
    if isinstance(tree, int):
        return frozenset((tree,)), frozenset()
    ls, lc = clades(tree[0]); rs, rc = clades(tree[1])
    s = ls | rs
    return s, lc | rc | {ls,rs}


def p(n,k):
    return F(2*n, k*(k+1)*comb(n,k))


def yule_cherries(n):
    probs = {1: F(1)}
    for size in range(2,n):
        next_probs = {}
        for c,prob in probs.items():
            hold = prob*F(2*c,size)
            gain = prob*(1-F(2*c,size))
            next_probs[c] = next_probs.get(c,F(0))+hold
            next_probs[c+1] = next_probs.get(c+1,F(0))+gain
        probs = next_probs
    assert sum(probs.values())==1
    return probs


def moment_shared(n, r):
    distribution = yule_cherries(n)
    m = sum((v*fall(c,r) for c,v in distribution.items()),F(0))
    count = F(fall(n,2*r),2**r)
    return m*m/count


def main():
    assertions = 0
    for n in range(3,7):
        trees = yule_trees(tuple(range(1,n+1)))
        groups = []
        marg = {frozenset(c): F(0) for k in range(2,n) for c in combinations(range(1,n+1),k)}
        cherry_mean = F(0)
        for tree,weight in trees:
            all_sets = {c for c in clades(tree)[1] if len(c)>1 and len(c)<n}
            cherries = {c for c in all_sets if len(c)==2}
            cherry_mean += weight*len(cherries)
            groups.append((cherries,all_sets,weight))
            for s in all_sets:
                marg[s]+=weight
        assert cherry_mean==F(n,3); assertions+=1
        for s,q in marg.items():
            assert q==p(n,len(s)), (n,s,q,p(n,len(s)))
            assertions+=1
        pmf = {}
        pmf_all = {}
        for a,aa,wa in groups:
            for b,bb,wb in groups:
                r = len(a & b)
                t = len(aa & bb)
                pmf[r] = pmf.get(r,F(0))+wa*wb
                pmf_all[t] = pmf_all.get(t,F(0))+wa*wb
        assert sum(pmf.values()) == 1; assertions += 1
        assert sum(pmf_all.values()) == 1; assertions += 1
        assert sum((q*k for k,q in pmf.items()),F(0)) == F(2*n,9*(n-1)); assertions+=1
        assert sum((q*k for k,q in pmf_all.items()),F(0)) == sum((comb(n,k)*p(n,k)**2 for k in range(2,n)), F(0)); assertions+=1
        for r in range(1,min(n//2,3)+1):
            actual = sum((q*fall(k,r) for k,q in pmf.items()), F(0))
            assert actual == moment_shared(n,r), (n,r,actual,moment_shared(n,r))
            assertions+=1
        print(f'n={n}: trees={len(trees)}, shared-cherry PMF='+str(dict(sorted(pmf.items()))))
    # Independent check of asymptotic combinatorics using exact finite factorial moments.
    for n in (20,40,80,160):
        means = [float(moment_shared(n,r)) for r in range(1,5)]
        print(f'n={n}: factorial moments r=1..4 {means}; limits {[float(F(2,9)**r) for r in range(1,5)]}')
        assert all(v>0 for v in means);assertions+=1
    # The exact expected count of size >=3 shared clades tends to zero.
    for n in (10,50,100,500,1000):
        tail=sum((comb(n,k)*p(n,k)**2 for k in range(3,n)),F(0))
        print(f'n={n}: expected shared clades of size >=3 = {float(tail):.10f}; n*expectation={float(n*tail):.10f}')
        assert tail <= F(2,n) ; assertions+=1
    # Independent exact checks of the pair-clade probability identities used in
    # the second-order rare-collision calculation (no two-tree enumeration).
    n=7
    aa=frozenset((1,2,3)); bb=frozenset((4,5,6)); four=frozenset((1,2,3,4))
    dist=yule_trees(tuple(range(1,n+1)))
    p33=sum((w for t,w in dist if aa in clades(t)[1] and bb in clades(t)[1]), F(0))
    p34nested=sum((w for t,w in dist if aa in clades(t)[1] and four in clades(t)[1]), F(0))
    expected33=F(35*n-141,35*__import__('math').prod(n-j for j in range(1,6)))
    assert p33==expected33==F(13,3150); assertions+=1
    assert p34nested==p(n,4)*F(1,6)==F(1,300); assertions+=1
    print('n=7 exact fixed disjoint triple-pair probability:',p33)
    print('n=7 exact nested triple-and-quad probability:',p34nested)
    # Bonferroni main-term combination (omitted event families are O(n^-3)
    # by the finite-pattern argument in the proof).
    for n in (200,1000,5000):
        P33=F(35*n-141, 35*__import__('math').prod(n-j for j in range(1,6)))
        e3=comb(n,3)*p(n,3)**2
        e4=comb(n,4)*p(n,4)**2
        e33=comb(n,3)*comb(n-3,3)*P33**2
        e34nest=comb(n,4)*4*(p(n,4)*F(1,6))**2
        approx=e3+e4-e33/2-e34nest
        coefficient=float(n*n*(approx-F(1,6*n)))
        print('n=',n,'second-order Bonferroni coefficient=',format(coefficient,'.9f'))
        assert abs(coefficient-float(F(1259,1800))) < 3.0/n
        assertions+=1
    print('PASS exact assertions:',assertions)

if __name__=='__main__':
    main()
