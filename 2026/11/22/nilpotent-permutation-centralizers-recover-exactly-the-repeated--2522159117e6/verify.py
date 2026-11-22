"""Independent finite checks of nilpotent partial bijections centralizing permutations.

Run with Python 3: python verify.py. No nonstandard dependencies.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial, isqrt


def permutation_from_parts(parts):
    n = sum(parts)
    p = list(range(n))
    a = 0
    for d in parts:
        for j in range(d):
            p[a+j] = a+(j+1)%d
        a += d
    return tuple(p)


def partial_injections(n):
    for k in range(n+1):
        for src in combinations(range(n), k):
            for dst in combinations(range(n), k):
                for ordered in permutations(dst):
                    f = [-1]*n
                    for x,y in zip(src,ordered):
                        f[x] = y
                    yield tuple(f)


def commute(f, sigma):
    # Compare f(sigma(x)) and sigma(f(x)), respecting undefined values.
    return all(f[sigma[x]] == (-1 if f[x] < 0 else sigma[f[x]])
               for x in range(len(f)))


def nilpotence_index(f):
    n = len(f)
    current = list(range(n))
    for depth in range(1, n+2):
        current = [(-1 if y < 0 else f[y]) for y in current]
        if all(y < 0 for y in current):
            return depth
    return None


def factors(parts):
    return Counter(parts)


def mul(A, B):
    C = Counter()
    for i,a in A.items():
        for j,b in B.items():
            C[i+j] += a*b
    return dict(C)


def cutoff_factor(r, d, cutoff):
    # Enumerate unordered chain-size multiplicities, rather than partial maps.
    out = Counter()
    def rec(j, left, denomin, edges):
        if j > cutoff:
            if left == 0:
                out[edges*d] += factorial(r)//denomin * d**edges
            return
        for m in range(left//j+1):
            rec(j+1, left-j*m, denomin*factorial(m), edges+(j-1)*m)
    rec(1,r,1,0)
    return dict(out)


def predicted_cutoff(parts, s):
    result={0:1}
    for d,r in factors(parts).items():
        result=mul(result, cutoff_factor(r,d,s))
    return result


def predicted_joint(parts):
    n=sum(parts)
    previous={}
    result={}
    for s in range(1,n+2):
        now=predicted_cutoff(parts,s)
        for rank in set(now)|set(previous):
            count=now.get(rank,0)-previous.get(rank,0)
            if count:
                result[(rank,s)]=count
        previous=now
    return result


def predicted_rank(parts):
    P={0:1}
    for d,r in factors(parts).items():
        Q={d*k:comb(r-1,k)*factorial(r)//factorial(r-k)*d**k
           for k in range(r)}
        P=mul(P,Q)
    return P


def recover_repeats(P,n):
    R=dict(P)
    out={}
    for d in range(1,n+1):
        a=R.get(d,0)
        if a==0:
            continue
        if a%d:
            raise ValueError('nonintegral leading count')
        discr=1+4*(a//d)
        root=isqrt(discr)
        if root*root!=discr or (1+root)%2:
            raise ValueError('nontriangular leading count')
        r=(1+root)//2
        if r<2:
            raise ValueError('bad multiplicity')
        out[d]=r
        Q={d*k:comb(r-1,k)*factorial(r)//factorial(r-k)*d**k
           for k in range(r)}
        # Exact formal division in ascending degree.
        remaining=Counter(R)
        quotient={}
        for i in range(max(remaining,default=0)+1):
            v=remaining.get(i,0)
            if v:
                quotient[i]=v
                for q,c in Q.items():
                    remaining[i+q]-=v*c
        if any(remaining.values()):
            raise AssertionError('not an exact factor')
        R=quotient
    assert R=={0:1}, R
    return out


def check(parts):
    sigma=permutation_from_parts(parts)
    n=len(sigma)
    observed=Counter()
    for f in partial_injections(n):
        if commute(f,sigma):
            idx=nilpotence_index(f)
            if idx is not None:
                observed[(sum(v>=0 for v in f),idx)]+=1
    expected=predicted_joint(parts)
    assert dict(observed)==expected, (parts,observed,expected)
    rcounts=Counter()
    for (rank,idx),cnt in observed.items():
        rcounts[rank]+=cnt
    assert dict(rcounts)==predicted_rank(parts), (parts,rcounts,predicted_rank(parts))
    assert recover_repeats(predicted_rank(parts),n)=={
        d:r for d,r in factors(parts).items() if r>=2}
    print('TYPE',parts,'TOTAL',sum(observed.values()),'RANK',dict(sorted(rcounts.items())),
          'MAX_INDEX',max(idx for rank,idx in observed))


if __name__=='__main__':
    for parts in [(1,), (1,1),(2,2),(1,1,1),(1,2,2),(3,3),
                  (1,1,2,2),(2,2,2),(1,1,1,1,1),(1,1,1,1,1,1),
                  (1,1,1,2),(1,1,2),(2,3),(1,4),(5,)]:
        check(parts)
    assert predicted_rank((5,))==predicted_rank((1,4))=={0:1}
    assert predicted_rank((2,2,2,5,5,7))=={
        0:1,2:12,4:24,5:10,7:120,9:240}
    print('NILPOTENT_PERMUTATION_CENTRALIZER_CHECKS_PASSED')
