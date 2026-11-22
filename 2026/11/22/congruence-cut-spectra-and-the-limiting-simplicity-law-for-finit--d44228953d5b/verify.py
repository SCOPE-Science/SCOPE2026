"""Reproducible finite checks for the strict-implication congruence spectrum.

Only standard Python 3 is required. Exhaustive finite checks are not an
all-size proof; the algebraic argument is in RESULT.md.
"""
from itertools import product
from collections import Counter
from functools import lru_cache


def strict(n, edge, a, b):
    return n-1 if a <= b else min(edge[b:a])


def heyting(n, a, b):
    return n-1 if a <= b else b


def pred_cuts(n, edge):
    return frozenset(k for k in range(1, n-1)
                     if min(edge[k:]) >= k)


def all_partitions(n):
    labels = [0] * n
    def rec(i, high):
        if i == n:
            yield tuple(labels)
            return
        for c in range(high+2):
            labels[i] = c
            yield from rec(i+1, max(high,c))
    yield from rec(1,0)


def compatible_partition(n, edge, p):
    eq = lambda a,b: p[a] == p[b]
    pairs = [(a,b) for a in range(n) for b in range(n) if eq(a,b)]
    for a,b in pairs:
        for c,d in pairs:
            if not (eq(min(a,c),min(b,d)) and
                    eq(max(a,c),max(b,d)) and
                    eq(heyting(n,a,c),heyting(n,b,d)) and
                    eq(strict(n,edge,a,c),strict(n,edge,b,d))):
                return False
    return True


def formula_poly(n):
    # Counts expanded from intersection probabilities by the binomial identity:
    # z^number_of_cuts = product_k(1+(z-1)*1_{cut k}).
    from math import comb
    p = Counter()
    for bits in product([0,1], repeat=max(0,n-2)):
        last = 0
        mult = n
        for j in range(1,n-1):
            if bits[j-1]:last=j
            mult *= n-last
        t=sum(bits)
        for s in range(t+1):
            p[s] += mult*comb(t,s)*(-1)**(t-s)
    return tuple(p[k] for k in range(n-1))


def test_axioms(n,edge):
    for a,b,c in product(range(n),repeat=3):
        A=lambda x,y:strict(n,edge,x,y)
        assert A(a,a)==n-1
        assert min(A(a,b),A(a,c))==A(a,min(b,c))
        assert min(A(a,c),A(b,c))==A(max(a,b),c)
        assert min(A(a,b),A(b,c)) <= A(a,c)


def main():
    # Direct truth-table construction without assuming the edge normal form.
    for n in (2,3):
        allowed=set()
        for table in product(range(n),repeat=n*n):
            A=lambda a,b:table[a*n+b]
            if all(A(a,a)==n-1 for a in range(n)) and all(
              min(A(a,b),A(a,c))==A(a,min(b,c)) and
              min(A(a,c),A(b,c))==A(max(a,b),c) and
              min(A(a,b),A(b,c))<=A(a,c)
              for a,b,c in product(range(n),repeat=3)):
                allowed.add(table)
        induced={tuple(strict(n,edge,a,b) for a in range(n) for b in range(n))
                 for edge in product(range(n),repeat=n-1)}
        assert allowed == induced
        print('truth_tables', n, len(allowed))
    for n in range(2,7):
        counts=Counter()
        for edge in product(range(n),repeat=n-1):
            if n<=4:
                test_axioms(n,edge)
            predicted=pred_cuts(n,edge)
            # Direct quotient compatibility for all named Heyting cuts.
            for k in range(1,n-1):
                p=tuple(a if a<k else k for a in range(n))
                assert compatible_partition(n,edge,p)==(k in predicted)
            if n<=4:
                # Independently test *all* equivalence relations.
                actual=[]
                for p in all_partitions(n):
                    if compatible_partition(n,edge,p):actual.append(p)
                expected=[tuple(a if a<k else k for a in range(n))
                          for k in [0, *sorted(predicted), n-1]]
                assert set(actual)==set(expected)
            counts[len(predicted)]+=1
        got=tuple(counts[k] for k in range(n-1))
        predicted=formula_poly(n)
        assert got==predicted,(n,got,predicted)
        assert sum(got)==n**(n-1)
        print('profile',n,got, 'simple_ratio',round(got[0]/sum(got),9))
    for n in range(2,14):
        possible=range(1,n-1)
        for mask in range(1<<max(0,n-2)):
            wanted=frozenset(k for k in possible if mask & (1<<(k-1)))
            edge=tuple(0 if j==0 else (n-1 if j in wanted else j-1)
                       for j in range(n-1))
            assert pred_cuts(n,edge)==wanted
        print('all_cut_patterns',n,1<<max(0,n-2))
    print('VERIFY_OK')

if __name__=='__main__':main()
