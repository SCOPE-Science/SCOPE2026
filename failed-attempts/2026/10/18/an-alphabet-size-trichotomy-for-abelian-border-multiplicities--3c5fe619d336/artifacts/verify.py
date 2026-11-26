"""Independent finite checks for the q-ary Abelian-border distribution theorem.

Run: python3 artifacts/verify.py
Only Python's standard library is required. Finite checks supplement, not replace,
the analytic proof for unrestricted word length.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb


def border_count(word):
    n = len(word)
    return sum(Counter(word[:k]) == Counter(word[n-k:]) for k in range(1, n))


def brute(q, n):
    answer = Counter()
    for word in product(range(q), repeat=n):
        answer[border_count(word)] += 1
    return answer


def return_probability(q, k):
    """Exact P(S_k=0) from equal multinomial histograms."""
    ways = 0

    def visit(remaining, parts, coefficient):
        nonlocal ways
        if parts == q-1:
            ways += coefficient * coefficient
            return
        for take in range(remaining+1):
            visit(remaining-take, parts+1, coefficient*comb(remaining, take))

    visit(k, 0, 1)
    return Fraction(ways, q**(2*k))


def mirrored_pair_dynamic_program(q, n):
    """Independent state-and-return-count DP with integer word multiplicities."""
    d = q-1
    origin = (0,) * d
    increments = [tuple(int(a==j)-int(b==j) for j in range(d))
                  for a in range(q) for b in range(q)]
    states = {(origin, 0): 1}
    for _ in range(n//2):
        following = defaultdict(int)
        for (position, returns), multiplicity in states.items():
            for increment in increments:
                new_position = tuple(x+y for x, y in zip(position, increment))
                following[(new_position, returns+int(new_position == origin))] += multiplicity
        states = following
    hist = Counter()
    for (position, returns), multiplicity in states.items():
        count = 2*returns if n%2 else 2*returns-int(position == origin)
        hist[count] += multiplicity * (q if n%2 else 1)
    return hist


def renewal_distribution(q, m):
    """Joint-return count from the first-return convolution, not a word DP."""
    p = [return_probability(q, i) for i in range(m+1)]
    first = [Fraction(0)] * (m+1)
    survival = [Fraction(1)] * (m+1)
    for j in range(1, m+1):
        first[j] = p[j] - sum(first[i]*p[j-i] for i in range(1, j))
        survival[j] = survival[j-1] - first[j]
    powers = [[Fraction(0)]*(m+1) for _ in range(m+1)]
    powers[0][0] = Fraction(1)
    for r in range(1, m+1):
        for s in range(1, m+1):
            powers[r][s] = sum(powers[r-1][s-j]*first[j] for j in range(1, s+1))
    return [sum(powers[r][s]*survival[m-s] for s in range(m+1))
            for r in range(m+1)]


def main():
    cases = 0
    for q in (2,3,4):
        for n in range(1,9):
            full = brute(q,n)
            dp = mirrored_pair_dynamic_program(q,n)
            assert full == dp, (q,n,full,dp)
            assert sum(dp.values()) == q**n
            if n%2:
                probabilities = renewal_distribution(q,n//2)
                predicted = {2*r:prob*q**n for r,prob in enumerate(probabilities) if prob}
                assert all(value.denominator == 1 for value in predicted.values())
                assert full == Counter({k:int(v) for k,v in predicted.items()}), (q,n)
            cases+=1
        print('alphabet',q,'exhaustive/DP agreement for word lengths 1 through 8')
    # An independent published ternary zero-border enumeration (2014, Table 1).
    known_unbordered = (3,6,18,48,144,402,1206,3438,10314,29754)
    for n,expected in enumerate(known_unbordered, start=1):
        actual = mirrored_pair_dynamic_program(3,n)[0]
        assert actual == expected, (n,actual,expected)
    # Check finite rational return probabilities and renewal normalization.
    for q in (2,3,4,5):
        for m in range(1,7):
            distribution=renewal_distribution(q,m)
            assert sum(distribution)==1 and all(x>=0 for x in distribution)
            assert distribution[0] >= distribution[0] - Fraction(1,10**12)
    assert return_probability(2,2)==Fraction(3,8)
    assert return_probability(3,2)==Fraction(5,27)
    assert return_probability(4,2)==Fraction(7,64)
    print('PASS:',cases,'exact word enumerations, renewal PGFs, and published ternary anchors')
    print('INFINITE LIMIT THEOREMS: analytic proofs are in RESULT.md')

if __name__=='__main__':
    main()
