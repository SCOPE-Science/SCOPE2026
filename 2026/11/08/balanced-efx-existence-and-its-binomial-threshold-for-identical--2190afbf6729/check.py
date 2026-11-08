"""Exact verification of equal-cardinality EFX for identical two-value goods.

Run: python3 check.py
No external packages. All tests are finite checks; the infinite-domain theorem
is established separately by its analytic proof.
"""
from itertools import product, combinations
from math import factorial


def is_efx(high_counts, capacity, high_value, low_value):
    scores = [h*high_value+(capacity-h)*low_value for h in high_counts]
    for i in range(len(high_counts)):
        for j in range(len(high_counts)):
            if i == j:
                continue
            least = low_value if high_counts[j] < capacity else high_value
            if scores[i] < scores[j] - least:
                return False
    return True


def exists_formula(n, r, q, high, low):
    return high <= 2*low or q % n == 0 or q > (r-1)*n


def labeled_count_for_type_profile(h, r, q):
    denominator = 1
    for x in h:
        denominator *= factorial(x) * factorial(r-x)
    return factorial(q)*factorial(len(h)*r-q)//denominator


def high_contrast_count_formula(n, r, q):
    if q > (r-1)*n:
        s=q-(r-1)*n
        return factorial(n)*factorial(q)//(
            factorial(s)*factorial(r)**s*factorial(r-1)**(n-s))
    if q % n == 0:
        a=q//n
        return factorial(q)*factorial(n*r-q)//(
            factorial(a)**n*factorial(r-a)**n)
    return 0


def brute_labeled_count(n,r,q,high,low):
    goods=tuple(range(n*r))
    total=0
    def alloc(remaining, hs):
        nonlocal total
        if len(hs)==n-1:
            last=sum(g<q for g in remaining)
            total+=is_efx(hs+[last],r,high,low)
            return
        for hand in combinations(remaining,r):
            handset=set(hand)
            alloc(tuple(g for g in remaining if g not in handset),
                  hs+[sum(g<q for g in hand)])
    alloc(goods,[])
    return total


if __name__=='__main__':
    candidates=existence_cases=count_cases=0
    for n in range(2,6):
        for r in range(1,5):
            for high,low in [(3,1),(4,1),(2,1),(3,2),(11,10),(101,100)]:
                by_q=[0]*(n*r+1)
                for h in product(range(r+1), repeat=n):
                    q=sum(h)
                    if is_efx(h,r,high,low):
                        by_q[q]+=labeled_count_for_type_profile(h,r,q)
                    candidates+=1
                for q,actual in enumerate(by_q):
                    assert bool(actual)==exists_formula(n,r,q,high,low), (n,r,high,low,q)
                    existence_cases+=1
                    if high>2*low:
                        assert actual==high_contrast_count_formula(n,r,q), (n,r,high,low,q)
                        count_cases+=1
    print('High-count cross-check PASS:',candidates,'vectors;',existence_cases,
          'existence cases;',count_cases,'exact-count cases')
    assignments=0
    for n,r in [(2,2),(2,3),(2,4),(3,2),(3,3)]:
        for q in range(n*r+1):
            actual=brute_labeled_count(n,r,q,3,1)
            assert actual==high_contrast_count_formula(n,r,q), (n,r,q,actual)
            assignments+=1
    print('Independent labeled-good allocation cross-check PASS:',assignments,'cases')
    assert not exists_formula(2,2,1,3,1)
    assert exists_formula(2,2,1,2,1)
    print('Contrast boundary PASS')
