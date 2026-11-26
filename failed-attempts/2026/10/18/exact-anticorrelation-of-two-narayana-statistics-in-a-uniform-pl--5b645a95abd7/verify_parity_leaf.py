"""Exact finite consistency checks for parity-depth and leaf statistics in plane trees."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from math import comb

@lru_cache(None)
def rooted_ordered_trees(size):
    if size == 1:
        return ((),)
    result = []
    def extend(remaining, children):
        if remaining == 0:
            result.append(tuple(children))
            return
        for child_size in range(1, remaining + 1):
            for child in rooted_ordered_trees(child_size):
                extend(remaining - child_size, children + [child])
    extend(size - 1, [])
    return tuple(result)

def count_statistics(root):
    """Return (vertices at even root distance, outdegree-zero vertices)."""
    def visit(node, depth):
        even = int(depth % 2 == 0)
        leaves = int(not node)
        for child in node:
            child_even, child_leaves = visit(child, depth + 1)
            even += child_even
            leaves += child_leaves
        return even, leaves
    return visit(root, 0)

def narayana(semilength, k):
    return comb(semilength, k) * comb(semilength, k - 1) // semilength

def verify():
    total_checks = 0
    for n in range(2, 12):
        objects = rooted_ordered_trees(n)
        size = len(objects)
        assert size == comb(2*n-2, n-1) // n
        total_checks += 1
        sample = [count_statistics(t) for t in objects]
        even_hist = Counter(a for a,b in sample)
        leaf_hist = Counter(b for a,b in sample)
        for k in range(1, n):
            exact = narayana(n-1, k)
            assert even_hist[k] == leaf_hist[k] == exact
            total_checks += 1
        mean_e = Fraction(sum(a for a,b in sample),size)
        mean_l = Fraction(sum(b for a,b in sample),size)
        mean_prod = Fraction(sum(a*b for a,b in sample),size)
        variance_e = Fraction(sum(a*a for a,b in sample),size)-mean_e**2
        variance_l = Fraction(sum(b*b for a,b in sample),size)-mean_l**2
        covariance = mean_prod-mean_e*mean_l
        assert mean_e == mean_l == Fraction(n,2)
        total_checks += 1
        assert variance_e == variance_l == Fraction(n*(n-2),4*(2*n-3))
        total_checks += 1
        if n >= 3:
            assert covariance == Fraction(-n,4*(2*n-3))
            assert covariance / variance_e == Fraction(-1,n-2)
            total_checks += 2
            derived_total=Fraction(comb(2*n,n),32)*(
                (2*n+1)-Fraction(1,2*n-1)-Fraction(6,(2*n-1)*(2*n-3)))
            assert mean_prod*size==derived_total
            total_checks += 1
        else:
            assert covariance == 0 and variance_e == 0
            total_checks += 1
    print('PASS',total_checks,'exact assertions; exhaustive plane trees n=2..11')
if __name__=='__main__':verify()
