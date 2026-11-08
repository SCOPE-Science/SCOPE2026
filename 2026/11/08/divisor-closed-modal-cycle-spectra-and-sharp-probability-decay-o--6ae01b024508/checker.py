"""Finite checks for modal validity spectra on permutation Kripke frames.
Run: python checker.py.  Enumerations illustrate; proofs of infinite assertions are mathematical.
"""
from fractions import Fraction
from itertools import permutations, product
from math import factorial, log


def cycle_lengths(sigma):
    n = len(sigma)
    seen = set()
    answer = []
    for i in range(n):
        if i in seen:
            continue
        u=i; c=0
        while u not in seen:
            seen.add(u); c += 1; u=sigma[u]
        assert u == i
        answer.append(c)
    return answer


def formula_valid_on_cycle(A,k):
    """Independent propositional letters p_a in OR_a (p_a iff X^a p_a)."""
    A=sorted(A)
    if not A: return False
    # Enumerate all valuations for each variable for small finite examples.
    vals = list(product((0,1), repeat=k))
    for assignments in product(vals, repeat=len(A)):
        # Translation invariance: nonvalid at some point iff nonvalid at 0
        disjunction = any(row[0] == row[a % k] for row,a in zip(assignments,A))
        if not disjunction:
            return False
    return True


def class_probability(A,N):
    """Probability generating coefficients by the exact permutation-cycle recurrence."""
    p=[Fraction(1)]
    for n in range(1,N+1):
        p.append(sum((p[n-a] for a in A if a<=n),Fraction(0)) / n)
    return p


def run():
    spec_tests=0
    for A in [(), (1,), (1,2), (1,3), (1,2,3), (1,2,4)]:
        for k in range(1,6):
            if len(A)*k>16: continue
            actual = formula_valid_on_cycle(A,k)
            # expected iff k divides a
            expected = any(a % k == 0 for a in A)
            assert actual == expected, (A,k,actual,expected)
            spec_tests += 1
    # General unary modal formulas with one propositional letter.
    # p <-> X^a p is valid on a k-cycle exactly when k divides a.
    single_tests=0
    for a in range(1,11):
        for k in range(1,12):
            actual = all(row[0]==row[a%k] for row in product((0,1),repeat=k))
            assert actual == (a%k==0)
            single_tests +=1
    count_tests=0
    for A in [(), (1,), (1,2), (1,3), (1,2,3), (1,2,4), (1,2,3,4), (1,2,3,6)]:
        C = class_probability(A,8)
        for n in range(1,9):
            count = sum(all(k in A for k in cycle_lengths(s)) for s in permutations(range(n)))
            assert Fraction(count,factorial(n)) == C[n], (A,n,count,C[n])
            count_tests += 1
    # Demonstrate leading log-decay exponent for L=1,2,3,4.
    for A in [(1,), (1,2), (1,3), (1,2,4)]:
        L=max(A)
        C = class_probability(A,180)
        n=180
        import math
        def exact_log_frac(frac):
            return math.log(frac.numerator) - math.log(frac.denominator)
        residual = exact_log_frac(C[n]) + n/L*log(n) - n/L
        assert abs(residual) < 10*n**((L-1)/L) + 20*log(n), (A,residual)
    print('PERMUTATION_MODAL_CYCLE_SPECTRA_OK', 'finite_spectra=',spec_tests,
          'single_cycle_checks=',single_tests,'enumerated_probabilities=',count_tests,
          'n_max=',8)

if __name__ == '__main__': run()
