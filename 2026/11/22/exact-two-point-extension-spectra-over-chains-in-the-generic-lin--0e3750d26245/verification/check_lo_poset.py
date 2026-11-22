#!/usr/bin/env python3
"""Independent finite checks for two-point extensions of a named chain
in the Fraisse limit of finite posets equipped with a linear extension.
All algorithms use only Python's standard library.
"""
from itertools import combinations
from math import comb


def polynomial_counts(n):
    C = (n+1)*(n+2)**2*(n+3)**2*(n+4)//144
    I = (n+1)*(n+2)*(n+3)*(n+4)*(3*n*n+9*n+10)//240
    assert 144*C == (n+1)*(n+2)**2*(n+3)**2*(n+4)
    assert 240*I == (n+1)*(n+2)*(n+3)*(n+4)*(3*n*n+9*n+10)
    return C, I


def cut_counts(n):
    c = i_count = 0
    for left in range(n+1):
        for right in range(left, n+1):
            lower_pairs = (left+1)*(right+1) - left*(left+1)//2
            upper_pairs = (n-right+1)*(n+right+2-2*left)//2
            c += lower_pairs*upper_pairs
            no_forced = (n-left+1)*(right+1) - (right-left)*(right-left+1)//2
            i_count += (left+1)*(n-right+1)*no_forced
    return c, i_count


def direct_poset_counts(n):
    """Enumerate every relation matrix on every total-order interleaving.

    The original n named points have a fixed chain. The other points are
    named X and Y. Enumerate all subsets of possible extra comparisons,
    then check transitivity directly on the full n+2 element structure.
    """
    old = tuple(range(n))
    counts = {"X<Y": 0, "Y<X": 0, "parallel": 0}
    for x_index, y_index in combinations(range(n+2), 2):
        for orientation in (("X", "Y"), ("Y", "X")):
            labels = [None]*(n+2)
            labels[x_index], labels[y_index] = orientation
            iterator = iter(old)
            for j in range(n+2):
                if labels[j] is None:
                    labels[j] = next(iterator)
            unknown_pairs = [ (u,v) for u in range(n+2) for v in range(u+1,n+2)
                              if not (isinstance(labels[u],int) and isinstance(labels[v],int)) ]
            fixed_pairs = [ (u,v) for u in range(n+2) for v in range(u+1,n+2)
                            if isinstance(labels[u],int) and isinstance(labels[v],int)]
            for mask in range(1<<len(unknown_pairs)):
                rows = [0]*(n+2)
                for u,v in fixed_pairs:
                    rows[u] |= 1<<v
                for bit,(u,v) in enumerate(unknown_pairs):
                    if mask >> bit & 1:
                        rows[u] |= 1<<v
                valid = True
                for u in range(n+2):
                    for v in range(u+1,n+2):
                        if rows[u] >> v & 1 and rows[v] & ~rows[u]:
                            valid = False
                            break
                    if not valid:
                        break
                if not valid:
                    continue
                ix,iy=labels.index('X'),labels.index('Y')
                if rows[ix] >> iy & 1:
                    counts['X<Y']+=1
                elif rows[iy] >> ix & 1:
                    counts['Y<X']+=1
                else:
                    counts['parallel']+=1
    return counts


def main():
    for n in range(17):
        c,i=polynomial_counts(n)
        assert (c,i)==cut_counts(n), (n,(c,i),cut_counts(n))
    print('CLOSED_FORM_VS_CUT_SUM_OK 0..16')
    for n in range(8):
        c,i=polynomial_counts(n)
        direct=direct_poset_counts(n)
        assert direct == {'X<Y':c,'Y<X':c,'parallel':2*i}, (n,direct,c,i)
        print('DIRECT_TRANSITIVITY_OK',n,c,i,2*(c+i))
    for n in range(25):
        c,i=polynomial_counts(n)
        ratio_num=(n+2)*(n+3)
        ratio_den=3*n*n+9*n+10
        assert 3*c*ratio_den == 5*i*ratio_num
        assert i>=c
    print('RATIO_AND_MONOTONICITY_FORMULA_OK')
    print('ALL_LO_POSET_CHECKS_OK')

if __name__=='__main__':
    main()
