"""Finite checks for a frequency-shift entropy plateau theorem.

The proof in RESULT.md, rather than these finite tests, establishes the asymptotic claim.
"""
from fractions import Fraction
from itertools import product
from math import log, sqrt


def possible_real_offset(word, beta):
    """Test finite transition-rule feasibility with arbitrary real initial discrepancy."""
    lo = None  # weak lower bound
    hi = None  # strict upper bound
    zeros = ones = 0
    for i, symbol in enumerate(word):
        if symbol == 0:
            zeros += 1
        else:
            ones += 1
        if i + 1 < len(word) and symbol == 1:
            threshold = ones - beta * zeros
            if word[i+1] == 1:
                lo = threshold if lo is None else max(lo, threshold)
            else:
                hi = threshold if hi is None else min(hi, threshold)
    return lo is None or hi is None or lo < hi


def counts_with_fixed_offset(n, beta, start=Fraction(0)):
    total = 0
    stack = [(0, start, -1)]
    while stack:
        i, disc, previous = stack.pop()
        if i == n:
            total += 1
            continue
        if previous == 1:
            if disc >= 0:
                stack.append((i+1, disc-1, 1))
            else:
                stack.append((i+1, disc+beta, 0))
        else:
            stack.append((i+1, disc+beta, 0))
            stack.append((i+1, disc-1, 1))
    return total


def golden(word):
    return all(not (a == b == 1) for a,b in zip(word,word[1:]))


def prefix_works_for_golden(word, beta):
    assert beta < 1 and golden(word)
    N = int((len(word) + 3) / (1 - beta)) + 2
    # The admissible prefix (10)^N has discrepancy N(beta-1).
    # Within this prefix, after every 1 the discrepancy is strictly negative.
    assert beta - 1 < 0
    assert N * (beta - 1) < -len(word) - 2
    disc = N * (beta-1)
    for i, x in enumerate(word):
        disc += beta if x == 0 else -1
        if x == 1 and i+1 < len(word) and word[i+1] != (1 if disc >= 0 else 0):
            return False
    if word and word[-1] == 1 and disc >= 0:
        return False
    return True


def fibonacci(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a


def run():
    sample = [Fraction(1,5),Fraction(2,5),Fraction(499,1000),Fraction(1,2),Fraction(2,3)]
    for pc in sample:
        beta=pc/(1-pc)
        for n in range(1, 15):
            words = list(product((0,1),repeat=n))
            feasible = sum(possible_real_offset(w,beta) for w in words)
            fib=fibonacci(n+2)
            assert feasible <= (n*n+n-1)*fib
            fixed=counts_with_fixed_offset(n,beta)
            assert fixed<=fib
            if pc < Fraction(1,2):
                assert all(possible_real_offset(w,beta) and prefix_works_for_golden(w,beta) for w in words if golden(w))
                assert feasible>=fib
        print(f"pc={pc}, n=14, feasible-offset words={feasible}, golden={fib}, fixed-offset={fixed}")
    print('PASS: all finite word, golden-extension and Fibonacci tests')
    print('Entropy predictions: log(phi)=',log((1+sqrt(5))/2),', h(1/2)=',log(2)/2)

if __name__=='__main__':run()
