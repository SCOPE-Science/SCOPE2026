#!/usr/bin/env python3
"""Reproduce the finite checks for the sharp rank-utility stable-matching bound.

No external dependencies. Every stable matching of the small instances is
independently tested for blocking pairs. The all-size result is proved in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial, prod
from random import Random


def rankings(preferences):
    return [{candidate: j for j, candidate in enumerate(row)} for row in preferences]


def stable(male_preferences, female_preferences, matching):
    n = len(male_preferences)
    mr = rankings(male_preferences)
    wr = rankings(female_preferences)
    inverse = [None] * n
    for i, j in enumerate(matching):
        inverse[j] = i
    return not any(
        mr[i][j] < mr[i][matching[i]] and wr[j][i] < wr[j][inverse[j]]
        for i in range(n) for j in range(n)
    )


def product_welfare(male_preferences, female_preferences, matching):
    n = len(male_preferences)
    mr = rankings(male_preferences)
    wr = rankings(female_preferences)
    inverse = [None] * n
    for i, j in enumerate(matching):
        inverse[j] = i
    return prod(n - mr[i][matching[i]] for i in range(n)) * prod(
        n - wr[j][inverse[j]] for j in range(n)
    )


def gale_shapley(male_preferences, female_preferences):
    n = len(male_preferences)
    wr = rankings(female_preferences)
    next_choice = [0] * n
    partner_of_woman = [-1] * n
    unmatched = list(range(n-1, -1, -1))
    while unmatched:
        man = unmatched.pop()
        woman = male_preferences[man][next_choice[man]]
        next_choice[man] += 1
        current = partner_of_woman[woman]
        if current < 0:
            partner_of_woman[woman] = man
        elif wr[woman][man] < wr[woman][current]:
            partner_of_woman[woman] = man
            unmatched.append(current)
        else:
            unmatched.append(man)
    ans = [None] * n
    for woman, man in enumerate(partner_of_woman):
        ans[man] = woman
    return tuple(ans)


def independent_bruteforce(male_preferences, female_preferences):
    n = len(male_preferences)
    choices = []
    for match in permutations(range(n)):
        if stable(male_preferences, female_preferences, match):
            choices.append((product_welfare(male_preferences, female_preferences, match), match))
    return choices


def cyclic_witness(n):
    men = []
    women = []
    for i in range(n):
        top, second = i, (i+1) % n
        men.append((top, second) + tuple(j for j in range(n) if j not in (top, second)))
    for j in range(n):
        first, last = (j-1) % n, j
        women.append((first,) + tuple(i for i in range(n) if i not in (first, last)) + (last,))
    return tuple(men), tuple(women)


def exhaustive(n):
    orders = tuple(permutations(range(n)))
    summary = Counter()
    extreme = 0
    examples = []
    for codes in product(range(len(orders)), repeat=2*n):
        men = tuple(orders[i] for i in codes[:n])
        women = tuple(orders[i] for i in codes[n:])
        gs = gale_shapley(men, women)
        st = independent_bruteforce(men, women)
        assert st and any(match == gs for _, match in st)
        base = product_welfare(men, women, gs)
        highest = max(score for score, _ in st)
        ratio = Fraction(highest, base)
        assert ratio <= (n-1)**n
        summary[ratio] += 1
        if ratio == (n-1)**n:
            extreme += 1
            if len(examples) < 1:
                examples.append((men, women, gs))
    assert sum(summary.values()) == factorial(n) ** (2*n)
    return summary, extreme, examples


def random_check(n, cases, seed):
    rng = Random(seed)
    for _ in range(cases):
        men = tuple(tuple(rng.sample(range(n), n)) for _ in range(n))
        women = tuple(tuple(rng.sample(range(n), n)) for _ in range(n))
        gs = gale_shapley(men, women)
        assert stable(men, women, gs)
        base = product_welfare(men, women, gs)
        for score, _ in independent_bruteforce(men, women):
            assert score <= base * (n-1)**n


def derangements(n):
    return sum((-1)**j * factorial(n) // factorial(j) for j in range(n+1))


def run():
    for n in range(2, 10):
        men, women = cyclic_witness(n)
        a = tuple(range(n))
        b = tuple((i+1)%n for i in range(n))
        assert stable(men, women, a) and stable(men, women, b)
        assert gale_shapley(men, women) == a
        assert Fraction(product_welfare(men, women, b),product_welfare(men, women, a)) == (n-1)**n
    small2, ext2, _ = exhaustive(2)
    small3, ext3, _ = exhaustive(3)
    assert small2 == Counter({Fraction(1,1):16})
    assert ext2 == 16
    assert ext3 == 12 == factorial(3)*derangements(3)*factorial(1)**6
    assert small3[Fraction(8,1)] == 12
    assert sum(c for q,c in small3.items() if q>1) == 5424
    random_check(4,1000,314159)
    random_check(5,150,271828)
    print('VERIFY_OK cyclic_sizes=2..9 exhaustive_2=16 exhaustive_3=46656')
    print('THREE_BY_THREE extremal_count=12 strict_gain_profiles=5424 max_product_ratio=8')
    print('SAMPLED_OK n4=1000 n5=150')


if __name__ == '__main__':
    run()
