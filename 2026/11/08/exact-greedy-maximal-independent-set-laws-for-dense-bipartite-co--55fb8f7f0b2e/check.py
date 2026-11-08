"""Exact checks for random greedy maximal independent sets in bipartite complements.

Python 3 standard library only. This finite checker is not a proof of
claims for arbitrary graph order; the accompanying analytic proof is.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import permutations, combinations
from math import factorial


def missing_cycle(n):
    """The 2n-cycle as omitted edges, with side sets indexed 0..n-1."""
    return [{i, (i+1) % n} for i in range(n)]


def missing_fano():
    """Heawood incidence graph as omitted edges of K_{7,7}."""
    return [{i % 7, (i+1) % 7, (i+3) % 7} for i in range(7)]


def missing_two_six_cycles():
    return [{i//3*3+i%3, i//3*3+(i%3+1)%3} for i in range(6)]


def validate_missing(neighbors):
    n = len(neighbors)
    d = len(neighbors[0])
    assert 2 <= d < n
    assert all(len(s) == d for s in neighbors)
    assert all(sum(j in s for s in neighbors) == d for j in range(n))
    assert all(len(neighbors[i]&neighbors[j]) <= 1
               for i,j in combinations(range(n), 2))
    return n,d


def graph_neighbors(neighbors):
    n=len(neighbors)
    result=[0]*(2*n)
    for i in range(n):
        for j in range(n):
            if j not in neighbors[i]:
                result[i] |= 1<<(n+j)
                result[n+j] |= 1<<i
    return result


def expected_two_point_law(neighbors):
    n,d=validate_missing(neighbors)
    missing=graph_neighbors(neighbors)
    whole=(1<<(2*n))-1

    @lru_cache(None)
    def size_law(active):
        if not active:
            return {0: Fraction(1)}
        k=active.bit_count()
        counts={}
        for i in range(2*n):
            if not active & (1<<i):
                continue
            rest=active & ~(missing[i]|(1<<i))
            for size,weight in size_law(rest).items():
                counts[size+1] = counts.get(size+1, Fraction(0))+weight/k
        return counts

    actual=size_law(whole)
    p=Fraction(d*n, n*n-(d-1)*(d-1))
    expected={d+1:p,n:1-p}
    if d+1 == n:
        expected={n:Fraction(1)}
    assert actual == expected,(n,d,actual,expected)
    return n,d,actual,size_law.cache_info().currsize


def expected_full_law(neighbors):
    n,d=validate_missing(neighbors)
    adj=graph_neighbors(neighbors)
    all_vertices=(1<<(2*n))-1
    @lru_cache(None)
    def law(active):
        if not active:
            return {0:Fraction(1)}
        k=active.bit_count()
        out={}
        for v in range(2*n):
            if active & (1<<v):
                for mask,p in law(active&~(adj[v]|(1<<v))).items():
                    key=mask|(1<<v)
                    out[key]=out.get(key,Fraction(0))+p/k
        return out
    actual=law(all_vertices)
    p=Fraction(d*n,n*n-(d-1)**2)
    expected={
        (1<<n)-1:(1-p)/2,
        ((1<<n)-1)<<n:(1-p)/2,
    }
    for a in range(n):
        star=(1<<a)
        for b in neighbors[a]:
            star |= 1<<(n+b)
        assert star not in expected
        expected[star]=p/(2*n)
    for b in range(n):
        star=1<<(n+b)
        for a in range(n):
            if b in neighbors[a]:
                star |= 1<<a
        assert star not in expected
        expected[star]=p/(2*n)
    assert len(expected)==2*n+2
    assert actual==expected, (n,d,actual,expected)
    uniform_p=Fraction(1,2*n+2)
    tv=sum(abs(v-uniform_p) for v in actual.values())/2
    assert tv == Fraction(n,n+1)-p
    return len(actual), tv


def brute_permutations(neighbors):
    n,d=validate_missing(neighbors)
    if n>4:
        return
    adj=graph_neighbors(neighbors)
    cnt={}
    for order in permutations(range(2*n)):
        chosen=0
        for i in order:
            if not (adj[i]&chosen):
                chosen |= 1<<i
        k=chosen.bit_count()
        cnt[k]=cnt.get(k,0)+1
    p=Fraction(d*n,n*n-(d-1)**2)
    if d+1 == n:
        assert cnt == {n: factorial(2*n)}
    else:
        assert Fraction(cnt.get(d+1,0),factorial(2*n)) == p
    return cnt


def maximal_independent_count(neighbors):
    n,d=validate_missing(neighbors)
    adj=graph_neighbors(neighbors)
    tally={}
    for mask in range(1<<(2*n)):
        if any((mask & (1<<i)) and (mask&adj[i]) for i in range(2*n)):
            continue
        if any(not(mask & (1<<i)) and not (mask&adj[i]) for i in range(2*n)):
            continue
        size=mask.bit_count()
        tally[size]=tally.get(size,0)+1
    expected={d+1:2*n,n:2}
    if d+1 == n:
        expected={n:2*n+2}
    assert tally==expected,(n,d,tally,expected)
    return tally


def inclusion_exclusion(n,d):
    from math import comb
    p=sum(((-1)**(t+1))*Fraction(comb(d,t)*factorial(t)*factorial(n),
           (n-d+1)*factorial(n+t-1)) for t in range(1,d+1))
    assert p==Fraction(d*n,n*n-(d-1)**2)
    return p


def main():
    count=0
    for n in range(3,9):
        H=missing_cycle(n)
        full_count,tv=expected_full_law(H)
        actual=expected_two_point_law(H)
        maximal=maximal_independent_count(H)
        p=inclusion_exclusion(n,2)
        if n<=4:
            brute_permutations(H)
        print('cycle',n,'prob',p,'law',actual[2],'maximal',maximal,'states',actual[3],'terminal sets',full_count,'TV',tv)
        count+=1
    for label,H in [('two-C6',missing_two_six_cycles()),('Fano',missing_fano())]:
        actual=expected_two_point_law(H)
        full_count,tv=expected_full_law(H)
        maximal=maximal_independent_count(H)
        p=inclusion_exclusion(actual[0],actual[1])
        print(label,'prob',p,'law',actual[2],'maximal',maximal,'states',actual[3],'terminal sets',full_count,'TV',tv)
        count+=1
    for d in range(1,10):
        for n in range(max(d+1,3),100):
            inclusion_exclusion(n,d)
            count+=1
    print('PASS',count,'exact model/identity cases')

if __name__=='__main__':
    main()
