"""Independent finite checks for coordinate-equality shattering.
No external packages are required.
"""
from collections import Counter
from decimal import Decimal, getcontext
from itertools import product
from math import comb, log, exp


def column_trace_mask(column, q):
    answer = 0
    for value in range(q):
        row_subset = sum(1 << i for i, v in enumerate(column) if v == value)
        answer |= 1 << row_subset
    return answer


def count_by_dynamic_program(m, q, d):
    one_column = Counter(column_trace_mask(c, q) for c in product(range(q), repeat=m))
    dp = {0: 1}
    for _ in range(d):
        next_dp = {}
        for seen, count in dp.items():
            for pattern, multiplicity in one_column.items():
                union = seen | pattern
                next_dp[union] = next_dp.get(union, 0) + count * multiplicity
        dp = next_dp
    full = (1 << (1 << m)) - 1
    return dp.get(full, 0)


def count_bruteforce(m, q, d):
    traces = [column_trace_mask(c, q) for c in product(range(q), repeat=m)]
    full = (1 << (1 << m)) - 1
    result = 0
    for chosen in product(traces, repeat=d):
        union = 0
        for bitmap in chosen:
            union |= bitmap
        result += union == full
    return result


def near_full_probability(m, q, d):
    """Exact inclusion-exclusion for rare subsets of sizes m-1 (and m-2 if q=3)."""
    getcontext().prec = 110
    p1 = Decimal(q-1) / Decimal(q)**(m-1)
    if q == 3:
        p2 = Decimal((q-1)**2) / Decimal(q)**(m-1)
        n2 = comb(m,2)
    else:
        p2 = Decimal(0)
        n2 = 0
    result = Decimal(0)
    for a in range(m+1):
        for b in range(n2+1):
            term_base = Decimal(1) - a*p1 - b*p2
            assert term_base >= 0
            sign = -1 if (a+b)%2 else 1
            result += sign * comb(m,a)*comb(n2,b)*(term_base**d)
    return result


def absent_other_upper_bound(m,q,d):
    """Union bound for missed nonempty target subsets outside critical classes."""
    total = 0.0
    critical = {1,2} if q==3 else {1}
    for j in range(m):
        if j in critical:
            continue
        p = (q-1)**j / q**(m-1)
        total += comb(m,j) * (1-p)**d
    return total


def main():
    cases = [(1,2,1), (2,2,1), (2,2,2), (3,2,3), (3,2,4),
             (2,3,2), (3,3,2), (3,3,3), (3,3,4),
             (2,4,2), (2,4,3), (3,4,2)]
    for m,q,d in cases:
        dp = count_by_dynamic_program(m,q,d)
        brute = count_bruteforce(m,q,d)
        assert dp == brute, (m,q,d,dp,brute)
        assert dp <= q**(m*d)
        print('EXACT_CHECK',m,q,d,dp,q**(m*d))
    for q in (3,4,5):
        for m in (5,6,7):
            d = int((q**(m-1)/(q-1))*log(m))
            critical_probability = near_full_probability(m,q,d)
            err = absent_other_upper_bound(m,q,d)
            assert Decimal(0) <= critical_probability <= Decimal(1)
            print('CRITICAL_BOUND',q,m,d,'upper=',format(critical_probability,'.9f'),
                  'error<=',format(err,'.6f'))
    print('ALL_CATEGORICAL_LITERAL_CHECKS_PASS',len(cases),'exact exhaustive cases')

if __name__ == '__main__':
    main()
