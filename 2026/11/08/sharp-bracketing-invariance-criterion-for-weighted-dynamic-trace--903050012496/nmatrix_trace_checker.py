"""Finite checks for trace-counting of the BMK three-valued disjunction.
Use: python3 nmatrix_trace_checker.py. Requires only Python 3 standard library.
"""
from functools import lru_cache
from itertools import product
from math import comb

V = (0, 1, 2)  # 2 stands for the undefined/error value k.
H = ((0,), (1,), (2,), (1,), (1,), (1, 2), (2,), (1, 2), (2,))

def outputs(x, y):
    return H[3*x+y]

def product_counts(u, v):
    w = [0, 0, 0]
    for x in V:
        for y in V:
            for z in outputs(x, y):
                w[z] += u[x]*v[y]
    return tuple(w)

@lru_cache(None)
def shapes(n):
    if n == 1:
        return (None,)
    return tuple((a,b) for p in range(1,n) for a in shapes(p) for b in shapes(n-p))

def leaf_count(t):
    return 1 if t is None else leaf_count(t[0]) + leaf_count(t[1])

def count_dp(t, w):
    if t is None:
        return w
    return product_counts(count_dp(t[0], w),count_dp(t[1],w))

def all_internal_labelings(t, leaves):
    """Enumerate every legal internal output labeling, independently of DP."""
    if t is None:
        return [(leaves[0], ())]
    left, right = t
    p = leaf_count(left)
    ret = []
    for a, xhist in all_internal_labelings(left, leaves[:p]):
        for b, yhist in all_internal_labelings(right, leaves[p:]):
            for z in outputs(a, b):
                ret.append((z, xhist+yhist+(z,)))
    return ret

def count_bruteforce(t, w):
    result = [0,0,0]
    n = leaf_count(t)
    for values in product(V,repeat=n):
        mass = 1
        for v in values:
            mass *= w[v]
        for out, _ in all_internal_labelings(t, values):
            result[out] += mass
    return tuple(result)

def symmetric_formula(a,b,n):
    return (a**n, ((a+3*b)**n-a**n)//3,((a+3*b)**n-a**n)//3)

def run():
    tests = 0
    # Independent direct tree-label enumeration for each shape through 5 leaves.
    for n in range(1,6):
        for t in shapes(n):
            direct = count_bruteforce(t,(1,1,1))
            derived = symmetric_formula(1,1,n)
            assert direct == derived == count_dp(t,(1,1,1)), (n,t,direct,derived)
            tests += 1
    # General equal-success/error input weights, including zero.
    for n in range(1,8):
        for a,b in product(range(4),repeat=2):
            for t in shapes(n):
                assert count_dp(t,(a,b,b)) == symmetric_formula(a,b,n)
                tests += 1
    # Boundary when only one of successful/error leaves is allowed.
    for n in range(1,8):
        for a,b in product(range(4),repeat=2):
            for t in shapes(n):
                assert sum(count_dp(t,(a,b,0))) == (a+b)**n
                assert sum(count_dp(t,(a,0,b))) == (a+b)**n
                tests += 2
    # Sharp fourth-leaf failure with BOTH 1 and k weighted differently.
    left = (((None,None),None),None)
    balanced = ((None,None),(None,None))
    assert all(leaf_count(t)==4 for t in (left,balanced))
    for a,b,c in product(range(5),repeat=3):
        zb = sum(count_dp(balanced,(a,b,c)))
        zl = sum(count_dp(left,(a,b,c)))
        assert zb-zl == -b*c*(b-c)**2, (a,b,c,zb,zl)
        assert sum(count_bruteforce(left,(a,b,c)))==zl
        assert sum(count_bruteforce(balanced,(a,b,c)))==zb
        tests += 3
    # Independent coordinatewise test of the general nonassociative trace identity.
    for vals in product(range(3), repeat=9):
        u, v, w = vals[:3], vals[3:6], vals[6:]
        lhs = product_counts(product_counts(u, v), w)
        rhs = product_counts(u, product_counts(v, w))
        delta = u[1]*w[2]-u[2]*w[1]
        assert tuple(x-y for x,y in zip(lhs, rhs)) == (0, -v[1]*delta, v[2]*delta)
        tests += 1
    # Confirm ordinary (set-valued) associativity and its separation from trace counts.
    assert all({z for u in outputs(x,y) for z in outputs(u,t)}==
               {z for u in outputs(y,t) for z in outputs(x,u)}
               for x,y,t in product(V,repeat=3))
    print('All checks passed:',tests)
    for n in range(1,8):
        v = symmetric_formula(1,1,n)
        print('leaves',n,'root counts',v,'total',sum(v))
    print('four-leaf difference (a,b,c)=(1,2,3):',
          sum(count_dp(balanced,(1,2,3)))-sum(count_dp(left,(1,2,3))))

if __name__ == '__main__':
    run()
