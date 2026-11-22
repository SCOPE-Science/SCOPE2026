"""Reproduce finite checks for a binomial-parity return-gap classification.

The proof of the theorem is symbolic and does not rely on an enumeration bound.
"""
from collections import Counter
from math import comb


def support_digit_predicate(n):
    run = 0
    while n:
        if n & 1:
            run += 1
        else:
            if run % 3 == 2:
                return False
            run = 0
        n >>= 1
    return run % 3 != 2


def target_binomial_sum(n):
    """Sum of summand parities; binomial coefficients with upper < lower are zero."""
    return sum((comb(-2*n+8*k, n+k)*comb(n, k)) % 2
               for k in range(n+1) if -2*n+8*k >= n+k)


def periodic_run_product(n):
    result = 1
    run = 0
    while n:
        if n & 1:
            run += 1
        else:
            if run:
                result *= (run % 3 != 2)
            run = 0
        n >>= 1
    if run:
        result *= (run % 3 != 2)
    return int(result)


def other_binomial_sum(n):
    """Previously known Fibonacci-transform formula, used only as a comparison."""
    return sum((comb(n-k,2*k)*comb(n,k)) % 2
               for k in range(n+1) if 2*k <= n-k)


def impulse(m):
    if m < 0:
        return 0
    values = [1, 1, 2]
    if m < 3:
        return values[m]
    for i in range(3, m+1):
        values.append(values[-1] + values[-2] + values[-3])
    return values[m]


def predicted_gap_counts(level):
    counts = Counter()
    counts[1] = sum(impulse(level-3*j-1) + impulse(level-3*j-2)
                    for j in range(level+1))
    counts[2] = 2*impulse(level-3) + sum(impulse(level-3*j)
                                      for j in range(2,level+1))
    for j in range(1,level-2):
        g = 2**j + 1 + (j % 3 == 1)
        counts[g] = impulse(level-j-3)
    return +counts


def suffix_automaton(level, state):
    out = []
    for n in range(1<<level):
        current = state
        for bit in format(n,f'0{level}b'):
            if bit == '0':
                if current == 2:
                    current = -1
                    break
                current = 0
            else:
                current = (current+1)%3
        if current in (0,1):
            out.append(n)
    return out


def verify():
    direct = 0
    for n in range(301):
        assert target_binomial_sum(n) == periodic_run_product(n), n
        assert periodic_run_product(n) == int(support_digit_predicate(n)), n
        assert other_binomial_sum(n) % 2 == periodic_run_product(n), n
        direct += 1
    automaton = 0
    for level in range(0,11):
        for state in (0,1,2):
            accepted = suffix_automaton(level,state)
            if state == 0:
                assert accepted == [n for n in range(1<<level)
                                    if support_digit_predicate(n)]
            automaton += len(accepted)
    gaps = 0
    for level in range(1,19):
        accepted = [n for n in range(1<<level)
                    if support_digit_predicate(n)]
        actual = Counter(b-a for a,b in zip(accepted,accepted[1:]))
        expected = predicted_gap_counts(level)
        assert actual == expected, (level,actual,expected)
        assert sum(expected.values()) == len(accepted)-1
        gaps += len(accepted)-1
    print(f'PASS target_binomial_checks={direct} '
          f'automaton_accepted={automaton} exact_gap_checks={gaps} '
          f'levels=18 largest_level_gap={max(predicted_gap_counts(18))}')


if __name__ == '__main__':
    verify()
