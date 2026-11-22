"""Exact finite checks for the self-inverse partial-automorphism census of even crowns.

Independent methods: cyclic-run composition, binary subset profiles, and
explicit poset-isomorphism tests for permutations of subsets. Python 3 only.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def run_type(length, initial_parity):
    if length == 1:
        return ('singleton', 1)
    if length % 2 == 0:
        return ('even', length)
    return ('odd', length, initial_parity)


def profile_of_subset(n, subset):
    if not subset or len(subset) == n:
        raise ValueError('only proper nonempty subsets')
    selected = set(subset)
    starts = [i for i in range(n) if i in selected and (i-1) % n not in selected]
    profile = Counter()
    for start in starts:
        length = 0
        while (start+length) % n in selected:
            length += 1
        profile[run_type(length, start % 2)] += 1
    return tuple(sorted(profile.items()))


def weak_compositions(total, size):
    if size == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - size + 2):
        for tail in weak_compositions(total-first, size-1):
            yield (first,)+tail


def profiles_by_runs(n):
    # This is the coefficient of n/2 * [z^n] sum_{r>=1} tr(M(z,u)^r)/r.
    answer = defaultdict(Fraction)
    for r in range(1, n//2+1):
        for lengths in weak_compositions(n, 2*r):
            for first_parity in (0,1):
                pos = first_parity
                typ = Counter()
                for j in range(r):
                    ell, gap = lengths[2*j:2*j+2]
                    typ[run_type(ell,pos)] += 1
                    pos = (pos+ell+gap) % 2
                assert pos == first_parity
                answer[tuple(sorted(typ.items()))] += Fraction(n, 2*r)
    assert all(v.denominator == 1 for v in answer.values())
    return {p: int(v) for p,v in answer.items()}


def profiles_by_subsets(n):
    ans = Counter()
    for mask in range(1,(1<<n)-1):
        ans[profile_of_subset(n, [i for i in range(n) if mask>>i&1])] += 1
    return dict(ans)


def multiply(A,B):
    out = Counter()
    for (f,t),va in A.items():
        for (g,u),vb in B.items():
            out[(f+g,t+u)] += va*vb
    return out


def power(P,k):
    R={(0,0):1}
    for _ in range(k): R=multiply(R,P)
    return R


def type_involutions(typ,c):
    ell=typ[1]
    a=2 if typ[0]=='odd' else 1
    one={(ell,0):1}
    if a==2: one[(1,(ell-1)//2)]=1
    total=Counter()
    for j in range(c//2+1):
        ways=factorial(c)//(factorial(c-2*j)*factorial(j)*2**j)*a**j
        for (f,t),v in power(one,c-2*j).items():
            total[(f,t+j*ell)] += ways*v
    return total


def formula(n):
    profiles=profiles_by_runs(n)
    counts=Counter({(0,0):1})
    for prof, domain_count in profiles.items():
        local={(0,0):1}
        for typ,c in prof:
            local=multiply(local,type_involutions(typ,c))
        for key,v in local.items(): counts[key]+=domain_count*v
    # Units form a parity-preserving dihedral group of order n.
    m=n//2
    counts[(n,0)]+=1
    counts[(2,(n-2)//2)]+=m
    if m%2==0: counts[(0,n//2)]+=1
    return counts


def relation(n,a,b):
    # 0 <= a,b < n; all odd-labeled points in the standard crown are minimal.
    # With zero-based labels, even indexes are minimal.
    if a==b: return 0
    if (b-a)%n in (1,n-1) and a%2==0: return -1
    if (b-a)%n in (1,n-1) and b%2==0: return 1
    return 0


def involutions_tuple(items):
    if not items:
        yield {}
        return
    first=items[0]
    for rest in involutions_tuple(items[1:]):
        yield {first:first, **rest}
    for j in range(1,len(items)):
        second=items[j]
        rem=items[1:j]+items[j+1:]
        for rest in involutions_tuple(rem):
            yield {first:second, second:first, **rest}


def brute(n):
    out=Counter({(0,0):1})
    for k in range(1,n+1):
        for S in combinations(range(n),k):
            for p in involutions_tuple(S):
                if any(relation(n,a,b)!=relation(n,p[a],p[b]) for a in S for b in S):
                    continue
                fixed=sum(p[x]==x for x in S)
                out[(fixed,(k-fixed)//2)] += 1
    return out


def rank_spectrum(P):
    q=Counter()
    for (f,t),c in P.items(): q[f+2*t]+=c
    return dict(sorted(q.items()))


def main():
    for n in (4,6,8,10,12):
        assert profiles_by_subsets(n)==profiles_by_runs(n), n
        calc=formula(n)
        if n<=8:
            direct=brute(n)
            assert calc==direct,(n,calc-direct,direct-calc)
        spectrum=rank_spectrum(calc)
        assert spectrum[0]==1 and spectrum[1]==n and spectrum[n-1]==2*n
        if n>=6:
            m=n//2
            expected=n*((5*m-7)//2) if m%2 else n*(5*m//2 - 3)
            # Odd m has (5m-7) even, and even m has 5m/2 integer.
            assert spectrum[n-2]==expected,(n,spectrum[n-2],expected)
        print(n, len(profiles_by_subsets(n)),sum(calc.values()), spectrum)
    print('EVEN_CROWN_INVOLUTION_CENSUS_VERIFIED 4,6,8 brute; 4,6,8,10,12 transfer/profile checks')

if __name__=='__main__': main()
