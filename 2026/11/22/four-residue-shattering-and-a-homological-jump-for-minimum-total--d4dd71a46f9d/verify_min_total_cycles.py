#!/usr/bin/env python3
"""Finite independent tests for the minimum-total-domination cycle theorem.

All library-free, Python 3. Uses the original open-neighborhood domination
condition, not the auxiliary graph, to enumerate optimizing concepts.
"""
from itertools import combinations
from math import comb


def direct_minimum_total_dominators(n):
    assert n >= 3
    full = (1 << n) - 1
    best = n + 1
    result = []
    for mask in range(1 << n):
        left = ((mask << 1) | (mask >> (n - 1))) & full
        right = (mask >> 1) | ((mask & 1) << (n - 1))
        if (left | right) != full:
            continue
        s = mask.bit_count()
        if s < best:
            best, result = s, [mask]
        elif s == best:
            result.append(mask)
    return result


def cycle_pattern(m):
    # The complete support polynomial of maximum independent sets of C_m.
    assert m >= 2
    if m % 2 == 0:
        return [1, m]
    return [1, m, m * (m - 3) // 2]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    while out[-1] == 0:
        out.pop()
    return out


def predicted_polynomial(n):
    if n % 2:
        return cycle_pattern(n)
    return mul(cycle_pattern(n//2), cycle_pattern(n//2))


def feasible_query(support, n):
    if not support:
        return True
    # H_n is the graph with edges between the distinct neighbors of every i.
    if n % 2:
        if len(support) > 2:
            return False
        if len(support) == 2:
            a,b = support
            return (a-b) % n not in (2,n-2)
        return True
    m = n//2
    for parity in (0,1):
        part = [(v-parity)//2 for v in support if v % 2 == parity]
        if m % 2 == 0:
            if len(part) > 1:
                return False
        else:
            if len(part) > 2:
                return False
            if len(part) == 2 and (part[0]-part[1]) % m in (1,m-1):
                return False
    return True


def bitmask(support):
    out = 0
    for v in support:
        out |= 1 << v
    return out


def main():
    comparisons = 0
    coefficients = 0
    for n in range(3, 21):
        concepts = direct_minimum_total_dominators(n)
        formula = predicted_polynomial(n)
        actual = [0]*len(formula)
        for k in range(min(n, 5)+1):
            for support in combinations(range(n),k):
                qry = bitmask(support)
                true_shattered = len({concept & qry for concept in concepts}) == 1 << k
                predicted = feasible_query(support, n)
                assert true_shattered == predicted, (n,support, true_shattered,predicted)
                if predicted:
                    actual[k] += 1
                comparisons += 1
        assert actual == (formula+[0]*max(0,len(actual)-len(formula)))[:len(actual)], (n,actual,formula)
        coefficients += len(actual)
        # A support of size at least 5 cannot shatter, as the formula has degree <=4.
        assert (len(formula)-1 <= 4)
        if n <= 15:
            for support in combinations(range(n),6):
                assert len({concept & bitmask(support) for concept in concepts}) < 64
                comparisons += 1
        print(f'n={n:2d} min_total={len(concepts):3d} polynomial={formula}')
    # Distinct parity/topology phases, checked by independent Euler calculation.
    for n in [3,4,5,6,7,8,9,10,12,14,18]:
        p = predicted_polynomial(n)
        reduced_chi = sum((-1)**(k-1)*v for k,v in enumerate(p))
        if n == 3:
            expected = 2
        elif n%2:
            expected = -(n*(n-5)//2 + 1)
        elif n%4 == 0:
            expected = -(n//2-1)**2
        elif n==6:
            expected = -4
        else:
            m=n//2
            expected = -(m*(m-5)//2+1)**2
        assert reduced_chi == expected, (n,reduced_chi,expected)
    print('MINIMUM_TOTAL_DOMINATION_CYCLE_PASS',comparisons,coefficients,11)

if __name__=='__main__':
    main()
